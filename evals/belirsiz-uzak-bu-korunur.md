# Belirsiz uzak mesafeli "bu"

## Kaynak

Filtre kazancı 0,5'e çıkarıldı. Gözlemci 50 Hz'de çalıştırıldı. Sensör 40 °C'de sürüklendi. Denetleyici komutu 10 ms içinde üretti. Bu, yakınsama süresini 18 saniyeye düşürdü.

## Talep

Mühendislik notu. Standart düzeyde düzenle; yalnızca son metni ver.

## Korunması gerekenler

- Son cümledeki "bu" göndergesi kaynakta dört olası öncül arasında belirsiz olduğu için belirsizlik korunmalı ya da kullanıcıdan açıklama istenmeli.
- 0,5, 50 Hz, 40 °C, 10 ms ve 18 saniye korunmalı.
- Metin belirsizlik korunarak olduğu gibi bırakılabilmeli.

## Kaçınılması gerekenler

- Göndergeyi rastgele bir öncüle ("kazanç artışı yakınsamayı düşürdü") çözmek
- Dört olguyu tek nedene bağlamak
- Son cümleyi silmek
- Kaynakta bulunmayan mekanizma eklemek

## Yapısal beklenti

- sert işaret: 0
- cümle: 5
