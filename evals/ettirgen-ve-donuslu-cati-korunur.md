# Ettirgen, edilgen ettirgen ve dönüşlü çatı korunur

## Kaynak

Proje ekibi ölçümleri bağımsız bir laboratuvara yaptırdı. Sonuçlar ikinci bir uzmana da kontrol ettirildi. Sensör her açılışta kendini sıfırlar. Kapak iç sıcaklık 60 °C'yi aşınca kendiliğinden açılır.

## Talep

Standart düzeyde düzenle.

## Korunması gerekenler

- `yaptırdı` ettirgendir: ölçümü laboratuvar yapmış, ekip yaptırmıştır. `yaptı` ya da `laboratuvar ölçtü` aktörü değiştirir.
- `kontrol ettirildi` edilgen ettirgendir ve ettiren kaynakta adlandırılmamıştır; proje ekibi ettiren olarak eklenmemeli.
- `kendini sıfırlar` dönüşlüdür; `sıfırlanır` ya da `sistem tarafından sıfırlanır` biçimine çevrilmemeli.
- `kendiliğinden açılır` dış eyleyensiz bir olaydır; `tarafından` eklenmemeli, aktör seçilip etkene çevrilmemeli.
- Geniş zamanlı iki cümle ürün davranışını betimler; geçmişe çevrilmemeli. 60 °C eşiği korunmalı.

## Kaçınılması gerekenler

- Ettirgen ekini düşürmek ya da çift aktörü teke indirmek
- Adlandırılmamış ettireni ya da dönüşlü yüklemin eyleyenini uydurmak
- Cümleleri birleştirip ilgisiz iki ölçümü tek özneye bağlamak

## Yapısal beklenti

- cümle: 4
- sert işaret: 0
