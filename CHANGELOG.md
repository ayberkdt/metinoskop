# Değişiklik Günlüğü

Bu dosyada Metinoskop'un kullanıcıya dönük davranış ve paket değişiklikleri kaydedilir.

Biçim [Keep a Changelog](https://keepachangelog.com/tr/1.1.0/) yaklaşımına, sürüm numaraları [Anlamsal Sürümleme](https://semver.org/lang/tr/) ilkelerine dayanır.

## [Unreleased]

### Eklendi

- Dört düzeyde (sözcük ve kalıp, cümle, paragraf, belge) yapay düzyazı denetimi: sıfır bilgi cümlesi kuralı ve silme testi, işlev tekrarı, savunmacı düzyazı, iddia → açımlama → önem → mini sonuç döngüsü, üretilmiş önem, üretilmiş karşıtlık, yol haritası ve okur yönlendirmesi, kalıp giriş ve sonuç, soyut yüklem sisi, boş soyut özne, açıklık testi, paragraf simetrisi ve zorlama denge kuralları.
- "Dolguyu başka dolguya çevirme" kesin kuralı; sert bastırma ile bağlama duyarlı yüksek risk ayrımı.
- Akademik ve teknik metin için ek bastırma kuralları ve geçerli bilimsel iddiayı koruma kuralı.
- `references/retorik-yapilar.md`: işlev ailelerine göre katalog; akademik makale, mühendislik raporu, teknik belge, analitik düzyazı, e-posta ve açıklayıcı yazı türlerinde zorlu önce/sonra örnekleri; yanlış dönüşüm tablosu ve kalması gereken karşı örnekler.
- On bir yeni davranışsal eval vakası: savunmacı akademik düzyazı, tekrar döngüsü, yol haritası, yapay denge, giriş hunisi, kalıp sonuç ve gelecek çalışma, soyut yüklem, paragraf simetrisi, gerekli ifade (yanlış pozitif), öğretici açıklama (muhatap duyarlılığı) ve zaten iyi metin.
- `scripts/style-lint.py`: şüpheli retorik örüntüleri işlev ailesine göre işaretleyen, yapı bulgularını raporlayan ve `--source` ile yeni eklenen örüntüleri ayıran bağımlılıksız stil denetimi; öz sınaması CI'a eklendi.
- Yapısal bütünlük ve okur yorgunluğu kuralları: yapı kavramsal sınırları izler ilkesi, süreklilik, başlık, derinlik ve başlık sıkıştırma testleri, paragrafın kavramsal birim olması, zihinsel model sürekliliği, yakınlık kuralı, açıklamanın bitmesi, slayt değil belge, listeleştirme, yapay gerilim ve paragraf askısı, bağlam yeniden başlatma ve çapraz gönderme, başlık tekrarı ve boş sarmalayıcılar, zorlama geçişler, yinelenme haritası, uzun ifadeler ve yığılmış çerçeve, cümle birleştirme ve şişkin cümle, okur emeği, yazarın yapısal ölçeği ve yapısal yanlış pozitif koruması.
- `references/yapisal-butunluk.md`: bölme testleri, parçalanma yoğunluğu uyarı işaretleri, katalogların tamamı, dört-beş mikro bölümü tek bölüme indiren onarım örnekleri ve korunması gereken yapı karşı örnekleri.
- On altı yeni yapısal eval vakası: aşırı bölümleme, başlık derinliği, tek paragraflık bölümler, kısa paragraf yığını, yapay gerilim, tekrarlanan bölüm girişleri ve sonuçları, çapraz gönderme, uzun çerçeve ifadeleri, ayrılmış kanıt, gereksiz listeleme; korunacak başlıklar, yöntem ayrımı, uzun ve kısa kalması gereken paragraflar ve yapısı iyi metin.
- Stil denetimi başlıkları ve liste ögelerini ayrıştırır; yapay gerilim, paragraf askısı, boş sarmalayıcı, çapraz gönderme, bağlam yeniden başlatma ve uzun çerçeve ailelerini işaretler; parçalanma yoğunluğu özetini, başlık yoğunluğu, tek paragraflık bölüm, derin başlık, kısa paragraf, liste yoğunluğu, başlık tekrarı ve bağlaçla açılış bulgularını raporlar; `--source` ile yapı ölçülerindeki değişimi gösterir.
- Doğrulayıcı `SKILL.md` için kendi yapı kuralını denetler: dördüncü düzey başlık yok, en fazla on iki üçüncü düzey başlık.
- Sıfır bilgi cümlesi kuralına sentez ve bilişsel sıkıştırma istisnası: silme testi iki sorudur; yeni önerme eklemeyen ama birden çok bulguyu tek karar cümlesinde toplayan ya da okurun çıkarım yükünü azaltan cümle korunur.
- Paragraf kuralı "baskın ve tutarlı düşünce hareketi" olarak esnetildi; aynı konu tek paragraf için yeterli sayılmaz, bulgu → öneri gibi sert söylem işlevi değişimlerinde paragraf sınırı meşrudur ve bulgu, yorum, öneri tek yoğun blokta paketlenmez.
- `scripts/eval-suite.py`: `evals/outputs/` altındaki on beş kayıtlı referans çıktı üzerinde kaynak değişmezi, sert kalıp eklenmesi ve `## Yapısal beklenti` denetimi; CI'a eklendi; `--export-judge-prompts` ile model hakem istemleri.
- Stil denetimi çıkış kodu sert ve bağlamsal aileleri ayırır (`--fail-on-introduced-hard`, `--fail-on-introduced-any`); başlıklar yığın tabanlı ağaçla sayılır, alt bölümleri dolu üst başlık tek paragraflık bölüm sayılmaz; başlık tekrarı sezgiseli sayı taşıyan veya uzun ilk cümleyi tekrar saymaz.
- Eval çalıştırıcısı başlık satırlarındaki noktalı bölüm numaralarını değişmez saymaz ve Kaynak bölümünü yalnızca vaka başlıklarında keser.
- Kaynak dil gölgesi ve Türkçe ritim kuralları: dil bilgisi doğru olduğu hâlde İngilizce iskelet taşıyan cümleyi tanıyan "kaynak dil gölgesi" kavramı; "ilişkiyi yeniden kur, sözcükleri değil" ilkesi; bilgi yapısının (konu, odak, verilmiş ve yeni bilgi) sözcük sırasını belirlemesi; açık özne denetimi ve özne düşürmenin kural değil kaynak olması; yan cümle mimarisi denetimi (çekimli cümle zinciri, sıralama ile alt sıralama ayrımı, fiilimsi dengesi, uzak yüklem); Türkçe kaynak geri kazanımı listesi ve geri kazanılabilirlik testi; yerli alternatif üretimi ve geri çeviri gölgesi testi; daha güçlü fiil uydurmama ve terim koruma kuralı; aşırı düzeltme koruması ve türe göre ritim.
- `references/turkce-ritim-ve-ceviri-golgesi.md`: gölgenin yirmiyi aşkın yüzü için katalog ve zorlu önce/sonra örnekleri (özne fazlası, `bu + söylem adı` paketi, `bir`, `sahip olmak`, `var/yok`, `olan` zinciri, çerçeve yığını, soyut ad ve hafif yüklem, eksilti, uzun cümle ritmi, iyelik zinciri, küçük kalkı aileleri); iyi Türkçenin eğilimleri; paragraf ve belge düzeyinde gölge; türlere göre davranış; dokunulmayacak karşı örnekler ve aşırı düzeltme belirtileri.
- Çalışma yönteminde altıncı denetim geçişi (F. Çeviri gölgesi: özne, yan cümle, niteleme, çerçeve, iyelik ve varlık, bilgi yapısı, yerli kaynak ve aşırı düzeltme denetimi); ses ve akış denetimine "Türkçe düşünülmüş gibi okunuyor mu?" sorusu.
- Yirmi dört yeni davranışsal eval vakası: yinelenen açık özne, `bu sonuç` ritmi, fazla `bir`, `sahip olmak` ve `bulunmaktadır` kalkıları, `ve` zinciri, yararlı ve aşırı `-ip`, art niteleme, gereksiz `olan`, çerçeve yığını, soyut ad yüklemi, özne düşürme akışı, aşırı yüklü cümle, İngilizce söylem belirteçleri; karşı tarafta korunması gereken doğal `ve`, gerekli `olan`, gerekli `açısından`, teknik adlaştırma, belirsizliği önleyen açık özne, yerli uzun cümle, hukuki kalıp, teknik özne tekrarı ve zaten Türkçe düşünülmüş metin. Her vakanın kayıtlı referans çıktısı ve yapısal beklentisi vardır; korunur vakalarında kayıtlı çıktı kaynağın kendisidir.
- Stil denetimi çeviri gölgesi ölçüleri: `sahip olmak`, varlık kalıbı ve çeviri kalkısı aileleri (bağlamsal); tek cümlede çerçeve yığını, `olan` zinciri, `bir` fazlası, `ve` zinciri, fiilimsi yığını ve iyelik zinciri; ardışık cümlelerde aynı özne; paragraf ve belge düzeyinde söylem belirteci ve `bu + söylem adı` yoğunluğu; 100 sözcük başına `bir`. Hepsi inceleme bulgusudur; tek `bir`, `olan`, `ve`, `açısından` işaretlenmez, paralel `açısından` çifti yığın sayılmaz. `--source` ile çıktıda yeni beliren gölge bulguları uyarı olarak listelenir. Öz sınama yerli metinde sıfır yanlış pozitif ister.
- Kayıtlı çıktı regresyonu çeviri gölgesi ölçülerini `## Yapısal beklenti` satırı olarak kabul eder (`sahip olmak`, `varlık kalıbı`, `çerçeve yığını`, `olan zinciri`, `ardışık özne`, `ve zinciri`, `fiilimsi yığını`, `iyelik zinciri`, `bağlaçla başlayan cümle`, `bir / 100 sözcük`); eval çalıştırıcısının öz sınaması `sahip olmak` vakasını da kapsar.
- Doğrulayıcı yeni referans dosyasını, SKILL.md'deki çeviri gölgesi ilkelerini, yirmi dört vakanın kapsam işaretlerini, en az otuz kayıtlı çıktıyı ve korunur vakalarında kayıtlı çıktının kaynağa eşit olmasını denetler.
- Epistemik mimari kuralları: epistemik kaynak ayrımı (gözlem, ölçüm, aktarım, alıntı, çıkarım, tahmin, öngörü, beklenti, plan, varsayım, yaygın kabul, yazar ve kurum yorumu, çözümsüz) ve "bilginin kaynağını düzenleyip yok etme" ilkesi; edilgen çatı için altı soruluk karar çerçevesi ve aktörlük koruma; gözlem–ilişki–çıkarım–nedensel iddia düzeyleri; aktarım ve atıf mesafesi; çekince ile pekiştirici ayrımı ve kiplik yığını; zaman–görünüş–kip bakış açısı denetimi; belirsizliğin kapsamı; bölümler arası kesinlik kayması; öneri–plan–karar–uygulama statü zinciri; olumsuz kanıt koruması. `references/epistemik-mimari.md` katalog, karşı örnek ve aşırı düzeltme belirtileriyle eklendi.
- Sözcük uyumu kuralları: sözcük uyumu için beş soru; eşdizim denetimi ve eşdizim ile klişe ayrımı; fiil istemi ve hâl çerçevesi; ilgeç seçimi ve edat gölgesi; hafif fiil ve genel fiil; yüklem kesinliği; sıfat–ad ve zarf–fiil uyumu; sözcük zincirleri, gönderge zinciri ve eş anlamlı kayması; teknik terim ve ödünç sözcük koruması; türe göre eşdizim. `references/esdizim-ve-istem.md` eklendi.
- Metinsel tutarlılık kuralları: konu ilerleyişi örüntüleri ve "ne değişti?" testi; olgu yığını; bağdaşıklık ile tutarlılık ayrımı ve "bağlaç ilişki kuramaz" ilkesi; bağlaç işlevi doğrulaması; sözcüksel bağdaşıklık; gönderge mesafesi ve yeniden tanıtım eşiği; paragraflar arası devir ve bilgi taşıyan köprü; konu sıfırlama; paragraf işlevi ve işlev kayması; zamansal bağdaşıklık; kapsam, odak ve olumsuzluk bağlanması; kayıt kararlılığı ve ses tutarlılığı; noktalama ritmi ve ara söz yükü; bellek yükü ve iddia–dayanak yakınlığı; aynı önerme yeni rol; kayıpsız argüman sıkıştırma. `references/metinsel-tutarlilik.md` eklendi.
- Çalışma yöntemine üç denetim geçişi daha (G. Epistemik mimari, H. Sözcük uyumu, I. Metinsel tutarlılık); ses ve akış denetimine kanıt bağı ve cümleler arası devir soruları; skill açıklamasına "kesinlik düzeyini bozma", "sözcükler doğal birleşsin", "paragraflar birbirini izlesin" tetikleyicileri.
- Elli altı yeni davranışsal eval vakası: on sekiz epistemik (edilgen korunur ve etkene çevrilir, bilinmeyen aktör, aktarım, ölçüm ile çıkarım, çekince, kiplik yığını, pekiştirici, meşru güçlü iddia, gerekçeli ve üslup kip değişimi, öneri–karar–uygulama, gözlenmedi ile yoktur, atıf kapsamı, kapsam işareti, sonuç bölümü kesinliği, iyi akademik paragraf); on beş eşdizim (tuhaf eşdizim, teknik eşdizim, yanlış ve doğru hâl çerçevesi, edat aktarımı, hafif fiil, süreç adı, genel fiil, epistemik güvensiz fiil, eş anlamlı kayması, kanonik terim, varlık yeniden adlandırma, hukuki formül, doğal e-posta, ödünç terim); yirmi üç tutarlılık (olgu yığını, sabit ve doğrusal ilerleyiş, desteksiz ve geçerli bağlaç, eş anlamlı dönüşü, gerekli ad tekrarı, uzak gönderge, kısa eksilti, bölüm başı sıfırlama, temiz devir, işlev kayması, kronoloji, kapsam ve olumsuzluk, kayıt kayması ve bilinçli kayıt değişimi, İngilizce ve teknik noktalama, uzak sınırlılık, aynı iddia yeni rol ve hacim, tutarlı metin). Hepsinin kayıtlı referans çıktısı ve yapısal beklentisi vardır.
- Stil denetimi söylem ölçüleri: çekince, pekiştirici, aktarım ve hafif fiil aileleri (bağlamsal); kiplik yığını, pekiştirici çatışması, aktarım sonrası sonuç, kip nöbetleşmesi, edilgen adlaştırma, ilgeç yoğunluğu, eş anlamlı kayması, konu sıfırlama, parantez yükü ve kayıt kayması bulguları. Hepsi inceleme içindir; hiçbir regex epistemik doğruluğa karar vermez. Öz sınama yerli, temiz, iyi yapılı ve iç içe metinlerde sıfır yanlış pozitif ister; kayıtlı çıktı regresyonu bu ölçüleri `## Yapısal beklenti` satırı olarak kabul eder.
- Doğrulayıcı üç yeni referansı, SKILL.md'deki on altı yeni ilke başlığını ve üç denetim geçişini, elli altı vakanın kapsam işaretlerini, en az doksan kayıtlı çıktıyı ve otuz üç korunur vakasında kayıtlı çıktının kaynağa eşit olmasını denetler.

### Değiştirildi

- Çalışma yöntemine dört geçişli yapay düzyazı denetimi eklendi; ses ve akış denetimi altıncı adım oldu ve gerekli sınırlılık ya da öğretici açıklamanın dolgu sanılıp silinmediğini kontrol eder.
- Müdahale düzeyleri ve değişiklik bütçesi, sıfır bilgi cümlelerini, işlev tekrarını ve kısalığın amaç olmadığını açıkça belirtecek biçimde güncellendi.
- Kaynak sadakati kuralına kaynaktaki sayılardan yeni sayı türetmeme maddesi eklendi.
- Bağlam profili muhatabın bilgi düzeyini içerecek biçimde genişletildi.
- Yüksek riskli kalıplar bölümü kalıp düzeyiyle sınırlandı; karşıtlık kalıpları üretilmiş karşıtlık bölümüne taşındı.
- Referans dosyaları yeni katalogla çapraz bağlandı; rapor rehberine retorik dolgu bölümü ve son denetim sorusu, örüntü rehberine yeni yanlış pozitifler, akıcılık rehberine yeni aşırı düzeltme belirtileri eklendi.
- `evals/README.md` vaka gruplarını ve sıfır bilgi, işlev tekrarı, savunmacı düzyazı, dolgu çevirisi, paragraf mimarisi ve muhatap duyarlılığı için hakem ölçütlerini tanımlar.
- Eval çalıştırıcısının öz sınaması tekrar döngüsü ve giriş hunisi vakalarını da kapsar.
- Skill açıklaması yeni kapsamı ve "dolguyu çıkar" tetikleyicisini içerir.
- `SKILL.md` kendi parçalanma kuralına uyacak biçimde yeniden düzenlendi: on üç mikro alt bölüm cümle, paragraf ve belge düzeyi altında kalın başlangıçlı paragraflara indirildi; müdahale düzeyleri ve çalışma yöntemi adımları alt başlıksız paragraflar oldu; yapı denetimi beşinci geçiş olarak eklendi.
- Müdahale düzeyleri yapısal kapsamı belirtir: hafif düzey başlıklara dokunmaz, standart düzey paragraf birleştirir ama hiyerarşiyi korur, derin düzey bölüm yapısını kavramsal sınırlara göre yeniden kurar.
- Bağlam profiline yapısal ölçek ve dışarıdan dayatılan yapı eklendi; terim tutarlılığı bölüm birleştirmede numaralı göndermeleri kapsar.
- Skill açıklaması "parçalanmayı gider" ve "başlıkları sadeleştir" tetikleyicilerini içerir.
- Skill açıklaması kaynak dil gölgesi kapsamını ve "çeviri gibi durmasın", "Türkçe düşünülmüş gibi olsun" tetikleyicilerini içerir; standart müdahale düzeyi çeviri gölgesini kapsar; sorun kümeleri ve referans yönlendirmesi yeni dosyayı gösterir.
- `turkce-oruntuler.md` çeviri kokusu bölümü, `akicilik.md` bilgi akışı, `retorik-yapilar.md` boş soyut özne ve `yapisal-butunluk.md` yığılmış çerçeve bölümleri yeni referansa çapraz bağlandı.
- `evals/README.md` çeviri gölgesi vaka grubunu ve üç yeni hakem ölçütünü (kaynak dil gölgesi, Türkçe kaynak kullanımı, gölge avında aşırı düzeltme) tanımlar.
- `evals/README.md` epistemik mimari, eşdizim ve istem, metinsel tutarlılık vaka gruplarını ve üç hakem ölçütünü daha (epistemik mimari, sözcük uyumu, metinsel tutarlılık) tanımlar; AGENTS.md bakım sözleşmesi üç yeni referansın kapsamını ve eklenmemesi gereken dönüşümleri belirtir; README yeni referansları, kullanım örneklerini ve sınırları belgeler.

### Düzeltildi

## [0.4.1] - 2026-07-31

### Düzeltildi

- Yapısal bütünlük eval'indeki `(Tablo 2)` çapraz göndermesi, açık bir `Tablo 2` başlığına bağlandı ve başlık–tablo–gönderme tutarlılığı koruma ölçütlerine eklendi.

## [0.4.0] - 2026-07-31

### Eklendi

- Raporlarda bölüm işlevini, kanıt zincirini, bulgu–yorum–öneri ayrımını ve yönetici özeti sadakatini ele alan rapor yazımı rehberi.
- Bulgu–yorum–öneri sınırı, rapor yapısal bütünlüğü ve yönetici özeti için üç davranışsal değerlendirme vakası.

### Değiştirildi

- Ana skill, raporları yalnızca cümle akışı açısından değil; dayanak, sınırlılık, öneri statüsü ve çapraz gönderme bütünlüğü açısından da denetleyecek biçimde güçlendirildi.
- README ve bakım sözleşmesi rapor düzenleme davranışını, sınırlarını ve doğrulama ölçütlerini açıkça belgeleyecek biçimde güncellendi.
- Çalışma yöntemindeki `Yeniden yaz` aşaması, değişiklik bütçesi ilkesiyle uyumlu olarak `Düzenle` biçiminde adlandırıldı.
- Eval çalıştırıcısının öz sınaması, rapor kaynak sadakati vakasını da kapsayacak biçimde genişletildi.
- Varsayılan çağrı istemi kesinlik düzeyi ve işlevsel yapı korumasını açıkça içerecek biçimde sıkılaştırıldı.

## [0.3.0] - 2026-07-31

### Eklendi

- Model çıktılarında sayı, tarih, URL, kod, dipnot, kapsam belirleyicisi, teknik ad, sembol ve ölçüm korumasını denetleyen bağımlılıksız eval çalıştırıcısı.
- Çalıştırıcı için metin ve JSON raporlama seçenekleri ile üç vakalı öz sınama.

### Değiştirildi

- Paket CI'ı deterministik eval çalıştırıcısının öz sınamasını da çalıştıracak biçimde genişletildi.
- README doğrulaması, pazarlama cümlelerinin birebir kopyası yerine yapısal öğelere ve sürüm numarasına bağlandı.

### Düzeltildi

- Teknik eval'deki klasik RK4–tolerans örneği, DOP853 bağıl tolerans örneğiyle değiştirildi.

## [0.2.0] - 2026-07-31

### Eklendi

- Belirsizliği koruma ve zorunlu yorum seçiminde kullanıcıdan açıklama isteme politikası.
- Olumsuzluk, nicelik, koşul, istisna ve kapsam belirleyicileri için kaynak sadakati kuralları.
- Uzun ve teknik metinler için terim ve gösterim tutarlılığı denetimi.
- Belirsizlik, kapsam ve koşul, üslup eşleştirme, biçim koruma ve teknik gösterim değerlendirme vakaları.

### Değiştirildi

- Çeviri kapsamı, kaynak dilden çeviri yerine Türkçeye çevrilmiş mevcut metni düzenlemekle sınırlandı.
- README'deki tanıtım cümlesi paket yapısını daha akıcı ve Türkçe bir söyleyişle anlatacak biçimde düzenlendi.
- Doğrudan kullanım örneği, projenin tercih ettiği `düzenle` fiiliyle uyumlu hâle getirildi.
- MIT lisans rozeti `LICENSE` dosyasına bağlandı.

### Düzeltildi

- Belirsiz gönderge yönergesi ile yalnızca son metni verme kuralı arasındaki çelişki giderildi.
- Akademik örnekte kaynağı belirsiz değerlendirmeyi yeni bir değerlendirmeyle yeniden kuran dönüşüm kaldırıldı.

## [0.1.0] - 2026-07-31

### Eklendi

- Anlamı, olguları, kesinlik düzeyini ve yazarın sesini koruyan Türkçe editör skill'i.
- Türkçe yapay ritim, akıcılık ve isteğe bağlı kavramsal giriş rehberleri.
- Akademik, hukuki, kurumsal, kişisel, kaynak sadakati, kavramsal giriş ve değişiklik bütçesi değerlendirme vakaları.
- Yerel paket doğrulayıcısı ve GitHub Actions iş akışı.
- MIT Lisansı.

### Tasarım

- Kavramsal giriş, ana tetikleyici kapsamından ayrılarak yalnızca açık kullanıcı talebiyle çalışan ikincil bir kabiliyet olarak tanımlandı.
- Doğal ve amacına uygun metni değiştirmemenin geçerli bir sonuç olduğu açıkça güvence altına alındı.

[Unreleased]: https://github.com/ayberkdt/metinoskop/compare/v0.4.1...HEAD
[0.4.1]: https://github.com/ayberkdt/metinoskop/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/ayberkdt/metinoskop/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/ayberkdt/metinoskop/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/ayberkdt/metinoskop/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/ayberkdt/metinoskop/tree/v0.1.0
