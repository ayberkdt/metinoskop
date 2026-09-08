---
name: metinoskop
description: Türkçe metinlerde mekanik yapay zekâ ritmini, basmakalıp geçişleri, gereksiz resmiyeti, kurumsal ve pazarlamacı cilayı, tiyatral vurguyu ve çeviri kokusunu azaltır; bilgi taşımayan cümleleri, dayanaksız önem iddialarını, savunmacı açıklamaları, yol haritası cümlelerini, kalıp giriş ve sonuçları, üretilmiş karşıtlık ve dengeyi sözcük, cümle, paragraf ve belge düzeyinde ayıklar; gereksiz başlık, erken bölünmüş paragraf, yapay gerilim, bağlam tekrarı, aşırı çapraz gönderme, listeleştirme ve uzun çerçeve ifadeleri gibi okuru yoran parçalanmayı onarır; dil bilgisi doğru olduğu hâlde İngilizce cümle iskeleti taşıyan metinde yinelenen açık özne, `bu sonuç` ritmi, `ve` ile dizilmiş çekimli cümle zinciri, `sahip olmak` ve `bulunmaktadır` kalkıları, çerçeve yığını, `olan` zinciri ve fazla `bir` gibi kaynak dil gölgesini Türkçenin özne düşürme, fiilimsi, ortaç, iyelik, hâl eki ve sözcük sırası kaynaklarıyla yeniden kurar; kimin bildiğini, nasıl bildiğini ve ne kadar kesin iddia ettiğini (gözlem, ölçüm, aktarım, çıkarım, öngörü, plan, öneri, karar) düzenleme boyunca aynı düzeyde tutar; eşdizim, fiil istemi, hâl ve ilgeç seçimi, hafif fiil ve terim kararlılığı ile sözcüklerin doğal Türkçedeki gibi birleşmesini sağlar; konu ilerleyişi, bağlaç geçerliliği, gönderge mesafesi, kapsam ve olumsuzluk bağlanması, kayıt kararlılığı ve noktalama ritmiyle metnin bir düşünceyi geliştirmesini gözetir. Anlamı, olguları, kesinlik düzeyini, iletişim amacını ve yazarın sesini koruyarak doğal Türkçeyle düzenler. Makale, tez, deneme, haber, rapor, teknik belge, tanıtım metni, e-posta, sosyal medya metni, açıklama veya Türkçeye çevrilmiş metin için "insanileştir", "doğal Türkçe yap", "AI gibi görünmesin", "robotik ifadeleri temizle", "dolguyu çıkar", "parçalanmayı gider", "başlıkları sadeleştir", "pazarlama dilini azalt", "çeviri gibi durmasın", "Türkçe düşünülmüş gibi olsun", "kesinlik düzeyini bozma", "sözcükler doğal birleşsin", "paragraflar birbirini izlesin" ya da "kendi üslubuma uyarla" dendiğinde kullan.
---

# Metinoskop

Türkçe metni bir sözcük yasaklama listesiyle değil; bağlam, iletişim amacı, kaynak sadakati ve doğal Türkçe ritmi üzerinden düzenle. Yapay üslubu yalnızca sözcüklerde değil, cümle, paragraf ve belge kuruluşunda ara. Okurun bir argümanın içinde, onu anlayacak kadar uzun kalabilmesini sağla.

## Kural önceliği

Çatışma olduğunda şu sırayı uygula:

1. Kullanıcının açık talebi ve belirttiği kapsam
2. Kaynak metindeki olgular, iddialar, belirsizlikler ve yazar tavrı
3. Kullanıcının sağladığı üslup örneği
4. Metnin iletişim amacı, türü ve muhatabı
5. Bu skill'deki genel dil tercihleri

Bir alt sıradaki kural, üst sıradakini bozmasın.

## Görevin sınırı

- Ana görev olarak mevcut metnin dilini, paragraf akışını ve gerekiyorsa bölüm yapısını düzenle.
- Kullanıcı açıkça kaynak bilgilerden bir giriş yazılmasını istemedikçe yeni bölüm üretme.
- Yeni olgu, tarih, sayı, alıntı, kaynak, özellik, sonuç, deneyim veya kişisel görüş üretme.
- Kaynak dilden Türkçeye çeviri yapma; Türkçeye çevrilmiş mevcut metni doğallaştır.
- Kullanıcı istemedikçe olay sırasını, sahne yapısını, bakış açısını veya anlatı sonucunu değiştirme. Anlatı yapısının yeniden kurulması bu skill'in kapsamı dışındadır.
- Alıntıları, kodu, URL'leri, dipnotları, kaynak işaretlerini, tablo hücrelerini ve Markdown yapısını koru. Başlık hiyerarşisini yalnızca kullanıcı yapısal düzenleme istediğinde veya derin düzeyde, kavramsal sınırlara göre değiştir.
- Bir metnin herhangi bir AI dedektöründen geçeceğini vaat etme. Dedektör için hata veya yapay çeşitlilik üretme.

## Bağlam profilini çıkar

Yazmadan önce sessizce belirle:

- **Tür:** akademik, teknik, haber, hukuki, kurumsal, tanıtım, gündelik, kişisel veya edebî
- **Amaç:** bilgi verme, açıklama, ikna, talep, eleştiri, savunma, değerlendirme, duygu aktarma veya resmî kayıt
- **Muhatap:** uzman, genel okur, yeni başlayan, müşteri, çalışma arkadaşı, kurum veya kişisel çevre
- **Ses:** resmiyet, doğrudanlık, kişi tercihi, terim yoğunluğu ve duygusal sıcaklık
- **Yapısal ölçek:** yazar uzun bağlantılı pasajlarla mı, kısa işlevli bölümlerle mi yazıyor; belge yapısı dışarıdan (dergi, mevzuat, şablon) dayatılmış mı?
- **İstenen değişiklik:** yalnızca belirtilen sorun mu, yoksa genel editörlük mü?
- **Rapor işlevi:** metin raporsa bölüm veya paragraf bağlam mı, yöntem mi, bulgu mu, yorum mu, sınırlılık mı, öneri mi taşıyor?

Bir metin aynı anda birden fazla amaç taşıyabilir. Kurumsal bir duyuru hem bilgi verebilir hem ikna edebilir; ikna amacını otomatik olarak silme. Muhatabın bilgi düzeyi, hangi açıklamanın gerekli hangisinin dolgu olduğunu belirler.

## İkincil kabiliyet: kavramsal giriş

Yalnızca kullanıcı açıkça temel bir kavramı tanıtan giriş yazılmasını istiyorsa kaynakta bulunan bilgilerle şu hareketi kur: okurun bildiği durumu veya somut bağlamı göster; kavramı gerekli kılan gerçek problemi ya da bilgi boşluğunu belirginleştir; bölümün cevaplayacağı soruyu doğal biçimde görünür kıl; kavramı, yöntemi veya yaklaşımı bu sorunun cevabı olarak sun.

Bu sıralamayı zorunlu şablon gibi uygulama. Kaynakta problem yoksa problem, risk veya aciliyet uydurma; doğrudan bağlamdan kavrama geç. Soruyu mutlaka soru işaretiyle yazma. Merakı retorik heyecanla değil, henüz cevaplanmamış somut noktayla kur.

## Müdahale düzeyi

Kullanıcının istediği kapsamı aşma. Kullanıcı yalnızca belirli bir sorun söylediyse müdahaleyi o sorunla sınırla; "tiyatral ifadeleri çıkar" talebi metnin tamamını yeniden yazma izni değildir.

**Hafif.** Belirgin klişeleri, sohbet botu kalıntılarını, tiyatral vurguyu ve gereksiz dolguyu temizle. Önerme taşımayan cümleyi yalnızca açık dolgu, bölüm duyurusu, üretilmiş önem veya sohbet kalıntısıysa çıkar. Cümle yapısını, paragraf sırasını, başlıkları ve kelime tercihlerini mümkün olduğunca koru.

**Standart.** Cümleleri ve paragraf içi akışı gerektiğinde yeniden kur. Mekanik ritmi, gereksiz resmiyeti, belirsiz göndergeleri, çeviri kokusunu ve kaynak dil gölgesini (yinelenen açık özne, çekimli cümle zinciri, `sahip olmak` ve `bulunmaktadır` kalkıları, çerçeve yığını, `olan` zinciri, fazla `bir`) düzelt. Sıfır bilgi cümlelerini, işlev tekrarını, savunmacı açıklamayı, üretilmiş önem ve karşıtlığı, yol haritası dilini, kalıp giriş ve sonuç cümlelerini, yapay gerilimi ve uzun çerçeve ifadelerini çıkar. Erken bölünmüş paragrafları birleştir; mevcut başlık hiyerarşisini koru. Kullanıcı bir düzey belirtmediyse bunu kullan.

**Derin.** Bilgi sırasını, paragraf yapısını ve bölüm yapısını kavramsal sınırlara göre yeniden düzenle. Hak edilmemiş başlıkları birleştir veya kaldır, tekrarları birleştir, ayrılmış kanıtı iddiasına yaklaştır, metin boyunca ton ve ritim tutarlılığı kur. Olguları, ayrıntıları, kesinlik düzeyini, yazar tavrını ve dışarıdan dayatılan yapıyı koru.

## Değişiklik bütçesi

Metin zaten doğal, açık ve kullanıcının istediği tona uygunsa metni olduğu gibi bırak veya yalnızca zorunlu düzeltmeleri yap. Her görevde görünür değişiklik üretmek zorunda değilsin.

Doğal, açık ve işlevini yerine getiren bir cümleyi sırf farklı görünsün diye değiştirme. Her değişikliğin belirli bir gerekçesi olsun: anlam açıklığı; cümle veya paragraf akışı; klişe ya da dolgu; önerme taşımayan cümle veya işlev tekrarı; mekanik ritim veya tek biçimli mimari; hak edilmemiş yapısal sınır, bağlam tekrarı veya kopmuş yakınlık; ton ve amaç uyumu; gönderge açıklığı; kaynak veya kesinlik sadakati.

Gerekçesi olmayan değişikliği geri al. Kısalık kendi başına amaç değildir; tekrar ve dolgu çıkarılınca ortaya çıkan sonuçtur. Bilgi taşıyan bir cümleyi kısaltmak için kesme; paragrafı uzun diye bölme, başlığı sayıyı azaltmak için birleştirme.

## Kaynak sadakati

Metindeki önermeleri sessizce ayır: doğrulanabilir olgu veya ölçüm; amaç, plan veya vaat; görüş ya da değerlendirme; duygu veya kişisel tavır; belirsizlik ve çekince; tekrar, dolgu veya işlevsiz süs. İlk beş sınıfın anlamını ve kesinlik düzeyini koru. Son sınıfı başka sözcüklerle yeniden üretme.

- Bir hedefi gerçekleşmiş sonuç gibi yazma.
- Bir değerlendirmeyi ölçülmüş olguya dönüştürme.
- Kronolojik yakınlığı nedensellik gibi sunma.
- Kaynak yalnızca ilişki bildiriyorsa etki veya neden iddiası ekleme.
- Karşılaştırma zemini yoksa `daha`, üstünlük ölçütü yoksa `en` ekleme.
- Olumsuzluğu, istisnaları, koşulları ve nicelik sınırlarını koru.
- `Bazı` ifadesini `tüm`, `en az` ifadesini kesin sayı, `yalnızca` ifadesini genel kapsam hâline getirme.
- Bir hükmün veya sonucun hangi kişi, dönem, grup, koşul ya da bağlamla sınırlı olduğunu silme.
- `Henüz`, `artık`, `genellikle`, `kural olarak` ve benzeri kapsam belirleyicileri işlevsiz dolgu gibi çıkarma.
- Soyut övgünün dayandığı somut bilgi kaynakta varsa onu öne çıkar. Yoksa yeni dayanak üretme.
- Kaynaktaki sayılardan yeni sayı türetme; oran, fark, ortalama veya birim başına değer hesaplayıp ekleme.

## Belirsizlik ve yorum seçimi

Kaynak metindeki bir ifade birden fazla makul yoruma açıksa anlamı kendin seçme. Belirsizlik korunarak doğal bir düzenleme yapılabiliyorsa ifadeyi koru. Düzenleme mutlaka bir yorum seçmeyi gerektiriyorsa kullanıcıdan açıklama iste. Kullanıcı inceleme veya karşılaştırma istediyse belirsizliği kısa bir notla belirt; yalnızca son metni istediyse açıklama eklemek yerine kaynak anlamını en az değiştiren yapıyı koru.

## Değerlendirme ile olguyu ayır

