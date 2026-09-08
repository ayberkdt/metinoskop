# AGENTS.md

Bu depo, Türkçe metinleri doğal ve kaynak sadakatini koruyan bir dille düzenleyen taşınabilir `metinoskop` agent skill'ini içerir.

## Temel dosyalar

- `SKILL.md`: Çalışma zamanında yüklenen ana skill yönergesi ve temel davranış sözleşmesidir.
- `references/turkce-oruntuler.md`: Türkçedeki mekanik yapay zekâ örüntülerini ve bağlama duyarlı düzeltme örneklerini içerir.
- `references/akicilik.md`: Bilgi sırası, cümleler arası bağ, gönderge açıklığı ve paragraf akışı rehberidir.
- `references/rapor-yazimi.md`: Raporlarda bölüm işlevi, kanıt zinciri, bulgu–yorum–öneri ayrımı ve yönetici özeti rehberidir.
- `references/retorik-yapilar.md`: Cümle, paragraf ve belge düzeyindeki yapay düzyazı mimarisinin işlev ailelerine göre kataloğu, türlere göre zorlu önce/sonra örnekleri ve kalması gereken karşı örneklerdir.
- `references/yapisal-butunluk.md`: Başlık, paragraf ve bölüm sınırlarının kavramsal sınırları izlemesi; bölme testleri, parçalanma yoğunluğu, yakınlık kuralı, yapay gerilim, çapraz gönderme, listeleştirme, uzun ifade katalogları, yapısal onarım örnekleri ve korunması gereken yapı karşı örnekleridir.
- `references/kavramsal-girisler.md`: Temel kavramlar için bağlam, problem, soru ve çözüm akışı kurma rehberidir.
- `agents/openai.yaml`: Destekleyen istemciler için kullanıcı arayüzü metadata'sıdır.
- `README.md`: İnsanlar için kurulum, kullanım, kapsam ve depo yapısı belgesidir.
- `evals/`: Sabit çıktı dayatmayan davranışsal değerlendirme vakalarını içerir.
- `scripts/eval-runner.py`: Model çıktısındaki kaynak değişmezlerini bağımlılık kullanmadan denetler.
- `scripts/style-lint.py`: Model çıktısındaki şüpheli retorik ve yapısal örüntüleri işlev ailesine göre işaretler; tek başına reddetmez, `--source` ile yeni eklenen kalıpları sert/bağlamsal ayrımıyla listeler.
- `scripts/eval-suite.py`: `evals/outputs/` altındaki kayıtlı referans çıktılar üzerinde değişmez, sert kalıp ve yapısal beklenti denetimi yapar; CI'da çalışır ve model hakem istemi üretebilir.
- `scripts/validate-package.py`: Paket yapısını ve adlandırma tutarlılığını bağımlılık kullanmadan doğrular.
- `LICENSE`: Paketin MIT Lisansı altında kullanılma, değiştirilme ve dağıtılma koşullarını belirtir.
- `CHANGELOG.md`: Sürümler arasındaki kullanıcıya dönük davranış ve paket değişikliklerini kaydeder.

## Bakım sözleşmesi

- `SKILL.md` davranışını değiştirdiğinizde README'deki özellik, kapsam ve örneklerin hâlâ doğru olduğunu kontrol edin.
- Skill adını her yüzeyde `metinoskop`, açık çağrıyı `$metinoskop` olarak koruyun.
- YAML frontmatter'da yalnızca `name` ve `description` alanlarını kullanın.
- Yeni ayrıntılı örüntüleri ana dosyaya yığmak yerine uygun `references/` dosyasına ekleyin. Sözcük ve kalıp düzeyi `turkce-oruntuler.md`, cümle, paragraf ve belge düzeyi `retorik-yapilar.md` dosyasına gider.
- Yeni retorik kalıpları tek tek yasaklanan sözcük listesi olarak değil, işlev ailesi olarak ekleyin; `SKILL.md`'de yalnızca ilke ve kısa tetikleyici listesi tutun.
- Silinen dolguyu daha sakin eş anlamlılarla geri koyan örnek eklemeyin. Bir "sonra" sürümü cümle siliyorsa silinen her cümlenin önerme taşımadığını örnek açıklamasında gösterin.
- Adlandırılmış sınırlılığı, ölçülmüş yöntem gerekçesini, kaynaktaki yazar değerlendirmesini veya yeni başlayanlara yönelik öğretici açıklamayı silen örnek eklemeyin.
- Yapısal örneklerde bölümleri sırf sayıyı azaltmak için birleştiren, paragrafı sırf uzun diye bölen veya tekrarlanabilirlik, mevzuat, dergi kuralı ve güvenlik adımlarının gerektirdiği ayrımı kaldıran dönüşüm eklemeyin. Her birleştirmenin hangi kavramsal sınıra dayandığını örnek açıklamasında gösterin.
- `SKILL.md` kendi yapı kuralına uymalıdır: dördüncü düzey başlık kullanmayın, her küçük kavrama `###` açmayın; ilişkili kuralları kalın başlangıçlı paragraflarla tek alt bölümde tutun. Doğrulayıcı bunu denetler.
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
- Sıfır bilgi cümlesi, savunmacı düzyazı, tekrar döngüsü, yol haritası, yapay denge, kalıp giriş ve sonuç, soyut yüklem, paragraf simetrisi, yanlış pozitif (`gerekli-ifade`), muhatap duyarlılığı (`egitsel-aciklama`) ve iyi metin (`iyi-metin`) davranışlarını karşılık gelen eval vakalarıyla koruyun.
- Yapısal davranışı aşırı bölümleme, başlık derinliği, tek paragraflık bölüm, kısa paragraf yığını, yapay gerilim, tekrarlanan bölüm giriş ve sonuçları, çapraz gönderme, uzun çerçeve, ayrılmış kanıt ve listeleştirme vakalarıyla; koruma davranışını `korunacak-basliklar`, `yontem-ayrimi`, `uzun-paragraf-korunur`, `kisa-paragraf-korunur` ve `yapisal-iyi-metin` vakalarıyla koruyun.
- `scripts/style-lint.py` kataloğuna aile eklerken öz sınamadaki yapay ve temiz metinleri güncelleyin; temiz metin sert bastırma ailesinde işaret üretmemelidir. Bağlama duyarlı bir aileyi `sert` düzeyine taşımayın; `--fail-on-introduced-hard` yalnızca sert aileler için deterministik hata verir.
- Yeni eval eklerken mümkünse `evals/outputs/<vaka>.txt` referans çıktısı ve `## Yapısal beklenti` bölümü ekleyin; yapısı korunacak vakalarda kaynağı olduğu gibi kaydedin. `python scripts/eval-suite.py` geçmeden commit oluşturmayın.
- Davranış kuralı değiştiğinde ilgili eval vakasını güncelleyin veya yeni bir vaka ekleyin.
- Kullanıcıya dönük davranış veya paket yapısı değiştiğinde `CHANGELOG.md` dosyasını güncelleyin.
- `SKILL.md` dosyasını 500 satırın altında tutun.
- Skill'i belirli bir agent ürününe gereksiz yere bağlamayın; ürün özelindeki metadata'yı `agents/` altında tutun.

## Değişiklik öncesi kontroller

Şu komutları çalıştırın:

```bash
python scripts/validate-package.py
python scripts/eval-runner.py --self-test
python scripts/style-lint.py --self-test
python scripts/eval-suite.py
npx --yes skills@1.5.20 add . --list
```

Doğrulama başarısızsa commit oluşturmayın. Yeni veya değişmiş örnekleri ayrıca kaynak sadakati ve örtük nedensellik açısından elle inceleyin.
