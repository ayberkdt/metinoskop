# Aşırı bölümlenmiş akademik metin

## Kaynak

### Veri kümesinin seçimi

Deneylerde 2022 yılına ait 48.000 kayıtlık trafik veri kümesi kullanılmıştır.

### Veri kümesinin özellikleri

Kayıtların %12'si eksik hız değeri içermektedir.

### Eksik değerlerin ele alınması

Eksik hız değerleri, aynı sensörün önceki ve sonraki ölçümlerinin ortalamasıyla doldurulmuştur.

### Bu seçimin gerekçesi

Bu yöntem, ön denemelerde medyanla doldurmaya göre doğrulama hatasını %2 azaltmıştır.

### Sınırlılık

Doldurma yalnızca 10 dakikadan kısa boşluklar için uygulanmıştır; daha uzun boşluklar içeren kayıtlar çıkarılmıştır.

## Talep

Makalenin veri bölümü. Derin düzeyde düzenle; hak edilmemiş başlıkları birleştir, bütün yöntem bilgisini koru.

## Korunması gerekenler

- 2022 yılı, 48.000 kayıt ve %12 eksik değer oranı korunmalı.
- Önceki ve sonraki ölçümlerin ortalamasıyla doldurma yöntemi korunmalı.
- Ön denemelerde medyana göre %2 azalma gerekçesi, ön deneme statüsüyle korunmalı.
- `Yalnızca` 10 dakikadan kısa boşluklar kapsamı ve daha uzun boşluklu kayıtların çıkarıldığı bilgisi korunmalı.
- Beş başlık tek bir bölüm başlığı (örneğin "Veri kümesi") altında bir veya iki paragrafa inebilmeli.
- Akademik ton korunmalı.

## Kaçınılması gerekenler

- Beş başlığı korumak veya her cümleye yeni adla başlık açmak
- Yöntem gerekçesini (%2) ya da 10 dakika sınırlılığını tekrar sanıp silmek
- Bilgiyi madde işaretli listeye çevirmek
- Kaynakta bulunmayan ön işleme adımı, sensör sayısı veya kaynak eklemek
- 10 dakika sınırını değiştirmek veya kesin kural gibi genelleştirmek
- Bölümleri birleştirirken "bununla birlikte", "bu doğrultuda" gibi zorlama geçişler eklemek

## Yapısal beklenti

- başlık: <= 1
- liste ögesi: 0
- sert işaret: 0