Soyut ifade her zaman gereksiz değildir. Yazarın duygusunu, değerlendirmesini veya ikna amacını taşıyabilir.

- Bilgi verme amacı taşıyan bölümde olgu gibi sunulan kanıtsız fayda ve üstünlük iddiasını daralt, kaynağı varsa ona bağla veya çıkar.
- "Bu proje bizim için önemli bir dönüm noktasıdır" gibi açık yazar değerlendirmesini, değerlendirme olduğu anlaşılacak biçimde koru.
- Tanıtım metninde ikna amacını koru; hazır reklam kalıplarını daha özgül ve ölçülü bir söyleyişle değiştir.
- Kullanıcı özellikle "pazarlama dilini kaldır" veya "nötrleştir" dediyse soyut fayda ve üstünlük iddialarını daha sıkı temizle.
- Reklam cümlesini yalnızca daha sakin eş anlamlılarla yeniden kurma. Cümlenin işlevini ve metindeki dayanağını değerlendir.

Yazar değerlendirmesi ile üretilmiş önem farklıdır: değerlendirme, kaynakta bir kişiye veya kuruma ait bir tavırdır; üretilmiş önem, bir olgu var diye eklenen genel önem cümlesidir. İlkini koru, ikincisini çıkar.

## Dört düzeyde yapay düzyazı

Hiçbir klişe sözcük içermeyen bir metin, her olgudan sonra önem cümlesi kuruyor, her paragrafı aynı şablonla kapatıyor ve her bölümü duyuruyla açıyorsa yine yapay okunur. Sözcük ve kalıp düzeyinde klişe, reklam dili, tiyatral vurgu, sohbet botu kalıntısı ve çeviri kokusuna; cümle düzeyinde bilgi taşımayan cümle, dayanaksız önem, savunmacı gerekçe, üretilmiş karşıtlık, soyut yüklem ve boş özneye; paragraf düzeyinde açımlama döngüsü, mini sonuç, zorlama denge ve tek biçimli şablona; belge düzeyinde kalıp giriş ve sonuç, yol haritası, aynı gerekçenin tekrarı ve yazarın sesini silen türdeş cilaya bak.

Hedef; gündelik, kesik veya bilerek kusurlu bir metin değil, her cümlesi yerini hak eden kesin, doğal ve tutumlu Türkçedir. Sözcük tek başına asla yasak değildir; yargı birimi sözcüğün bağlamdaki işlevidir. Ayrıntılı katalog ve örnekler için [Retorik yapılar](references/retorik-yapilar.md) dosyasını oku.

### Cümle düzeyi

**Sıfır bilgi cümlesi.** Bir cümle normalde şunlardan en az birini taşımalıdır: yeni bir olgu; gerekli bir nitelendirme; zaten açık olmayan bir mantıksal ilişki; kaynağın desteklediği somut bir yorum; gerçek bir konu değişiminin gerektirdiği geçiş; kaynakta bulunan bir yazar değerlendirmesi; gerekli bir yöntem gerekçesi; yorumu değiştiren bir sınırlılık, koşul veya belirsizlik; ya da yeni önerme eklemeden önceki bilgiyi anlamlı biçimde birleştiren bir sentez (üç dağınık bulguyu tek karar cümlesinde toplamak, uzun bir teknik zinciri okurun yerine sıkıştırmak, paragrafın sonucunu gerçekten netleştirmek). Yeni önerme yokluğu işlev yokluğu değildir. Silme testi iki sorudur: cümleyi çıkardığında önermeler, akıl yürütme, kronoloji, yorum ve yazar tavrı değişiyor mu; değişmiyorsa, cümle yeni bilgi eklemese bile önceki bilgiyi anlamlı biçimde birleştiriyor veya okurun çıkarım yükünü azaltıyor mu? İkisine de hayırsa cümleyi çıkar. Sentez ile açımlamayı ayır: sentez birden çok önceki olguyu tek ilişkide veya kararda toplar, açımlama tek olguyu başka sözcüklerle yineler. Önceki cümleyi soyut sözcüklerle yineleyen, önceki olgunun önemli olduğunu söyleyen, metnin birazdan ne söyleyeceğini duyuran, bir cümle önce söyleneni özetleyen, kanıt eklemeden sonucun önemini öven, zaten açık veya gerekçelendirilmiş bir tercihi savunan ve somut sonucu belirsiz soyut adlarla yeniden anlatan cümleler bu testi genellikle geçemez.

> Model 120. derecede en düşük hatayı verdi. Bu sonuç, yöntemin farklı koşullar altındaki davranışının anlaşılması açısından önemli bir bulgudur.

Kaynakta bağımsız bir önem iddiası yoksa ikinci cümle silinir. "Bu bulgu yöntemin davranışına ışık tutmaktadır" diye yeniden yazılmaz; bu, aynı dolgunun yeni sözcüklerle kurulmasıdır.

**Dolguyu başka dolguya çevirme.** Kesin kural: reklam dili, önem şişirmesi, retorik çerçeve, savunmacı açıklama, boş geçiş veya kalıp sonuç çıkarılırken aynı retorik işlev daha sakin eş anlamlılarla korunmaz. "Çığır açan sonuç" → "oldukça önemli sonuç", "bir üst seviyeye taşıyor" → "önemli ölçüde geliştiriyor", "bu noktada vurgulamak gerekir" → "burada belirtmek gerekir" dönüşümleri yanlıştır. Cümlenin bağımsız bir bilgi işlevi yoksa cümleyi sil; varsa yalnızca o bilgiyi bırak.

**İşlev tekrarı.** Yalnızca yinelenen sözcükleri değil, yinelenen retorik işlevleri ara. "Bu sonuç önemlidir", "Bu bulgu dikkat çekicidir", "Bu durum kayda değerdir" ve "Bu da yöntemin önemini ortaya koymaktadır" sözcük olarak farklı, işlev olarak aynıdır; tekrar sayılır. Aynı işlevi gören cümleleri paragraf ve belge boyunca birlikte ele al: kaynakta dayanağı olan varsa onu koru, diğerlerini çıkar.

**Savunmacı düzyazı.** Dil modelleri her cümleyi görünmez bir hakeme karşı savunur gibi yazar. "Burada amaç ... değildir", "Dikkat edilmesi gereken nokta ...", "Şunu vurgulamak gerekir ki ...", "Bu noktayı özellikle belirtmek gerekir", "Bu ayrım önemlidir", "Bu tercih tesadüfi değildir", "Bu seçim bilinçlidir", "Bu durum bir eksiklik olarak görülmemelidir", "Bu, yöntemin bir zayıflığı değildir", "Bunun nedeni oldukça basittir", "Bu yaklaşımın amacı ...", "Buradaki temel fikir ...", "Bu noktada önemli olan ...", "Asıl önemli olan ...", "Bu açıdan bakıldığında ...", "Bu çerçevede değerlendirmek gerekir", "Bu nedenle burada ... tercih edilmiştir", "Bunun özellikle altını çizmek gerekir", "Yanlış anlaşılmaması gereken nokta ...", "Bu sonuç şaşırtıcı değildir", "Bu durum beklenen bir sonuçtur" aileleri gerçek bir belirsizliği veya yöntem sorusunu cevaplamıyorsa yüksek risklidir. Bunları mekanik olarak silme; her biri için sor: bu cümle okurun hangi somut yanlış anlamasını önlüyor? Somut cevap yoksa çıkar. Yöntem gerekçesi, tercih değiştiğinde yorum, tekrarlanabilirlik veya geçerlilik değişecekse meşrudur; ön deneme sonucu, ıraksama, veri kısıtı gibi somut dayanağı varsa dayanakla birlikte koru. Olağan bilimsel uygulamayı önceden savunma.

**Üretilmiş önem.** Bir sonuç var diye önem üretme. "... açısından önemlidir", "... kritik öneme sahiptir", "... önemli bir rol oynamaktadır", "... temel bir rol üstlenmektedir", "... belirleyici olmaktadır", "... dikkat çekici bir sonuçtur", "... kayda değer bir bulgudur", "... önemli çıkarımlar sunmaktadır", "... önemli bilgiler sağlamaktadır", "... değerli içgörüler sunmaktadır", "... anlayışımızı geliştirmektedir", "... daha iyi anlaşılmasını sağlamaktadır", "... literatüre katkı sunmaktadır", "... literatürdeki boşluğu doldurmaktadır", "... yeni bir perspektif sunmaktadır", "... gelecekteki çalışmalar için temel oluşturmaktadır" ifadeleri kaynak açıkça gerekçelendirmiyorsa çıkar; somut sonucun kendisini bırak. Kaynak önemi dayanağıyla birlikte kuruyorsa tam o güçte koru. Bir cümlenin kaynakta yer alması onu korumaya yetmez; düzenlenen metnin kendisi dolgu içerebilir. Önem cümlesi yalnızca bir kişiye veya kuruma atfedilmişse, kendi dayanağını taşıyorsa ya da türün gerektirdiği açık bir değerlendirme konumundaysa yazar değerlendirmesi sayılır; bulgu paragrafındaki genel "bu bulgu önemlidir" cümlesi bu üç koşulun hiçbirini karşılamaz.

**Üretilmiş karşıtlık.** Karşıtlık bilgi taşıyorsa meşrudur; yalnızca retorik güç için kurulmuşsa yapaydır. Tekrar eden "X değil, Y", "Mesele X değil, Y", "Asıl mesele X", "Buradaki soru X değil", "X'ten ziyade Y", "X yerine Y", "Bir yandan X, diğer yandan Y", "Her ne kadar X olsa da Y", "X basitçe ... değildir", "X yalnızca ... ile sınırlı değildir", "X bunun ötesine geçmektedir", "X bir ... olmaktan öte ..." ve "yalnızca ... değil, aynı zamanda ..." yapılarını incele. Kabul edilen önermeyi güçlü göstermek için reddedilen bir seçenek uydurma; reddedilen taraf kaynakta yoksa yalnızca kabul edilen önermeyi yaz.

**Soyut yüklem sisi.** `ortaya koymak`, `gözler önüne sermek`, `işaret etmek`, `yansıtmak`, `vurgulamak`, `altını çizmek`, `öne çıkarmak`, `dikkat çekmek`, `rol oynamak`, `katkı sağlamak`, `olanak sağlamak`, `imkân tanımak`, `mümkün kılmak`, `çerçeve sunmak`, `perspektif sunmak`, `içgörü sunmak`, `zemin hazırlamak`, `temel oluşturmak`, `kapı aralamak`, `ışık tutmak`, `şekillendirmek`, `desteklemek`, `güçlendirmek`, `geliştirmek` yüklemlerini tek tek yasaklama; her birinde hangi somut ilişkinin kodlandığını sor ve mümkünse yüklemi o ilişkiyle değiştir. "Sonuçlar sıcaklığın hata üzerinde belirleyici rol oynadığını göstermektedir" cümlesinin kanıtı yalnızca "Hata 20 °C'de %3, 40 °C'de %11 oldu" ise ölçümleri yaz; çıkarım cümlesi kaynağın kendi iddiasıysa koru.

**Boş soyut özne.** Tekrarlanan `bu durum`, `bu yaklaşım`, `bu yapı`, `bu süreç`, `bu çerçeve`, `bu bağlam`, `bu bulgu`, `bu sonuç`, `bu özellik`, `bu yöntem`, `bu perspektif`, `söz konusu durum`, `ilgili süreç` özneleri güçlü bir yapaylık işaretidir. Mekanik olarak değiştirme: mümkünse somut göndergeye çöz; özne yalnızca dolguyu taşımak için varsa cümleyi çıkar. Gönderge belirsizse belirsizlik kuralı geçerlidir.

**Açık olanı açıklama.** Cümle, hedef okurun zaten bildiği olağan bir olguyu felsefi gerekçe gerektiriyormuş gibi açıklıyor mu? "Doğrulama verisinin eğitim verisinden ayrı tutulması önemlidir; çünkü aksi halde model daha önce gördüğü örnekler üzerinde değerlendirilmiş olur" cümlesi giriş düzeyindeki ders notunda gereklidir; uzman okura yazılmış araştırma makalesinde standart dışı bir tercihi açıklamıyorsa gereksizdir. Yeni başlayanlara yönelik metinden öğretici açıklamayı, benzetmeyi veya örneği silme. Muhatap belirsizse açıklamayı koru; "açık olan" kararını yalnızca tür ve okur açıkça belliyken ver.

### Paragraf düzeyi

**İddia → açımlama → önem → mini sonuç.** Şu diziyi tanı: olgu → aynı olgunun başka sözcüklerle tekrarı → genel önem cümlesi → soyut mini sonuç.

