# AGENTS.md

Bu depo, Türkçe metinleri doğal ve kaynak sadakatini koruyan bir dille düzenleyen taşınabilir `metinoskop` agent skill'ini içerir.

## Temel dosyalar

- `SKILL.md`: Çalışma zamanında yüklenen ana skill yönergesi ve tek davranış kaynağıdır.
- `references/turkce-oruntuler.md`: Türkçedeki mekanik yapay zekâ örüntülerini ve bağlama duyarlı düzeltme örneklerini içerir.
- `references/akicilik.md`: Bilgi sırası, cümleler arası bağ, gönderge açıklığı ve paragraf akışı rehberidir.
- `agents/openai.yaml`: Destekleyen istemciler için kullanıcı arayüzü metadata'sıdır.
- `README.md`: İnsanlar için kurulum, kullanım, kapsam ve depo yapısı belgesidir.
- `scripts/validate-package.py`: Paket yapısını ve adlandırma tutarlılığını bağımlılık kullanmadan doğrular.

## Bakım sözleşmesi

- `SKILL.md` davranışını değiştirdiğinizde README'deki özellik, kapsam ve örneklerin hâlâ doğru olduğunu kontrol edin.
- Skill adını her yüzeyde `metinoskop`, açık çağrıyı `$metinoskop` olarak koruyun.
- YAML frontmatter'da yalnızca `name` ve `description` alanlarını kullanın.
- Yeni ayrıntılı örüntüleri ana dosyaya yığmak yerine uygun `references/` dosyasına ekleyin.
- Kaynakta bulunmayan olgu, tarih, sayı, alıntı, nedensellik veya kişisel ayrıntı üreten örnek eklemeyin.
- Bir örneğin "sonra" sürümündeki her önermenin "önce" sürümünde karşılığı bulunmalıdır.
- `SKILL.md` dosyasını 500 satırın altında tutun.
- Skill'i belirli bir agent ürününe gereksiz yere bağlamayın; ürün özelindeki metadata'yı `agents/` altında tutun.

## Değişiklik öncesi kontroller

Şu komutları çalıştırın:

```bash
python scripts/validate-package.py
npx --yes skills@1.5.20 add . --list
```

Doğrulama başarısızsa commit oluşturmayın. Yeni veya değişmiş örnekleri ayrıca kaynak sadakati ve örtük nedensellik açısından elle inceleyin.
