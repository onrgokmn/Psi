# FORP-TR V5.0: preregistered, NOT YET EXECUTED on human data.
# Input file must be a secure, authorized and deidentified institutional data export.
# No clinical dataset or licensed scale items are distributed with this template.

library(stats)
library(splines)
# install.packages('sandwich') only in an approved analytic environment
library(sandwich)

run_forp_v5 <- function(d) {
  required <- c('who5_6m','forp_total','who5_t0','phq9_t0','gad7_t0',
                'age','sex_model','diagnosis_family','duration_years',
                'episodes_ordinal','treatment_cat','remission_t0')
  stopifnot(all(required %in% names(d)))
  d$forp10 <- d$forp_total / 10
  d$age10 <- (d$age - 45) / 10
  d$duration_log <- log1p(d$duration_years)
  d$diagnosis_family <- factor(d$diagnosis_family)
  d$treatment_cat <- factor(d$treatment_cat)
  d$sex_model <- factor(d$sex_model)
  d$remission_t0 <- factor(d$remission_t0)
  if ('centre' %in% names(d)) d$centre <- factor(d$centre)

  confounders <- c('who5_t0','phq9_t0','gad7_t0','age10','sex_model',
                   'diagnosis_family','duration_log','episodes_ordinal',
                   'treatment_cat','remission_t0')
  if ('centre' %in% names(d) && nlevels(d$centre) > 1) confounders <- c(confounders,'centre')
  f_full <- reformulate(c('forp10',confounders), response='who5_6m')
  f_red <- reformulate(confounders,response='who5_6m')
  dat <- d[complete.cases(d[,all.vars(f_full)]), ]
  m_full <- lm(f_full,data=dat)
  m_red <- lm(f_red,data=dat)
  vv <- sandwich::vcovHC(m_full,type='HC3')
  ix <- match('forp10',names(coef(m_full)))
  b <- coef(m_full)[ix]; se <- sqrt(vv[ix,ix]); df <- df.residual(m_full)
  cval <- qt(.975,df); p <- 2*pt(-abs(b/se),df)
  r2f <- summary(m_full)$r.squared; r2r <- summary(m_red)$r.squared
  primary <- data.frame(n=nrow(dat), beta_per10=b, se_hc3=se,
       ci_low=b-cval*se,ci_high=b+cval*se,p=p,
       delta_R2=r2f-r2r,partial_R2=(r2f-r2r)/(1-r2r))

  # Secondary 3-knot restricted cubic spline implementation, with 10th, 50th, 90th
  # T0-exposure knots locked BEFORE seeing six-month outcomes.
  # A natural cubic spline with one interior knot (median) and boundary knots
  # at 10th and 90th percentiles represents the 3-knot restricted cubic basis.
  knots <- as.numeric(quantile(d$forp_total,c(.10,.50,.90),na.rm=TRUE,type=7))
  stopifnot(length(unique(knots))==3)
  # Truncated-power restricted cubic spline basis with 3 fixed knots.
  # The linear exposure and the single extra nonlinear term form a nested comparison.
  # Harrell-style tail restriction (linear above last knot and below first knot).
  tp3 <- function(z) pmax(z,0)^3
  k1 <- knots[1]; k2 <- knots[2]; k3 <- knots[3]
  dat$rcs_nonlin <- (tp3(dat$forp_total-k1) -
       ((k3-k1)/(k3-k2))*tp3(dat$forp_total-k2) +
       ((k2-k1)/(k3-k2))*tp3(dat$forp_total-k3)) / ((k3-k1)^2)
  f_spline <- reformulate(c('forp10','rcs_nonlin',confounders),response='who5_6m')
  m_spline <- lm(f_spline,data=dat)
  vc_spline <- sandwich::vcovHC(m_spline,type='HC3')
  nonlinear_beta <- unname(coef(m_spline)['rcs_nonlin'])
  nonlinear_se <- sqrt(vc_spline['rcs_nonlin','rcs_nonlin'])
  nonlinear_t <- nonlinear_beta/nonlinear_se
  secondary <- data.frame(n=nrow(dat), knots_10=knots[1],knots_50=knots[2],
           knots_90=knots[3], nonlinear_coef=nonlinear_beta,
           robust_se=nonlinear_se,
           robust_two_sided_p=2*pt(-abs(nonlinear_t),df.residual(m_spline)))
  list(primary=primary,primary_fit=m_full,reduced_fit=m_red,
       secondary_spline_model=m_spline,secondary_test=secondary,locked_knots=knots,
       reminder='secondary spline p-values are exploratory, not confirmatory.')
}