> Model 120. derecede en düşük hatayı verdi. Başka bir ifadeyle bu derece diğer seçeneklerden daha başarılıydı. Bu sonuç derece seçiminin kritik önemini göstermektedir. Dolayısıyla uygun derece seçimi performans açısından belirleyicidir.

Kaynak yalnızca ilk önermeyi kuruyorsa son üç cümle fazladır; diziyi kaynağın desteklediği önermeye indir. Tekrarı ad ve fiilleri eş anlamlılarla değiştirerek koruma. Paragraf testi: paragraf kaç gerçekten farklı önerme içeriyor? Dört cümle iki önerme taşıyorsa yeniden kur veya sıkıştır.

**Paragraf simetrisi.** Neredeyse eşit uzunlukta paragraflar, her paragrafın konu cümlesiyle başlayıp sonuç cümlesiyle bitmesi, sabit üç veya dört cümlelik paragraflar, tekrarlayan "nokta → açıklama → sonuç" mimarisi, düzenli kısa-uzun cümle nöbetleşmesi ve her bölümde gereksiz giriş ile mini özet yapaylık işaretidir. Sorun belirli bir uzunluk değil tek biçimliliktir; tek cümlelik paragraf da on cümlelik paragraf da meşru olabilir. Uzunlukları insan gibi görünsün diye rastgeleleştirme; paragraf boyutunu bilgi yapısı belirlesin.

**Zorlama denge.** Her iddiaya kendi karşı iddiasını ekleme. "Bir yandan ... Öte yandan ...", "Avantajlarına rağmen ...", "Bununla birlikte ...", "Her ne kadar ... olsa da ...", "Bu yaklaşım güçlü olmakla birlikte bazı sınırlamalara da sahiptir" yalnızca ölçülü görünmek için kurulmuşsa çıkar. Gerçek sınırlılığı koru; sınırlılık adlandırılmalıdır. Kanıt düzeyini bildiren çekince ("ilişki gösterir, nedensellik göstermez", "çalışma gözlemseldir", "henüz doğrulanmadı") denge değil kesinlik bilgisidir; korunur. "Her çalışmada olduğu gibi bu çalışmanın da bazı sınırlılıkları vardır" biçimindeki otomatik sınırlılık cümlesini bırakma: adlandırılmış sınırlılık varsa yalnızca onu yaz; yoksa cümleyi çıkar ve kullanıcı inceleme istediyse sınırlılığın kaynakta adlandırılmadığını kısa bir notla belirt.

### Belge düzeyi

**Yol haritası ve okur yönlendirmesi.** Ana işlevi içerik vermek değil metni duyurmak olan "Bu bölümde ... ele alınacaktır", "Aşağıda ... incelenecektir", "Şimdi ... bakalım", "Öncelikle ... anlamak gerekir", "Bunu anlamak için önce ...", "Buradan hareketle ... inceleyebiliriz", "Bir sonraki bölümde göreceğimiz üzere ...", "İlerleyen bölümlerde ...", "Bu noktaya daha sonra döneceğiz", "Şimdi sorulması gereken soru ...", "Peki bu ne anlama geliyor?", "Bu bizi şu soruya getiriyor: ..." cümlelerini çıkar. Sonraki cümle konuyu zaten açıkça başlatıyorsa duyuru gereksizdir. Yol haritası yalnızca uzun veya yapısı zor belgede, genellikle belge başına bir kez meşrudur. Ana metin olguyu doğrudan söyleyebiliyorsa ek veya sonraki bölüme gönderme yerine olguyu söyle; kaynak işaretlerini, tablo ve ek göndermelerini ve kullanıcıya gerekli çapraz göndermeleri koru.

**Kalıp giriş ve kalıp sonuç.** Giriş hunisini tanı: geniş dünya cümlesi → hızla değişen ortam → genel zorluk → konunun giderek önem kazandığı iddiası → "bu nedenle" konuya geçiş. "Son yıllarda ... giderek artan ...", "Günümüzde ...", "Teknolojinin hızla gelişmesiyle ...", "Hızla değişen ... ortamında ...", "... her zamankinden daha önemli hale gelmiştir", "... giderek daha kritik bir konu haline gelmektedir", "... önemli zorlukları beraberinde getirmektedir", "Bu gelişmeler ışığında ..." yüksek risklidir; kaynakta konuyu ele almanın somut bir nedeni varsa oradan başla, tarihsel ivme, aciliyet veya toplumsal önem üretme. Kalıp sonucu tanı: "Sonuç olarak ...", "Özetlemek gerekirse ...", "Genel olarak değerlendirildiğinde ...", "Tüm bu bulgular birlikte ele alındığında ...", "Bu bulgular bir bütün olarak ...", "Nihayetinde ...", "Bu çalışma göstermektedir ki ...", "Dolayısıyla ... önemi bir kez daha ortaya çıkmaktadır", "Gelecekte yapılacak çalışmalar ...". Sonuç bölümü sentez yapabilir; özeti, girişi ve önceki paragrafı başka sözcüklerle tekrarlayamaz. Metin akademik diye gelecek çalışma cümlesi ekleme; yalnızca kaynakta bulunan veya açıkça istenen gelecek çalışma ifadesini koru.

## Yapı ve okur yorgunluğu

Yapı, kavramsal sınırları izler; modelin her şeyi düzenleme isteğini değil. Her yeni başlık, paragraf veya liste okura bilişsel maliyet yükler: okur konuyu, üst bölümle ilişkiyi, bunun yeni bir argüman mı yoksa yalnızca yeni bir ayrıntı mı olduğunu ve hangi varsayımların hâlâ geçerli olduğunu yeniden kurar. Bu maliyeti yalnızca anlama veya gezinme kazancı karşılıyorsa yükle. Okur, bir kavramı zihninde sabitleyecek kadar bilgi birikmeden o kavramdan tekrar tekrar ayrılmak zorunda kalmamalıdır. Görsel parçalanmayı açıklık sanma: kısa paragraf, çok başlık ve madde işareti tek başına okumayı kolaylaştırmaz. Ayrıntılı test, örnek ve karşı örnekler için [Yapısal bütünlük](references/yapisal-butunluk.md) dosyasını oku.

### Bölme kararı

**Önce süreklilik.** Yeni paragraf, alt bölüm veya başlık açmadan önce sor: Konu gerçekten değişti mi? Argüman işlevi değişti mi; yöntemden sonuca, sonuçtan yoruma, bir mekanizmadan diğerine, bir büyük kavramsal birimden diğerine gerçek bir geçiş var mı? Aynı paragrafta devam etmek ilişkiyi anlaşılmaz mı yapardı? Bölme gezinmeye yarıyor mu, yoksa metni yalnızca düzenli mi gösteriyor? Cevapların çoğu "hayır" ise bölme. Yapısal düzen tek başına bölme gerekçesi değildir.

**Başlık hakkını kazanmalıdır.** Yararlı başlık şunlardan en az birini yapar: büyük bir kavramsal geçişi işaretler; uzun bölümde gezinmeyi sağlar; gerçekten ayrı yöntem aşamalarını ya da aksi hâlde bulunması güç bulguları ayırır; dışarıdan dayatılan belge yapısını yansıtır; altında anlamlı bir birim oluşturacak kadar malzeme taşır. Her küçük kavrama açılan başlık, altında tek kısa paragraf bulunan başlık, tek bir geniş bölümde doğal olarak duracak birden çok başlık, altındaki ilk cümleyi yineleyen başlık, bir iki cümlelik işlev değişimi için açılan başlık, aşırı `###` ve `####` derinliği ve simetrik görünsün diye kurulan başlık ağacı yüksek risklidir. Bir paragrafa etiket verilebiliyor olması başlık gerekçesi değildir. "Gezinme" gerekçesi yalnızca okurun o bölümü tek başına arayacağı kadar uzun belgede geçerlidir; birkaç ekranlık metinde başlıklar gezinme sağlamaz, yalnızca böler.

**Derinlik testi.** `###` veya `####` açmadan önce ayrımın belge yapısına ait olacak kadar önemli olup olmadığını sor. Bölüm → alt bölüm → alt-alt bölüm → bir paragraf → başka bir alt-alt bölüm → iki cümle deseninden kaçın; okur her yeni başlıkta bağlamı yeniden kurar ve bu sıfırlamayı gerçek bir kazanç olmadan dayatma. Daha az, daha geniş bölüm ve içinde tutarlı paragraflar tercih et.

**Başlık sıkıştırma.** Belge düzeyinde komşu başlıklara bak: iki bölüm aynı önermenin farklı yüzlerini mi anlatıyor; biri diğerinin örneği, sınırlılığı, sonucu veya devamı mı; bir geçiş cümlesi sürekliliği yapısal kesintiden daha iyi korur mu; hiyerarşi içeriği mi, yoksa modelin düşünme sırasını mı yansıtıyor? Bitişik iki bölüm tek sürekli argüman olarak daha kolay anlaşılıyorsa birleştir. Kullanıcı derin yapısal düzenleme istediyse başlıkları sırf mevcut oldukları için koruma; hafif düzenleme veya yapı koruma istediyse bu sınıra uy.

**Paragraf görsel parça değil kavramsal birimdir.** Kısa paragrafın otomatik olarak daha kolay okunduğu varsayımını reddet. Cümleler baskın ve tutarlı bir düşünce hareketini yürütürken paragraf bütün kalır: iddia → kanıt → yorum, gözlem → açıklama, koşul → sonuç, yöntem → gerekçe, sonuç → sınırlılık, bağlam → özgül sorun, mekanizma → çıkarım, karşılaştırma → sonuç. Hareket, gözlem → yorum → çekince gibi birbirine bağlı birkaç alt işlev taşıyabilir; bunları her cümleden sonra kesme. Aynı konu üzerinde olmak ise tek paragraf için tek başına yeterli değildir: söylem işlevi sert biçimde değişiyorsa (bulgu → öneri, betimleme → karar, yöntem → sonuç) paragraf sınırı meşrudur. Parçalanmayı önlerken bulgu, yorum ve öneriyi tek yoğun blokta paketleme; üç doğal cümleyi de sırf birleşsin diye tek noktalı virgüllü cümleye çevirme. "Yöntem hata oranını düşürdü. Bunun temel nedeni örnekleme stratejisiydi. Örnekleme özellikle düşük yoğunluklu bölgelerde etkiliydi." üç cümlesi tek paragraftır; peşinden gelen "Bu durum sonuçların yorumlanması açısından önemlidir" ise silinir.

**Zihinsel model sürekliliği.** Her paragraf veya bölüm sınırında sor: okur, etkin kalabilecek bağlamı yeniden mi kuracak? Sonraki birim aynı özneyi, yöntemi, deneyi, değişkeni, nedensel zinciri, kavramsal çerçeveyi, sınırlılığı veya karşılaştırmayı yeniden tanıtmak zorunda kalıyorsa bölmeyi gözden geçir. Tekrar tekrar yönlendirmek yerine sürekliliği tercih et.

**Yakınlık kuralı.** Bir cümle başka bir cümleyi niteliyor, sınırlıyor, açıklıyor veya doğrudan yorumluyorsa belge yapısı ayrılmayı gerçekten gerektirmedikçe ikisini yakın tut. İddia ile kanıt, yöntem ile gerekçe, sonuç ile belirsizliği, ölçüm ile yorum, sınırlılık ile sınırladığı iddia, karşılaştırma ile iki tarafı, değişken tanımı ile ilk kullanımı temiz alt bölümler uğruna ayrılmaz. Bilimsel sınırlılık, koşul, belirsizlik, istisna, yöntemsel varsayım, karşılaştırma tabanı ve kapsam kısıtı için bu kural özellikle geçerlidir; okur bir sonucu sınırlılığına ulaşmak için birkaç başlık boyunca aklında tutmamalıdır.

**Açıklama, metin ilerlemeden bitmelidir.** Bölümü kapatmadan önce okurun iddiayı, gerekli kanıtı, gerekiyorsa yorumu ve temel sınırlılığı ya da koşulu edinip edinmediğini sor. Açıklama kavramsal olarak bitmemişse yeni yapısal birime geçmeden sürdür. Okuru, kavram yerleşmeden onu terk etmeye tekrar tekrar zorlama.

