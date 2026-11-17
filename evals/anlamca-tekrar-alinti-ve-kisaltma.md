# Alıntı sözcükte ve kısaltmada anlam tekrarı

## Kaynak

Kullanıcı ATM makinesinde PIN numarasını üç kez yanlış girdi. Sistem SMS mesajıyla uyarı gönderdi ve kartı geri iade etmedi. Ekip, yanlış girişleri ayırmak için en optimum eşiği 0,35 olarak belirledi; eşik IP adresi ve cihaz kimliğiyle birlikte API arayüzü üzerinden kaydediliyor.

## Talep

Olay inceleme notu. Standart düzeyde düzenle.

## Korunması gerekenler

- Kısaltmanın açılımının baş sözcüğünü yineleyen ad silinmeli: `ATM makinesi` → `ATM`, `PIN numarası` → `PIN`, `API arayüzü` → `API`.
- Alıntı sözcüğün anlamında bulunan öge silinmeli: `geri iade` → `iade`, `en optimum` → `optimum` ya da `en uygun`.
- `IP adresi` ve `SMS mesajı` korunabilmeli: açılımların başı (Internet **Protocol**, Short Message **Service**) `adres` ve `mesaj` değildir; ikisi tekrar sayılmaz.
- Üç kez, 0,35 ve olumsuzluk (`iade etmedi`) korunmalı; eşiğin amacı (`yanlış girişleri ayırmak için`) korunmalı.
- `Belirledi` kararı ve `kaydediliyor` güncel durumu korunmalı.

## Kaçınılması gerekenler

- `IP adresi` ifadesini `IP` diye kısaltmak
- `0,35` sayısını `0.35` biçimine çevirmek ya da eşiği yuvarlamak
- Kartın neden iade edilmediğini ya da uyarının içeriğini uydurmak
- `Optimum` eşiği ölçülmüş en iyi değer gibi güçlendirmek (`en doğru sonucu veren eşik`)
- Kısaltmaları açılımlarıyla uzun uzun yazıp metni şişirmek

## Yapısal beklenti

- sert işaret: 0
- cümle: <= 3
