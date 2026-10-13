# Doğru ama yanlış paragrafta duran cümleler

## Kaynak

## Yöntem

Modeller 2.000 örnekle eğitildi ve öğrenme oranı 0,001'de sabit tutuldu. En küçük model test kümesinde %9,8 hata verdi. Hiperparametreler beş katlı çapraz doğrulamayla seçildi.

## Bulgular

En iyi model test kümesinde %4,2 hata verdi. Test kümesi eğitimde hiç kullanılmayan 500 örnekten oluşuyordu. Hata, model büyüdükçe azaldı.

## Talep

Makalemin bu iki bölümünü düzenle; cümleler tek tek iyi ama bir şey oturmuyor.

## Korunması gerekenler

- İki başlık ve sırası korunmalı.
- Her cümlenin önermesi korunmalı: 2.000 eğitim örneği, 0,001 öğrenme oranı, beş katlı çapraz doğrulama, 500 örneklik test kümesi, en iyi model %4,2, en küçük model %9,8, hatanın model büyüdükçe azalması.
- En küçük modelin test hatası bulgulara, test kümesinin tanımı yönteme taşınabilmeli; düzeltme cümleleri yeniden yazmak değil, yerine koymaktır.

## Kaçınılması gerekenler

- Cümleleri yerinde bırakıp yalnızca sözcüklerini değiştirmek
- Test hatalarından birini ya da test kümesinin tanımını silmek
- Hatanın azalmasına neden eklemek (`büyük modeller daha iyi genelleştiği için`)
- `En iyi model` ile `en büyük model` arasında kaynakta kurulmamış bir eşitlik kurmak
- Başlıkları birleştirmek

## Yapısal beklenti

- sert işaret: 0
- başlık: 2
- cümle: <= 6
