# Belirsizliği önleyen açık özne

## Kaynak

Filtre ölçümü 50 Hz'de alır. Gözlemci durumu günceller. Filtre kazancı yeniden hesaplar. Gözlemci güncellenmiş durumu denetleyiciye iletir. Filtre bu aşamada hiçbir veri iletmez.

## Talep

Teknik belge. Standart düzeyde düzenle; metin çeviri gibi durmasın.

## Korunması gerekenler

- Filtre ve gözlemci iki ayrı aktördür; her eylemin hangi aktöre ait olduğu açık kalmalı.
- Özneler dönüşümlü geldiği için açık özne tekrarı korunabilmeli; özne düşürüldüğünde eylem yanlış aktöre gitmemeli.
- 50 Hz korunmalı.
- Filtrenin bu aşamada hiçbir veri iletmediği olumsuzluğu korunmalı.
- Metin zaten doğalsa olduğu gibi bırakılabilmeli.

## Kaçınılması gerekenler

- "Filtre ... Gözlemci ... Filtre ..." dizisini tekrar sanıp özneleri düşürmek
- Aynı aktöre ait olmayan eylemleri tek `-ip` zincirinde birleştirmek
- Filtre ve gözlemciyi "sistem" gibi tek özne altında toplamak
- Olumsuz cümleyi silmek veya olumluya çevirmek
- Kaynakta bulunmayan güncelleme sıklığı, gecikme veya veri türü eklemek

## Yapısal beklenti

- sert işaret: 0
- düzyazı paragrafı: 1
