# Doğru ama alışılmadık hâl çerçevesi korunur

## Kaynak

Sistem bu hatadan etkilenmez; yalnızca gecikmeye duyarlıdır. Gecikme 20 ms'yi aştığında kestirim hatası 2 kat artar.

## Talep

Teknik belge. Standart düzeyde düzenle; sözcükler doğal birleşsin.

## Korunması gerekenler

- Çıkma hâli ("hatadan etkilenmez") ve yönelme hâli ("gecikmeye duyarlıdır") iki ayrı ilişki kurduğu için korunmalı.
- `Yalnızca`, 20 ms ve 2 kat korunmalı.
- Metin zaten doğalsa olduğu gibi bırakılabilmeli.

## Kaçınılması gerekenler

- "Hatayı etkilemez" gibi hâl değiştirip ilişkiyi tersine çevirmek
- "Gecikmeden etkilenir" gibi duyarlılığı başka ilişkiye çevirmek
- Kapsam sınırını silmek
- Kaynakta bulunmayan eşik ya da neden eklemek

## Yapısal beklenti

- sert işaret: 0
- cümle: 2
