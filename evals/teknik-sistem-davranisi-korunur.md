# Ürün belirtimi korunur

## Kaynak

Denetleyici her komutu doğrular ve geçersiz komutu `E-41` koduyla reddeder. Geçerli komutlar 20 ms içinde işlenir. Bellek doluyken denetleyici en eski kaydı siler. Cihaz IP67 koruma sınıfındadır.

## Talep

Ürün belirtim belgesinden bir paragraf. Standart düzeyde düzenle.

## Korunması gerekenler

- Belirtim geniş zamanda kalmalı; ürünün genel davranışı tek seferlik olaya çevrilmemeli.
- `E-41`, 20 ms ve IP67 korunmalı.
- Bellek dolu durumundaki davranış korunmalı.

## Kaçınılması gerekenler

- `doğruladı / reddetti / sildi` biçimine çevirip belirtimi bir test kaydına indirmek
- Kaynakta bulunmayan bir test, ölçüm ya da tarih eklemek
- Hata kodunu ya da koruma sınıfını değiştirmek
- Koşullu davranışı koşulsuz genellemeye çevirmek

## Yapısal beklenti

- zamansal sürtünme: 0
- cümle: 4