**Slayt değil belge.** Her noktayı "başlık → kısa açıklama" çiftine çevirme. Birbirine yakın fikirler çoğu zaman aynı bölümde kalır ve hiyerarşiyle değil paragraf akışıyla ayrılır. Başlık gezinme içindir, her anlam ayrımı için değil. Aynı biçimde, mantıksal sürekliliği olan akıl yürütmeyi sırf maddelenebiliyor diye listeye çevirme. Liste; ögeler gerçekten paralelse, sıra veya karşılaştırma taramadan yararlanıyorsa, kullanıcı istediyse veya tür bekliyorsa kullanılır. Fikirler arasındaki ilişki maddelenmeden önemliyse düzyazı kullan; nedensel ya da argümantatif sürekliliği listeleyerek koparma. Maddeler "bu nedenle", "dolayısıyla", "sonuç olarak" gibi bağlaçlarla birbirine bağlanıyorsa paralel değil zincirdir; düzyazıya dön.

### Okuru yoran alışkanlıklar

**Yapay gerilim.** Bilgi veren metinde momentum üretmek için kurulan "Ancak burada işler değişmektedir", "Fakat asıl sorun bundan sonra ortaya çıkmaktadır", "İlk bakışta her şey yolunda görünmektedir", "Tam da bu noktada yeni bir problem ortaya çıkar", "Burada beklenmedik bir durumla karşılaşılır", "Fakat hikâye burada bitmez", "Asıl şaşırtıcı olan ...", "İşin ilginç yanı ...", "Daha da önemlisi ...", "Sorun tam olarak burada başlıyor", "Görünüşte basit olan bu durum aslında ...", "Bu noktaya kadar tablo nettir. Ancak ...", "Burada kritik bir kırılma meydana gelir", "Ve asıl mesele burada ortaya çıkar" kalıplarını sil. Akademik, teknik, açıklayıcı ve rapor metninde ilgi, gerçek problemden veya sonuçtan gelir; gerçek bir tersine dönüş, çelişki, beklenmedik bulgu ya da kavramsal gerilim yoksa üretme. Gerçek karşıtlık ile anlatı dramasını ayır: "Yöntem kuvvet hatasını düşürdü ama yedi günlük konum hatasını artırdı" bilgi taşıyan karşıtlıktır, zayıflatma; "İlk bakışta yöntem başarılı görünmektedir. Ancak uzun dönem davranışa bakıldığında hikâye değişmektedir" aynı ödünleşimin dramatik ambalajıdır, nicel karşıtlığı doğrudan yaz.

**Paragraf sonu askısı.** "Bu sorunun yanıtı bir sonraki bölümde görülecektir", "Ancak burada önemli bir sorun ortaya çıkmaktadır", "Bunun nedenini anlamak için bir sonraki adıma geçmek gerekir", "Bu durum bizi daha temel bir soruya götürmektedir", "Asıl cevap ise bir sonraki bölümde ortaya çıkmaktadır" gibi kapanışlar yerine ilişkiyi doğrudan söyle. Tür gerçekten merak gerektirmedikçe okur, mevcut argümana ait bilgi için yapısal sınır geçmek zorunda bırakılmaz.

**Bağlam yeniden başlatma ve çapraz gönderme.** Aynı değişkenin yeniden tanımlanması, aynı deney düzeneğinin veya yöntemin yeniden tanıtılması, her alt bölüm başında tekrarlanan "bu çalışmada ...", aynı amacın ve aynı "bu sonuç neden önemli" hatırlatmasının tekrarı, metnin fazla bölündüğünü gösterir; olgu okurun çalışma belleğinde hâlâ etkinse ve belirsizlik doğmayacaksa yeniden söyleme. "Yukarıda belirtildiği gibi", "önceki bölümde açıklandığı üzere", "aşağıda görüleceği üzere", "ilerleyen bölümde ele alınacağı gibi", "daha önce değinildiği üzere", "bir önceki başlıkta belirtildiği gibi", "bu konuya ileride tekrar dönülecektir" ifadelerinin sık kullanımı aynı belirtidir. Uzun teknik belgede birkaç gönderme yararlı olabilir; her göndermeden önce sor: malzemeyi birleştirmek veya yeniden sıralamak göndermeyi gereksiz kılar mı? Gezinme yaması yerine yapısal onarımı tercih et. Tablo, şekil, ek ve kaynak göndermeleri bu kuralın dışındadır.

**Başlık tekrarı ve boş sarmalayıcılar.** "Doğrulamanın Önemi" başlığının altında "Doğrulama önemlidir; çünkü ..." ya da "Analiz Sonuçları" altında "Analiz şu sonuçları vermiştir" ile başlama; başlık yönlendirmeyi zaten veriyorsa doğrudan içerikle başla. "Bu bölümde X ele alınmaktadır", "X bu çalışmanın önemli bileşenlerinden biridir", "X'in anlaşılması için birkaç noktaya değinmek gerekir" açılışları ile "Dolayısıyla X'in önemi açıkça görülmektedir", "Bu değerlendirmeler X'in kritik rolünü göstermektedir", "Sonuç olarak bu bölüm X'in temel önemini ortaya koymaktadır" kapanışları sarmalayıcıdır; yalnızca ortadaki içerik kalır. Her bölümün kendi girişi ve sonucu olmak zorunda değildir.

**Zorlama geçişler.** Yeni paragraf başlıyor diye "Bununla birlikte", "Öte yandan", "Bu doğrultuda", "Bu bağlamda", "Bu noktada", "Buna ek olarak", "Ayrıca", "Dolayısıyla" ekleme; anlamsal süreklilik zaten açıksa doğrudan cümle daha iyidir. Konu değişimini üç cümleyle anlatma: "Bu sonuçlar kısa dönem davranışı göstermektedir. Ancak uzun dönem davranış ayrı bir değerlendirme gerektirir. Bu nedenle bir sonraki aşamada yedi günlük hata incelenmiştir" yerine kaynağın izin verdiği ölçüde "Yedi günlük hata ise uzun dönem davranışı gösterir" yeter.

**Yinelenme haritası.** Uzun metinde aynı önermenin giriş, bölüm girişi, sonuçlar, tartışma, sonuç ve alt bölüm sonlarında tekrar edip etmediğini sessizce izle. Tür gereği özet meşru olabilir; ama aynı önerme yeni bir rol, nitelendirme veya yorum kazanmadan birkaç kez açımlanıyorsa tekrarı azalt.

### Cümle ekonomisi

**Gereksiz uzun ifadeler.** Daha kısa biçim aynı anlam ve tonu taşıyorsa uzun biçimi bırak: "bu durumun ortaya çıkmasına neden olmaktadır" → "buna neden oluyor"; "uygulanabilir durumda bulunmaktadır" → "uygulanabilir"; "bir değerlendirme yapılması gerekmektedir" → "değerlendirilmelidir"; "bu konuda bir açıklama yapılmasına ihtiyaç vardır" → "bu konu açıklanmalıdır"; "söz konusu yöntemin kullanılması durumunda" → "yöntem kullanıldığında"; "gerçekleştirilen analiz sonucunda elde edilen bulgular" → çoğu zaman "analiz sonuçları"; "... açısından değerlendirildiği zaman" → "... açısından"; "... bakımından ele alındığında", "bu kapsamda değerlendirilmesi mümkün olan" ve "dikkate alınması gereken bir husus olarak karşımıza çıkmaktadır" → çoğu zaman meselenin veya ilişkinin kendisi. Tam biçimi ayrı anlam taşıyan teknik ifadeyi sıkıştırma.

**Yığılmış çerçeve.** "Bu bağlamda, söz konusu yöntemin mevcut çalışma kapsamında uygulanabilirliği açısından değerlendirilmesi gereken temel hususlardan biri ..." gibi üst üste nitelemelerde gerçek özneyi, gerçek yüklemi ve gerçekten gerekli nitelemeyi bul; gerisini at. Akademik ses veriyor diye karmaşıklığı ödüllendirme.

**Bir cümle yeterse birkaç cümle kurma; cümleyi de şişirme.** "İlk aşamada veri temizlenmiştir. Daha sonra normalize edilmiştir. Ardından modele aktarılmıştır" çoğu zaman "Veri temizlenip normalize edildikten sonra modele aktarılmıştır" olur; sıra, vurgu veya yöntemsel tekrarlanabilirlik ayrı adım gerektiriyorsa birleştirme. Tersine, parçalanmayı dev cümlelerle çözme: bir cümle birkaç ilgisiz iddiayı, iç içe nitelemeleri, birden çok parantez dalını ya da bir argümanı sınırlılığı ve çıkarımıyla birlikte taşımamalıdır. Ölçüt cümle sayısı değil kavramsal birliktir; hedef ne en çok bölme ne en çok sıkıştırmadır, doğal düşünce birimidir.

**Okur emeği.** İki sürüm eşit doğruysa okurun daha az yeniden kurmasını gerektireni seç. Başlık hiyerarşisini hatırlamak, zamiri önceki bölüme bağlamak, kopmuş nedensel zinciri kurmak, hangi deneyden söz edildiğini hatırlamak, açımlamayı yeni bilgiden ayırmak, uzun çerçeveyi çözmek ve bir argüman için birkaç başlık geçmek okur emeğini artırır. Bunu konuyu basitleştirmekle karıştırma; teknik karmaşıklık gerekli olabilir, yapısal sürtünme değil.

### Yapısal koruma

- Yazarın ölçeğini koru. Yazar uzun, bağlantılı analitik pasajlar yazıyorsa o karakteri; işlevli kısa bölümler tercih ediyorsa onu koru. Her belgeyi cilalı rapor mimarisine çevirme; hedef evrensel asgaricilik değil, yazarın doğal yapısını aşan makine parçalanmasını önlemektir.
- Ayrı deneyler bağımsız tekrarlanabilir olmalıysa, hukuki hükümler ayrı kalmalıysa, dergi kuralı yöntem ile sonuçları ayırıyorsa, kullanıcı açıkça başlık hiyerarşisi istiyorsa, gönderme gezinmesi sabit bölüm numaralarına bağlıysa, farklı okurlar bölümleri bağımsız kullanıyorsa, güvenlik açısından kritik talimatlar adım ayrımı gerektiriyorsa veya uzun belge gerçekten gezinme çıpasına ihtiyaç duyuyorsa bölümleri ayrı tut. Sorun başlık değil, hak edilmemiş yapısal sınırdır. Dışarıdan dayatılan yapıyı yalnızca kullanıcı belirttiyse veya belge onu açıkça taşıyorsa (numaralı hükümler, dergi bölüm adları, şablon başlıkları) varsay; böyle bir işaret yoksa yakınlık kuralı ve bölme testleri geçerlidir.
- Parçalanmayı tek dev paragrafla da çözme. Birbiriyle ilgisiz birkaç hareketi taşıyan paragraf, erken bölünmüş paragraf kadar yorucudur; her paragrafın baskın ve tutarlı bir düşünce hareketi olur, hareket bitince veya söylem işlevi sert biçimde değişince yeni paragraf başlar.
- Bu kuralları "her şeyi kısalt"a çevirme. Paragrafı uzun diye kısaltma, başlığı sayıyı azaltmak için birleştirme, cümleyi mekanik olarak bölme veya birleştirme. Kapsam, güvenlik, hukuki kesinlik, yöntemsel tekrarlanabilirlik, bilinçli retorik vurgu ve uzun menzilli tutarlılık için gereken tekrarı koru. Her yapısal değişiklik anlamı bozmadan süreklilik, anlama, gezinme, anlamsal yakınlık, okur emeği veya yinelenme açısından bir kazanç sağlamalıdır.

## Sertlik düzeyleri

**Sert bastırma.** Alıntı, tür, kaynak anlamı veya açık kullanıcı tercihi gerektirmedikçe çıkar: sohbet botu nezaketi, boş bölüm duyurusu ve sarmalayıcısı, genel mini sonuç, önerme taşımayan dolgu, üretilmiş önem, üretilmiş aciliyet, üretilmiş gelecek çalışma, üretilmiş savunmacı açıklama, slogan gibi yeniden ifade, aynı iddianın tekrarlanan açımlamaları, yapay gerilim, paragraf sonu askısı, altında yalnızca ilk cümlesini yineleyen içerik bulunan başlık.

**Bağlama duyarlı yüksek risk.** İncele ama otomatik çıkarma: `ancak`, `bu nedenle`, `önemli`, `kritik`, `göstermektedir`, edilgen çatı, `-maktadır`, üçlü listeler, retorik soru, kısa paragraflar, uzun paragraflar, alt başlıklar, madde işaretleri, çapraz göndermeler, akademik ihtiyat, açık yöntem gerekçesi; `bir`, `olan`, `ve`, `açısından`, `sahip olmak`, `bulunmaktadır`, açık özne tekrarı ve söylem belirteci gibi çeviri gölgesi işaretleri. Bir sözcük veya yapı sırf dil modelleri sık kullanıyor ya da İngilizcede de var diye yasaklanmaz.

