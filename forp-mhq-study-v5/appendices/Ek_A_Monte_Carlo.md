# Ek A · Monte Carlo ile örneklem ve analiz planının doğrulanması

**Yalnız tasarım simülasyonu:** Buradaki hiçbir satır gerçek psikiyatri hastalarına ait değildir. Raporlanan yüzdeler yalnız belirli varsayımlar altında veri toplama planının istatistiksel özelliklerini incelemek içindir. Bu sayılar makalenin klinik Results bölümüne taşınmaz.

## Hipotez, veri üretimi ve analitik mekanizma

- FORP toplamı (0–40) ile T0 PHQ-9, GAD-7, WHO-5, tanı, epizod yükü, hastalık süresi, başlangıç tedavisi/remisyon arasında yapılandırılmış korelasyonlar üretildi. Gerçek Balıkesir dağılımları bilinmediğinden bu parametrik girdiler **varsayımsaldır**.
- Altıncı ay WHO-5 skoru 0–100 ile sınırlandı ve dört puanlık basamaklara yuvarlandı. Maruziyetin varsayımsal ilişkisi, kısmi R² hedefi 0 / 0,01 / 0,02 olacak biçimde kalibre edildi; bu **doğrulanmış klinik etki değildir**.
- Ana analiz baştan tanımlanmış 13 başlangıç model terimine göre düzeltilmiş doğrusal regresyon; HC3 belirsizlik, iki yönlü α=0,05.
- Gözlem oranı MAR ana senaryosunda yaklaşık %80. MCAR kontrol ve T6 iyi oluşunun eksik kalma mekanizmasını etkilediği **MNAR ihlal senaryosu** ayrıca uygulandı.
- Tüm senaryolar için **500 bağımsız Monte Carlo tekrarı**; Python seed `20261031`. Nominal tip-I hata oranı sıfır-etki senaryosunda ampirik olarak ölçüldü.
- Ampirik güç = p<0,05 oranı; Monte Carlo standart hata = sqrt[p(1−p)/500]. Bunu örneklem katsayısının güven aralığıyla karıştırmıyoruz.

## Ana senaryo: MAR takip kaybında güç

| Başlangıç N | Ort. T6 n | H0 yanlış-pozitif | Güç (kısmi R² 0,01) | Güç (kısmi R² 0,02) |
|---:|---:|---:|---:|---:|
| 400 | 320 | 0.038 | 0.420 | 0.660 |
| 500 | 400 | 0.048 | 0.502 | 0.764 |
| 600 | 480 | 0.056 | 0.594 | 0.830 |
| 700 | 561 | 0.046 | 0.584 | 0.896 |
| 850 | 680 | 0.044 | 0.718 | 0.946 |
| 1000 | 800 | 0.038 | 0.760 | 0.978 |

![Monte Carlo güç eğrisi](../figures/monte_carlo_power.png)

## İkincil eksik veri mekanizmaları: hassasiyet

| Başlangıç N | Mekanizma | Etki varsayımı | T6 n | Ampirik reddetme | Ortalama β (10 puan FORP başına) | Kapsama |
|---:|---|---:|---:|---:|---:|---:|
| 600 | MCAR | 0.00 | 480 | 0.054 | -0.010 | 0.946 |
| 600 | MCAR | 0.02 | 480 | 0.872 | -2.963 | 0.936 |
| 600 | MNAR | 0.00 | 480 | 0.072 | 0.591 | 0.928 |
| 600 | MNAR | 0.02 | 481 | 0.600 | -2.038 | 0.832 |
| 700 | MCAR | 0.00 | 560 | 0.052 | 0.055 | 0.948 |
| 700 | MCAR | 0.02 | 560 | 0.904 | -2.849 | 0.950 |
| 700 | MNAR | 0.00 | 560 | 0.112 | 0.612 | 0.888 |
| 700 | MNAR | 0.02 | 560 | 0.666 | -2.093 | 0.844 |
| 850 | MCAR | 0.00 | 681 | 0.060 | -0.045 | 0.940 |
| 850 | MCAR | 0.02 | 681 | 0.946 | -2.866 | 0.954 |
| 850 | MNAR | 0.00 | 680 | 0.130 | 0.620 | 0.868 |
| 850 | MNAR | 0.02 | 680 | 0.770 | -2.084 | 0.806 |

## Bulguların doğru yorumu

- N=500 için, kısmi R²=0,02 varsayımında %76,4 ampirik güç; bu nedenle önceki 500 kişilik hedef, revize karıştırıcı model altında güvenli bir hedef değildir.
- N=700 senaryosunda yaklaşık 560 takipli kişiyle aynı varsayım için %89,6 güç; Monte Carlo belirsizliği yaklaşık ±2,7 yüzde puanı (%95 yaklaşık aralık). Kısmi R²=0,01 için güç yalnız %58,4.
- MNAR senaryosunda sıfır-etki altında tip-I hata yaklaşık %11,2 (N=700); ayrıca β tahmini değişebilir. **MAR varsayımı veri tarafından kanıtlanamaz**, bu nedenle MAR/MNAR duyarlılıkları zorunludur.
- Simüle edilen olay dağılımları, epizod sıklığı, remisyon ve PHQ/GAD dağılımları merkezin gerçek verilerine dayanmaz. Örneklem hedefi ve model karmaşıklığı klinik fizibilite ve varsayım belirsizliğiyle birlikte değerlendirilmelidir.
- Bu hesap **birincil regresyon eğimi** içindir; tanı-özel olay analizi, alt grup etkileşimi, spline nonlinear test veya ordinal DFA için otomatik güç sağlamaz.

## Yeniden üretme

```bash
OPENBLAS_NUM_THREADS=1 MC_REPS=500 python analysis/monte_carlo_power.py
```

Dosyalar: `analysis/monte_carlo_results.csv`, `analysis/monte_carlo_metadata.json`, `figures/monte_carlo_power.png`. MC simülasyonu ile gerçek hasta kohortu birbirine karıştırılmamalıdır.