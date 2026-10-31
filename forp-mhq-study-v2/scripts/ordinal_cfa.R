# FUTURE empirical ordinal CFA: execute only after authorized Turkish scale translation + real data
# install.packages(c("lavaan", "semTools", "psych"))
library(lavaan)
library(semTools)
d <- read.csv("data/real_cohort_local_not_public.csv", stringsAsFactors=FALSE)
item_names <- sprintf("forp_item_%02d", 1:10)
stopifnot(all(item_names %in% colnames(d)))
model <- paste0("FORP =~ ", paste(item_names, collapse=" + "))
fit <- cfa(model, data=d, ordered=item_names, estimator="WLSMV", std.lv=TRUE, missing="pairwise")
print(summary(fit, standardized=TRUE, fit.measures=TRUE))
print(fitMeasures(fit,c("cfi","tli","rmsea","srmr")))
print(reliability(fit))
# Fit gender and diagnosis measurement invariance only if group frequencies support estimation.
# For test-retest, specify ICC(A,1): two-way absolute-agreement single-measure model.