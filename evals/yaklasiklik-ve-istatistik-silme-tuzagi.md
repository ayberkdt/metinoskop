# Dolguyu silerken yaklaşıklık ve istatistik niteleyicisini silme tuzağı

## Kaynak

Yapılan ölçümler neticesinde, sistemin yanıt süresinin ortalama 240 milisaniye düzeyinde olduğu tespit edilmiş olup en yüksek değerin 410 milisaniye olarak kaydedildiği görülmüştür. Kullanıcı sayısının yaklaşık 3.000 civarında seyrettiği değerlendirilmektedir.

## Talep

Daha sade yaz.

## Korunması gerekenler

- `Yapılan ölçümler neticesinde`, `düzeyinde olduğu tespit edilmiş olup`, `olarak kaydedildiği görülmüştür` resmî dolgu katmanıdır; çözülmeli.
- `ortalama 240 milisaniye` bir grup ortalamasıdır; `ortalama` silinirse tek ölçüm gibi okunur.
- `en yüksek değer 410 milisaniye` üst sınırı bildirir; `en yüksek` kalmalı.
- `yaklaşık 3.000` bir tahmindir; `yaklaşık` silinirse tahmin sayıma döner. `yaklaşık ... civarında` anlam tekrarıdır, biri kalır.
- `değerlendirilmektedir` kullanıcı sayısının ölçüm değil değerlendirme olduğunu söyler; `3.000 kullanıcı var` gibi kesin bildirime çevrilmemeli.

## Kaçınılması gerekenler

- `Ortalama yanıt süresi` yerine `Yanıt süresi 240 milisaniye` yazmak
- `yaklaşık` ve `civarında`yı birlikte silip `3.000 kullanıcı` yazmak
- Değerlendirmeyi ölçüme çevirmek (`kullanıcı sayısı 3.000'dir`) ya da kaynakta olmayan bir aktör (`ekip`) eklemek
- `en yüksek değer`i `bazen` ya da `zaman zaman` gibi sıklık ifadesine çevirmek

## Serbest değişmezler

- tespit edil — `tespit edilmiş olup` resmî dolgu katmanıdır; ölçüm cümlesi bildirme kipinde yazıldığında gözlem statüsü yüklemde korunur.

## Yapısal beklenti

- cümle: <= 3
- sert işaret: 0
