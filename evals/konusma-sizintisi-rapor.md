# Ajan raporuna sızan konuşma

## Kaynak

İstediğin gibi önbellek sorununu inceledim. Önce `cache.py` dosyasına baktım, sonra yük testini çalıştırdım. Verdiğin günlük dosyasına göre 14 Ekim'deki 37 zaman aşımının 29'u önbellek yenilemesiyle aynı dakikada oluştu. Burada sunucu saatlerinin senkron olduğunu varsaydım; bunu doğrulayamadım.

Yenileme aralığını 5 dakikadan 15 dakikaya çıkarırsak zaman aşımları azalabilir. İstersen bir sonraki adımda bunu deneyebilirim ya da yük testini tekrarlayabiliriz. Umarım faydalı olur!

## Talep

Bu raporu ekip liderine gönderilecek hâle getir.

## Korunması gerekenler

- `cache.py` incelemesi ve yük testinin çalıştırılması yöntem bilgisi olarak korunmalı; ajanın çalışma sırası (`önce ... sonra`) gerekmez.
- 14 Ekim, 37 zaman aşımı, bunların 29'unun önbellek yenilemesiyle aynı dakikada oluşması korunmalı; bilginin günlük kayıtlarına dayandığı anlaşılmalı.
- Sunucu saatlerinin senkron olduğu varsayımı ve bu varsayımın doğrulanmadığı korunmalı.
- 5 ve 15 dakika, koşul (`çıkarılırsa`) ve olasılık (`azalabilir`) korunmalı.
- Metin, konuşmayı görmemiş ekip liderine olduğu gibi gönderilebilmeli.

## Kaçınılması gerekenler

- `istediğin gibi`, `verdiğin`, `istersen`, `deneyebilirim`, `tekrarlayabiliriz`, `Umarım faydalı olur` ya da başka bir konuşma göndermesi, kullanıcıya teklif veya kapanış nezaketi bırakmak
- `inceledim`, `baktım`, `varsaydım` gibi ilk tekil şahıs süreç anlatımını bırakmak
- Varsayımı ya da doğrulanmadığını ajanın sesi sayıp silmek
- `azalabilir` olasılığını `azaltır`, `çıkarılmalıdır` ya da `çıkarılacak` biçimine yükseltmek
- `biz` yerine kaynakta adı geçmeyen bir aktör (`ekip`, `yönetim`) yazmak
- Yük testinin sonucunu ya da zaman aşımlarının nedenini kaynakta olmadan yazmak
- Metne `İşte rapor` girişi, değişiklik açıklaması ya da kullanıcıya not eklemek

## Yapısal beklenti

- konuşma sızıntısı: 0
- sert işaret: 0
- cümle: <= 5
