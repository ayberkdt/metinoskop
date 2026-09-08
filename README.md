# Metinoskop

[![Validate package](https://github.com/ayberkdt/metinoskop/actions/workflows/validate.yml/badge.svg)](https://github.com/ayberkdt/metinoskop/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-2e7d32)](LICENSE)
![Agent Skill](https://img.shields.io/badge/agent-skill-2563eb)
![Language: Türkçe](https://img.shields.io/badge/language-T%C3%BCrk%C3%A7e-c62828)

Türkçe metinlerdeki mekanik yapay zekâ ritmini, basmakalıp ifadeleri, kurumsal dolguyu, cümle, paragraf ve belge düzeyindeki yapay retorik mimariyi ve okuru yoran yapısal parçalanmayı ayıklayan taşınabilir agent skill paketi ve editoryal rehberler.

Metinoskop, metni sırf farklı görünsün diye yeniden yazmaz. Anlamı, olguları, kesinlik düzeyini, yazarın tavrını ve uygun resmiyet düzeyini koruyarak yalnızca gerekli editoryal müdahaleyi yapar.

## Ne yapar?

- Mekanik cümle ritmini ve tekrarlanan kalıpları düzeltir.
- Gereksiz `-maktadır/-mektedir` zincirlerini ve isim-fiil yığılmalarını sadeleştirir.
- Kurumsal dolgu, reklam dili ve tiyatral vurguyu azaltır.
- Belirsiz göndergeleri kaynakta bulunmayan bir yorum seçmeden ele alır ve kopuk paragraf geçişlerini açıklaştırır.
- İngilizceden taşınmış söz dizimini doğal Türkçeye yaklaştırır: dil bilgisi doğru olduğu hâlde İngilizce iskelet taşıyan cümlede sözcükleri bir kez daha çevirmek yerine ilişkiyi Türkçenin özne düşürme, fiilimsi, ortaç, iyelik, hâl eki ve sözcük sırası kaynaklarıyla yeniden kurar; yinelenen açık özneyi, `bu sonuç` ritmini, `ve` ile dizilmiş çekimli cümle zincirini, `sahip olmak` ve `bulunmaktadır` kalkılarını, `olan` zincirini, çerçeve yığınını ve fazla `bir` sözcüklerini gölge olarak tanır; gerekli açık özneyi, teknik adlaştırmayı, hukuki kalıbı ve zaten Türkçe düşünülmüş metni olduğu gibi bırakır.
- Kullanıcının sağladığı yazı örneğine göre ses ve ton eşleştirmesi yapar.
- Olumsuzluk, nicelik, koşul, istisna ve kapsam belirleyicilerini korur.
- Teknik terimleri, sembolleri, birimleri ve belge biçimini tutarlı tutar.
- Raporlarda bulgu, yorum, sınırlılık, öneri ve karar sınırlarını; tablo, atıf ve çapraz göndermeleri korur.
- Silindiğinde hiçbir önerme kaybolmayan ve önceki bilgiyi sentezlemeyen cümleleri çıkarır: dayanaksız önem iddiaları, savunmacı açıklamalar, olgu → açımlama → önem → mini sonuç döngüleri, bölüm duyuruları, kalıp giriş ve sonuçlar. Birden çok bulguyu tek karar cümlesinde toplayan ya da okurun çıkarım yükünü azaltan sentez cümlesini korur.
- Üretilmiş karşıtlık ve zorlama dengeyi çıkarır; adlandırılmış sınırlılığı ve ölçülmüş yöntem gerekçesini korur.
- Soyut yüklemleri kaynaktaki somut ilişkiyle değiştirir; boş soyut özneleri göndergeye çözer.
- Tek biçimli paragraf mimarisini bilgi yapısına göre yeniden kurar; uzunlukları insan gibi görünsün diye rastgeleleştirmez.
- Silinen dolguyu daha sakin eş anlamlılarla geri koymaz.
- Muhataba göre karar verir: uzman metninde açık olanın açıklamasını çıkarır, ders notunda öğretici açıklamayı korur.
- Yapıyı kavramsal sınırlara göre kurar: hak edilmemiş başlıkları ve tek paragraflık bölümleri birleştirir, erken bölünmüş paragrafları tek harekete toplar, sonuçla sınırlılığını yakınlaştırır, gereksiz derinliği düzleştirir.
- Yapay gerilimi, paragraf sonu askılarını, bağlam yeniden başlatmalarını, aşırı çapraz göndermeyi, boş bölüm sarmalayıcılarını ve zorlama geçişleri kaldırır.
- Uzun çerçeve ifadelerini ve yığılmış nitelemeleri kısaltır; nedensel akıl yürütmeyi listeye çevirmez, parçalanmayı dev cümlelerle de çözmez.
- Tekrarlanabilirlik, mevzuat, dergi kuralı, güvenlik adımları ve uzun belge gezinmesi gerektiren yapıyı korur; yazarın yapısal ölçeğini aşan makine parçalanmasını hedefler, evrensel asgariciliği değil.
- Kaynakta bulunmayan olgu, tarih, sayı, alıntı veya kişisel ayrıntı eklemez; kaynaktaki sayılardan yeni sayı türetmez.
- Kanıt mimarisini korur: her iddianın kaynağını (gözlem, ölçüm, aktarım, çıkarım, tahmin, öngörü, plan, yorum) ve kesinlik düzeyini düzenleme boyunca aynı tutar; aktarımı olguya, çıkarımı ölçüme, ilişkiyi nedenselliğe, öneriyi karara, kararı uygulamaya, "gözlenmedi"yi "yoktur"a çevirmez; kaynağın adlandırmadığı aktörü uydurmaz, edilgeni yalnızca aktör bilinip ilgiliyse etkene çevirir; çekinceyi kanıt, pekiştiriciyi retorik sayar; kip değişimini gerçek bakış açısı değişimine bağlar; sonuç bölümünün sonuçlar bölümünden güçlü konuşmasına izin vermez.
- Sözcükleri doğal Türkçedeki gibi birleştirir: tuhaf eşdizimi alışılmış eşleşmeyle, yanlış hâl çerçevesini fiilin doğal istemiyle, İngilizce edat izini gerçek ilişkiye uyan ilgeçle, hafif fiili gerçek yüklemle kurar; genel fiilin gizlediği kesin ilişkiyi kaynak destekliyorsa yazar; aynı varlığı tek adla anar, teknik terimi, ödünç sözcüğü, hukuki formülü ve süreç adını korur.
- Metnin bir düşünceyi geliştirmesini gözetir: her cümlenin öncekinden büyümesini, bağlacın önermelerin desteklediği ilişkiyi taşımasını, göndergenin mesafesinde geri kazanılabilmesini, kapsam işaretinin ve olumsuzluğun bağlandığı ögede kalmasını, kaydın ve noktalamanın Türkçe gruplamaya uymasını, sınırlılığın sınırladığı iddianın yanında durmasını sağlar; olgu yığınını işlevlere göre gruplar, kronolojiyi nedenselliğe çevirmez, eksik öncül uydurmaz.

## Temel ilkeler

1. Kullanıcının açık talebi ve belirttiği kapsam önceliklidir.
2. Kaynak metindeki olgular, belirsizlikler ve yazar tavrı korunur.
3. Doğal ve işlevini yerine getiren cümleler sırf değişiklik üretmek için bozulmaz.
4. Kronolojik yakınlık nedensellik gibi sunulmaz.
5. Birden fazla makul yorum varsa anlam editör tarafından seçilmez.
6. Metnin bir AI dedektöründen geçeceği vaat edilmez.
7. Bir cümle silindiğinde hiçbir önerme, ilişki, kronoloji, yorum veya yazar tavrı kaybolmuyorsa çıkarılır; dolgu başka dolguya çevrilmez.
8. Sözcükler tek başına yasaklanmaz; yargı birimi sözcüğün bağlamdaki işlevidir. Kısalık amaç değil, tekrar ve dolgunun çıkarılmasının sonucudur.
9. Yapı kavramsal sınırları izler. Her yeni başlık, paragraf veya liste okura bilişsel maliyet yükler; bu maliyet yalnızca anlama veya gezinme kazancıyla karşılanır. Okur, kavram zihninde yerleşmeden onu terk etmeye zorlanmaz; görsel parçalanma açıklık sayılmaz.

## İsteğe bağlı yardımcı kabiliyet

Metinoskop'un ana görevi mevcut metni düzenlemektir. Kullanıcı açıkça isterse, verilen kaynak bilgilerden temel bir kavram için bağlam, problem, soru ve çözüm ilişkisini gözeten kısa bir giriş de kurabilir. Bu yetenek otomatik olarak devreye girmez ve Metinoskop'u genel amaçlı bir içerik üretim aracına dönüştürmez.

## Kurulum

### Skills CLI

Metinoskop'u desteklenen agent ortamlarına genel olarak kurmak için:

```bash
npx skills add ayberkdt/metinoskop --global
```

Mevcut kurulumu güncellemek için:

```bash
npx skills update metinoskop --global
```

Yalnızca geçerli projeye kurmak isterseniz `--global` seçeneğini kaldırın. Kurulumdan sonra agent oturumunu yenileyin veya skill listesini yeniden yükleyin.

### Elle kurulum

Depoyu kullandığınız agent ortamının skill dizinine klonlayın:

```bash
git clone https://github.com/ayberkdt/metinoskop.git /path/to/skills/metinoskop
```

Çalışma zamanında gereken ana dosya `SKILL.md` dosyasıdır. `references/` klasörü ayrıntılı Türkçe örüntü, retorik yapılar (`retorik-yapilar.md`), yapısal bütünlük, Türkçe ritim ve kaynak dil gölgesi (`turkce-ritim-ve-ceviri-golgesi.md`), epistemik mimari (`epistemik-mimari.md`), eşdizim ve istem (`esdizim-ve-istem.md`), metinsel tutarlılık (`metinsel-tutarlilik.md`), akıcılık, rapor yazımı ve kavramsal giriş rehberlerini; `agents/openai.yaml` ise destekleyen istemciler için arayüz metadata'sını içerir.

## Kullanım

Skill'i doğrudan adıyla çağırabilirsiniz:

```text
$metinoskop

Aşağıdaki metni anlamını ve olgularını koruyarak doğal Türkçeyle düzenle:

[metin]
```

Doğal dilde bir talep de yeterlidir:

```text
Bu metni insanileştir; robotik ifadeleri ve pazarlama dilini temizle.
```

Metinoskop kaynak dilden çeviri yapmaz; Türkçeye çevrilmiş mevcut bir metni doğallaştırır.

Belirli bir müdahale düzeyi isteyebilirsiniz:

```text
Bu e-postaya hafif bir Metinoskop düzenlemesi uygula. Cümle yapısını mümkün olduğunca koru.
```

```text
Bu raporu derin düzeyde düzenle. Paragraf akışını yeniden kur fakat hiçbir sayı, tarih veya iddiayı değiştirme.
```

### Rapor düzenleme

Raporlarda yalnızca cümle akışını değil, önermelerin statüsünü de koruyabilirsiniz:

```text
$metinoskop

Bu raporu doğal ve profesyonel Türkçeyle düzenle. Bulgu, yorum, sınırlılık ve önerileri birbirine dönüştürme; tablo, atıf ve çapraz göndermeleri koru.

[rapor]
```

Metinoskop raporu daha “insani” göstermek için gündelikleştirmez veya süslemez. Bürokratik dolguyu azaltır, gerçek ilişkileri görünür kılar ve her iddiayı kaynakta taşıdığı kanıt düzeyinde tutar. Yönetici özeti ancak kullanıcı isterse üretilir ve rapor gövdesindeki bilgi ile sınırlı kalır.

### Retorik dolguyu çıkarma

Sözcük düzeyinde temiz görünen ama her olgudan sonra önem cümlesi kuran, her tercihi savunan ve her bölümü duyuruyla açan metinler için:

```text
$metinoskop

Bu makale bölümünü düzenle. Bilgi taşımayan cümleleri, dayanaksız önem iddialarını, savunmacı açıklamaları ve bölüm duyurularını çıkar; yöntem gerekçelerini, adlandırılmış sınırlılıkları, sayıları ve atıfları koru.

[metin]
```

Metinoskop dört düzeyde bakar: sözcük ve kalıp, cümle, paragraf, belge. Silinen dolgu daha sakin eş anlamlılarla geri konmaz; "çığır açan sonuç" ifadesi "oldukça önemli sonuç" olmaz, cümlenin bağımsız bilgisi yoksa cümle gider. Uzunluklar insan gibi görünsün diye rastgeleleştirilmez; paragraf boyutunu bilgi yapısı belirler.

### Yapısal parçalanmayı giderme

Her kavrama başlık açan, paragrafı her cümlede kesen, her bölümü duyuruyla açıp askıyla kapatan ve göndermeyle yamalanmış metinler için:

```text
$metinoskop

Bu bölümü derin düzeyde düzenle. Hak edilmemiş başlıkları birleştir, erken bölünmüş paragrafları baskın hareketlerine göre topla, sonuçla sınırlılığını yan yana getir; bütün ölçümleri, yöntem ayrıntılarını ve numaralı göndermelerin gerektirdiği bölümleri koru.

[metin]
```

Metinoskop yeni bir başlık, paragraf veya listeyi yalnızca kavramsal sınır gerektiriyorsa açık bırakır; bölümleri sayıyı azaltmak için birleştirmez, paragrafları uzun diye bölmez. Standart düzeyde mevcut başlık hiyerarşisi korunur; derin düzeyde başlıklar kavramsal sınırlara göre yeniden kurulur. Dergi kuralı, mevzuat, tekrarlanabilir deney bölümleri, güvenlik adımları ve uzun belgelerin gezinme başlıkları her düzeyde korunur.

### Çeviri gölgesini giderme

Sözcükleri, ekleri ve noktalaması doğru olduğu hâlde çeviri gibi okunan metin için:

```text
$metinoskop

Bu bölümü düzenle; metin Türkçeye çevrilmiş gibi değil, Türkçe düşünülmüş gibi okunsun. Her cümlede yinelenen özneyi, "bu sonuç / bu durum" paketlerini, "sahip olmak" ve "bulunmaktadır" kalıplarını, "ve" ile dizilmiş cümle zincirlerini ve çerçeve yığınlarını Türkçe yapıyla yeniden kur; sayıları, terimleri ve kesinlik düzeyini koru.

[metin]
```

Metinoskop sözcükleri bir kez daha çevirmez; cümlenin taşıdığı ilişkiyi bulup Türkçenin tercih ettiği araçla kurar. "Yöntem yüksek bir hesaplama maliyetine sahiptir" cümlesi "Yöntemin hesaplama maliyeti yüksektir" olur; "Model ... Model ... Model ..." dizisi tek aktörlü paragrafta özne düşürülerek birleşir, iki aktörlü paragrafta olduğu gibi kalır. Kaynak "ilişkili" diyorsa "neden olur" yazılmaz; alan terimleri öz Türkçe hevesiyle değiştirilmez; hukuki kalıp, teknik adlaştırma ve zaten Türkçe düşünülmüş metin dokunulmadan bırakılır.

### Kanıt mimarisini koruma

Akademik makale, teknik rapor ya da olay incelemesinde kimin ne bildiğinin ve ne kadar kesin söylediğinin değişmemesi için:

```text
$metinoskop

Bu tartışma bölümünü düzenle. Her iddiayı kaynaktaki kanıt düzeyinde tut: aktarımı olguya, ilişkiyi nedenselliğe, öneriyi karara çevirme; kaynağın adlandırmadığı aktörü uydurma; çekinceleri koru, dayanaksız pekiştiricileri kaldır.

[metin]
```

Metinoskop "Ekip, gecikmenin tedarikçi onayından kaynaklandığını bildirdi" cümlesini "Gecikme tedarikçi onayından kaynaklandı" yapmaz; "Kararın ertelenmesine karar verildi" cümlesine kaynakta adı geçmeyen bir yönetim eklemez; "bu veri kümesinde etki gözlenmedi" cümlesini "etki yoktur" yapmaz. Ölçümle desteklenen kesin iddiaya da çekince eklemez.

### Sözcük uyumu ve konu ilerleyişi

Yapısı Türkçe olduğu hâlde sözcükleri tuhaf birleşen ya da cümleleri iyi olduğu hâlde bir düşünceyi geliştirmeyen metin için:

```text
$metinoskop

Bu bölümü düzenle. Sözcükler doğal birleşsin: tuhaf eşdizimleri, yanlış hâl çerçevelerini ve hafif fiilleri gerçek yüklemle kur; teknik terimleri ve aynı nesnenin adını koru. Paragraflar birbirini izlesin: desteksiz "bu nedenle" ilişkilerini kaldır, kapsam işaretlerini ve olumsuzluğu yerinde tut, sınırlılığı sınırladığı iddianın yanına getir.

[metin]
```

"Karar gerçekleştirmek" "karar almak", "X hakkında odaklanmak" "X'e odaklanmak" olur; "gürültüden etkilenmez" ise "gürültüyü etkilemez" olmaz, çünkü hâl değişimi ilişkiyi değiştirir. "Sonuçlar hata oranının düştüğünü göstermiştir. Bu nedenle modelin genellenebilirliği yüksektir" cümlesindeki bağlaç, önermelerin desteklemediği bir ilişki kurduğu için kalmaz; eksik öncül de uydurulmaz.

### Yazarın sesini eşleştirme

Kendi yazınızdan kısa bir örnek vererek metnin o sese yaklaşmasını sağlayabilirsiniz:

```text
$metinoskop

Önce aşağıdaki iki paragraftan üslubumu çıkar:
[yazı örneği]

Şimdi bu metni aynı resmiyet, ritim ve doğrudanlık düzeyiyle düzenle:
[düzenlenecek metin]
```

Yazım yanlışları ve tesadüfi tekrarlar üslup özelliği olarak taklit edilmez.

### İsteğe bağlı kavramsal giriş

Temel bir kavramı kuru bir tanımla açmak yerine, kaynakta bulunan bilgiler arasında bütünlüklü bir giriş kurabilirsiniz:

```text
$metinoskop

Önbellek kavramını tanıtan kısa bir giriş yaz. Kaynakta bulunan bağlam, problem, soru ve çözüm arasında doğal bir akış kur; yeni risk veya fayda ekleme.

[kaynak bilgiler]
```

Problem kaynakta yoksa Metinoskop problem uydurmaz; bağlamdan doğrudan soruya veya kavrama geçer. Soru işareti ve retorik merak zorunlu değildir.

## Kısa örnek

**Önce**

> Günümüzün hızla değişen iş dünyasında yenilikçi platformumuz, siparişleri tek ekranda topluyor ve tekrar eden onayları otomatikleştiriyor. Bu güçlü çözüm yalnızca süreçleri kolaylaştırmakla kalmıyor, sipariş başına gereken adım sayısını beşten üçe indirerek verimliliği de bir üst seviyeye taşıyor.

**Sonra**

> Platform, siparişleri tek ekranda topluyor ve tekrar eden onayları otomatikleştiriyor. Bu değişiklik, sipariş başına gereken adım sayısını beşten üçe indiriyor.

Düzenlenmiş sürüm yeni özellik üretmez; kaynakta bulunan işlev ve ölçümü koruyup reklam kalıplarını çıkarır.

## Kapsam ve sınırlar

Metinoskop bir dil ve paragraf akışı editörüdür.

- Olgu doğrulaması yapmaz.
- Kaynakta olmayan bilgi üretmez.
- Kaynak dilden Türkçeye çeviri yapmaz; mevcut Türkçe çeviriyi düzenler.
- Belirsizliği gidermek için kaynakta bulunmayan bir yorum seçmez.
- Olumsuzlukları, koşulları, istisnaları ve nicelik sınırlarını silmez.
- Kullanıcı istemedikçe olay sırasını, sahne yapısını, bakış açısını veya anlatı sonucunu değiştirmez.
- Hukuki, akademik veya teknik metindeki gerekli terminolojiyi otomatik olarak gündelikleştirmez.
- Raporlarda bulguyu nedensel yoruma, öneriyi karara veya planı sonuca dönüştürmez.
- Her düzgün cümleyi değiştirmeye çalışmaz; metin zaten doğal ve uygunsa olduğu gibi bırakabilir.
- Kısaltmayı amaç edinmez; bilgi taşıyan cümleyi kısalık için kesmez.
- Yeni başlayanlara yönelik metinden öğretici açıklamayı, benzetmeyi veya örneği silmez.
- İnsan yazmış gibi görünmesi için hata, argo, rastgelelik veya cümle uzunluğu gürültüsü üretmez.
- Başlıkları sayıyı azaltmak için birleştirmez, paragrafları uzun diye bölmez, cümleleri mekanik olarak kısaltmaz veya birleştirmez.
- Kullanıcı hafif düzenleme veya yapı koruma istediyse başlık hiyerarşisine dokunmaz.
- Kaynağın adlandırmadığı aktörü uydurmaz; atıfı, çekinceyi, kapsam işaretini ve olumsuzluğu yönettikleri önermeden ayırmaz; bir iddiayı yeni kanıt olmadan sonraki bölümde güçlendirmez.
- Alanın terimini, ödünç sözcüğü, hukuki formülü ve süreç adını "daha Türkçe" olsun diye değiştirmez; hâl değişimiyle ilişkiyi değiştirmez; daha doğrudan fiil uğruna nedensellik eklemez.
- Kronolojiyi nedenselliğe çevirmez, eksik öncül uydurmaz, bilinçli kayıt değişimini (uyarı, alıntı, örnek) düzleştirmez, teknik noktalamayı bozmaz.

Kavramsal giriş yalnızca kullanıcı açıkça giriş yazılmasını istediğinde kullanılan ikincil bir kabiliyettir; olay örgüsünün, sahne yapısının veya bakış açısının yeniden kurulması değildir.

## Nasıl çalışır?

Metinoskop düzenleme sırasında altı aşamalı bir denetim uygular:

1. Metnin türünü, amacını, muhatabını; korunacak kapsam belirleyicilerini, terimleri ve gösterimleri belirler. Raporlarda bölüm ve paragraf işlevlerini de çıkarır.
2. Ritim, dolgu, reklam cilası, belirsiz atıf, çeviri kokusu ve akış sorunlarını; önem şişirmesi, savunmacı açıklama, işlev tekrarı, yol haritası ve tek biçimli mimariyi; yinelenen açık özne, `bu sonuç` ritmi, çekimli cümle zinciri, hafif yüklem ve çerçeve yığını gibi kaynak dil gölgesini kümeler hâlinde inceler.
3. Kullanıcının istediği müdahale düzeyinde düzenler.
4. Son metindeki sayı, tarih, iddia, nedensellik, karşılaştırma, koşul, istisna, nicelik sınırı, terim ve gösterimleri kaynakla karşılaştırır. Raporlarda bulgu–yorum–öneri sınırlarını, dayanakları ve çapraz göndermeleri de karşılaştırır.
5. Dokuz geçişli denetim yapar: kalıp, cümle ("bunu silersem hangi bilgi kaybolur?"), paragraf (farklı önerme sayısı, mini sonuç, zorlama denge, erken bölünme), belge (tekrarlanan giriş ve sonuç, tek biçimli mimari, aynı gerekçenin tekrarı), yapı (başlık sayısı ve derinliği, tek paragraflık bölümler, kopmuş yakınlık, çapraz gönderme sıklığı, yapay gerilim, gereksiz liste, uzun ifade), çeviri gölgesi (özne, yan cümle, niteleme, çerçeve, iyelik ve varlık, bilgi yapısı, yerli kaynak, aşırı düzeltme), epistemik mimari (kaynak ve statü, aktörlük, atıf, çekince–pekiştirici, kip, bölümler arası kesinlik), sözcük uyumu (eşdizim, istem, ilgeç, hafif fiil, terim kimliği) ve metinsel tutarlılık (konu ilerleyişi, bağlaç geçerliliği, gönderge mesafesi, kapsam ve olumsuzluk, kayıt, noktalama, iddia–dayanak yakınlığı).
6. Ses, ton, gönderge açıklığı ve paragraf akışını son kez gözden geçirir; gerekli sınırlılık veya öğretici açıklamanın dolgu sanılıp silinmediğini, metnin Türkçe düşünülmüş gibi okunup okunmadığını, her iddianın kaynaktaki kişiye ve kesinlik düzeyine bağlı kalıp kalmadığını ve her cümlenin öncekinden yararlı bir şey alıp sonrakine bırakıp bırakmadığını kontrol eder.

Kullanıcı açıkça kavramsal giriş istediğinde, düzenleme akışından önce kaynakta bulunan bağlam, problem, soru ve çözüm ilişkisi ayrıca çıkarılır.

Ayrıntılı örüntüler yalnızca gerektiğinde `references/` altından yüklenir; böylece ana skill yönergesi kısa ve taşınabilir kalır.

## Depo yapısı

```text
metinoskop/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── akicilik.md
│   ├── kavramsal-girisler.md
│   ├── rapor-yazimi.md
│   ├── retorik-yapilar.md
│   ├── turkce-oruntuler.md
│   ├── turkce-ritim-ve-ceviri-golgesi.md
│   ├── epistemik-mimari.md
│   ├── esdizim-ve-istem.md
│   ├── metinsel-tutarlilik.md
│   └── yapisal-butunluk.md
├── evals/
│   ├── akademik.md
│   ├── belirsizlik.md
│   ├── bicim-koruma.md
│   ├── hukuki.md
│   ├── kapsam-ve-kosul.md
│   ├── kurumsal.md
│   ├── kisisel.md
│   ├── kaynak-sadakati.md
│   ├── kavramsal-giris.md
│   ├── degisiklik-butcesi.md
│   ├── rapor-bulgu-yorum-oneri.md
│   ├── rapor-yapisal-butunluk.md
│   ├── teknik.md
│   ├── uslup-eslestirme.md
│   ├── yonetici-ozeti.md
│   ├── savunmaci-akademik.md
│   ├── iddia-tekrar-dongusu.md
│   ├── yol-haritasi.md
│   ├── yapay-denge.md
│   ├── giris-hunisi.md
│   ├── sonuc-ve-gelecek-calisma.md
│   ├── soyut-yuklem.md
│   ├── paragraf-simetrisi.md
│   ├── gerekli-ifade.md
│   ├── egitsel-aciklama.md
│   ├── iyi-metin.md
│   ├── asiri-bolumleme.md
│   ├── derin-baslik.md
│   ├── tek-paragraf-bolumler.md
│   ├── kisa-paragraf-yigini.md
│   ├── yapay-gerilim.md
│   ├── tekrarlanan-bolum-girisleri.md
│   ├── tekrarlanan-bolum-sonuclari.md
│   ├── asiri-capraz-gonderme.md
│   ├── uzun-cerceve-ifadeleri.md
│   ├── ayrilmis-kanit.md
│   ├── gereksiz-listeleme.md
│   ├── korunacak-basliklar.md
│   ├── yontem-ayrimi.md
│   ├── uzun-paragraf-korunur.md
│   ├── kisa-paragraf-korunur.md
│   ├── yapisal-iyi-metin.md
│   ├── tekrarlanan-acik-ozne.md
│   ├── bu-sonuc-ritmi.md
│   ├── asiri-bir.md
│   ├── sahip-olmak-kalkisi.md
│   ├── bulunmaktadir-kalkisi.md
│   ├── ve-zinciri.md
│   ├── dogal-ve-korunur.md
│   ├── yararli-ip-yapisi.md
│   ├── asiri-ip-zinciri.md
│   ├── art-niteleme.md
│   ├── gerekli-olan.md
│   ├── gereksiz-olan.md
│   ├── cerceve-yigini.md
│   ├── gerekli-acisindan.md
│   ├── soyut-ad-yuklemi.md
│   ├── teknik-adlastirma-korunur.md
│   ├── ozne-dusurme-akisi.md
│   ├── belirsizlik-icin-acik-ozne.md
│   ├── dogal-uzun-cumle-korunur.md
│   ├── asiri-yuklu-cumle.md
│   ├── ingilizce-soylem-belirtecleri.md
│   ├── hukuki-kalip-korunur.md
│   ├── teknik-ozne-tekrari-korunur.md
│   ├── yerli-turkce-metin.md
│   ├── (on sekiz epistemik mimari vakası: edilgen-korunur ... iyi-akademik-paragraf)
│   ├── (on beş eşdizim ve istem vakası: tuhaf-esdizim ... odunc-terim-korunur)
│   ├── (yirmi üç metinsel tutarlılık vakası: olgu-yigini ... tutarli-metin-korunur)
│   └── outputs/
├── scripts/
│   ├── eval-runner.py
│   ├── eval-suite.py
│   ├── style-lint.py
│   └── validate-package.py
├── .github/
│   └── workflows/
│       └── validate.yml
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Geliştirme ve doğrulama

Bağımlılık gerektirmeyen yerel paket kontrolü:

```bash
python scripts/validate-package.py
```

### Deterministik eval ön denetimi

Bir eval vakası için üretilen çıktıyı dosyaya kaydettikten sonra kaynak değişmezlerini denetleyebilirsiniz:

```bash
python scripts/eval-runner.py evals/teknik.md outputs/teknik.txt
```

JSON raporu almak için `--json` seçeneğini ekleyin. Çalıştırıcı; sayı ve tarihleri, URL'leri, satır içi kodu, kod bloklarını, dipnotları, kapsam belirleyicilerini, teknik adları, sembolleri ve ölçümleri kontrol eder. Birebir çıktı eşleşmesi aramaz; akıcılık, ton ve genel anlam uyumu insan veya model hakemine bırakılır.

Çalıştırıcının yerleşik örneklerini sınamak için:

```bash
python scripts/eval-runner.py --self-test
```

### Stil denetimi

Bir çıktıdaki şüpheli retorik örüntüleri işlev ailesine göre işaretlemek için:

```bash
python scripts/style-lint.py outputs/iddia-tekrar-dongusu.txt --source evals/iddia-tekrar-dongusu.md
```

`scripts/style-lint.py` üretilmiş önem, savunmacı açıklama, yol haritası, boş bölüm sarmalayıcısı, yapay gerilim, paragraf sonu askısı, çapraz gönderme, bağlam yeniden başlatma, uzun çerçeve ifadesi, kalıp giriş ve sonuç, üretilmiş karşıtlık, zorlama denge, soyut yüklem, boş özne ve sohbet botu kalıntısı ailelerini işaretler; parçalanma yoğunluğunu (başlık sayısı ve derinliği, başlık başına paragraf, tek paragraflık bölüm, kısa paragraf oranı, liste ögesi, çapraz gönderme) özetler ve paragraf uzunluğu tek biçimliliği, önem cümlesiyle kapanış, başlık tekrarı, bağlaçla açılış ve işlev tekrarı gibi yapı bulgularını raporlar. `--source` ile yapı ölçülerindeki değişimi de gösterir. Tek bir sözcüğe bakarak metni reddetmez; `--source` verildiğinde kaynakta olmayıp çıktıda beliren kalıpları kalıp düzeyinde ayrıca listeler (aynı aileden farklı bir kalıp da yeni sayılır). `--fail-on-introduced-hard` yalnızca sert bastırma ailesinden yeni kalıp eklendiğinde başarısız çıkış kodu verir; bağlamsal aileler (`yani`, `öte yandan`, `işaret etmek`) uyarı olarak kalır. `--fail-on-introduced-any` katı moddur. Rapor ayrıca çeviri gölgesi ölçülerini verir: `sahip olmak` ve varlık kalıbı işaretleri, tek cümlede çerçeve yığını ve `olan` zinciri, aynı özneyle başlayan ardışık cümleler, `ve` zinciri, fiilimsi yığını, iyelik zinciri, söylem belirteciyle başlayan cümle oranı ve 100 sözcük başına `bir`. Bunlar yalnızca inceleme bulgusudur; tek `bir`, `olan`, `ve` ya da `açısından` işaretlenmez ve `--source` ile çıktıda yeni beliren gölge bulguları uyarı olarak listelenir. Söylem ölçüleri de aynı statüdedir: çekince, pekiştirici, aktarım ve hafif fiil aileleri; tek cümlede kiplik yığını ve pekiştirici çatışması, atıflı cümleden sonra gelen "bu nedenle", bir paragrafta gerekçesiz kip nöbetleşmesi, edilgen ile adlaştırma yığını, ilgeç yoğunluğu, aynı nesneye giden genel adlar, "bu çalışmada" ile açılan bölümler, ara söz yükü ve sohbet gerilimi ile bürokratik kayıt çatışması. Hiçbir regex epistemik doğruluğa karar vermez. Öz sınama için:

```bash
python scripts/style-lint.py --self-test
```

### Kayıtlı çıktı regresyonu

`evals/outputs/` altındaki referans düzenlemeler üzerinde değişmez, sert kalıp ve yapısal beklenti denetimini çalıştırmak için:

```bash
python scripts/eval-suite.py
```

`scripts/eval-suite.py` CI'da çalışır; her vaka için model hakem istemi üretmek üzere `--export-judge-prompts DIR` seçeneğini kullanabilirsiniz. Taze model çıktısı üretip otomatik puanlayan tam davranışsal regresyon henüz depoda yoktur.

Agent Skills keşfini denetlemek için:

```bash
npx --yes skills@1.5.20 add . --list
```

GitHub Actions, `main` dalına gönderilen her değişiklikte ve pull request'lerde bu kontrolleri çalıştırır.

`evals/` klasörü tek bir beklenen çıktı dayatmaz. Her vaka; korunması gereken olguları, kesinlik düzeyini ve biçimi, ayrıca kaçınılması gereken davranışları tanımlar. Rapor vakaları bulgu–yorum–öneri sınırını, yapısal bütünlüğü ve yönetici özetinin gövdeye sadakatini de sınar. Retorik mimari vakaları savunmacı düzyazıyı, tekrar döngülerini, yol haritasını, yapay dengeyi, kalıp giriş ve sonuçları, soyut yüklemleri, paragraf simetrisini; ayrıca yanlış pozitif ve zaten iyi metin durumlarını sınar. Yapısal bütünlük vakaları aşırı bölümlemeyi, başlık derinliğini, tek paragraflık bölümleri, kısa paragraf yığınını, yapay gerilimi, tekrarlanan bölüm giriş ve sonuçlarını, çapraz göndermeyi, uzun çerçeve ifadelerini, ayrılmış kanıtı ve listeleştirmeyi; karşı tarafta korunması gereken başlıkları, tekrarlanabilir yöntem ayrımını, uzun ve kısa kalması gereken paragrafları ve yapısı iyi metni sınar. Çeviri gölgesi vakaları yinelenen açık özneyi, `bu sonuç` ritmini, fazla `bir` sözcüklerini, `sahip olmak` ve `bulunmaktadır` kalkılarını, `ve` zincirini, yararlı ve aşırı `-ip` yapısını, art nitelemeyi, `olan` zincirini, çerçeve yığınını, soyut ad yüklemini, özne düşürme akışını, aşırı yüklü cümleyi ve İngilizce söylem belirteçlerini; karşı tarafta korunması gereken doğal `ve`, gerekli `olan` ve `açısından`, teknik adlaştırma, belirsizliği önleyen açık özne, yerli uzun cümle, hukuki kalıp, teknik özne tekrarı ve zaten Türkçe düşünülmüş metni sınar. Epistemik vakalar edilgen çatının korunmasını ve etkene çevrilmesini, bilinmeyen aktörü, aktarımı, ölçüm ile çıkarımı, çekince ve pekiştiriciyi, kip değişimini, öneri–karar–uygulama statülerini, olumsuz kanıtı, atıf kapsamını ve bölümler arası kesinliği; eşdizim vakaları tuhaf ve teknik eşdizimi, hâl çerçevesini, edat aktarımını, hafif fiili, süreç adını, genel fiili, eş anlamlı kaymasını, kanonik terimi, hukuki formülü ve ödünç terimi; tutarlılık vakaları olgu yığınını, ilerleyiş örüntülerini, desteksiz ve geçerli bağlacı, gönderge mesafesini, bölüm başı sıfırlamayı, paragraf devrini, işlev kaymasını, kronolojiyi, kapsam ve olumsuzluk bağlanmasını, kayıt kararlılığını, noktalamayı, uzak sınırlılığı ve meşru ya da hacim yinelemesini sınar. Böylece farklı ama geçerli düzenlemeler aynı editoryal ölçütlerle değerlendirilebilir.

## Sürümleme

Proje anlamsal sürümleme yaklaşımını izler. Kullanıcıya dönük davranış ve paket değişiklikleri [CHANGELOG.md](CHANGELOG.md) dosyasında kaydedilir. En güncel sürüm etiketi `v0.4.1`'dir.

## Katkı

Hata örneklerini ve geliştirme önerilerini [GitHub Issues](https://github.com/ayberkdt/metinoskop/issues) üzerinden paylaşabilirsiniz. Davranış değişikliği yapan pull request'lerde `SKILL.md`, README ve ilgili eval vakalarının birbiriyle uyumlu kalması gerekir.

## Lisans

Bu proje MIT Lisansı altında yayımlanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.