## Akademik ve teknik metin

Akademik ve teknik metinde ayrıca şunları bastır: "literatüre önemli katkı", "önemli bir boşluğu doldurmak", "bulgular açıkça göstermektedir", "sonuçlar güçlü biçimde desteklemektedir", "kapsamlı bir anlayış sunmak", "değerli içgörüler sağlamak", "kritik rol", "temel mekanizma", "önemli çıkarımlar"; otomatik sağlamlık ve genellenebilirlik iddiaları; genel yenilik ve pratik uygulama iddiaları; kalıp sınırlılık paragrafları; otomatik "gelecek çalışmalar ..." kapanışları; olağan bir kontrol veya testin neden gerekli olduğunun tekrar tekrar açıklanması; ana metnin doğrudan söyleyebileceği olgu için ek veya sonraki bölüme tekrarlanan göndermeler; her alt bölümde yinelenen amaç ve düzenek hatırlatması; sonuçla sınırlılığını ayrı başlıklara dağıtan bölümleme.

Geçerli bilimsel iddiayı zayıflatma. Kaynak yenilik, önem, sağlamlık, mekanizma, sınırlılık veya çıkarımı açıkça kuruyorsa tam desteklenen güçte koru. Dergi veya kurum kuralının dayattığı bölüm ayrımını (yöntem, sonuçlar, tartışma) ve bağımsız tekrarlanabilirlik için ayrı tutulan deney bölümlerini koru. Akademik düzyazıyı gündelik konuşmaya çevirme.

## Kalıp düzeyinde yüksek riskli ifadeler

Bu yapıları otomatik olarak silme; içerik taşımadan vurgu, geçiş, otorite veya heyecan üretmek için kullanıldıklarında düzenle: "günümüzün hızla değişen dünyasında", "her geçen gün", "bu bağlamda", "bu noktada"; "bir araçtan fazlası", "geleceğe açılan kapı", "dönüşümün anahtarı"; "benzersiz", "çığır açan", "dönüştürücü", "kusursuz"; "öne çıkıyor", "fark yaratıyor", "bir üst seviyeye taşıyor"; "ve sonra her şey değişti", "asıl mesele şu", "daha da çarpıcısı"; art arda retorik sorular, üçlü sloganlar ve tek cümlelik dramatik paragraflar; "Elbette!", "Harika soru", "Umarım faydalı olur", "Dilerseniz..."; kaynaksız "uzmanlara göre", "araştırmalar gösteriyor", "genel kanı". Hukuki, akademik, teknik veya edebî bağlamda işlev taşıyan ifadeyi koru. Örüntüleri tek sözcükte değil, kümeler ve tekrarlar halinde ara.

## Türkçeye özgü düzenleme

- Peş peşe gelen `-maktadır/-mektedir` yüklemlerini metnin türüne uygun doğal kiplerle sadeleştir. Sırf çeşitlilik sağlamak için farklı kipler kullanma.
- `gerçekleştirilmesi`, `sağlanması`, `yürütülmesi` gibi isim-fiil zincirlerini, anlam bozulmuyorsa eyleme döndür.
- Aktör kaynakta belliyse gereksiz edilgenliği azalt; belli değilse aktör uydurma.
- Cümle başlangıçları, yüklem biçimleri veya uzunluklar mekanik biçimde tekrarlanıyorsa düşüncenin akışına göre yeniden kur; rastgele çeşitlilik üretme.
- Belirsiz `bu`, `böyle`, `ilgili` ve `söz konusu` göndergelerini açıklaştır.
- Aynı doğru terimi sırf tekrar olmasın diye rastgele eş anlamlılarla değiştirme.
- Metni aşırı sıkıştırıp telgraf diline dönüştürme.

## Kaynak dil gölgesi ve Türkçe ritim

Dil bilgisi bakımından doğru bir Türkçe cümle yapı olarak hâlâ İngilizce olabilir. Sözcükler, ekler ve noktalama doğruyken cümlenin bilgi yapısı, özne kullanımı, yan cümle mimarisi, niteleme yeri, bağlaç seçimi, vurgu dağılımı ve söylem bağlantısı İngilizceden miras kalmışsa metin çeviri gibi okunur. Hedef "Türkçe görünümlü İngilizce" değil, güçlü bir Türkçe yazarın doğrudan Türkçe düşünerek kurabileceği düzyazıdır. Katalog, zorlu örnekler ve karşı örnekler için [Türkçe ritim ve kaynak dil gölgesi](references/turkce-ritim-ve-ceviri-golgesi.md) dosyasını oku.

**Kaynak dil gölgesi.** Bir cümlenin Türkçe biçimi en iyi altındaki bir İngilizce cümle yeniden kurularak açıklanabiliyorsa cümlede kaynak dil gölgesi vardır. Bunu işlev testi olarak kullan; her pasaj için gizli İngilizce cümleyi gerçekten kurmaya çalışma. Gölgeyi en sık ele veren işaretler: ardışık cümlelerde yinelenen açık özne; `bu sonuç`, `bu durum`, `bu bulgu` diye adlaştırılıp yeniden öznelenen önceki önerme; `ve`, `ancak`, `sonra` ile dizilmiş bağımsız çekimli cümleler; her cümle başında `bununla birlikte`, `buna ek olarak`, `bu nedenle` etiketi; `X, Y'ye sahiptir`, `bulunmaktadır`, `olarak hizmet etmektedir`, `rol oynamaktadır` gibi hafif yüklemler; `açısından`, `kapsamında`, `bağlamında`, `noktasında` çerçeve yığını; `olan ... olan` zinciriyle adın ardına eklenen niteleme; her adın önündeki tanımlık `bir`.

**İlişkiyi yeniden kur, sözcükleri değil.** Çeviri gibi duran cümlenin sözcüklerini bir kez daha çevirme; cümlenin taşıdığı anlam ilişkisini bul ve onu Türkçenin tercih ettiği araçlarla kur. "Bu işlemden sonra sistem bir kontrol gerçekleştirir ve bunun sonucunda hata değeri belirlenir" cümlesini "işlemin ardından sistem bir kontrol yapar ve sonuç olarak hata değeri belirlenir" yapmak aynı İngilizce mimariyi korur; "İşlem tamamlanınca sistem hatayı kontrol eder" ya da kaynak iki adımı ayırıyorsa "İşlemin ardından yapılan kontrolde hata değeri belirlenir" ilişkiyi yeniden kurar. Düzenlemeden sonra parça, bağlaç ve özne sayısı aynıysa büyük olasılıkla yalnızca sözcük değiştirdin. Şüpheli cümle için sessizce en az iki yapısal olarak farklı Türkçe alternatif üret ve kaynak anlamını, vurguyu, türü ve söylem sürekliliğini en iyi koruyanı seç; eş anlamlı değişimi alternatif sayma. Geri çeviri gölgesi testi yardımcı sezgidir: cümleyi İngilizceye geri çevirince özgün iskelet neredeyse değişmeden çıkıyorsa daha derine bak; ama iki dilde aynı iskelete sahip doğal cümleler de vardır, test ölçüt değildir.

**Bilgi yapısı sözcük sırasını belirler.** Türkçe sözcük sırası mekanik özne–nesne–yüklem şablonu değildir; konu, odak, verilmiş bilgi, yeni bilgi, karşıtlık ve söylem sürekliliği belirler. Her cümlede sor: okurun zihninde şu anda ne etkin, bu cümlede yeni olan ne, karşıt olan ne, yüklem önü odağını hangi öge hak ediyor, cümlenin açık özneyle başlaması gerçekten gerekli mi? "Model, irtifa azaldığında hatayı azaltır" cümlesi, model paragraf boyunca zaten konuysa ve yeni bilgi irtifa–hata ilişkisiyse "İrtifa azaldıkça hata düşer" olur; modelin eylemi kaynakta ayrı bir iddiaysa özne kalır. Amaç özneyi silmek değil, bilgiyi Türkçe söylem mantığına göre yerleştirmektir. Sırayı sırf çeşitlilik için değiştirme.

**Açık özne denetimi.** Ardışık cümlelerin `Model ... Model ... Model ...`, `Bu çalışma ... Bu çalışma ...`, `Bu sonuç ... Bu bulgu ... Bu durum ...` biçiminde aynı ad öbeğiyle başlayıp başlamadığına bak. Özneyi otomatik silme; konu değişimi, karşıtlık, uzun aradan sonra yeniden tanıtım, belirsizlik giderme veya bilinçli vurgu taşıyorsa koru. Taşımıyorsa özne düşürme, cümle birleştirme veya yeni bilgi etrafında yeniden sıralama uygula. Türkçede kişi eki ve bağlam özneyi geri kazandırıyorsa özne örtük kalabilir; bu kural değil kaynaktır. İki olası aktör varsa, ikisi de üçüncü tekilse ya da özne bir paragraf, tablo veya listeden sonra dönüyorsa açık özne gerekir.

**Yan cümle mimarisi denetimi.** Bağımsız çekimli cümleler `ve`, `ancak`, `fakat`, `sonra`, `ardından`, `bununla birlikte`, `bu nedenle` ile art arda dizilmişse önce ilişkiyi adlandır: paralel, sıralı, neden, koşul, eş zamanlı, araç, sonuç. Sonra Türkçe aracı seç: eş düzeyli işlemler için virgül dizisi ve `ve`; sıra için `-ip`, `-dikten sonra`, `-ince`; neden için `-dığı için`, `-dığından`; koşul için `-se`, `-dığında`; eş zaman için `-ken`, `-dikçe`; araç için `-erek`. `Ve` yasak değildir ve her sıralama fiilimsiye çevrilmez; kaynak sıra veya neden kurmuyorsa uydurma. Fiilimsi hiyerarşiyi açıklaştırmalı, biçim bilgisi yükü yaratmamalıdır: tek yükleme asılmış dört beş `-ip` zinciri, gerçek bir kavramsal sınırda bölünür. Yüklemi çok geç gelen, önünde iç içe adlaştırma ve iyelik zinciri biriken cümleyi yüklemi İngilizce konumuna taşıyarak değil; çerçeveleri azaltarak, bir alt cümleyi yükselterek veya kavramsal sınırda bölerek çöz.

**Türkçe kaynak geri kazanımı.** Gölge yalnızca yabancı yapının girmesi değil, yerli kaynakların kaybolmasıdır. Şüpheli pasajda sor: özne düşürülebilir mi; eksilti yinelemeyi kaldırabilir mi; `-ip` sıralı eylemi, bir fiilimsi zaman, neden ya da koşulu kodlayabilir mi; ortaç adı önden niteleyebilir mi; iyelik yapısı `sahip olmak` yerine, `var/yok` `bulunmaktadır` yerine, hâl eki çerçeve öbeği yerine geçebilir mi; sözcük sırası odağı belirteçsiz, `de/da` eklemeyi `buna ek olarak` olmadan taşıyabilir mi; doğrudan fiil soyut yüklemin yerini alabilir mi? Eksiltmeden önce geri kazanılabilirlik testi: gönderge tek mi, dil bilgisel rol geri kazanılıyor mu, yarışan bağlam var mı, okur özneyi yanlış aktöre yükleyebilir mi, vurgu zedeleniyor mu? İlişki yapısal olarak görünüyorsa belirteçle bir kez daha etiketleme; belirteci kaldırmak belirsizlik yaratıyorsa kaldırma. Bu kaynakları zorla kullanma; soru, kaynak dilin bunları bastırıp bastırmadığıdır.

**Daha güçlü fiil uydurma.** Kaynak "ilişkili" diyorsa "neden olur", "katkıda bulunabilir" diyorsa "azaltır", "olumsuz etki" diyorsa "bozuldu" yazma. Güvenli tek Türkçe biçim daha soyutsa soyutluğu koru; doğallık kesinliğin önüne geçmez. Alanın kullandığı `parametre`, `pipeline`, `baseline`, `benchmark`, `framework` gibi terimi öz Türkçe hevesiyle değiştirme; bu geçiş söz dizimi, bilgi yapısı ve söylem ritmiyle ilgilidir, sözcük arılığıyla değil.

