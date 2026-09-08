# Akışı iyileştiren özne düşürme

## Kaynak

Yeni sürüm 3 Eylül'de yayımlandı. Yeni sürüm açılış süresini 4,2 saniyeden 1,9 saniyeye düşürdü. Yeni sürüm ayrıca iki bilinen hatayı giderdi. Yeni sürüm henüz tüm kullanıcılara dağıtılmadı; dağıtım kademeli yapılıyor. Yeni sürümün bellek kullanımı ölçülmedi.

## Talep

Sürüm notu. Standart düzeyde düzenle.

## Korunması gerekenler

- 3 Eylül, 4,2 saniye, 1,9 saniye ve iki hata korunmalı.
- Sürümün `henüz` tüm kullanıcılara dağıtılmadığı ve dağıtımın kademeli yapıldığı korunmalı.
- Bellek kullanımının ölçülmediği korunmalı.
- Tek aktör (yeni sürüm) olduğu için özne düşürüldüğünde belirsizlik doğmamalı; ilk cümlede sürüm açıkça adlandırılmalı.

## Kaçınılması gerekenler

- Beş cümlenin her birini "Yeni sürüm" ile başlatmayı sürdürmek
- Özneyi "güncelleme", "yeni yapı", "bu sürüm" gibi eş anlamlılarla çeşitlendirmek
- Bütün cümleleri tek `-ip` zincirine sıkıştırmak
- Dağıtım sınırını silmek veya "dağıtım tamamlandı" diye yazmak
- Kaynakta bulunmayan hata açıklaması, dağıtım tarihi veya bellek değeri eklemek

## Yapısal beklenti

- ardışık özne: 0
- fiilimsi yığını: 0
- sert işaret: 0
