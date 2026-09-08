# Teknik belgede yararlı özne tekrarı

## Kaynak

Denetleyici komutu doğrular. Denetleyici komutu uygular. Denetleyici uygulama sonucunu günlüğe yazar. Bu üç adım ayrı ayrı kaydedilir; herhangi biri başarısız olursa denetleyici kalan adımları çalıştırmaz ve `E-41` hata kodunu döndürür.

## Talep

Teknik belge. Standart düzeyde düzenle; metin çeviri gibi durmasın.

## Korunması gerekenler

- Üç adımın ayrı ayrı kaydedildiği kaynakta açıkça belirtildiği için üç ayrı cümle ve yinelenen "Denetleyici" öznesi korunabilmeli.
- Herhangi bir adım başarısız olursa kalan adımların çalıştırılmadığı ve `E-41` kodunun döndürüldüğü korunmalı.
- Adım sırası korunmalı.
- Metin zaten doğalsa olduğu gibi bırakılabilmeli.

## Kaçınılması gerekenler

- Üç adımı "denetleyici komutu doğrulayıp uygular ve sonucu günlüğe yazar" biçiminde tek cümleye birleştirmek
- "Denetleyici" öznesini düşürmek veya eş anlamlılarla çeşitlendirmek
- `E-41` kodunu değiştirmek
- Başarısızlık koşulunu silmek veya genel bir uyarıya çevirmek
- Kaynakta bulunmayan zaman aşımı, yeniden deneme veya günlük biçimi eklemek

## Yapısal beklenti

- sert işaret: 0
- düzyazı paragrafı: 1
- cümle: 4
