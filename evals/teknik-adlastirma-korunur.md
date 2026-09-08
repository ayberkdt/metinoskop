# Korunması gereken teknik adlaştırma

## Kaynak

Kalman kazancının hesaplanması, yenilik kovaryansının tersinin alınmasını gerektirir. Filtrenin yakınsama hızının başlangıç kovaryansına duyarlılığı Tablo 3'te verilmiştir. Duyarlılık yalnızca ilk 50 adımda görülmüş, sonrasında kazanç 0,12 değerinde sabitlenmiştir.

## Talep

Makale yöntem paragrafı. Standart düzeyde düzenle; metin çeviri gibi durmasın.

## Korunması gerekenler

- "Kalman kazancının hesaplanması" ve "yenilik kovaryansının tersinin alınması" isim-fiilleri iki teknik işlemi adlandırdığı için korunmalı.
- "Yakınsama hızının başlangıç kovaryansına duyarlılığı" tamlaması, Tablo 3'ün adlandırdığı büyüklük olduğu için korunmalı.
- Tablo 3, 50 adım ve 0,12 korunmalı.
- `Yalnızca` sınırı korunmalı.
- Metin zaten doğalsa olduğu gibi bırakılabilmeli.

## Kaçınılması gerekenler

- Teknik adlaştırmaları "kazancı hesaplamak için kovaryansın tersini alırız" gibi ders notu diline açmak
- İyelik zincirini çözerken hangi büyüklüğün hangisine ait olduğunu değiştirmek ("başlangıç kovaryansının yakınsama hızı")
- "Kalman", "yenilik kovaryansı", "yakınsama" terimlerini öz Türkçe hevesiyle değiştirmek
- Duyarlılığın ilk 50 adımla sınırlı olduğunu genelleştirmek
- Kaynakta bulunmayan kovaryans değeri, adım süresi veya neden eklemek

## Yapısal beklenti

- sert işaret: 0
- düzyazı paragrafı: 1