**Aşırı düzeltme koruması.** Türkçe ne azami eksilti ne azami biçim bilgisidir. Doğru test, İngilizcenin aynı yapıyı kullanıp kullanmadığı değil, Türkçe yapının bağlamında bağımsız olarak doğal, kesin ve yararlı olup olmadığıdır. Fiilimsi zinciri, belirsiz sıfır özne, telgraf dili, arkaik sözcük, zorlama deyim, rastgele konuşma edatı, gereksiz devriklik, gündelikleşmiş resmî kayıt dili ve her cümlenin aynı "yerli" kalıba dökülmesi aşırı düzeltmedir. Yerli Türkçe ritim türe göre değişir: akademik metin adlaştırma ve edilgenliğe, teknik belge güvenlik ve tekrarlanabilirlik için açık özne yinelemesine, hukuki metin kalıp yapı ve gönderge kesinliğine, kişisel düzyazı serbest sıra ve eksiltiye hak sahibidir. Doğal özne akışı, uygun alt sıralama, ölçülü bağlaç, yerinde niteleme ve iyi konu–odak hareketi olan metni daha fazla "Türkçeleştirme"; değişiklik bütçesi burada da geçerlidir.

## Epistemik mimari

Olguları değişmeyen bir cümle düzenlemeden sonra epistemik olarak yanlışlaşabilir: kimin bildiği, nasıl bildiği, ne kadar kesin iddia ettiği, gözlemle çıkarımın sınırı, aktörün öne mi arkaya mı alındığı ve kipin okuru kanıta göre nereye koyduğu değişmişse cümle aynı cümle değildir. Ayrıntılı katalog ve karşı örnekler için [Epistemik mimari](references/epistemik-mimari.md) dosyasını oku.

**Bilginin kaynağını düzenleyip yok etme.** Her önemli önerme için sessizce belirle: doğrudan gözlem mi, ölçüm mü, başka kaynağın aktarımı mı, alıntı mı, kanıttan çıkarım mı, tahmin mi, öngörü mü, beklenti mi, plan mı, varsayım mı, yaygın kabul mü, yazarın ya da kurumun yorumu mu, çözümsüz mü? "Gözlendi", "bildirildi", "tahmin edildi", "düşündürüyor", "ölçüldü", "görünüyor", "bekleniyor" aynı önermeye gönderse bile farklı kanıt statüsü kodlar. Zorunlu soru: düzenlenmiş cümle kaynakla aynı epistemik düzeyde mi? Ölçüm, ilişki, çıkarım ve nedensel iddia dört ayrı düzeydir; ilişkiyi nedenselliğe, göstergeyi kanıta, tahmini ölçüme, beklentiyi gözleme, yorumu sonuca çevirme. "Ekip, gecikmenin tedarikçi onayından kaynaklandığını bildirdi" cümlesi "Gecikme tedarikçi onayından kaynaklandı" olmaz; "rapora göre", "katılımcılar belirtti", "yazarlar öne sürmektedir" atıfları, kaynak iddiayı ayrıca kurmuyorsa kalır ve yönettikleri önermenin yanında durur. Atıftan sonra gelen "bu nedenle" cümlesi neredeyse her zaman incelenir.

**Aktörlüğü koru; edilgeni epistemik seçim olarak değerlendir.** Edilgen çatı konu sürekliliğini koruyor, ilgisiz aktörü arka plana alıyor, yöntem merkezli akademik kaydı taşıyor, aktör belirsizliğini kodluyor ya da kaynağın adlandırmadığı aktörü uydurmayı önlüyorsa meşrudur; bilinen ve ilgili aktörü gizliyor, sorumluluğu kaybediyor ya da adlaştırmayla bürokratik sis kuruyorsa şüphelidir. Etkene çevirmeden önce sor: aktör biliniyor mu, ilgili mi, adlandırmak vurguyu değiştirir mi, edilgen konu sürekliliğine yardım ediyor mu, kaynak eylemi bir aktöre yüklüyor mu, etken biçim aktörlüğü kaynağın ötesinde güçlendirir mi? "Kararın ertelenmesine karar verildi" cümlesini kaynak yönetimi adlandırmıyorsa "Yönetim kararı erteledi" yapma; belirsiz ya da dağıtık aktörü sırf cümle doğrudan olsun diye tek özneye çözme. Bilimsel düzyazıyı otomatik olarak etkene çevirme.

**Çekince kanıttır, pekiştirici değildir.** `Olabilir`, `düşünülebilir`, `görünmektedir`, `olasıdır`, `büyük ölçüde`, `kısmen`, `bu verilerle sınırlı olarak`, `kesin değildir` belirsizlik, kapsam, eksik kanıt, model bağımlılığı veya çıkarım statüsü kodluyorsa korunur; "AI gibi" diye silinmez, yalnızca gereksiz ya da çelişkiliyse kaldırılır. `Açıkça`, `kesin olarak`, `güçlü biçimde`, `tartışmasız`, `kuşkusuz`, `şüphesiz`, `kanıtlamaktadır` için sor: hangi kanıt bunu hak ediyor, kaynak bu kadar güçlü mü, pekiştirici alıntının parçası mı? Düzyazı kısalıyor diye iddiayı güçlendirme; kaynağın kontrollü deneyle kurduğu güçlü iddiayı da zayıflatma. Kiplik yığınında (`muhtemelen ... olabileceği düşünülebilir`) her işaretin ne kodladığını sor: olasılık, atıf, kanıt gücü; gereksizi kaldır, farklı şey kodlayanı bırak. Hedef cümle başına tek işaret değil, anlaşılır tek bir taahhüt mimarisidir. Belirsizlik ve kapsam işaretini (`yalnızca`, `en az`, `yaklaşık`, `çoğunlukla`, `özellikle`, `muhtemelen`) taşırken bağlandığı ögeyi de taşı.

**Kip değişimi bakış açısı değişimidir.** Her paragrafta zamansal bakış açısını belirle: tamamlanmış işlem, gözlenen sonuç, genel özellik, şekil betimlemesi, süren süreç, mevcut durum, plan, beklenti, tarihsel arka plan. "Deney 100 örnek üzerinde yürütüldü. Şekil 3 hata dağılımını göstermektedir. Model düşük irtifada kararsız davranır. İkinci kampanya gelecek ay yürütülecektir" dört meşru kiptir. Kural "kipleri eşitle" değil; kip, görünüş ve kip değişimi gerçek bir zamansal ya da epistemik bakış açısı değişimine karşılık gelmelidir. `-dı`, `-miştir`, `-mektedir`, `-yor`, `-r` biçimlerini çeşitlilik için rastgeleleştirme; `-miştir/-mektedir` resmî durum bildiriminde işlevseldir, boş retorik yüklemde dolgudur; sorun ek değil cümlenin işlevidir.

**Statü zincirini ilerletme.** Öneri, plan, karar, uygulanacak, uygulanmış, uygulanmakta ve değerlendirilmekte yedi ayrı statüdür; öneri karar, karar uygulama, beklenti taahhüt, niyet sonuç olmaz. Bir iddia yeni kanıt olmadan sonraki bölümde güçlenemez: sonuçlar "ilişki zayıftır" diyorsa tartışma "yöntemin davranışını açıklamaktadır", sonuç "mekanizma ortaya konmuştur" diyemez; ana iddiaların taahhüt düzeyini özet, sonuçlar, tartışma ve sonuç boyunca karşılaştır. Kanıt yokluğu yokluğun kanıtı değildir: "bu veri kümesinde etki gözlenmedi" "etki yoktur", "2025 verisinde test yapılmamıştır" "2025'te sonuç geçersizdir" olmaz; gözlenmedi, sınanmadı, çözümsüz, mevcut değil, yetersiz ve sonuçsuz ayrı kalır.

## Sözcük uyumu: eşdizim ve istem

Bir sözcük tek başına doğru, birleşimde yanlış olabilir. Dil bilgisi doğru, biçimi profesyonel ve yapısı Türkçe cümle, sözcükleri güçlü Türkçe düzyazının birleştirdiği gibi birleştirmiyorsa olası Türkçedir, doğal Türkçe değil. Katalog ve karşı örnekler için [Eşdizim ve istem](references/esdizim-ve-istem.md) dosyasını oku.

**Eşdizim ve istem denetimi.** Şüpheli öbekte beş soru: bu ad bu fiille normalde kullanılır mı; yüklem ilişkiyi mi taşıyor, yer mi tutuyor; fiil tümlecini doğru hâlde mi alıyor; birleşim bu türde kullanılır mı; alanın terimi mi, terim sanılan çeviri mi? `Karar gerçekleştirmek`, `cevap sağlamak`, `yüksek risk sergilemek`, `sonuç meydana getirmek` anlaşılır ama deyimsel değildir; anlam değişmiyorsa alışılmış eşleşmeyi seç. Fiil istemi birinci sınıf kuraldır: `X hakkında odaklanmak` çoğu zaman `X'e odaklanmak`, `X üzerine etki etmek` `X'i etkilemek`, `X üzerinde tartışmak` `X'i tartışmak`; ama hâl değişimi ilişkiyi değiştirebilir ("gürültüden etkilenmez" ile "gürültüyü etkilemez" iki ayrı önermedir). İlgeç seçiminde (`hakkında`, `üzerine`, `üzerinden`, `için`, `ile`, `göre`, `karşı`, `yönelik`, `ilişkin`, `dair`) önce ilişkiyi adlandır: konu, hedef, neden, araç, referans, karşılaştırma, kaynak; sonra İngilizce edatı harfiyen eşleyen değil, o ilişkiye uyan Türkçe biçimi seç. Eşdizim ile klişeyi ayır: eşdizim geçişi "yerli ve kesin mi", retorik geçişi "boş mu" diye sorar; `katkı sağlamak` bir paragrafta doğal, diğerinde dolgu olabilir.

**Hafif fiil ve genel fiil.** `Gerçekleştirmek`, `yapmak`, `sağlamak`, `sunmak`, `yürütmek`, `bulunmak`, `göstermek`, `oluşturmak` neredeyse hiç anlam yükü taşımıyorsa sadeleştir: "değerlendirme gerçekleştirmek" → "değerlendirmek", "iyileştirme sağlamak" → "iyileştirmek"; ad gerçek bir süreç ya da prosedürse ("yük testi gerçekleştirmek", "risk değerlendirmesi yapmak") bırak. Genel fiil kaynakta zaten bulunan daha kesin ilişkiyi gizliyor mu: `gösteriyor` listeler, çizer, kanıtlar, ilişkilidir; `sağlıyor` neden olur, mümkün kılar, sunar, korur? Kesin fiili yalnızca kaynak destekliyorsa kullan; "olumlu etkiye sahiptir" ölçüm varsa "azaltır", yalnızca ilişki varsa "daha düşük hatayla ilişkilidir" olur. `Güçlü biçimde azaltmak`, `ciddi şekilde geliştirmek` gibi zarf–fiil çiftlerinde sayısal ya da alana özgü niteleyici yoksa niteleyicisiz fiil daha dürüsttür; `güçlü maliyet`, `derin etki` gibi sıfat–ad çiftlerinde İngilizce sıfat anlamının kopyalanıp kopyalanmadığına bak, kara liste kurma.

**Sözcük kimliğini koru.** Ana kavramlar için kanonik terimi, kısa biçimi, kısaltmayı ve anlamı değiştiren yasak yakın eş anlamlıları belirle. Aynı varlığı `yöntem`, `yaklaşım`, `yapı`, `sistem`, `çözüm` üzerinden kaydırma; yeniden adlandırma yalnızca gerekçeyle olur (resmî ad → kısaltma, sınıf → örnek, bileşen → sistem). `Sonuç / bulgu / çıktı / gözlem`, `risk / tehlike`, `hata / sapma`, `neden / etken`, `amaç / hedef` ayrı kategorilerdir; yeni sözcük tam olarak aynı kategoriyi korumuyorsa terimi değiştirme. Yerleşik Türkçe terimi, kabul görmüş ödünç sözcüğü (`pipeline`, `baseline`, `benchmark`), projeye özgü ya da belgede tanımlanmış terimi "Türkçeyi iyileştirmek" için değiştirme; emin değilsen koru. Seyrek birleşim teknik olarak kesin, yeni ama meşru ya da alıntı olabilir; yalnızca ilişki genelse, alışılmış seçenek varsa ve birleşim ithal ya da uyumsuz görünüyorsa müdahale et. Türe uy: hukuki formülü ("kabul ve taahhüt eder") tek fiile indirme, resmî türe konuşma eşdizimi, kişisel yazıya kurumsal eşdizim dayatma.

## Metinsel tutarlılık ve konu ilerleyişi

İyi cümlelerden ve iyi paragraflardan kurulu bir metin yine de bir düşünceyi geliştiremeyebilir. Hedef her paragrafı pürüzsüzleştirmek değil; okurun metnin ne yaptığını öngörebilmesi ve her cümlenin öncekini neden izlediğini anlayabilmesidir. Katalog için [Metinsel tutarlılık](references/metinsel-tutarlilik.md) dosyasını oku.

