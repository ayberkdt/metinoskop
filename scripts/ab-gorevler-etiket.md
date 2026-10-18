# Etiket ve anons görevleri

`SKILL.md` › **Etiket ve anons yok** kuralının ayrık sınaması. Skill bu görevlere bakılarak düzeltilmez. T1–T3 yazma kipidir ve LLM'in açıklayıcı metinde etiket (`Kısa cevap:`, `Sezgisel açıklama:`) ile anons (`Merak etmeyin`, `tanışın`) kurma eğilimini sınar; T4 etiketli bir taslağın düzeltilmesidir; T5'te belgenin alan etiketleri (`Uç nokta:`, `Yöntem:`, `Uyarı:`) kalmalı, yalnızca içerik türünü duyuran etiket gitmelidir. Model örneklerine bu başlık verilmez, yalnızca `## T1` ile başlayan görevler verilir. Her görevin çıktısını yalnızca son metin olarak ver.

## T1

İstek: Veri ekibinin iç wiki'si için "Ortalama ile medyan arasındaki fark" bölümünü yaz. Bilgiler: ortalama bütün değerlerin toplamının değer sayısına bölümüdür; medyan sıralanmış değerlerin ortasındaki değerdir; aykırı değer ortalamayı kaydırır, medyanı az etkiler; bizim gecikme raporlarımızda medyan kullanılıyor çünkü birkaç çok yavaş istek ortalamayı şişiriyor.

## T2

İstek: Yeni başlayanlar için Git'te `merge` ile `rebase` arasındaki farkı 120 sözcüğü geçmeyecek biçimde açıkla.

## T3

İstek: Müşterilere yeni özelliği duyuran kısa bir e-posta yaz. Bilgiler: uygulamaya çevrimdışı mod geldi; internet yokken eklenen notlar 30 güne kadar cihazda saklanıyor ve bağlantı gelince eşitleniyor; mod Ayarlar > Depolama bölümünden açılıyor.

## T4

İstek: Aşağıdaki metni blogda yayımlanacak hâle getir.

Metin: **Kısa cevap:** TCP ve UDP farklı amaçlara hizmet eder. **Kavramsal ayrım:** TCP paketlerin sırayla ve eksiksiz ulaşmasını garanti eder; UDP garanti vermez. **Sezgisel açıklama:** UDP, kayıp paketi yeniden göndermediği için daha az gecikmeyle çalışır. **Detaylı açıklama:** Görüntülü görüşme uygulamaları çoğunlukla UDP kullanır; dosya aktarımı TCP üzerinden yapılır. Merak etmeyin, bu ayrımı öğrenmek sanıldığı kadar zor değil! Bu yazıda ikisini ne zaman seçeceğinizi öğreneceksiniz.

## T5

İstek: Aşağıdaki API belgesi bölümünü düzenle.

Metin:

Uç nokta: `/v1/raporlar`

Yöntem: GET

**Sezgisel açıklama:** Bu uç nokta, hesabınızdaki raporları bir liste olarak döndürür.

Sayfa boyutu: en fazla 50 kayıt.

Uyarı: Silinmiş raporlar listede görünmez.
