# Teknik `adreslemek` korunur

## Kaynak

Denetleyici belleği 16 bitlik sayfalar hâlinde adresler. Adresleme birimi sayfa sınırını aşan erişimi reddeder.

## Talep

Gömülü sistem belirtim belgesi. Standart düzeyde düzenle.

## Korunması gerekenler

- Bilgisayar mühendisliğinde `adreslemek` gerçek teknik anlamdır; `address` kalkısı değildir.
- 16 bitlik sayfa ve sayfa sınırı davranışı korunmalı.
- Ürün belirtimi geniş zamanda kalmalı.
- Metin zaten doğalsa olduğu gibi bırakılabilmeli.

## Kaçınılması gerekenler

- `Adreslemek` yerine `ele almak`, `çözmek` gibi karşılıklar koymak
- `Adresleme birimi` terimini değiştirmek
- Bit genişliğini değiştirmek
- Ret davranışını olasılığa çevirmek

## Yapısal beklenti

- cümle: 2
- sert işaret: 0
