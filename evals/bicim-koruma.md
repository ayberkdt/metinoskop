# Biçim koruma

## Kaynak

### Sonuçlar

| Model | Hata |
|---|---:|
| A | %4,2 |
| B | %3,8 |

Ayrıntılar için [rapora](https://example.com/report) bakın. `max_iter=500` kullanılmıştır.[^1]

[^1]: Deney 12 Temmuz 2026'da yürütüldü.

## Talep

Metni doğal Türkçeyle düzenle; Markdown yapısını ve teknik gösterimleri koru.

## Korunması gerekenler

- `### Sonuçlar` başlık düzeyi korunmalı.
- Tablo satırları, sütunları ve hücre eşleşmeleri korunmalı.
- Bağlantı metni ile `https://example.com/report` URL'si değişmemeli.
- `max_iter=500` satır içi kod olarak kalmalı.
- `[^1]` dipnot işareti ve dipnot içeriği korunmalı.
- `%4,2`, `%3,8` ve `12 Temmuz 2026` gösterimleri değişmemeli.

## Kaçınılması gerekenler

- Tablo hücrelerini veya model-hata eşleşmelerini yer değiştirmek
- URL'yi değiştirmek
- Kod ifadesini Türkçeleştirmek ya da kod biçimini kaldırmak
- Dipnotu bağlı olduğu iddiadan ayırmak
- Yüzde veya ondalık gösterimini bozmak
- Başlığı farklı bir düzeye taşımak
