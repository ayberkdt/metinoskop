# Geçmişten önceki olay korunur

## Kaynak

İkinci test başlamadan önce sensör zaten kalibre edilmişti. Kalibrasyon 12 Ağustos'ta yapılmış ve sonuçları kayıt altına alınmıştı. Test sırasında sapma 0,3 dereceyi aşmadı.

## Talep

Deney raporu paragrafı. Standart düzeyde düzenle.

## Korunması gerekenler

- `Kalibre edilmişti` ikinci testten önce tamamlanmış olmayı bildirir; bu öncelik ilişkisi korunmalı.
- 12 Ağustos ve 0,3 derece korunmalı.
- İki olayın sırası (kalibrasyon → ikinci test) korunmalı.
- Metin zaten doğalsa olduğu gibi bırakılabilmeli.

## Kaçınılması gerekenler

- `Kalibre edilmişti` biçimini `kalibre edildi` yapıp öncelik ilişkisini düzleştirmek
- Kalibrasyonu test sırasında yapılmış gibi göstermek
- `Zaten` sözcüğünü dolgu sayıp silmek; sözcük önceliği işaretler
- Sapmanın eşiği aşmamasını ölçülmüş bir başarı iddiasına çevirmek

## Yapısal beklenti

- cümle: 3
- sert işaret: 0
