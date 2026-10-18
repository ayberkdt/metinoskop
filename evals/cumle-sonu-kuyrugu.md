# Cümle sonuna eklenmiş değerlendirme kuyruğu

## Kaynak

Yeni önbellek katmanı ortalama yanıt süresini 800 ms'den 240 ms'ye indirdi, kullanıcı deneyimini önemli ölçüde iyileştirerek. Hata oranı %2,1'den %1,4'e düştü, bu da sistemin güvenilirliğinin arttığını göstermektedir. Bellek kullanımı ise 1,2 GB'tan 1,8 GB'a çıktı, sunucu maliyetlerinde artışa yol açarak. Ekip, ölçümleri üç gün boyunca tekrarlayarak sonuçları doğruladı.

## Talep

Bu metni geliştir.

## Korunması gerekenler

- 800 ms → 240 ms, %2,1 → %1,4 ve 1,2 GB → 1,8 GB ölçümleri korunmalı.
- Bellek artışının sunucu maliyetini yükselttiği bilgisi korunmalı; bu, kuyrukta duran ama önerme taşıyan bir bilgidir ve öznesi ve yüklemiyle kurulmalı.
- Ölçümlerin üç gün boyunca tekrarlandığı ve sonuçların doğrulandığı korunmalı; yüklemden önce gelen `tekrarlayarak` doğal zarf-fiildir.
- Hata oranındaki düşüş kaynakta önbelleğe bağlanmıyor; düzenleme de bağlamamalı.

## Kaçınılması gerekenler

- Virgülden sonra `-arak/-erek` ile biten cümle (`…indirdi, … iyileştirerek.`) ya da `, bu da …` eki bırakmak
- `kullanıcı deneyimini önemli ölçüde iyileştirerek` ve `sistemin güvenilirliğinin arttığını göstermektedir` değerlendirmelerini korumak ya da başka sözcüklerle yeniden kurmak; ikisi de ölçülmemiş bir sonuca varıyor
- Hata oranındaki düşüşü önbellek katmanının öznesine bağlamak (`yanıt süresini ve hata oranını indirdi`)
- Doğal zarf-fiili (`tekrarlayarak doğruladı`) kuyruk sanıp bozmak
- Kaynakta olmayan neden, oran ya da maliyet tutarı eklemek

## Yapısal beklenti

- cümle sonu kuyruğu: 0
- sert işaret: 0
- cümle: <= 4
