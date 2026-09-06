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
