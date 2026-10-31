# Kör Klinik Nüks / Kötüleşme Adjudikasyonu · Çalışma El Kitabı

**Araştırma statüsü:** Tanı-özel olayları kodlamak için önceden belirlenmiş operasyonel çerçeve; kendisi valide bir tanı ölçeği değildir. Kesin epizod kriterleri yerel klinik panelle ve etik kurul başvurusunda onaylanıp prospektif veriler açılmadan kilitlenmelidir.

## Olay sınıflama ağacı

1. Altıncı aya kadar potansiyel klinik olay var mı? Yatış veya ilaç değişimi *yalnız sinyal* oluşturur; klinik tanı koşulu değildir.
2. Olay tarihinden önce kayıtlı remisyonda/stabil dönemde mi? Değilse **mevcut epizodda kötüleşme** değerlendirilir; nüks kodlanmaz.
3. Hangi ana tanı ailesine ait? Tanı-özel epizod ölçütlerini dosyadan, görüşme notundan ve tanı kayıtlarından doğrula.
4. Yeni epizodun süre, belirti ve klinik etki ölçütleri belgeli mi? Belgeli değilse **belirsiz / yetersiz veri** kaydı kullan.
5. Değerlendirici 1 ve 2 bağımsız form doldurur; uyumsuzsa üçüncü değerlendirici gerekçeyi yazar; FORP veya aile yanıtı görülmez.

## Tanıya özel yaklaşım

**Depresif bozukluk:** Önceden belgelenmiş iyileşme veya remisyon sonrasında yeniden gelişen, klinik değerlendirmeye göre majör depresif epizodu karşılayan sendrom ve en az iki hafta süre. Remisyonda olmayan kişi için klinik artış 'kötüleşme'.

**Bipolar bozukluk:** Yeni manik, hipomanik veya depresif epizodun ilgili süre, işlev kaybı ve tanı ölçütleriyle doğrulanması. Hastane yatışı tek başına 'mani nüksü' değildir.

**Psikoz spektrumu:** Belgelenmiş stabilizasyon sonrası pozitif psikotik belirtilerin açık, klinik olarak anlamlı yeniden ortaya çıkışı; kayıtlı anamnez ve klinisyen muayenesi gerekir. Psikososyal sorunlara bağlı yatış otomatik nüks sayılmaz.

**OKB, anksiyete ve travma ilişkili bozukluklar:** Süreğen belirtilerde semptom şiddetlenmesi ile remisyondan sonra sendrom dönüşü açıkça ayrılır; ilgili ölçütler ve stabil/iyileşmiş dönem klinisyen panelince önceden tanımlanır. Tanı-özel karşılaştırılabilirlik kısıtlıdır. 'Tüm tanılarda ortak nüks oranı' çıkarımı yapılmaz.

## Veri alanları ve körlük kontrolü

`participant_code`, `event_date`, `diagnostic_family`, `prior_remission_documented`, `event_duration_days`, `symptom_threshold_met`, `functional_change`, `new_episode_yes_no_uncertain`, `clinical_deterioration_yes_no_uncertain`, `source_notes`, `rater_1`, `rater_2`, `adjudicator`, `resolution_date`, `blinding_deviation`.

Değerlendirici ekranında `FORP_total`, `FORP_items`, aile destek puanı, açıklanma endişesi ve bu konulardaki nitel görüşme metinleri **yer almaz**. Klinik notta açıkça yer alabilecek benzer ifadeler tümüyle kontrol edilemeyeceği için sapmalar kaydedilir.

## Kalite kontrolü

İlk 20 dosyada olay tanımları ve formlar eğitim amaçlı birlikte gözden geçirilir. Sonuçlara bakarak epizod tanımı değiştirilmez. İki değerlendiricinin ham uyum ve uygun anlaşma katsayısı (ör. kappa, yeterli olay varsa) raporlanır; seyrek olayda güven aralıkları vurgulanır. Hakem kararı ve tarihçi ayrı saklanır.