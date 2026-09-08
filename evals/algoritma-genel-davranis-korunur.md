# Algoritmanın genel davranışı korunur

## Kaynak

Filtre önce tahmini üretir, ardından ölçüm geldiğinde durumu günceller. Kazanç matrisi her adımda yenilik kovaryansından hesaplanır. RK4 her adımda türevi dört kez değerlendirir. Bu davranış adım büyüklüğünden bağımsızdır.

## Talep

Makalenin yöntem bölümünde algoritmanın genel davranışını tanımlayan paragraf. Standart düzeyde düzenle.

## Korunması gerekenler

- Algoritma tanımı geniş zamanda kalmalı; makalede geçiyor diye geçmişe çevrilmemeli.
- Adım sırası, `dört kez` ve kazanç matrisinin kaynağı korunmalı.
- Metin zaten doğal ve tutarlıysa olduğu gibi bırakılabilmeli.

## Kaçınılması gerekenler

- `üretti / güncelledi / değerlendirdi` biçimine çevirip tanımı tek seferlik bir koşuya indirmek
- Kaynakta bulunmayan bir deney, koşu ya da ölçüm bağlamı eklemek
- Teknik terimleri (kazanç matrisi, yenilik kovaryansı, RK4) değiştirmek
- Genel davranışı `bu çalışmada` çerçevesine bağlamak

## Yapısal beklenti

- geniş zaman doygunluğu: 0
- zamansal sürtünme: 0
- cümle: 4
