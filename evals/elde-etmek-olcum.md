# Ölçüm varken `elde etmek`

## Kaynak

Yeni ayarla hata oranında %20'lik bir iyileşme elde edilmiştir. Bellek kullanımında da azalma elde edilmiştir; kullanım 512 MB'tan 410 MB'a inmiştir.

## Talep

Teknik rapor paragrafı. Standart düzeyde düzenle.

## Korunması gerekenler

- %20, 512 MB ve 410 MB korunmalı.
- Ölçüm varken soyut `iyileşme elde edildi` yapısı yerine ölçümün kendisi öne çıkabilmeli.
- İki ayrı ölçüm ayrı kalmalı.

## Kaçınılması gerekenler

- `Elde edilmiştir` yapısını iki cümlede de bırakmak
- Kaynakta bulunmayan bir yüzde türetmek (örneğin bellek azalmasının yüzdesini hesaplamak)
- İki ölçümü tek iddiada birleştirmek
- `Başarı elde etmek` gibi yerleşik kullanımları da yasaklamak

## Yapısal beklenti

- cümle: <= 2