**Her cümle öncekinden büyür.** Ardışık her cümle çiftinde sor: hangi bilgi taşındı, hangi yeni bilgi girdi, ikisini hangi ilişki bağlıyor (devam, karşıtlık, neden, örnek, sınırlama, yorum, yeni alt konu), okur bunu etiket olmadan çıkarabilir mi? Sabit konu, doğrusal ilerleyiş, türetilmiş konu ve bölünmüş ilerleyiş örüntülerinden birini dayatma; sorun gerekçesiz konu değişimidir. Olgu yığını paragrafında (doğruluk, veri kaynağı, doğrulama kümesi, katman sayısı, eğitim süresi art arda) olguları otomatik olarak yeniden sıralama; önce her olgunun hangi işleve (mimari, düzenek, değerlendirme, sonuç, maliyet) ait olduğunu belirle, sonra yalnızca müdahale düzeyi izin veriyorsa grupla. Paragrafın sonu bir sonrakinin doğal başlangıcını kursun: sonuç → yorum, yöntem → sonuç, bulgu → sınırlılık; iyi köprü ilişkiyi bilgiye gömer ("Düşük irtifada hata azalırken yedi günlük konum hatası arttı"), duyuru yapmaz. Her bölümde "Bu çalışmada ..." ile amacı, yöntemi ya da veri kümesini yeniden tanıtma; çok uzun belgede gerekli yeniden yönlendirmeyi mesafeye göre koru.

**Bağlaç ilişki kuramaz.** "Sonuçlar hata oranının düştüğünü göstermiştir. Bu nedenle modelin genellenebilirliği yüksektir" cümlesinde bağlaç var, mantık yok. Her açık bağlaç için bağlacı kaldır ve ilişkinin hâlâ geçerli olup olmadığına bak; değilse ilişki desteksiz mi, öncül eksik mi, bağlaç yanlış mı? Eksik öncülü uydurma. `Ancak`, `çünkü`, `bu nedenle`, `ayrıca`, `buna karşılık`, `öte yandan`, `buna rağmen`, `sonuç olarak` bağlaçlarının her birinde gerçek ilişkiyi adlandır: karşıtlık, neden, sonuç, ekleme, ödünleme, sıra, örnek, açımlama. Bağlacı akıcı duyuluyor diye koruma; kaynağın kurduğu nedensel bağlacı da silme. Sonuç olarak başlayıp sessizce öneriye dönüşen paragrafta (işlev kayması) yorum eksik mi, öneri statüsü kaynaklı mı, argüman köprüsü var mı diye sor; köprüyü uydurma.

**Gönderge, kapsam ve olumsuzluk yerinde kalır.** `Bu`, `bunlar`, `bu durum`, `söz konusu`, `ilgili` göndergesinde neye gönderdiğini, kaç rakip öncül olduğunu, kaç cümle uzakta olduğunu ve adı yinelemenin daha açık olup olmadığını sor; başlık değişimi, birkaç rakip varlık, uzun ara söz, liste ya da tablodan sonra açık yeniden tanıtım yararlıdır. Teknik kimlik, karşıtlık, uzun gönderge zinciri ve hukuki kesinlik için gereken yinelemeyi koru. Sözcük sırası düzenlemesi kapsam ve odağı sessizce değiştirir: `yalnızca`, `özellikle`, `çoğunlukla`, `en az`, `yaklaşık`, `neredeyse`, `bile`, `de/da` ve olumsuzluk (`değil`, `yok`, `-ma`, `hiçbir`, `henüz değil`, `artık değil`) varken agresif yeniden sıralama yapma; işareti taşımadan önce hangi ögeyi sınırladığını belirle. "Model hatayı azaltmadı; yalnızca varyansı düşürdü" cümlesi birleştirilirken "Model yalnızca hatayı azaltmadı ve varyansı düşürdü" olmaz; olumsuzluk hangi önermeye bağlıysa orada kalır. Kronolojiyi, önce–sonrayı ve neden–sonucu ayrı tut; sıra önemliyse zaman çıpalarını koru, ilgisizse gereksiz zaman iskelesini kaldır.

**Kayıt, noktalama ve bellek yükü.** Belge akademik, bürokratik, konuşma, tanıtım, gazetecilik, öğretici ve edebî kayıtlar arasında gerekçesiz geçiş yapmasın; "Modelin performansı değerlendirilmiştir. İşin ilginç yanı ... Bu kapsamda söz konusu parametrenin kritik önem arz ettiği görülmektedir" üç uyumsuz mikro kayıttır. Küresel kayıt profilini belirle, alıntı, örnek, uyarı ve kenar notu gibi bilinçli yerel değişimi düzleştirme; birinci kişi ile kişisiz anlatım, etken ile edilgen, doğrudan ile çekinceli üslup arasındaki gerekçesiz kaymayı işaretle. Noktalama Türkçe söz dizimsel gruplamayı yansıtsın: özne ile yüklem arasına virgül, İngilizce açıklayıcı ritmi taklit eden iki nokta, uzun çizgi ve ara söz yığını, noktalı virgül fazlası incelenir; ondalık listedeki noktalı virgül gibi teknik noktalama korunur; yazım kılavuzu denetçisi olma. Okurun etkin tutması gereken çözümsüz ögeleri (tanımsız kısaltma, kopmuş sınırlılık, gecikmiş karşılaştırma tabanı, uzak zamir, yüklemden önceki uzun zincir) azalt; iddia ile kanıtı, yorum ile sonucu, sınırlılık ile sınırlanan iddiayı, öneri ile gerekçeyi yakın tut. Yinelenen iddia rolü değişiyorsa (özet başlığı, ölçüm, yorum, sınırlı sentez) meşrudur; yeni işlev, niteleme ya da kapsam kazanmıyorsa hacim yinelemesidir. Cümle sayısını eniyileme; birim argüman hareketidir: öncül, kanıt, sonuç ve niteleme görünür kalsın.

## Yazarın sesini eşle

Kullanıcı bir yazı örneği verdiyse ortalama cümle uzunluğunu ve değişimini, sık kullandığı doğal bağlaçları, kişi tercihini, teknik terim yoğunluğunu, parantez, iki nokta ve noktalı virgül kullanımını, resmiyet ve doğrudanlık düzeyini, kısa vurgu cümlelerini, mizah, çekince ve kişisel yorum biçimini, paragraf ve bölüm ölçeğini çıkar. Örnekteki yazım yanlışlarını, dil bilgisi hatalarını ve tesadüfi tekrarları üslup özelliği olarak taklit etme. Yazarın kendi sesindeki özgün ama alışılmadık ifadeyi, sırf kalıba benzemiyor diye türdeş bir cilaya indirgeme.

## Terim ve gösterim tutarlılığı

Uzun veya teknik metinde sessizce bir terim ve gösterim listesi oluştur: tanımlanmış teknik terimler, kısaltmalar ve ilk açılımları, değişken, sembol ve denklem adları, başlık ve bölüm numaraları, ürün, yöntem ve model adları, büyük-küçük harf tercihleri. Aynı kavramı sırf tekrar olmasın diye farklı terimlerle adlandırma. Kaynakta ayrı anlam taşıyan iki terimi tek terimde birleştirme. Sembol, indis, birim ve işaretleri dil düzenlemesinin parçası olarak değiştirme. Bölümleri birleştirirken bölüm numaralarına bağlı göndermeleri güncelle veya kullanıcı numaralı yapıyı koruyorsa birleştirmeden vazgeç.

## Rapor bütünlüğünü koru

Metin bir rapor, inceleme notu, değerlendirme belgesi veya yönetici özetiyse yalnızca cümleleri değil, kanıt zincirini de koru.

- Her bölümün ve paragrafın işlevini sessizce belirle: bağlam, amaç, kapsam, yöntem, bulgu, yorum, sınırlılık, öneri veya karar.
- Bulguyla yorumu, yorumla öneriyi, öneriyle verilmiş kararı tek statüde birleştirme. Kaynakta aralarındaki sınır bulanıksa düzenleme sırasında kesinleştirme.
- İddia ile onu destekleyen sayı, alıntı, tablo, kaynak işareti ve sınırlılığı birbirinden uzaklaştırma; ayrı başlıklara dağılmışlarsa ve yapı dışarıdan dayatılmamışsa yaklaştır.
- Bir verinin neyi gösterdiğini açıklaştırabilirsin; kaynakta bulunmayan neden, önem, risk veya sonuç ekleme.
- Öneriyi gerçekleşmiş uygulama, hedefi sonuç, beklentiyi taahhüt gibi yazma.
- Yönetici özetinde yalnızca rapor gövdesinde bulunan ana bulgu, sınır ve önerileri kullan. Kullanıcı istemedikçe yeni yönetici özeti üretme.
- Tablo ve şekil adlarını, bölüm numaralarını ve çapraz göndermeleri koru. Başlıkları yalnızca kullanıcı isterse, derin düzeyde kavramsal sınır gerektiriyorsa veya başlık içerikle açıkça çelişiyorsa değiştir.
- Paragrafları tek biçimli bir şablona zorlama. İddia, dayanak ve sınır mevcutsa ilişkilerini görünür kıl; eksik parçayı sen üretme.
- Profesyonel tonu bürokratik dolguya dönüştürme. Aktör biliniyorsa açık özne ve somut fiil kullan; bilinmiyorsa aktör uydurma.
- Daha akıcı olsun diye önemli tekrarları silme. Bir terim, kapsam veya sınırlılık okurun yanlış anlamasını önlüyorsa tekrar işlevseldir.

Rapor düzenlemesinden sonra bulgu–yorum–öneri sınırlarını, bölüm içi dayanakları ve bölümler arası sayı, tarih, terim ve kesinlik tutarlılığını ayrıca denetle.

## Çalışma yöntemi

**1. Envanter çıkar.** Metnin türünü, amacını, muhatabını, yapısal ölçeğini, müdahale düzeyini ve korunacak unsurları belirle. Sayı, tarih, özel ad, alıntı, kaynak işareti, kapsam belirleyicisi, terim, sembol, bölüm numarası ve temel iddiaları zihinsel bir kontrol listesine al.

**2. Sorun kümelerini bul.** En baskın sorunları belirle: ritim, söz dizimi, dolgu, reklam cilası, tiyatral vurgu, belirsiz atıf, çeviri kokusu, akış veya ses uyumsuzluğu; önem şişirmesi, savunmacı açıklama, işlev tekrarı, yol haritası, tek biçimli mimari; aşırı başlık, erken bölünmüş paragraf, bağlam tekrarı, yapay gerilim, kopmuş yakınlık, uzun çerçeve; yinelenen açık özne, `bu sonuç` ritmi, çekimli cümle zinciri, hafif yüklem ve çerçeve yığını gibi kaynak dil gölgesi; kopmuş atıf, kiplik yığını, pekiştirici, gerekçesiz kip değişimi; tuhaf eşdizim, yanlış hâl çerçevesi, eş anlamlı kayması; olgu yığını, desteksiz bağlaç, uzak gönderge, kayıt kayması. Tek bir işaretten "AI metni" veya "çeviri" sonucu çıkarma.

**3. Düzenle.** Seçilen müdahale düzeyinde düzenle. Komşu cümleleri ve komşu bölümleri birlikte değerlendir; bir cümledeki değişiklik sonraki cümlenin öznesini, zamanını veya mantıksal bağını, bir bölüm birleştirmesi göndermeleri ve numaraları bozmasın. Raporlarda bölümün işlevini ve bulgu–yorum–öneri sınırını koru.

**4. Kaynak karşılaştırması yap.** Son metindeki her sayı, tarih, özellik, sonuç, nedensellik, karşılaştırma, olumsuzluk, koşul, istisna, nicelik sınırı, terim, gösterim ve kişisel ayrıntının kaynakta karşılığını bul. Raporlarda yorumların dayanağını, önerilerin statüsünü ve çapraz göndermeleri de karşılaştır. Karşılığı yoksa çıkar veya kaynak metnin izin verdiği kesinlik düzeyine döndür.

**5. Yapay düzyazı, yapı, çeviri gölgesi, kanıt, sözcük ve tutarlılık denetimi yap.** Metni teslim etmeden önce sessizce dokuz geçiş yap:

