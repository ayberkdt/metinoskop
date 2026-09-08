# İngilizce `ve` cümle zinciri

## Kaynak

Sensör veriyi 100 Hz'de okur ve veriyi bir alçak geçiren filtreden geçirir ve filtrelenmiş veriyi denetleyiciye gönderir ve denetleyici bu veriyle 10 ms içinde komut üretir ve komut sürücüye iletilir. Sürücü komutu uygular ve uygulama sonucunu günlüğe yazar.

## Talep

Teknik belge. Standart düzeyde düzenle; bağımsız çekimli cümle zincirini Türkçe yan cümle yapısıyla yeniden kur.

## Korunması gerekenler

- İşlem sırası (oku → filtrele → gönder → komut üret → ilet → uygula → günlüğe yaz) korunmalı.
- 100 Hz ve 10 ms değerleri doğru eylemlerle eşleşmeli.
- Aktör değişimleri (sensör, denetleyici, sürücü) açık kalmalı; hangi eylemi kimin yaptığı belirsizleşmemeli.
- İkinci cümledeki "uygular ve günlüğe yazar" eş düzeyli iki eylemi bağlayan `ve` korunabilmeli.

## Kaçınılması gerekenler

- Beş çekimli cümleyi aynı `ve` ile dizmeyi sürdürmek
- Bütün eylemleri tek yükleme asılmış `-ip` zincirine çevirmek
- Aktör değiştiği yerde özneyi düşürüp eylemi yanlış aktöre bırakmak
- Kaynakta bulunmayan filtre kesim frekansı, gecikme veya hata davranışı eklemek
- "Ardından", "daha sonra", "bunun sonucunda" gibi belirteçlerle her adımı etiketlemek

## Yapısal beklenti

- ve zinciri: 0
- fiilimsi yığını: 0
- sert işaret: 0
