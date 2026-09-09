# Yerel hata ile hata sınıfı

## Kaynak

Günlükteki bu hata bağlantının koptuğunu gösterir. Bu tür hatalar her zaman bağlantı kaybını göstermez; zaman aşımı da aynı kaydı üretir.

## Talep

Arıza çözümleme notu; ilk cümle günlükte görülen tek bir kaydı, ikinci cümle hata sınıfının genel davranışını anlatıyor.

## Korunması gerekenler

- İlk cümle belirli bir kaydı yorumluyor; ikinci cümle bir hata sınıfı hakkında genel bir iddia.
- İkinci cümlenin geniş zamanı ve olumsuzluğu (`göstermez`) korunmalı.
- `Her zaman` kapsam belirtisi korunmalı.
- Zaman aşımının aynı kaydı ürettiği bilgisi korunmalı.

## Kaçınılması gerekenler

- İki cümleyi aynı kipe eşitlemek
- Yerel yorumu geniş zamanla genel kurala yükseltmek
- Genel iddiayı tek bir kayda indirgemek
- Olumsuzluğu ya da `her zaman` sınırını silmek

## Yapısal beklenti

- cümle: <= 2