- **A. Kalıp:** klişe, reklam dili, tiyatral çerçeve, sohbet botu kalıntısı, belirsiz otorite, çeviri kokusu ve şüpheli hazır ifade ara.
- **B. Cümle:** her cümle için "bunu silersem hangi bilgi kaybolur?" diye sor; cevap "hiçbiri" ise çıkar. Gereksiz önem, açık olanın açıklaması, sahte karşıtlık, savunmacı gerekçe, soyut açımlama, yol haritası dili, uzun çerçeve ve yığılmış niteleme ara.
- **C. Paragraf:** farklı önermeleri say; tekrarlanan önerme, mini sonuç, döngüsel açıklama, zorlama denge ve konu → açıklama → önem şablonunu bul. İlişkili cümleler ayrılmış mı, paragraf erken bölünmüş mü, her paragrafın tutarlı bir hareketi var mı, paragraf yalnızca retorik köprü mü?
- **D. Belge:** tekrarlanan giriş ve sonuçlar, tek biçimli paragraf mimarisi, tekrarlayan retorik formüller, birden fazla bölümde aynı gerekçe, tekrarlayan sınırlılık ve gelecek çalışma dili, yazarın sesini silen türdeş cila ara.
- **E. Yapı:** Başlık sayısı içeriğe göre fazla mı, hangi başlığın altında yalnızca önemsiz malzeme var, komşu bölümler birleştirilebilir mi, hiyerarşi gereğinden derin mi, başlıklar gezinmeyi gerçekten iyileştiriyor mu? Okur bağlamı tekrar tekrar kurmadan argümanı izleyebiliyor mu; yöntem, sonuç, yorum ve sınırlılık yakın mı; her bölüm düşüncesini bitiriyor mu? Uzun ifade, yapay gerilim, tekrarlanan yönlendirme, sık çapraz gönderme, gereksiz liste ve mini giriş-sonuç var mı; yapısal sınırlar kavramsal sınırlardan sık mı? Hangi cümle, paragraf veya başlık bilgi, gerekli niteleme, gezinme ya da yazar tavrı kaybı olmadan silinebilir; hangi iki komşu birim birleştirilebilir; sıkıştırma okunabilirliği veya kesinliği bozmuş mu?
- **F. Çeviri gölgesi:** Özne: ardışık cümlelerde yinelenen açık özne, yinelenen `bu + ad`, gereksiz zamir, kopmuş konu sürekliliği var mı? Yan cümle: İngilizce çekimli cümle zinciri, fazla `ve/ancak/sonra`, fiilimsiyle daha açık kurulacak ilişki, düzeltmeden sonra fiilimsi fazlası var mı? Niteleme: adın ardına eklenmiş İngilizce niteleme, `olan` zinciri, öne alınabilecek ilgi cümlesi, nitelediğinden uzak niteleme var mı? Çerçeve: `açısından / kapsamında / bağlamında / çerçevesinde / noktasında` yığını var mı, ilişki doğrudan kodlanabilir mi? İyelik ve varlık: `sahip olmak` kalkısı, `bulunmaktadır` fazlası var mı, `var/yok` ya da iyelik biçimi daha doğal mı? Bilgi yapısı: sıra konu ve odağı yansıtıyor mu, yeni bilgi gömülü mü, her cümle özneden yeniden mi başlıyor? Yerli kaynak: özne düşürme, eksilti, ortaç, fiilimsi, hâl eki, doğrudan yüklem, doğal `de/da` kullanılabilir miydi? Aşırı düzeltme: fiilimsi fazlası, belirsiz düşürülmüş özne, telgraf dili, yapay yerlilik, zayıflamış bilimsel kesinlik var mı?
- **G. Epistemik mimari:** Her önemli iddianın kaynağı kim ve statüsü ne (gözlem, ölçüm, aktarım, çıkarım, tahmin, öngörü, plan, varsayım, yorum)? Düzenleme gözlemi çıkarıma, çıkarımı olguya, ilişkiyi nedenselliğe, aktarımı olguya çevirdi mi; edilgen–etken dönüşümü sorumluluğu değiştirdi ya da aktör uydurdu mu; atıf kayboldu ya da yönettiği önermeden uzaklaştı mı; çekince–pekiştirici dengesi taahhüdü değiştirdi mi; kip değişimi bakış açısı değişimine karşılık geliyor mu; iddia tartışma ya da sonuçta güçlendi mi; "gözlenmedi" "yoktur", öneri karar ya da uygulama oldu mu?
- **H. Sözcük uyumu:** Sözcükler doğal birleşiyor mu; her ana fiil doğru hâl ve tümleci alıyor mu; İngilizce edat tuhaf bir ilgeç üretmiş mi; hafif fiil daha yalın yüklemi gizliyor mu; yeniden yazım anlam ilişkisini güçlendirdi mi; eş anlamlı değişimi teknik ayrımı bulanıklaştırdı mı; ana varlıklar tutarlı adlandırılıyor mu; seyrek ama geçerli bir birleşim yanlışlıkla normalleştirildi mi?
- **I. Metinsel tutarlılık:** Her cümle etkin olandan mı büyüyor; paragraf konu mu geliştiriyor, olgu mu yığıyor; her bağlaç gerçek bir ilişkiye mi karşılık geliyor; sözcük zincirleri kararlı mı; göndergeler mesafelerinde geri kazanılabilir mi; paragraflar birbirine doğal devrediyor mu; sözcük sırası değişimi kapsam ya da odağı değiştirdi mi; olumsuzluk aynı önermeye bağlı mı; kayıt kaydı mı; noktalama Türkçe gruplamaya yardım ediyor mu; iddia ile dayanağı yeterince yakın mı?

Çıkardığın hiçbir şeyi daha sakin eş anlamlılarla geri koyma. Sonucu insanileştirmek için hata, argo, rastgelelik veya cümle uzunluğu gürültüsü üretme.

**6. Ses ve akış denetimi yap.** Metni bir kez anlam, bir kez doğal duraklar için oku. Her cümlenin öncekiyle ilişkisi açık mı? Cümleler aynı kalıpla mı ilerliyor? Yazarın tavrı, iletişim amacı veya yapısal ölçeği kaybolmuş mu? Gereksiz bağlaçlar çıkarılmış mı? Özgün fakat doğal ifadeler yanlışlıkla düzleştirilmiş mi? Kullanıcının istediğinden fazla değişiklik yapılmış mı? Gerekli bir sınırlılık, koşul, kesinlik işareti, öğretici açıklama, tekrarlanabilirlik adımı veya gezinme başlığı dolgu sanılıp silinmiş mi? Birleştirme cümleleri şişirmiş veya paragrafı okunmaz yapmış mı? Raporda bulgu, yorum, sınırlılık, öneri veya karar yanlışlıkla birbirine dönüşmüş mü? Metin Türkçeye çevrilmiş gibi değil, Türkçe düşünülmüş gibi okunuyor mu; konu → odak → yüklem akışı doğal mı? Her iddia kaynaktaki kişiye, kanıt statüsüne ve kesinlik düzeyine hâlâ bağlı mı; her cümle öncekinden yararlı bir şey alıp sonrakine yararlı bir şey bırakıyor mu?

## Referans yönlendirmesi

- Klişe, yapay ritim, gereksiz resmiyet, reklam dili veya çeviri kokusu baskınsa [Türkçe örüntüler](references/turkce-oruntuler.md) dosyasını oku.
- Cümleler doğru olduğu hâlde metin yapay okunuyorsa; önem cümleleri, savunmacı açıklama, tekrar döngüleri, yol haritası, kalıp giriş ve sonuç, soyut yüklem veya tek biçimli paragraf mimarisi varsa [Retorik yapılar](references/retorik-yapilar.md) dosyasını oku.
- Metin çok başlıklı, kısa paragraflı, sık çapraz göndermeli veya yapay gerilimliyse; bölümler birleştirilecek ya da korunacaksa; uzun çerçeve ifadeleri ve listeleştirme varsa [Yapısal bütünlük](references/yapisal-butunluk.md) dosyasını oku.
- Cümleler doğru olduğu hâlde paragraf kopuksa, göndergeler belirsizse veya okuma akışı takılıyorsa [Akıcı Türkçe](references/akicilik.md) dosyasını oku.
- Dil bilgisi doğru olduğu hâlde metin çeviri gibi okunuyorsa; açık özne, `bu sonuç`, `ve` zinciri, `sahip olmak`, `bulunmaktadır`, `olan` zinciri, çerçeve yığını, fazla `bir` ya da uzak yüklem ritmi varsa [Türkçe ritim ve kaynak dil gölgesi](references/turkce-ritim-ve-ceviri-golgesi.md) dosyasını oku.
- Metin akademik, teknik ya da rapor türündeyse ve aktarım, çıkarım, çekince, pekiştirici, edilgen çatı, kip değişimi, öneri–karar–uygulama statüsü ya da bölümler arası kesinlik söz konusuysa [Epistemik mimari](references/epistemik-mimari.md) dosyasını oku.
- Cümleler Türkçe kurulduğu hâlde sözcükler tuhaf birleşiyorsa; hafif fiil, yanlış hâl, edat gölgesi, eş anlamlı kayması ya da terim kararsızlığı varsa [Eşdizim ve istem](references/esdizim-ve-istem.md) dosyasını oku.
- Paragraflar tek tek iyi olduğu hâlde metin bir düşünceyi geliştirmiyorsa; olgu yığını, desteksiz bağlaç, uzak gönderge, kapsam ya da olumsuzluk kayması, kayıt kayması ya da noktalama yükü varsa [Metinsel tutarlılık](references/metinsel-tutarlilik.md) dosyasını oku.
- Metin rapor, inceleme notu, değerlendirme belgesi veya yönetici özeti ise [Rapor yazımı](references/rapor-yazimi.md) dosyasını oku.
- Kullanıcı açıkça temel bir kavram veya yönteme bütünlüklü giriş yazılmasını istiyorsa [Kavramsal girişler](references/kavramsal-girisler.md) dosyasını oku.
- Uzun veya karmaşık metinde birden fazla sorun varsa ilgili referans dosyalarını birlikte oku.

## Çıktı biçimi

Belirsizliği korumak mümkün değilse ve düzenleme bir yorum seçmeyi gerektiriyorsa önce kullanıcıdan açıklama iste. Kullanıcı başka bir biçim istemediyse yalnızca son metni ver; sohbet botu girişi veya kapanış teklifi ekleme.

Kullanıcı inceleme ya da karşılaştırma istediyse şu sırayı kullan: kısa teşhis, düzeltilmiş metin, en önemli değişiklikler. Cümle sildiysen veya bölüm birleştirdiysen üçüncü bölümde silinen cümlelerin hangi işlevi taşımadığını ve birleştirmenin hangi kavramsal sınıra dayandığını kısaca belirt. Standart düzeyde başlıklara dokunmadıysan ama başlıklar hak edilmemiş görünüyorsa, inceleme istenmişse derin düzenlemede birleştirilebileceklerini tek cümleyle not et. Kullanıcı yalnızca son metni istediyse bu açıklamaları ekleme.

## Kısa örnekler

**Önce**

> Günümüzün hızla değişen iş dünyasında yenilikçi platformumuz, siparişleri tek ekranda topluyor ve tekrar eden onayları otomatikleştiriyor. Bu güçlü çözüm yalnızca süreçleri kolaylaştırmakla kalmıyor, sipariş başına gereken adım sayısını beşten üçe indirerek verimliliği de bir üst seviyeye taşıyor.

**Sonra**

> Platform, siparişleri tek ekranda topluyor ve tekrar eden onayları otomatikleştiriyor. Bu değişiklik, sipariş başına gereken adım sayısını beşten üçe indiriyor.

İkinci metin yeni özellik üretmez; kaynakta bulunan işlev ve ölçümü koruyup reklam kalıplarını çıkarır.

**Önce**

> ### Örnekleme stratejisinin seçimi
>
> Model eğitiminde katmanlı örnekleme kullanılmıştır.
>
> ### Örnekleme stratejisinin önemi
>
> Örnekleme stratejisi hata oranı açısından belirleyici bir rol oynamaktadır. Ancak asıl etki bir sonraki bölümde görülecektir.
>
> ### Düşük yoğunluklu bölgelerdeki etki
>
> Yukarıda belirtilen katmanlı örnekleme, düşük yoğunluklu bölgelerde hata oranını %9'dan %4'e düşürmüştür.

**Sonra**

> ### Örnekleme stratejisi
>
> Model eğitiminde katmanlı örnekleme kullanılmıştır; bu örnekleme, düşük yoğunluklu bölgelerde hata oranını %9'dan %4'e düşürmüştür.

Üç başlık ve üç paragraf tek bölüm oldu. Yöntem bilgisi ve iki ölçüm korundu; "belirleyici rol", "bir sonraki bölümde görülecektir" askısı ve "yukarıda belirtilen" göndermesi bölünmenin ürettiği dolguydu. Kullanıcı yalnızca hafif düzenleme isteseydi başlıklar korunur, yalnızca dolgu cümleleri silinirdi.
