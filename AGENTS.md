# AGENTS.md

Bu depo, Türkçe metinleri doğal ve kaynak sadakatini koruyan bir dille düzenleyen taşınabilir `metinoskop` agent skill'ini içerir.

## Temel dosyalar

- `SKILL.md`: Çalışma zamanında yüklenen ana skill yönergesi ve temel davranış sözleşmesidir.
- `references/turkce-oruntuler.md`: Türkçedeki mekanik yapay zekâ örüntülerini ve bağlama duyarlı düzeltme örneklerini içerir.
- `references/akicilik.md`: Bilgi sırası, cümleler arası bağ, gönderge açıklığı ve paragraf akışı rehberidir.
- `references/rapor-yazimi.md`: Raporlarda bölüm işlevi, kanıt zinciri, bulgu–yorum–öneri ayrımı ve yönetici özeti rehberidir.
- `references/retorik-yapilar.md`: Cümle, paragraf ve belge düzeyindeki yapay düzyazı mimarisinin işlev ailelerine göre kataloğu, türlere göre zorlu önce/sonra örnekleri ve kalması gereken karşı örneklerdir.
- `references/yapisal-butunluk.md`: Başlık, paragraf ve bölüm sınırlarının kavramsal sınırları izlemesi; bölme testleri, parçalanma yoğunluğu, yakınlık kuralı, yapay gerilim, çapraz gönderme, listeleştirme, uzun ifade katalogları, yapısal onarım örnekleri ve korunması gereken yapı karşı örnekleridir.
- `references/turkce-ritim-ve-ceviri-golgesi.md`: Dil bilgisi doğru olduğu hâlde İngilizce iskelet taşıyan Türkçe için kaynak dil gölgesi kavramı; bilgi yapısı ve sözcük sırası, özne düşürme, çekimli cümle zinciri, fiilimsi kaynakları, söylem belirteçleri, `bu + söylem adı` paketi, `bir`, `sahip olmak`, `var/yok`, `olan` zinciri, çerçeve yığını, soyut ad yüklemi, eksilti ve geri kazanılabilirlik, uzun cümle ritmi, iyelik zinciri katalogları; yerli alternatif üretimi ve geri çeviri testi; iyi Türkçenin eğilimleri; türlere göre davranış; dokunulmayacak karşı örnekler ve aşırı düzeltme belirtileridir.
- `references/epistemik-mimari.md`: Epistemik kaynak (gözlem, ölçüm, aktarım, çıkarım, tahmin, öngörü, plan, varsayım, yorum), aktör ve edilgen çatı karar çerçevesi, gözlem–çıkarım–yorum düzeyleri, aktarım ve atıf mesafesi, çekince ve pekiştirici, kiplik yığını, zaman–görünüş–kip bakış açısı, belirsizliğin kapsamı, bölümler arası kesinlik kayması, öneri–karar–uygulama ve olumsuz kanıt katalogları; karşı örnekler ve aşırı düzeltme belirtileridir.
- `references/esdizim-ve-istem.md`: Sözcük uyumu, eşdizim denetimi, eşdizim ile klişe ayrımı, fiil istemi ve hâl çerçevesi, ilgeç seçimi ve edat gölgesi, hafif fiiller, yüklem kesinliği, genel fiil aşırı kullanımı, sıfat–ad ve zarf–fiil uyumu, sözcük zincirleri, eş anlamlı kayması, teknik terim ve türe göre eşdizim; karşı örnekler ve aşırı düzeltme belirtileridir.
- `references/metinsel-tutarlilik.md`: Konu ilerleyişi, "ne değişti?" testi ve olgu yığını, bağdaşıklık ile tutarlılık ayrımı, bağlaç işlevi doğrulaması, sözcüksel bağdaşıklık, gönderge mesafesi, paragraflar arası devir, konu sıfırlama, paragraf işlevi ve işlev kayması, zamansal bağdaşıklık, kapsam ve odak bağlanması, olumsuzluk kapsamı, kayıt kararlılığı, noktalama ritmi, bellek yükü ve iddia–dayanak yakınlığı, aynı önerme yeni rol, kayıpsız sıkıştırma; karşı örnekler ve aşırı düzeltme belirtileridir.
- `references/kavramsal-girisler.md`: Temel kavramlar için bağlam, problem, soru ve çözüm akışı kurma rehberidir.
- `agents/openai.yaml`: Destekleyen istemciler için kullanıcı arayüzü metadata'sıdır.
- `README.md`: İnsanlar için kurulum, kullanım, kapsam ve depo yapısı belgesidir.
- `evals/`: Sabit çıktı dayatmayan davranışsal değerlendirme vakalarını içerir.
- `scripts/eval-runner.py`: Model çıktısındaki kaynak değişmezlerini bağımlılık kullanmadan denetler.
- `scripts/style-lint.py`: Model çıktısındaki şüpheli retorik ve yapısal örüntüleri işlev ailesine göre işaretler; tek başına reddetmez, `--source` ile yeni eklenen kalıpları sert/bağlamsal ayrımıyla listeler. Çeviri gölgesi ölçülerini (`sahip olmak`, varlık kalıbı, çerçeve yığını, `olan` zinciri, tekrarlanan cümle başlangıcı, `ve` zinciri, fiilimsi yığını, iyelik zinciri, bağlaçla başlayan cümle, `bir` yoğunluğu) ve söylem ölçülerini (çekince, pekiştirici, aktarım ve hafif fiil aileleri; kiplik yığını, pekiştirici çatışması, aktarım sonrası sonuç, kip nöbetleşmesi, edilgen adlaştırma, ilgeç yoğunluğu, eş anlamlı kayması, konu sıfırlama, parantez yükü, kayıt kayması) yalnızca inceleme bulgusu olarak raporlar.
- `scripts/eval-suite.py`: `evals/outputs/` altındaki kayıtlı referans çıktılar üzerinde değişmez, sert kalıp ve yapısal beklenti denetimi yapar; CI'da `--require-all` ile çalışır ve model hakem istemi üretebilir.
- `scripts/behavioral-regression.py`: `SKILL.md` ve referansları gerçek bir modele verip `evals/critical-cases.txt` vakalarını taze üretir, deterministik denetimden ve model hakeminden geçirir; `.github/workflows/behavioral.yml` bunu haftalık ve elle tetiklemeyle çalıştırır. Kayıtlı çıktı denetimi fixture'ları, bu betik skill'i sınar.
- `scripts/validate-package.py`: Paket yapısını ve adlandırma tutarlılığını bağımlılık kullanmadan doğrular.
- `LICENSE`: Paketin MIT Lisansı altında kullanılma, değiştirilme ve dağıtılma koşullarını belirtir.
- `CHANGELOG.md`: Sürümler arasındaki kullanıcıya dönük davranış ve paket değişikliklerini kaydeder.

