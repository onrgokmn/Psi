# FORP-TR V6 | Hakem revizyonu ve prospektif araştırma protokolü

**Durum: Planlanan tıpta uzmanlık tezi; yapılmış klinik araştırma değildir.** Etik kurul onayı, Türkçe FORP-MHQ kullanım/uyarlama izni ve OSF ön kaydı henüz alınmadı. Simülasyon verileri klinik bulgu olarak sunulmamalıdır.

## Önceden belirlenen araştırma

- **Birincil sonuç:** Altıncı ay WHO-5 toplam skoru (0–100).
- **Maruziyet:** Başlangıç FORP-MHQ / 10; `β₁` 10 FORP puanı başına ayarlanmış WHO-5 ortalama farkıdır.
- **Örneklem:** Güç hesabı yaklaşık **560 gözlenen altıncı ay sonucuna** dayalıdır; %20 kayıp varsayımıyla **700** başlangıç katılımcısı hedeflenir. MI ana analizi daha çok başlangıç katılımcısının kısmen gözlenen verisini kullanabilir.
- **Ana karıştırıcı seti:** Başlangıç WHO-5, PHQ-9, GAD-7, yaş, cinsiyet, tanı ailesi, log(1+hastalık süresi), epizod yükü, tedavi türü, remisyon ve varsa merkez.
- **Kayıp veri birincil stratejisi:** MAR altında 40 MICE ataması, aynı OLS/HC3 modeli, Rubin birleştirme; tam-olgu, IPW ve MNAR delta (-5/-10/-15) duyarlılık.
- **Keşifsel ikincil:** Önceden tanımlı 3 düğümlü restricted cubic spline; **ayrı güç hesabı yapılmadı**. Tanı/kültür alt grupları da keşifseldir.
- **Klinik sonlanım:** WHO-5 özbildiriminden ayrı, tanıya özgü olay tanımları ve iki bağımsız kör psikiyatrist; notlardan nüks korkusu ve maruziyeti açığa çıkaran ifadeler maskelenir. Kontrole gelmeyenler izinli kayıt/güvenli iletişimle taranır.
- **Aşamalar:** Ölçek izni, çeviri, bilişsel görüşme ve 30–40 kişilik pilot ana kohorttan ayrı; ardından prospektif kohort; nitel görüşme alt çalışması.
- **Takip ve güvenlik:** Yüz yüze poliklinik, onamlı telefon veya kurum onaylı güvenli portal; tanı içeren SMS yok. T3/T6: 5 WHO-5 yanıtı + puanlamadan bağımsız 2 klinik risk sorusu; olumlu yanıt için aynı gün klinisyen değerlendirmesi.

## Yalnız Ek A'daki yöntem simülasyonu

| Kısmi R² varsayımı | Monte Carlo ile eşlenen β (WHO-5 / 10 FORP) |
|---|---:|
| 0,01 | −2,038 |
| 0,02 | −2,908 |

Kalibrasyon katsayıları varsayılan WHO-5 artık SS=14 ve simüle FORP koşullu varyansına bağlıdır; **gerçek hasta bulgusu değildir**. Orijinal tam-olgu senaryosunda N=700 / gözlenen n≈560 için güç %89,6 (500 tekrar); tamamlayıcı MAR/MI yöntem-senaryosu %91,7 (300 tekrar, 15 atama), gerçek 40-atamalı analizin birebir simülasyonu **değildir**. WHO-5 için literatürdeki 10/100 puanlık eşik birey-içi değişim yorumudur, ayarlanmış kişiler-arası β için kanıtlanmış MCID değildir.

## Belge seti

31 Ekim 2026 tarihli **37 dosyalık tam ZIP** (Türkçe tez, İngilizce protokol, istatistik planı, ölçüm ve güvenlik ekleri, OSF taslağı, Word/PDF, 22 slayt PPTX, Monte Carlo kodu ve sonuçları) ChatGPT konuşmasında ayrıca teslim edilmiştir. Bu GitHub klasöründe sürüm özeti tutulur; ZIP içeriğinin tamamının buraya yüklendiği iddia edilmez.

## Doğrulanmış ana kaynaklar

1. FORP-MHQ: https://doi.org/10.1111/bjc.12536
2. Nüks korkusu derlemesi: https://doi.org/10.1016/j.cpr.2023.102342
3. WHO-5 Türkçe: https://doi.org/10.1017/S1463423619000343
4. WHO WHO-5: https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01
5. Guillemin: https://doi.org/10.1016/0895-4356(93)90142-N
6. ITC: https://www.intestcom.org/files/guideline_test_adaptation_2ed.pdf
