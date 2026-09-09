# Geçmişteki düzenli davranış korunur

## Kaynak

Önceki sürüm her çevrimde bu kontrolü yapardı. Yeni sürümde kontrol yalnızca başlangıçta çalışıyor. Değişikliğin nedeni sürüm notlarında belirtilmedi.

## Talep

Teknik değişiklik notu. Standart düzeyde düzenle.

## Korunması gerekenler

- `Yapardı` geçmişteki düzenli davranışı bildirir; tek seferlik olaya da bugünkü davranışa da çevrilmemeli.
- `Yalnızca başlangıçta` kapsam sınırı korunmalı.
- Eski ve yeni sürüm karşıtlığı korunmalı.
- Nedenin belirtilmediği korunmalı.

## Kaçınılması gerekenler

- `Yapardı` biçimini `yaptı` yapıp alışkanlığı tek olaya indirmek
- `Yapardı` biçimini `yapar` yapıp geçmiş alışkanlığı bugüne taşımak
- Kaynakta bulunmayan bir değişiklik gerekçesi eklemek
- `Yalnızca` sınırını silip yeni sürümün davranışını genişletmek

## Yapısal beklenti

- cümle: 3
- sert işaret: 0
