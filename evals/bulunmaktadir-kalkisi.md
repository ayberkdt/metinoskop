# `Bulunmaktadır` kalkısı

## Kaynak

Tabloda üç farklı hata türü bulunmaktadır. Her hata türü için ayrı bir eşik değeri yer almaktadır. Sistemde iki çalışma kipi mevcuttur. Yapılandırma dosyası dört zorunlu alan içermektedir. Bu alanlardan biri için varsayılan değer bulunmamaktadır; kullanıcı bu alanı doldurmak zorundadır.

## Talep

Teknik belge. Standart düzeyde düzenle; varlık kalıplarını doğrudan Türkçe ilişkiyle kur.

## Korunması gerekenler

- Üç hata türü, her biri için ayrı eşik, iki çalışma kipi ve dört zorunlu alan korunmalı.
- Bir alanın varsayılan değeri bulunmadığı ve kullanıcının onu doldurmak zorunda olduğu korunmalı; zorunluluk korunmalı.
- Teknik ton korunmalı.

## Kaçınılması gerekenler

- Beş cümlenin hepsini `bulunmaktadır`, `yer almaktadır`, `mevcuttur`, `içermektedir` ile bırakmak
- Tablonun ne yaptığı kaynakta belirtilmediği hâlde "tablo üç hata türünü karşılaştırır" gibi işlev uydurmak
- Varsayılan değeri olmayan alanı silmek veya zorunluluğu öneriye çevirmek
- Kaynakta bulunmayan hata türü adı, eşik değeri, kip adı veya alan adı eklemek
- Metni tek uzun cümleye sıkıştırmak

## Yapısal beklenti

- varlık kalıbı: <= 1
- sert işaret: 0
