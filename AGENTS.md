# AGENTS.md

Bu depo, Türkçe metinleri doğal ve kaynak sadakatini koruyan bir dille düzenleyen taşınabilir `metinoskop` agent skill'ini içerir.

## Temel dosyalar

- `SKILL.md`: Çalışma zamanında yüklenen ana skill yönergesi ve temel davranış sözleşmesidir.
- `references/turkce-oruntuler.md`: Türkçedeki mekanik yapay zekâ örüntülerini ve bağlama duyarlı düzeltme örneklerini içerir.
- `references/akicilik.md`: Bilgi sırası, cümleler arası bağ, gönderge açıklığı ve paragraf akışı rehberidir.
- `references/rapor-yazimi.md`: Raporlarda bölüm işlevi, kanıt zinciri, bulgu–yorum–öneri ayrımı ve yönetici özeti rehberidir.
- `references/kavramsal-girisler.md`: Temel kavramlar için bağlam, problem, soru ve çözüm akışı kurma rehberidir.
- `agents/openai.yaml`: Destekleyen istemciler için kullanıcı arayüzü metadata'sıdır.
- `README.md`: İnsanlar için kurulum, kullanım, kapsam ve depo yapısı belgesidir.
- `evals/`: Sabit çıktı dayatmayan davranışsal değerlendirme vakalarını içerir.
- `scripts/eval-runner.py`: Model çıktısındaki kaynak değişmezlerini bağımlılık kullanmadan denetler.
- `scripts/validate-package.py`: Paket yapısını ve adlandırma tutarlılığını bağımlılık kullanmadan doğrular.
- `LICENSE`: Paketin MIT Lisansı altında kullanılma, değiştirilme ve dağıtılma koşullarını belirtir.
- `CHANGELOG.md`: Sürümler arasındaki kullanıcıya dönük davranış ve paket değişikliklerini kaydeder.

## Bakım sözleşmesi

- `SKILL.md` davranışını değiştirdiğinizde README'deki özellik, kapsam ve örneklerin hâlâ doğru olduğunu kontrol edin.
- Skill adını her yüzeyde `metinoskop`, açık çağrıyı `$metinoskop` olarak koruyun.
- YAML frontmatter'da yalnızca `name` ve `description` alanlarını kullanın.
- Yeni ayrıntılı örüntüleri ana dosyaya yığmak yerine uygun `references/` dosyasına ekleyin.
- Kaynakta bulunmayan olgu, tarih, sayı, alıntı, nedensellik veya kişisel ayrıntı üreten örnek eklemeyin.
- Bir örneğin "sonra" sürümündeki her önermenin "önce" sürümünde karşılığı bulunmalıdır.
- "Sonra" sürümü hedeflenen ilkeyi görünür biçimde uygulamalıdır; yalnızca noktalama veya tek bir bağlaç değişikliği yeterli değildir.
- Belirsiz aktörü veya göndergeyi açıklığa kavuştururken kaynakta bulunmayan bir cevap seçmeyin.
- Belirsizlik korunabiliyorsa koruyun; yorum seçimi zorunluysa kullanıcıdan açıklama isteyin.
- Olumsuzluk, koşul, istisna, nicelik sınırı ve kapsam belirleyicilerini dilsel dolgu gibi çıkarmayın.
- Teknik terim, kısaltma, sembol, birim, denklem numarası ve büyük-küçük harf tercihlerini tutarlı koruyun.
- Rapor örneklerinde bulguyu yoruma, yorumu öneriye, öneriyi karar veya gerçekleşmiş sonuca dönüştürmeyin.
- Raporun tablo, atıf, dipnot, başlık ve çapraz göndermelerini destekledikleri içerikle birlikte koruyun.
- Yönetici özeti vakalarında gövdede bulunmayan çıkarım, fayda, risk veya eylem üretmeyin.
- Skill'i kaynak dilden çeviri yapacak biçimde genişletmeyin; kapsam Türkçeye çevrilmiş mevcut metni düzenlemektir.
- Kavramsal girişi yalnızca kullanıcı açıkça giriş yazılmasını istediğinde devreye alın; kaynakta bulunmayan problem, risk, aciliyet veya çözüm vaadi üretmeyin.
- Doğal metni değiştirmeme ilkesini `evals/degisiklik-butcesi.md` vakasıyla koruyun.
- Belirsizlik, kapsam, üslup, biçim ve teknik gösterim kurallarını karşılık gelen eval vakalarıyla koruyun.
- Rapor davranışını bulgu–yorum–öneri, yapısal bütünlük ve yönetici özeti eval'leriyle koruyun.
- Davranış kuralı değiştiğinde ilgili eval vakasını güncelleyin veya yeni bir vaka ekleyin.
- Kullanıcıya dönük davranış veya paket yapısı değiştiğinde `CHANGELOG.md` dosyasını güncelleyin.
- `SKILL.md` dosyasını 500 satırın altında tutun.
- Skill'i belirli bir agent ürününe gereksiz yere bağlamayın; ürün özelindeki metadata'yı `agents/` altında tutun.

## Değişiklik öncesi kontroller

Şu komutları çalıştırın:

```bash
python scripts/validate-package.py
python scripts/eval-runner.py --self-test
npx --yes skills@1.5.20 add . --list
```

Doğrulama başarısızsa commit oluşturmayın. Yeni veya değişmiş örnekleri ayrıca kaynak sadakati ve örtük nedensellik açısından elle inceleyin.
