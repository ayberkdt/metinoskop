# Etiketle açılan cümle ve anons

## Kaynak

## Önbellek mi, tampon mu?

**Kısa cevap:** İkisi farklı işler yapar.

**Kavramsal ayrım:** Önbellek sık okunan veriyi saklar. Tampon ise veriyi iki bileşen arasında aktarırken geçici olarak tutar.

**Sezgisel açıklama:** Aynı veri ikinci kez istendiğinde önbellek onu yeniden hesaplatmaz.

**Detaylı açıklama:** Sistemimizde önbellek Redis üzerinde çalışır ve kayıtları 10 dakika tutar. Tampon, günlük yazıcısının önünde 4 MB'lık bir kuyruk olarak durur.

Merak etmeyin, ikisini de yapılandırmak kolay. Bu yazıda ikisinin ayarlarını adım adım öğreneceksiniz.

## Talep

Bu README bölümünü geliştir.

## Korunması gerekenler

- Ayrımın iki tarafı (önbellek sık okunan veriyi saklar; tampon aktarım sırasında geçici tutar), ikinci istekte yeniden hesaplatmama, Redis, 10 dakika, 4 MB ve günlük yazıcısı korunmalı.
- Etiketin altındaki bilgi taşıyan cümle etiketsiz kalmalı; yalnızca etiket gider.
- `Kısa cevap` cümlesi ayrımın kendisi yazıldığında bilgi taşımaz.

## Kaçınılması gerekenler

- `Kısa cevap:`, `Kavramsal ayrım:`, `Sezgisel açıklama:`, `Detaylı açıklama:` etiketlerini kalın, başlık, madde ya da başka bir etiketle (`Özetle:`, `Temel fark:`) korumak
- `Merak etmeyin` güvencesini ve `kolay` değerlendirmesini korumak; metinde olmayan ayarları `bu yazıda öğreneceksiniz` diye duyurmak
- Etiketi silip yerine `İki kavram arasındaki temel fark şudur` gibi duyuru cümlesi yazmak
- Kaynakta olmayan yapılandırma adımı, süre ya da boyut eklemek

## Yapısal beklenti

- etiketli cümle: 0
- anons cümlesi: 0
- sert işaret: 0
- cümle: <= 5
