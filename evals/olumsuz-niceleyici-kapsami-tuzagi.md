# Olumsuzluk ve niceleyici kapsamı tuzağı

## Kaynak

Gece çalıştırılan regresyon koşusunda her test başarıyla geçmedi. Bu durum önemli bir husus olarak değerlendirilmektedir. Başarısız testlerin sayısının 7 olduğu tespit edilmiştir. Hatalı testler yalnızca ödeme modülünde görüldü.

## Talep

Sadeleştir.

## Korunması gerekenler

- `her test ... geçmedi` kısmi olumsuzluktur: testlerin hepsi geçmedi, bir kısmı başarısız oldu. Türkçede tümel niceleyici olumsuzluğun altında dar kapsam alır (Kamali ve Zeijlstra 2024); `hiçbir test geçmedi` tümel olumsuzluktur ve başka bir önermedir.
- Başarısız test sayısı 7 korunmalı.
- `yalnızca` ödeme modülünü sınırlar; başka ögeye bağlanmamalı.
- Gece koşusu ve regresyon koşusu bağlamı korunmalı.

## Kaçınılması gerekenler

- `Hiçbir test geçmedi`, `testler geçmedi` ya da `testler başarısız oldu` yazarak kısmi olumsuzluğu tümele çevirmek
- `kimse`, `asla`, `hiç` gibi olumsuz uyum ögesi eklemek (`her` → `tüm` aynı tümel ailedir ve olumsuzluk altında aynı kısmi okumayı verir; ekleme sayılmaz)
- `yalnızca`yı başka ögenin yanına taşımak (`Yalnızca hatalı testler ...`)
- `önemli bir husus` cümlesini başka bir önem kalıbıyla geri getirmek
- Cümleleri noktalı virgülle birleştirmek

## Serbest değişmezler

- değerlendir — `önemli bir husus olarak değerlendirilmektedir` aktörsüz önem dolgusudur; kimin değerlendirdiğini ve neye göre önemli olduğunu söylemez, önerme taşımaz.

## Yapısal beklenti

- cümle: <= 3
- sert işaret: 0
- noktalı virgül: 0
