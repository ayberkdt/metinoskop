# Yaklaşıklık ve istatistik niteleyicileri korunur

## Kaynak

On iki haftalık izlemede yanıt süresinin medyanı 180 ms, ortalaması 240 ms oldu. En yüksek değer 410 ms ile ikinci haftada görüldü. Etkin kullanıcı sayısı yaklaşık 3.000'dir; bu sayı oturum kayıtlarından tahmin edildi.

## Talep

Standart düzeyde düzenle.

## Korunması gerekenler

- `medyanı` ve `ortalaması` iki ayrı istatistiktir; biri ötekinin yerine yazılmamalı, ikisi tek değere indirilmemeli.
- `En yüksek değer` üst sınırdır ve haftasıyla birlikte kalmalı.
- `yaklaşık 3.000` ve `tahmin edildi` tahmin statüsünü iki kez kurar; bu tekrar dolgu değildir, biri silinirse sayı ya da yöntem kaybolur.
- Sayılar, birimler ve on iki haftalık süre korunmalı.

## Kaçınılması gerekenler

- `yaklaşık`ı ya da `tahmin edildi`yi gereksiz çekince sayıp silmek
- Medyan ile ortalamayı `ortalama yanıt süresi 180–240 ms` gibi tek bir aralığa birleştirmek
- Kaynakta olmayan bir neden ya da değerlendirme eklemek

## Yapısal beklenti

- cümle: 3
- sert işaret: 0
