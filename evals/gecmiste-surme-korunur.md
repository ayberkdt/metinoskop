# Geçmişte süren eylem korunur

## Kaynak

14 Mayıs testinde basınç düşerken pompa hâlâ çalışıyordu. Operatör alarmı 03.12'de fark etti ve ana vanayı kapattı. Kapatma anında yedek hat devrede değildi. Yedek hattın neden devrede olmadığı henüz belirlenmedi.

## Talep

Olay raporu paragrafı. Standart düzeyde düzenle.

## Korunması gerekenler

- `Çalışıyordu` geçmişte süren artalan eylemi bildirir; basınç düşüşüyle eş zamanlılığı korumalı.
- 14 Mayıs, 03.12 ve olay sırası korunmalı.
- `Henüz belirlenmedi` çözümsüzlük bildirir; olumsuz bir sonuca çevrilmemeli.
- Metin zaten doğalsa olduğu gibi bırakılabilmeli.

## Kaçınılması gerekenler

- `Çalışıyordu` biçimini `çalıştı` yapıp süren eylemi sınırlı olaya çevirmek
- `Çalışıyordu` biçimini `çalışıyor` yapıp geçmiş olayı şimdiye taşımak
- Eş zamanlılığı sıralı olaya çevirmek (`önce basınç düştü, sonra pompa çalıştı`)
- Yedek hattın devrede olmama nedenini uydurmak ya da `henüz` sözcüğünü silmek

## Yapısal beklenti

- cümle: 4
- sert işaret: 0
