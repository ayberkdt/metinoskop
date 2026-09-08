# Fazla `bir`

## Kaynak

Bu, bir sensörden gelen bir veri akışını bir filtreden geçirerek bir tahmin üreten bir yöntemdir. Yöntem bir başlangıç değeri, bir gürültü modeli ve bir güncelleme adımı gerektirmektedir. Her bir güncelleme adımında bir ölçüm alınmakta ve bir düzeltme uygulanmaktadır. Yöntem tek bir sensörle sınanmıştır; birden fazla sensörle henüz sınanmamıştır.

## Talep

Teknik açıklama. Standart düzeyde düzenle.

## Korunması gerekenler

- Yöntemin bir sensörden gelen veriyi filtreden geçirip tahmin ürettiği korunmalı.
- Üç gereksinim (başlangıç değeri, gürültü modeli, güncelleme adımı) korunmalı.
- Her güncelleme adımında ölçüm alınıp düzeltme uygulandığı korunmalı.
- "Tek bir sensörle sınandı" ifadesindeki sayı anlamı ve "birden fazla sensörle henüz sınanmadı" sınırı korunmalı.
- Sayı ya da gerçek tekillik bildiren `bir` (tek bir sensör) silinmemeli.

## Kaçınılması gerekenler

- İlk cümledeki beş `bir` sözcüğünü olduğu gibi bırakmak
- Bütün `bir` sözcüklerini, sayı bildirenler dahil, mekanik olarak silmek
- "Tek bir sensörle" ifadesini "sensörlerle" veya "bir sensörle" biçimine indirgemek
- `Henüz` sınırını silmek veya sınamayı plana çevirmek
- Kaynakta bulunmayan filtre türü, sensör sayısı veya başarım bilgisi eklemek

## Yapısal beklenti

- sert işaret: 0
- bir / 100 sözcük: <= 6