## Bakım sözleşmesi

- `SKILL.md` davranışını değiştirdiğinizde README'deki özellik, kapsam ve örneklerin hâlâ doğru olduğunu kontrol edin.
- Skill adını her yüzeyde `metinoskop`, açık çağrıyı `$metinoskop` olarak koruyun.
- YAML frontmatter'da yalnızca `name` ve `description` alanlarını kullanın.
- Yeni ayrıntılı örüntüleri ana dosyaya yığmak yerine uygun `references/` dosyasına ekleyin. Sözcük ve kalıp düzeyi `turkce-oruntuler.md`, cümle, paragraf ve belge düzeyi `retorik-yapilar.md`, İngilizce iskelet taşıyan cümle mimarisi ve Türkçe kaynak geri kazanımı `turkce-ritim-ve-ceviri-golgesi.md` dosyasına gider.
- Çeviri gölgesi kurallarını "kötü Türkçe sözcük" kara listesine çevirmeyin; `bir`, `olan`, `ve`, `açısından`, `sahip`, `bulunmaktadır` tek başına asla işaret değildir. Her aile için kalması gereken bir karşı örnek bulundurun ve türe göre davranışı (akademik adlaştırma, teknik açık özne tekrarı, hukuki kalıp, kişisel eksilti) koruyun.
- Çeviri gölgesi örneklerinde kaynağın kesinlik düzeyini güçlendiren fiil ("ilişkili" → "neden olur", "olumsuz etki" → "bozuldu") kullanmayın; alan terimlerini öz Türkçe hevesiyle değiştirmeyin; tek yükleme dört beş fiilimsi asan, iki aktörlü paragrafta özneyi düşüren ya da yapay yerlilik (arkaik sözcük, konuşma edatı, gereksiz devriklik) ekleyen "sonra" sürümü eklemeyin.
- Epistemik örneklerde aktarımı olguya, çıkarımı ölçüme, ilişkiyi nedenselliğe, öneriyi karara, kararı uygulamaya, "gözlenmedi"yi "yoktur"a çeviren; kaynağın adlandırmadığı bir aktör uyduran; çekinceyi "AI gibi" diye silen ya da ölçümle desteklenen kesin iddiaya çekince ekleyen; kipleri üslup için nöbetleştiren "sonra" sürümü eklemeyin. Epistemik mimari `epistemik-mimari.md`, sözcük birleşimleri `esdizim-ve-istem.md`, konu ilerleyişi ve bağlaç geçerliliği `metinsel-tutarlilik.md` dosyasına gider; retorik dolgu ile eşdizim sorununu, yapısal sınır ile söylem tutarlılığını ayrı tutun.
- Eşdizim örneklerinde hâl değişimiyle ilişkiyi değiştiren ("gürültüden etkilenmez" → "gürültüyü etkilemez"), teknik terimi ya da hukuki formülü "doğallaştıran", seyrek ama kesin birleşimi genel eşdizime indiren, süreç adını yalın fiile çeviren "sonra" sürümü eklemeyin. Tutarlılık örneklerinde kronolojiyi nedenselliğe çeviren, eksik öncül uyduran, kapsam işaretini ya da olumsuzluğu başka ögeye bağlayan, gerekli yinelemeyi silen, bilinçli kayıt değişimini düzleştiren ya da ondalık listedeki noktalı virgülü kaldıran "sonra" sürümü eklemeyin.
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
- `scripts/style-lint.py` kataloğuna aile eklerken öz sınamadaki yapay ve temiz metinleri güncelleyin; temiz metin sert bastırma ailesinde işaret üretmemelidir. Bağlama duyarlı bir aileyi `sert` düzeyine taşımayın; `--fail-on-introduced-hard` yalnızca sert aileler için deterministik hata verir. Çeviri gölgesi sezgiselleri (`sahip`, `varlik`, `kalki` aileleri ve `ceviri` bulguları) her zaman bağlamsal kalır; yeni bir sezgisel eklerken öz sınamadaki yerli metnin (`NATIVE_TEXT`) sıfır çeviri gölgesi bulgusu üretmeye devam ettiğini doğrulayın.
- Çeviri gölgesi davranışını `tekrarlanan-acik-ozne`, `bu-sonuc-ritmi`, `asiri-bir`, `sahip-olmak-kalkisi`, `bulunmaktadir-kalkisi`, `ve-zinciri`, `yararli-ip-yapisi`, `asiri-ip-zinciri`, `art-niteleme`, `gereksiz-olan`, `cerceve-yigini`, `soyut-ad-yuklemi`, `ozne-dusurme-akisi`, `asiri-yuklu-cumle` ve `ingilizce-soylem-belirtecleri` vakalarıyla; koruma davranışını `dogal-ve-korunur`, `gerekli-olan`, `gerekli-acisindan`, `teknik-adlastirma-korunur`, `belirsizlik-icin-acik-ozne`, `dogal-uzun-cumle-korunur`, `hukuki-kalip-korunur`, `teknik-ozne-tekrari-korunur` ve `yerli-turkce-metin` vakalarıyla koruyun. Korunur vakalarının kayıtlı çıktısı kaynağın kendisidir; doğrulayıcı bunu denetler.
- Epistemik davranışı `edilgen-korunur`, `edilgen-etkene`, `bilinmeyen-aktor`, `aktarim-olgu-olmaz`, `olcum-ile-cikarim`, `cekince-korunur`, `kiplik-yigini`, `dayanaksiz-pekistirici`, `mesru-guclu-iddia`, `gerekceli-kip-degisimi`, `uslup-kip-nobetlesmesi`, `oneri-karar-degil`, `karar-uygulama-degil`, `gozlenmedi-yoktur-degil`, `atif-kapsami`, `kapsam-isareti-baglanmasi`, `sonuc-sonuclardan-guclu` ve `iyi-akademik-paragraf`; eşdizim davranışını `tuhaf-esdizim`, `teknik-esdizim-korunur`, `yanlis-hal-cercevesi`, `dogru-alisilmadik-hal`, `edat-aktarimi`, `hafif-fiil-sismesi`, `surec-adi-korunur`, `genel-fiil-kesin-iliski`, `epistemik-guvensiz-fiil`, `esanlam-kaymasi-teknik`, `kanonik-terim-tekrari`, `varlik-yeniden-adlandirma`, `hukuki-formul-korunur`, `dogal-is-epostasi` ve `odunc-terim-korunur`; tutarlılık davranışını `olgu-yigini`, `sabit-konu-korunur`, `dogrusal-ilerleyis-korunur`, `desteksiz-bu-nedenle`, `gecerli-nedensel-baglac`, `esanlam-donusu`, `gerekli-ad-tekrari`, `uzak-bu`, `kisa-mesafe-eksilti`, `bolum-basi-sifirlama`, `temiz-devir`, `islev-kaymasi`, `kronoloji-nedensellik`, `kapsam-isareti-tasinmasi`, `olumsuzluk-kapsami`, `kayit-kaymasi`, `bilincli-kayit-degisimi`, `ingilizce-noktalama`, `teknik-noktalama-korunur`, `uzak-sinirlilik`, `ayni-iddia-yeni-rol`, `ayni-iddia-hacim` ve `tutarli-metin-korunur` vakalarıyla koruyun. Söylem sezgiselleri (`kiplik`, `pekistirici`, `aktarim`, `hafif_fiil` aileleri ve `soylem` bulguları) bağlamsal kalır; yeni bir sezgisel eklerken öz sınamadaki yerli, temiz, iyi yapılı ve iç içe metinlerin sıfır söylem bulgusu üretmeye devam ettiğini doğrulayın.
- Her eval'in `evals/outputs/<vaka>.txt` referans çıktısı olmak zorundadır (CI `--require-all`); mümkünse `## Yapısal beklenti` bölümü ekleyin, yapısı korunacak vakalarda kaynağı olduğu gibi kaydedin. Gold çıktı bir sözleşmedir: kaydetmeden önce her iddianın epistemik statüsünü kaynakla karşılaştırın; rastgele atanmamış gruplar arasındaki farkı nedensel fiille yazan, şişmiş iddiayı indirirken kaynakta olmayan olumsuz iddia ya da çekince ekleyen, statüyü (süreç → karar, öneri → uygulama) kaydıran gold kabul edilmez. Kaynakta geçen bir dolgu işaretinin silinmesi değişmez denetimine takılıyorsa `## Serbest değişmezler` bölümünde gerekçesiyle muaf tutun; çıktıyı işareti geri koymak için bükmeyin. `python scripts/eval-suite.py --require-all` geçmeden commit oluşturmayın.
- `SKILL.md` çalışma zamanında yüklenen dosyadır ve dikkat ekonomisine tabidir: doğrulayıcı 400 satır, 60 KB ve 1.200 baytlık `description` sınırı koyar. Yeni bir kural eklerken ana dosyaya "ne zaman fark et → hangi kararı ver → hangi referansı oku → neyi asla bozma" düzeyinde birkaç cümle, ayrıntıyı referansa yazın; `description` bir katalog değil tetikleyici tanımıdır.
- Linter sezgisellerine yapabileceğinden fazlasını vaat eden ad vermeyin: `tekrarlanan_cumle_baslangici` cümle başlangıcı tekrarıdır, özne tespiti değildir; hakem karar verir.
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
python scripts/eval-suite.py --require-all
python scripts/behavioral-regression.py --dry-run
npx --yes skills@1.5.20 add . --list
```

Skill davranışını değiştiren bir değişiklikten sonra, API anahtarı varsa `python scripts/behavioral-regression.py` ile kritik vakaları gerçek modelde çalıştırın; CI bunu haftalık yapar.

Doğrulama başarısızsa commit oluşturmayın. Yeni veya değişmiş örnekleri ayrıca kaynak sadakati ve örtük nedensellik açısından elle inceleyin.
