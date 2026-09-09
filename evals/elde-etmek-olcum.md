# Ölçüm varken `elde etmek`

## Kaynak

Yeni ayarla hata oranında %20'lik bir iyileşme elde edilmiştir. Bellek kullanımında da azalma elde edilmiştir; kullanım 512 MB'tan 410 MB'a inmiştir.

## Talep

Teknik rapor paragrafı. Standart düzeyde düzenle.

## Korunması gerekenler

- %20, 512 MB ve 410 MB korunmalı.
- Ölçüm varken soyut `iyileşme elde edildi` yapısı yerine ölçümün kendisi öne çıkabilmeli.
- Yerine konan yapı da doğal eşdizim olmalı: hata oranı `azalır`, `düşer`; `hata oranı iyileşti` Türkçede tuhaftır.
- İki ayrı ölçüm ayrı kalmalı.

## Kaçınılması gerekenler

- `Elde edilmiştir` yapısını iki cümlede de bırakmak
- Kaynakta bulunmayan bir yüzde türetmek (örneğin bellek azalmasının yüzdesini hesaplamak)
- İki ölçümü tek iddiada birleştirmek
- Kalkıyı kaldırırken yeni bir tuhaf eşdizim üretmek (`hata oranı iyileşti`)
- `Başarı elde etmek` gibi yerleşik kullanımları da yasaklamak

## Yapısal beklenti

- cümle: <= 2
