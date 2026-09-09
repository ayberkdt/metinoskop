---
name: metinoskop
description: Türkçe metinleri anlamı, olguları, kesinlik düzeyini ve yazarın sesini koruyarak doğallaştırır; yapay zekâ ya da çeviri kaynaklı retorik, cümle, paragraf ve belge örüntülerini, çeviri kokusunu, epistemik statü kaymalarını, eşdizim ve istem sorunlarını ve metinsel tutarsızlığı düzenler. Makale, rapor, teknik belge, e-posta, tanıtım metni, deneme veya Türkçeye çevrilmiş metin için "insanileştir", "doğal Türkçe yap", "AI gibi görünmesin", "dolguyu çıkar", "parçalanmayı gider", "çeviri gibi durmasın", "kesinlik düzeyini bozma" ya da "üslubuma uyarla" dendiğinde kullan.
---

# Metinoskop

Türkçe metni bir sözcük yasaklama listesiyle değil; bağlam, iletişim amacı, kaynak sadakati ve doğal Türkçe ritmi üzerinden düzenle. Yapay üslubu yalnızca sözcüklerde değil, cümle, paragraf ve belge kuruluşunda ara. Okurun bir argümanın içinde, onu anlayacak kadar uzun kalabilmesini sağla. Bu dosya ilkeleri ve karar noktalarını verir; katalog, örnek ve karşı örnekler `references/` altındadır.

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

**Standart.** Cümleleri ve paragraf içi akışı gerektiğinde yeniden kur. Mekanik ritmi, gereksiz resmiyeti, belirsiz göndergeleri, çeviri kokusunu düzelt. Sıfır bilgi cümlelerini, işlev tekrarını, savunmacı açıklamayı, üretilmiş önem ve karşıtlığı, yol haritası dilini, kalıp giriş ve sonuç cümlelerini, yapay gerilimi ve uzun çerçeve ifadelerini çıkar. Erken bölünmüş paragrafları birleştir; mevcut başlık hiyerarşisini koru. Kullanıcı bir düzey belirtmediyse bunu kullan.

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

Hedef; gündelik, kesik veya bilerek kusurlu bir metin değil, her cümlesi yerini hak eden kesin, doğal ve tutumlu Türkçedir. Sözcük tek başına asla yasak değildir; yargı birimi sözcüğün bağlamdaki işlevidir. Kalıp katalogları için [Retorik yapılar](references/retorik-yapilar.md) dosyasını oku.

### Cümle düzeyi

**Sıfır bilgi cümlesi.** Bir cümle yeni bir olgu, gerekli bir nitelendirme, açık olmayan bir mantıksal ilişki, kaynağın desteklediği somut bir yorum, gerçek bir konu değişiminin gerektirdiği geçiş, kaynakta bulunan bir yazar değerlendirmesi, gerekli bir yöntem gerekçesi, yorumu değiştiren bir sınırlılık ya da önceki bilgiyi anlamlı biçimde birleştiren bir sentez taşımalıdır. Silme testi iki sorudur: cümleyi çıkardığında önermeler, akıl yürütme, kronoloji, yorum ve yazar tavrı değişiyor mu; değişmiyorsa, cümle önceki bilgiyi birleştiriyor veya okurun çıkarım yükünü azaltıyor mu? İkisine de hayırsa cümleyi çıkar. Sentez birden çok olguyu tek ilişkide toplar; açımlama tek olguyu başka sözcüklerle yineler. "Model 120. derecede en düşük hatayı verdi. Bu sonuç, yöntemin davranışının anlaşılması açısından önemli bir bulgudur" örneğinde ikinci cümle silinir; "ışık tutmaktadır" diye yeniden kurulmaz.

**Dolguyu başka dolguya çevirme.** Kesin kural: reklam dili, önem şişirmesi, retorik çerçeve, savunmacı açıklama, boş geçiş veya kalıp sonuç çıkarılırken aynı retorik işlev daha sakin eş anlamlılarla korunmaz. "Çığır açan sonuç" → "oldukça önemli sonuç", "bu noktada vurgulamak gerekir" → "burada belirtmek gerekir" dönüşümleri yanlıştır. Cümlenin bağımsız bir bilgi işlevi yoksa cümleyi sil; varsa yalnızca o bilgiyi bırak.

**İşlev tekrarı.** Yalnızca yinelenen sözcükleri değil, yinelenen retorik işlevleri ara. "Bu sonuç önemlidir", "Bu bulgu dikkat çekicidir", "Bu da yöntemin önemini ortaya koymaktadır" sözcük olarak farklı, işlev olarak aynıdır. Aynı işlevi gören cümleleri paragraf ve belge boyunca birlikte ele al: kaynakta dayanağı olan varsa onu koru, diğerlerini çıkar.

**Savunmacı düzyazı.** "Burada amaç ... değildir", "Bu ayrım önemlidir", "Bu tercih tesadüfi değildir", "Bu durum bir eksiklik olarak görülmemelidir", "Bu sonuç şaşırtıcı değildir" ve benzerleri gerçek bir belirsizliği veya yöntem sorusunu cevaplamıyorsa yüksek risklidir. Mekanik olarak silme; her biri için sor: bu cümle okurun hangi somut yanlış anlamasını önlüyor? Somut cevap yoksa çıkar. Yöntem gerekçesi, tercih değiştiğinde yorum, tekrarlanabilirlik veya geçerlilik değişecekse meşrudur; ön deneme sonucu gibi somut dayanağı varsa dayanakla birlikte koru. Olağan bilimsel uygulamayı önceden savunma.

**Üretilmiş önem.** Bir sonuç var diye önem üretme. "... açısından önemlidir", "... kritik rol oynamaktadır", "... değerli içgörüler sunmaktadır", "... literatürdeki boşluğu doldurmaktadır", "... gelecekteki çalışmalar için temel oluşturmaktadır" ve benzerleri kaynak açıkça gerekçelendirmiyorsa çıkar; somut sonucun kendisini bırak. Kaynak önemi dayanağıyla birlikte kuruyorsa tam o güçte koru. Bir cümlenin kaynakta yer alması onu korumaya yetmez. Önem cümlesi yalnızca bir kişiye veya kuruma atfedilmişse, kendi dayanağını taşıyorsa ya da türün gerektirdiği açık bir değerlendirme konumundaysa yazar değerlendirmesi sayılır.

**Üretilmiş karşıtlık.** Karşıtlık bilgi taşıyorsa meşrudur; yalnızca retorik güç için kurulmuşsa yapaydır. "X değil, Y", "Asıl mesele X", "X'ten ziyade Y", "Bir yandan X, diğer yandan Y", "X yalnızca ... ile sınırlı değildir", "yalnızca ... değil, aynı zamanda ..." yapılarını incele. Kabul edilen önermeyi güçlü göstermek için reddedilen bir seçenek uydurma; reddedilen taraf kaynakta yoksa yalnızca kabul edilen önermeyi yaz.

**Soyut yüklem sisi.** `ortaya koymak`, `işaret etmek`, `vurgulamak`, `rol oynamak`, `katkı sağlamak`, `mümkün kılmak`, `ışık tutmak`, `şekillendirmek` ve benzerlerini tek tek yasaklama; her birinde hangi somut ilişkinin kodlandığını sor ve mümkünse yüklemi o ilişkiyle değiştir. Kanıt yalnızca "Hata 20 °C'de %3, 40 °C'de %11 oldu" ise ölçümleri yaz; çıkarım cümlesi kaynağın kendi iddiasıysa koru. Daha somut yüklem kaynağın kurmadığı nedenselliği kuramaz.

**Boş soyut özne.** Tekrarlanan `bu durum`, `bu yaklaşım`, `bu süreç`, `bu bulgu`, `bu sonuç`, `söz konusu durum` özneleri güçlü bir yapaylık işaretidir. Mekanik olarak değiştirme: mümkünse somut göndergeye çöz; özne yalnızca dolguyu taşımak için varsa cümleyi çıkar. Gönderge belirsizse belirsizlik kuralı geçerlidir.

**Açık olanı açıklama.** Cümle, hedef okurun zaten bildiği olağan bir olguyu gerekçe gerektiriyormuş gibi açıklıyor mu? Doğrulama kümesinin neden ayrı tutulduğu giriş düzeyindeki ders notunda gereklidir; uzman okura yazılmış makalede standart dışı bir tercihi açıklamıyorsa gereksizdir. Yeni başlayanlara yönelik metinden öğretici açıklamayı, benzetmeyi veya örneği silme. Muhatap belirsizse açıklamayı koru.

### Paragraf düzeyi

**İddia → açımlama → önem → mini sonuç.** Olgu → aynı olgunun başka sözcüklerle tekrarı → genel önem cümlesi → soyut mini sonuç dizisini tanı. Kaynak yalnızca ilk önermeyi kuruyorsa son üç cümle fazladır; diziyi kaynağın desteklediği önermeye indir. Tekrarı eş anlamlılarla koruma. Paragraf testi: paragraf kaç gerçekten farklı önerme içeriyor?

**Paragraf simetrisi.** Neredeyse eşit uzunlukta paragraflar, her paragrafın konu cümlesiyle başlayıp sonuç cümlesiyle bitmesi, tekrarlayan "nokta → açıklama → sonuç" mimarisi ve her bölümde gereksiz giriş ile mini özet yapaylık işaretidir. Sorun belirli bir uzunluk değil tek biçimliliktir. Uzunlukları insan gibi görünsün diye rastgeleleştirme; paragraf boyutunu bilgi yapısı belirlesin.

**Zorlama denge.** Her iddiaya kendi karşı iddiasını ekleme. "Bir yandan ... Öte yandan ...", "Her ne kadar ... olsa da ...", "güçlü olmakla birlikte bazı sınırlamalara da sahiptir" yalnızca ölçülü görünmek için kurulmuşsa çıkar. Gerçek sınırlılığı koru; sınırlılık adlandırılmalıdır. Kanıt düzeyini bildiren çekince ("çalışma gözlemseldir", "henüz doğrulanmadı") denge değil kesinlik bilgisidir; korunur. Adlandırılmış sınırlılık yoksa "her çalışmada olduğu gibi bazı sınırlılıkları vardır" cümlesini çıkar.

### Belge düzeyi

**Yol haritası ve okur yönlendirmesi.** Ana işlevi içerik vermek değil metni duyurmak olan "Bu bölümde ... ele alınacaktır", "Şimdi ... bakalım", "Bu noktaya daha sonra döneceğiz", "Peki bu ne anlama geliyor?" cümlelerini çıkar. Yol haritası yalnızca uzun veya yapısı zor belgede, genellikle belge başına bir kez meşrudur. Ana metin olguyu doğrudan söyleyebiliyorsa sonraki bölüme gönderme yerine olguyu söyle; kaynak işaretlerini, tablo ve ek göndermelerini koru.

**Kalıp giriş ve kalıp sonuç.** Giriş hunisini tanı: geniş dünya cümlesi → hızla değişen ortam → genel zorluk → "giderek önem kazanıyor" → "bu nedenle" konuya geçiş. Kaynakta konuyu ele almanın somut bir nedeni varsa oradan başla; tarihsel ivme, aciliyet veya toplumsal önem üretme. Kalıp sonucu tanı: "Sonuç olarak ...", "Tüm bu bulgular birlikte ele alındığında ...", "Gelecekte yapılacak çalışmalar ...". Sonuç bölümü sentez yapabilir; özeti, girişi ve önceki paragrafı başka sözcüklerle tekrarlayamaz. Metin akademik diye gelecek çalışma cümlesi ekleme.

## Yapı ve okur yorgunluğu

Yapı, kavramsal sınırları izler; modelin her şeyi düzenleme isteğini değil. Her yeni başlık, paragraf veya liste okura bilişsel maliyet yükler; bu maliyeti yalnızca anlama veya gezinme kazancı karşılıyorsa yükle. Okur, bir kavramı zihninde sabitleyecek kadar bilgi birikmeden o kavramdan tekrar tekrar ayrılmak zorunda kalmamalıdır. Görsel parçalanmayı açıklık sanma: kısa paragraf, çok başlık ve madde işareti tek başına okumayı kolaylaştırmaz. Test, örnek ve karşı örnekler için [Yapısal bütünlük](references/yapisal-butunluk.md) dosyasını oku.

### Bölme kararı

**Önce süreklilik.** Yeni paragraf, alt bölüm veya başlık açmadan önce sor: konu gerçekten değişti mi; argüman işlevi değişti mi; aynı paragrafta devam etmek ilişkiyi anlaşılmaz mı yapardı; bölme gezinmeye yarıyor mu, yoksa metni yalnızca düzenli mi gösteriyor? Cevapların çoğu "hayır" ise bölme.

**Başlık hakkını kazanmalıdır.** Yararlı başlık büyük bir kavramsal geçişi işaretler, uzun bölümde gezinmeyi sağlar, gerçekten ayrı yöntem aşamalarını ayırır, dışarıdan dayatılan yapıyı yansıtır ya da altında anlamlı bir birim taşır. Her küçük kavrama açılan başlık, altında tek kısa paragraf bulunan başlık, ilk cümleyi yineleyen başlık ve simetrik görünsün diye kurulan başlık ağacı yüksek risklidir. "Gezinme" gerekçesi yalnızca okurun o bölümü tek başına arayacağı kadar uzun belgede geçerlidir.

**Derinlik testi.** `###` veya `####` açmadan önce ayrımın belge yapısına ait olacak kadar önemli olup olmadığını sor. Bölüm → alt bölüm → alt-alt bölüm → bir paragraf → iki cümle deseninden kaçın; daha az, daha geniş bölüm ve içinde tutarlı paragraflar tercih et.

**Başlık sıkıştırma.** Komşu başlıklara bak: iki bölüm aynı önermenin farklı yüzlerini mi anlatıyor; biri diğerinin örneği, sınırlılığı veya devamı mı; hiyerarşi içeriği mi, modelin düşünme sırasını mı yansıtıyor? Tek sürekli argüman olarak daha kolay anlaşılıyorsa birleştir. Hafif düzenleme veya yapı koruma istendiyse bu sınıra uy.

**Paragraf görsel parça değil kavramsal birimdir.** Cümleler baskın ve tutarlı bir düşünce hareketini (iddia → kanıt → yorum, gözlem → açıklama, sonuç → sınırlılık) yürütürken paragraf bütün kalır; hareketi her cümleden sonra kesme. Aynı konu üzerinde olmak tek paragraf için yeterli değildir: söylem işlevi sert biçimde değişiyorsa (bulgu → öneri, yöntem → sonuç) paragraf sınırı meşrudur. Bulgu, yorum ve öneriyi tek yoğun blokta paketleme.

**Zihinsel model sürekliliği.** Her sınırda sor: okur, etkin kalabilecek bağlamı yeniden mi kuracak? Sonraki birim aynı özneyi, yöntemi, değişkeni veya sınırlılığı yeniden tanıtmak zorunda kalıyorsa bölmeyi gözden geçir.

**Yakınlık kuralı.** Bir cümle başka bir cümleyi niteliyor, sınırlıyor veya yorumluyorsa belge yapısı ayrılmayı gerçekten gerektirmedikçe ikisini yakın tut. İddia ile kanıt, sonuç ile sınırlılık, ölçüm ile yorum, karşılaştırma ile tabanı temiz alt bölümler uğruna ayrılmaz; okur bir sonucu sınırlılığına ulaşmak için birkaç başlık boyunca aklında tutmamalıdır.

**Açıklama, metin ilerlemeden bitmelidir.** Bölümü kapatmadan önce okurun iddiayı, gerekli kanıtı, yorumu ve temel sınırlılığı edinip edinmediğini sor; bitmemişse yeni yapısal birime geçmeden sürdür.

**Slayt değil belge.** Her noktayı "başlık → kısa açıklama" çiftine çevirme; yakın fikirler aynı bölümde kalır ve paragraf akışıyla ayrılır. Mantıksal sürekliliği olan akıl yürütmeyi sırf maddelenebiliyor diye listeye çevirme; maddeler "bu nedenle", "dolayısıyla" ile birbirine bağlanıyorsa paralel değil zincirdir, düzyazıya dön.

### Okuru yoran alışkanlıklar

**Yapay gerilim.** Bilgi veren metinde momentum üretmek için kurulan "Ancak burada işler değişmektedir", "İlk bakışta ...", "Fakat hikâye burada bitmez", "İşin ilginç yanı ...", "Daha da önemlisi ..." kalıplarını sil. Gerçek karşıtlık ile anlatı dramasını ayır: "Yöntem kuvvet hatasını düşürdü ama yedi günlük konum hatasını artırdı" bilgi taşıyan karşıtlıktır; dramatik ambalajını at, nicel karşıtlığı doğrudan yaz.

**Paragraf sonu askısı.** "Bu sorunun yanıtı bir sonraki bölümde görülecektir", "Bu durum bizi daha temel bir soruya götürmektedir" gibi kapanışlar yerine ilişkiyi doğrudan söyle.

**Bağlam yeniden başlatma ve çapraz gönderme.** Aynı değişkenin, düzeneğin veya amacın her alt bölümde yeniden tanıtılması ve "yukarıda belirtildiği gibi", "ileride tekrar dönülecektir" sıklığı metnin fazla bölündüğünü gösterir. Her göndermeden önce sor: malzemeyi birleştirmek veya yeniden sıralamak göndermeyi gereksiz kılar mı? Tablo, şekil, ek ve kaynak göndermeleri bu kuralın dışındadır.

**Başlık tekrarı ve boş sarmalayıcılar.** Başlık yönlendirmeyi zaten veriyorsa doğrudan içerikle başla. "Bu bölümde X ele alınmaktadır" açılışları ile "Sonuç olarak bu bölüm X'in önemini ortaya koymaktadır" kapanışları sarmalayıcıdır; yalnızca ortadaki içerik kalır.

**Zorlama geçişler.** Yeni paragraf başlıyor diye "Bununla birlikte", "Bu doğrultuda", "Buna ek olarak" ekleme; anlamsal süreklilik açıksa doğrudan cümle daha iyidir. Konu değişimini üç cümleyle anlatma.

**Yinelenme haritası.** Uzun metinde aynı önermenin giriş, bölüm girişi, sonuçlar, tartışma ve sonuçta tekrar edip etmediğini izle. Aynı önerme yeni bir rol, nitelendirme veya yorum kazanmadan birkaç kez açımlanıyorsa tekrarı azalt.

### Cümle ekonomisi

**Gereksiz uzun ifadeler.** Daha kısa biçim aynı anlam ve tonu taşıyorsa uzun biçimi bırak: "bir değerlendirme yapılması gerekmektedir" → "değerlendirilmelidir"; "söz konusu yöntemin kullanılması durumunda" → "yöntem kullanıldığında"; "dikkate alınması gereken bir husus olarak karşımıza çıkmaktadır" → meselenin kendisi. Tam biçimi ayrı anlam taşıyan teknik ifadeyi sıkıştırma.

**Yığılmış çerçeve.** Üst üste nitelemelerde gerçek özneyi, gerçek yüklemi ve gerçekten gerekli nitelemeyi bul; gerisini at. Akademik ses veriyor diye karmaşıklığı ödüllendirme.

**Bir cümle yeterse birkaç cümle kurma; cümleyi de şişirme.** Sıra, vurgu veya tekrarlanabilirlik ayrı adım gerektirmiyorsa yapay olarak parçalanmış cümleleri birleştir; parçalanmayı dev cümlelerle de çözme. Ölçüt cümle sayısı değil kavramsal birliktir.

**Okur emeği.** İki sürüm eşit doğruysa okurun daha az yeniden kurmasını gerektireni seç. Bunu konuyu basitleştirmekle karıştırma; teknik karmaşıklık gerekli olabilir, yapısal sürtünme değil.

### Yapısal koruma

- Yazarın ölçeğini koru; hedef evrensel asgaricilik değil, yazarın doğal yapısını aşan makine parçalanmasını önlemektir.
- Bağımsız tekrarlanabilir deneyleri, hukuki hükümleri, dergi kuralının ayırdığı bölümleri, sabit bölüm numaralarına bağlı göndermeleri, güvenlik açısından kritik adımları ve uzun belgenin gezinme çıpalarını ayrı tut. Dışarıdan dayatılan yapıyı yalnızca kullanıcı belirttiyse veya belge onu açıkça taşıyorsa varsay.
- Parçalanmayı tek dev paragrafla da çözme; her paragrafın baskın bir düşünce hareketi olur.
- Bu kuralları "her şeyi kısalt"a çevirme. Her yapısal değişiklik anlamı bozmadan süreklilik, anlama, gezinme, yakınlık, okur emeği veya yinelenme açısından bir kazanç sağlamalıdır.

## Sertlik düzeyleri

**Sert bastırma.** Alıntı, tür, kaynak anlamı veya açık kullanıcı tercihi gerektirmedikçe çıkar: sohbet botu nezaketi, boş bölüm duyurusu ve sarmalayıcısı, genel mini sonuç, önerme taşımayan dolgu, üretilmiş önem, aciliyet, gelecek çalışma ve savunmacı açıklama, slogan gibi yeniden ifade, aynı iddianın tekrarlanan açımlamaları, yapay gerilim, paragraf sonu askısı, altında yalnızca ilk cümlesini yineleyen içerik bulunan başlık.

**Bağlama duyarlı yüksek risk.** İncele ama otomatik çıkarma: `ancak`, `bu nedenle`, `önemli`, `göstermektedir`, edilgen çatı, `-maktadır`, üçlü listeler, retorik soru, kısa ve uzun paragraflar, alt başlıklar, madde işaretleri, çapraz göndermeler, akademik ihtiyat, açık yöntem gerekçesi; `bir`, `olan`, `ve`, `açısından`, `sahip olmak`, `bulunmaktadır`, açık özne tekrarı ve söylem belirteci gibi çeviri kokusu işaretleri; `olabilir`, `düşünülebilir` gibi çekinceler. Bir sözcük veya yapı sırf dil modelleri sık kullanıyor ya da İngilizcede de var diye yasaklanmaz.

## Akademik ve teknik metin

Akademik ve teknik metinde ayrıca şunları bastır: "literatüre önemli katkı", "bulgular açıkça göstermektedir", "değerli içgörüler sağlamak", "kritik rol"; otomatik sağlamlık ve genellenebilirlik iddiaları; kalıp sınırlılık paragrafları; otomatik "gelecek çalışmalar ..." kapanışları; olağan bir kontrolün neden gerekli olduğunun tekrar tekrar açıklanması; her alt bölümde yinelenen amaç ve düzenek hatırlatması; sonuçla sınırlılığını ayrı başlıklara dağıtan bölümleme.

Geçerli bilimsel iddiayı zayıflatma. Kaynak yenilik, önem, sağlamlık, mekanizma, sınırlılık veya çıkarımı açıkça kuruyorsa tam desteklenen güçte koru. Dergi veya kurum kuralının dayattığı bölüm ayrımını ve bağımsız tekrarlanabilirlik için ayrı tutulan deney bölümlerini koru. Akademik düzyazıyı gündelik konuşmaya çevirme.

## Kalıp düzeyinde yüksek riskli ifadeler

Bu yapıları otomatik olarak silme; içerik taşımadan vurgu, geçiş, otorite veya heyecan üretmek için kullanıldıklarında düzenle: "günümüzün hızla değişen dünyasında", "bu bağlamda", "bu noktada"; "bir araçtan fazlası", "dönüşümün anahtarı"; "benzersiz", "çığır açan", "kusursuz"; "fark yaratıyor", "bir üst seviyeye taşıyor"; "ve sonra her şey değişti", "asıl mesele şu"; art arda retorik sorular ve tek cümlelik dramatik paragraflar; "Elbette!", "Umarım faydalı olur"; kaynaksız "uzmanlara göre", "araştırmalar gösteriyor". Hukuki, akademik, teknik veya edebî bağlamda işlev taşıyan ifadeyi koru. Örüntüleri tek sözcükte değil, kümeler ve tekrarlar hâlinde ara; katalog [Türkçe örüntüler](references/turkce-oruntuler.md) dosyasındadır.

## Türkçeye özgü düzenleme

- Peş peşe gelen `-maktadır/-mektedir` yüklemlerini metnin türüne uygun doğal kiplerle sadeleştir; sırf çeşitlilik için farklı kipler kullanma.
- `gerçekleştirilmesi`, `sağlanması`, `yürütülmesi` gibi isim-fiil zincirlerini, anlam bozulmuyorsa eyleme döndür; teknik işlemi adlandıran isim-fiili koru.
- Edilgenliği yalnızca aktör belli diye etkene çevirme; aktörlüğü, konu sürekliliğini, vurguyu ve epistemik işlevi koru, kaynağın adlandırmadığı aktörü uydurma.
- Cümle başlangıçları, yüklem biçimleri veya uzunluklar mekanik biçimde tekrarlanıyorsa düşüncenin akışına göre yeniden kur; rastgele çeşitlilik üretme.
- Belirsiz `bu`, `böyle`, `ilgili` ve `söz konusu` göndergelerini açıklaştır.
- Aynı doğru terimi sırf tekrar olmasın diye rastgele eş anlamlılarla değiştirme.
- Metni aşırı sıkıştırıp telgraf diline dönüştürme.

## Çeviri kokusu ve Türkçe ritim

Dil bilgisi bakımından doğru bir Türkçe cümle yapı olarak hâlâ İngilizce olabilir: bilgi yapısı, özne kullanımı, yan cümle mimarisi, niteleme yeri, bağlaç seçimi ve söylem bağlantısı İngilizceden miras kalmışsa metin çeviri gibi okunur. Hedef, güçlü bir Türkçe yazarın doğrudan Türkçe düşünerek kurabileceği düzyazıdır. Katalog, zorlu örnekler ve karşı örnekler [Türkçe ritim ve çeviri kokusu](references/turkce-ritim-ve-ceviri-kokusu.md) dosyasındadır.

**Kokuyu sözcükte değil ilişkide ara.** Bir cümlenin Türkçe biçimi en iyi altındaki bir İngilizce cümle yeniden kurularak açıklanabiliyorsa koku vardır; bunu işlev testi olarak kullan, her pasaj için gizli İngilizce cümleyi kurmaya çalışma. En sık işaretler: ardışık cümlelerde yinelenen açık özne; `bu sonuç`, `bu durum` diye yeniden öznelenen önceki önerme; `ve`, `ancak`, `sonra` ile dizilmiş bağımsız çekimli cümleler; her cümle başında söylem belirteci; `sahip olmak`, `bulunmaktadır`, `rol oynamak` gibi hafif yüklemler; `açısından`, `kapsamında`, `noktasında` çerçeve yığını; `olan ... olan` zinciri; her adın önünde tanımlık `bir`. Çeviri gibi duran cümlenin sözcüklerini bir kez daha çevirme; taşıdığı anlam ilişkisini bul ve onu yeniden kur. Düzenlemeden sonra parça, bağlaç ve özne sayısı aynıysa büyük olasılıkla yalnızca sözcük değiştirdin.

**Bilgi yapısı ve Türkçenin kendi kaynaklarıyla yeniden kur.** Sözcük sırasını konu, odak, verilmiş ve yeni bilgi belirler, mekanik özne–nesne–yüklem şablonu değil. Şüpheli pasajda sor: özne düşürülebilir mi (tek aktör, kişi eki geri kazandırıyor); eksilti yinelemeyi kaldırabilir mi; ilişkiyi adlandırıp (paralel, sıralı, neden, koşul, eş zaman, araç) `-ip`, `-ince`, `-dığından`, `-ken`, `-erek` kodlayabilir mi; ortaç adı önden niteleyebilir mi; iyelik `sahip olmak`, `var/yok` `bulunmaktadır`, hâl eki çerçeve öbeği yerine geçebilir mi; `de/da` eklemeyi belirteçsiz taşıyabilir mi? Şüpheli cümle için en az iki yapısal olarak farklı alternatif üret ve kaynak anlamını, vurguyu ve türü en iyi koruyanı seç. Özne iki aktör arasında belirsizlik doğuracaksa, paragraf ya da tablodan sonra dönüyorsa ya da karşıtlık kuruyorsa açık kalır; belirteç kaldırılınca ilişki belirsizleşiyorsa kalır.

**Kesinliği bozma, aşırı Türkçeleştirme.** Kaynak "ilişkili" diyorsa "neden olur", "olumsuz etki" diyorsa "bozuldu" yazma; güvenli tek Türkçe biçim daha soyutsa soyutluğu koru. Alanın terimini (`parametre`, `pipeline`, `baseline`) öz Türkçe hevesiyle değiştirme. Tek yükleme asılmış dört beş fiilimsi, belirsiz düşürülmüş özne, telgraf dili, arkaik sözcük, zorlama deyim, gereksiz devriklik, gündelikleşmiş resmî kayıt dili ve her cümlenin aynı "yerli" kalıba dökülmesi aşırı düzeltmedir. Akademik metin adlaştırma ve edilgenliğe, teknik belge güvenlik için açık özne yinelemesine, hukuki metin kalıp yapıya, kişisel düzyazı serbest sıra ve eksiltiye hak sahibidir. Doğal özne akışı ve iyi konu–odak hareketi olan metni daha fazla "Türkçeleştirme".

## Kanıt ve kesinlik

Olguları değişmeyen bir cümle düzenlemeden sonra epistemik olarak yanlışlaşabilir: kimin bildiği, nasıl bildiği, ne kadar kesin iddia ettiği, gözlemle çıkarımın sınırı ve aktörün konumu değişmişse cümle aynı cümle değildir. Katalog ve karşı örnekler [Kanıt ve kesinlik](references/kanit-ve-kesinlik.md) dosyasındadır.

**Bilginin kaynağını düzenleyip yok etme.** Her önemli önerme için statüyü belirle: gözlem, ölçüm, aktarım, alıntı, çıkarım, tahmin, öngörü, plan, varsayım, yaygın kabul, yazar ya da kurum yorumu, çözümsüz. "Gözlendi", "bildirildi", "düşündürüyor", "ölçüldü", "bekleniyor" aynı önermeye gönderse bile farklı statü kodlar; düzenlenmiş cümle kaynakla aynı epistemik düzeyde olmalıdır. Ölçüm, ilişki, çıkarım ve nedensel iddia dört ayrı düzeydir; "daha doğrudan" fiil bir düzeyi yükseltemez: rastgele atanmamış iki grup arasındaki fark "etkiler" ya da "azaltır" olmaz. Atıflı iddia ("ekip bildirdi", "rapora göre", "yazarlar öne sürmektedir") kaynak iddiayı ayrıca kurmuyorsa atıflı kalır ve yönettiği önermenin yanında durur; atıftan sonra gelen "bu nedenle" cümlesi neredeyse her zaman incelenir. Kesinliği aşağı çekerken de kaynağa önerme ekleme: şişmiş iddia kaynağın düzeyine iner, yerine olumsuzu ("mekanizma ortaya konmamıştır") ya da yeni bir çekince yazılmaz.

**Aktörlüğü koru; edilgeni epistemik seçim olarak değerlendir.** Edilgen çatı konu sürekliliğini koruyor, ilgisiz aktörü arka plana alıyor, yöntem merkezli akademik kaydı taşıyor ya da kaynağın adlandırmadığı aktörü uydurmayı önlüyorsa meşrudur; bilinen ve ilgili aktörü gizliyor ya da sorumluluğu kaybediyorsa şüphelidir. Etkene çevirmeden önce sor: aktör biliniyor mu, ilgili mi, adlandırmak vurguyu değiştirir mi, kaynak eylemi o aktöre yüklüyor mu? "Kararın ertelenmesine karar verildi" cümlesini kaynak yönetimi adlandırmıyorsa "Yönetim kararı erteledi" yapma. Bilimsel düzyazıyı otomatik olarak etkene çevirme.

**Çekince kanıttır, pekiştirici değildir.** `Olabilir`, `düşünülebilir`, `görünmektedir`, `kısmen`, `bu verilerle sınırlı olarak` belirsizlik, kapsam veya çıkarım statüsü kodluyorsa korunur; yalnızca gereksiz ya da çelişkiliyse kaldırılır. `Açıkça`, `kesin olarak`, `tartışmasız`, `kanıtlamaktadır` için sor: hangi kanıt bunu hak ediyor, alıntının parçası mı? Kısalık için iddiayı güçlendirme; kontrollü deneyle kurulmuş güçlü iddiayı da zayıflatma. Kiplik yığınında (`muhtemelen ... olabileceği düşünülebilir`) her işaretin ne kodladığını sor: olasılık, atıf, kanıt gücü; gereksizi kaldır. Kapsam işaretini (`yalnızca`, `en az`, `yaklaşık`, `özellikle`) taşırken bağlandığı ögeyi de taşı.

**Kip ve statü zincirini ilerletme.** Kip değişimi gerçek bir zamansal ya da epistemik bakış açısı değişimine (tamamlanmış işlem, gözlenen sonuç, genel özellik, şekil betimlemesi, plan) karşılık gelmelidir; `-dı`, `-miştir`, `-mektedir`, `-yor`, `-r` biçimlerini çeşitlilik için nöbetleştirme, `-miştir` resmî durum bildiriminde işlevseldir. Öneri, plan, karar, uygulanacak, uygulanmış ve değerlendirilmekte ayrı statülerdir; öneri karar, karar uygulama, beklenti taahhüt olmaz. Bir iddia yeni kanıt olmadan sonraki bölümde güçlenemez; sonuçlar "ilişki zayıftır" diyorsa sonuç bölümü "mekanizma ortaya konmuştur" diyemez. Kanıt yokluğu yokluğun kanıtı değildir: "gözlenmedi" "yoktur", "sınanmadı" "geçersizdir" olmaz.

**Zamansal ankrajı koru.** Tamamlanmış bir çalışma, deney, test ya da süreç anlatılıyorsa `inceler / kullanır / uygular` gibi zamansız-genel kipleri sırf akademik göründükleri için kullanma; yapılan işi doğal olarak `incelendi / kullanıldı / uygulandı` ekseninde anlat. Her pasajda baskın zamansal ankrajı belirle: tamamlanmış çalışma olayı, genel davranış, mevcut durum, belge içi gönderme, plan. Açık geçmiş tarih, tamamlanmış örneklem ya da `bu çalışmada` çerçevesiyle geniş zamanlı yüklem yan yana geldiğinde zamansal sürtünme vardır. Ancak algoritmanın genel davranışı, bilimsel genel gerçek, ürün belirtimi, yeniden kullanılabilir prosedür veya belgenin güncel işlevi gerçekten zamansızsa geniş zamanı koru; tek gözlemi geniş zamana çevirip genelleştirme, genel ilişkiyi geçmişe çevirip tek olaya indirme. Düzeltmeyi `yapıldı / edildi` zincirine ya da `-miştir` doygunluğuna dönüştürme; tekdüzeliği kiple değil sözdizimiyle çöz. Geçmişin kendi içindeki ilişkileri düzleştirme: `-yordu` artalanı, `-mıştı` daha önce tamamlanmış olmayı, `-ardı` düzenli davranışı bildirir; kaynak bu ilişkiyi kurmuyorsa da bu ekleri uydurma.

**Şimdiki zamanı eksik bırakma.** `-yor` yalnız o anda süren eylemi anlatmaz; mevcut sistem davranışı, güncel durum, okurun önündeki belgenin işlevi ve şu anda tartışılan bulgunun yorumu için de doğal olabilir. `Repo bunu yasaklar`, `Bu sonuç ... gerektirir`, `Şekil 4 ... gösterir` gibi yerel ve güncel önermeleri sırf resmî görünsün diye zamansız geniş zamana taşıma; bağlam güncel geçerlilik taşıyorsa `yasaklıyor / gerektiriyor / gösteriyor / işaret ediyor` biçimlerini değerlendir. Göndergeye bak: `bu sonuç` ile `bu tür sonuçlar` aynı kapsamda değildir. Gerçek genel yasa, algoritma tanımı, yeniden kullanılabilir prosedür ve normatif kural geniş zamanda kalır. `-yor` biçimini de yeni bir mekanik varsayılan yapma; kip doğallaştırması kanıt düzeyini ve dayanaksız cümlenin silinmesini geçersiz kılmaz. Ayrıntı için [Zamansal ankraj ve rapor kipi](references/zamansal-ankraj-ve-rapor-kipi.md).

## Sözcük birleşimleri

Bir sözcük tek başına doğru, birleşimde yanlış olabilir; dil bilgisi doğru ve yapısı Türkçe cümle, sözcükleri güçlü Türkçe düzyazının birleştirdiği gibi birleştirmiyorsa olası Türkçedir, doğal Türkçe değil. Katalog ve karşı örnekler [Sözcük birleşimleri](references/sozcuk-birlesimleri.md) dosyasındadır.

**Eşdizim ve istem denetimi.** Şüpheli öbekte sor: bu ad bu fiille normalde kullanılır mı; fiil tümlecini doğru hâlde mi alıyor; İngilizce edat harfiyen bir ilgeç mi üretmiş (`X hakkında odaklanmak` → `X'e odaklanmak`); hafif fiil (`değerlendirme gerçekleştirmek`, `iyileştirme sağlamak`) daha yalın yüklemi mi gizliyor; genel fiil (`göstermektedir`, `sağlamaktadır`) kaynakta zaten bulunan kesin ilişkiyi mi örtüyor; niteleyici (`güçlü biçimde azaltmak`) ölçülebilir mi? Anlam değişmiyorsa alışılmış eşleşmeyi seç; hâl değişimi ilişkiyi değiştirebilir ("gürültüden etkilenmez" ile "gürültüyü etkilemez" iki ayrı önermedir). Ad gerçek bir süreç ya da prosedürse ("risk değerlendirmesi yapmak") bırak. Eşdizim ile klişeyi ayır: eşdizim geçişi "yerli ve kesin mi", retorik geçişi "boş mu" diye sorar.

**Sözcüksel kalkıyı denetle.** Birleşim dil bilgisel olsa bile İngilizce kaynak fiilin ya da adın varsayılan Türkçe karşılığını taşıyorsa alanın yerleşik kullanımını ve Türkçenin doğal eşdizimini denetle: `framework→çerçeve`, `campaign→kampanya`, `provide→sağlamak`, `perform→gerçekleştirmek`, `capture→yakalamak`, `address→adreslemek`, `exhibit→sergilemek`, `experience→deneyimlemek`, `enable→mümkün kılmak` eşleşmelerini otomatik kabul etme. Sor: anadili Türkçe bir uzman, İngilizce özgün cümleyi hiç görmeseydi bu ilişkiyi bu sözcüklerle mi kurardı? Karar birimi sözcük değil, sözcük + tümleç + bağlam + tür + alandır; tek sözcük yasaklanmaz. Teknik terimi (`referans çerçevesi`, `belleği adreslemek`), gerçek kampanyayı, yerleşik akademik eşdizimi (`hipotezi desteklemek`) ve alan jargonunu yalnızca yabancı kökenli göründüğü için değiştirme. Daha doğal fiil daha güçlü iddia olmasın.

**Sözcük kimliğini koru.** Aynı varlığı `yöntem`, `yaklaşım`, `yapı`, `sistem`, `çözüm` üzerinden kaydırma; yeniden adlandırma yalnızca gerekçeyle olur. `Sonuç / bulgu / çıktı / gözlem`, `hata / sapma`, `amaç / hedef` ayrı kategorilerdir; yeni sözcük tam olarak aynı kategoriyi korumuyorsa terimi değiştirme. Yerleşik terimi, ödünç sözcüğü (`pipeline`, `baseline`), projeye özgü ya da belgede tanımlanmış terimi ve hukuki formülü ("kabul ve taahhüt eder") "Türkçeyi iyileştirmek" için değiştirme; emin değilsen koru. Seyrek birleşim teknik olarak kesin ya da alıntı olabilir; yalnızca ilişki genelse ve alışılmış seçenek varsa müdahale et. Resmî türe konuşma eşdizimi, kişisel yazıya kurumsal eşdizim dayatma.

## Metinsel tutarlılık ve konu ilerleyişi

İyi cümlelerden kurulu bir metin yine de bir düşünceyi geliştiremeyebilir. Hedef her paragrafı pürüzsüzleştirmek değil; okurun her cümlenin öncekini neden izlediğini anlayabilmesidir. Katalog [Metinsel tutarlılık](references/metinsel-tutarlilik.md) dosyasındadır.

**Her cümle öncekinden büyür.** Ardışık her cümle çiftinde sor: hangi bilgi taşındı, hangi yeni bilgi girdi, ikisini hangi ilişki bağlıyor, okur bunu etiket olmadan çıkarabilir mi? Olgu yığını paragrafında olguları otomatik olarak yeniden sıralama; önce her olgunun işlevini (mimari, düzenek, değerlendirme, sonuç) belirle, sonra yalnızca müdahale düzeyi izin veriyorsa grupla. Paragrafın sonu bir sonrakinin doğal başlangıcını kursun; iyi köprü ilişkiyi bilgiye gömer, duyuru yapmaz. Her bölümde "Bu çalışmada ..." ile düzeneği yeniden tanıtma; çok uzun belgede gerekli yeniden yönlendirmeyi mesafeye göre koru. Aynı önerme yeni bir rol (ölçüm, yorum, sınırlı öneri) kazanıyorsa yinelenebilir; kazanmıyorsa hacim yinelemesidir.

**Bağlaç ilişki kuramaz.** "Sonuçlar hata oranının düştüğünü göstermiştir. Bu nedenle modelin genellenebilirliği yüksektir" cümlesinde bağlaç var, mantık yok. Her açık bağlaç için bağlacı kaldır ve ilişkinin hâlâ geçerli olup olmadığına bak; değilse ilişki desteksiz mi, öncül eksik mi, bağlaç yanlış mı? Eksik öncülü uydurma; kaynağın kurduğu nedensel bağlacı da silme. Kronolojiyi, önce–sonrayı ve neden–sonucu ayrı tut. Sonuç olarak başlayıp sessizce öneriye dönüşen paragrafta öneri statüsü kaynaklı mı diye sor; köprüyü uydurma.

**Gönderge, kapsam ve olumsuzluk yerinde kalır.** `Bu`, `bu durum`, `söz konusu` göndergesinde kaç rakip öncül olduğunu ve kaç cümle uzakta olduğunu sor; başlık değişimi, birkaç rakip varlık, liste ya da tablodan sonra açık yeniden tanıtım yararlıdır. `Yalnızca`, `özellikle`, `en az`, `bile`, `de/da` ve olumsuzluk (`değil`, `yok`, `hiçbir`, `henüz değil`) varken agresif yeniden sıralama yapma; işareti taşımadan önce hangi ögeyi sınırladığını belirle. "Model hatayı azaltmadı; yalnızca varyansı düşürdü" birleştirilirken "Model yalnızca hatayı azaltmadı ve varyansı düşürdü" olmaz. Belge akademik, bürokratik, sohbet ve tanıtım kayıtları arasında gerekçesiz geçiş yapmasın; alıntı, uyarı ve örnek gibi bilinçli yerel değişimi düzleştirme. Noktalama Türkçe söz dizimsel gruplamayı yansıtsın: özne ile yüklem arasına virgül, uzun çizgi ve ara söz yığını incelenir, ondalık listedeki noktalı virgül gibi teknik noktalama korunur. İddia ile kanıtı, sınırlılık ile sınırlanan iddiayı, öneri ile gerekçeyi yakın tut.

## Yazarın sesini eşle

Kullanıcı bir yazı örneği verdiyse ortalama cümle uzunluğunu ve değişimini, sık kullandığı doğal bağlaçları, kişi tercihini, teknik terim yoğunluğunu, noktalama alışkanlığını, resmiyet ve doğrudanlık düzeyini, mizah, çekince ve kişisel yorum biçimini, paragraf ve bölüm ölçeğini çıkar. Örnekteki yazım yanlışlarını, dil bilgisi hatalarını ve tesadüfi tekrarları üslup özelliği olarak taklit etme. Yazarın özgün ama alışılmadık ifadesini türdeş bir cilaya indirgeme.

## Terim ve gösterim tutarlılığı

Uzun veya teknik metinde sessizce bir terim ve gösterim listesi oluştur: tanımlanmış teknik terimler, kısaltmalar ve ilk açılımları, değişken, sembol ve denklem adları, başlık ve bölüm numaraları, ürün, yöntem ve model adları, büyük-küçük harf tercihleri. Aynı kavramı sırf tekrar olmasın diye farklı terimlerle adlandırma. Kaynakta ayrı anlam taşıyan iki terimi tek terimde birleştirme. Sembol, indis, birim ve işaretleri değiştirme. Bölümleri birleştirirken bölüm numaralarına bağlı göndermeleri güncelle veya kullanıcı numaralı yapıyı koruyorsa birleştirmeden vazgeç.

## Rapor bütünlüğünü koru

Metin bir rapor, inceleme notu, değerlendirme belgesi veya yönetici özetiyse yalnızca cümleleri değil, kanıt zincirini de koru.

- Her bölümün ve paragrafın işlevini sessizce belirle: bağlam, amaç, kapsam, yöntem, bulgu, yorum, sınırlılık, öneri veya karar.
- Bulguyla yorumu, yorumla öneriyi, öneriyle verilmiş kararı tek statüde birleştirme. Kaynakta aralarındaki sınır bulanıksa düzenleme sırasında kesinleştirme.
- İddia ile onu destekleyen sayı, alıntı, tablo, kaynak işareti ve sınırlılığı birbirinden uzaklaştırma; yapı dışarıdan dayatılmamışsa yaklaştır.
- Bir verinin neyi gösterdiğini açıklaştırabilirsin; kaynakta bulunmayan neden, önem, risk veya sonuç ekleme.
- Öneriyi gerçekleşmiş uygulama, hedefi sonuç, beklentiyi taahhüt gibi yazma.
- Yönetici özetinde yalnızca rapor gövdesinde bulunan ana bulgu, sınır ve önerileri kullan. Kullanıcı istemedikçe yeni yönetici özeti üretme.
- Tablo ve şekil adlarını, bölüm numaralarını ve çapraz göndermeleri koru. Başlıkları yalnızca kullanıcı isterse, derin düzeyde kavramsal sınır gerektiriyorsa veya başlık içerikle açıkça çelişiyorsa değiştir.
- Profesyonel tonu bürokratik dolguya dönüştürme. Aktör biliniyorsa açık özne ve somut fiil kullan; bilinmiyorsa aktör uydurma.
- Daha akıcı olsun diye önemli tekrarları silme. Bir terim, kapsam veya sınırlılık okurun yanlış anlamasını önlüyorsa tekrar işlevseldir.

Rapor düzenlemesinden sonra bulgu–yorum–öneri sınırlarını, bölüm içi dayanakları ve bölümler arası sayı, tarih, terim ve kesinlik tutarlılığını ayrıca denetle. Ayrıntı için [Rapor yazımı](references/rapor-yazimi.md) dosyasını oku.

## Çalışma yöntemi

**1. Envanter çıkar.** Metnin türünü, amacını, muhatabını, yapısal ölçeğini, müdahale düzeyini ve korunacak unsurları belirle. Sayı, tarih, özel ad, alıntı, kaynak işareti, kapsam belirleyicisi, terim, sembol, bölüm numarası, temel iddiaları ve her iddianın epistemik statüsünü zihinsel bir kontrol listesine al.

**2. Sorun kümelerini bul.** En baskın sorunları belirle: kalıp ve ritim; retorik dolgu (önem, savunma, tekrar, yol haritası, kalıp giriş ve sonuç); yapısal parçalanma; çeviri kokusu; epistemik kayma; eşdizim ve istem; tutarlılık. Tek bir işaretten "AI metni" veya "çeviri" sonucu çıkarma.

**3. Düzenle.** Seçilen müdahale düzeyinde düzenle. Komşu cümleleri ve komşu bölümleri birlikte değerlendir; bir cümledeki değişiklik sonraki cümlenin öznesini, zamanını veya mantıksal bağını, bir bölüm birleştirmesi göndermeleri ve numaraları bozmasın. Raporlarda bölümün işlevini ve bulgu–yorum–öneri sınırını koru.

**4. Kaynak karşılaştırması yap.** Son metindeki her sayı, tarih, özellik, sonuç, nedensellik, karşılaştırma, olumsuzluk, koşul, istisna, nicelik sınırı, terim, gösterim ve kişisel ayrıntının kaynakta karşılığını bul; her iddianın kaynağı, statüsü ve kesinlik düzeyi aynı mı? Karşılığı yoksa çıkar veya kaynak metnin izin verdiği kesinlik düzeyine döndür.

**5. Yapay düzyazı, yapı, çeviri kokusu, kanıt, sözcük ve tutarlılık denetimi yap.** Metni teslim etmeden önce sessizce dokuz geçiş yap:

- **A. Kalıp:** klişe, reklam dili, tiyatral çerçeve, sohbet botu kalıntısı, belirsiz otorite, çeviri kokusu.
- **B. Cümle:** her cümle için "bunu silersem hangi bilgi kaybolur?"; gereksiz önem, açık olanın açıklaması, sahte karşıtlık, savunmacı gerekçe, soyut açımlama, yol haritası dili, uzun çerçeve.
- **C. Paragraf:** farklı önerme sayısı, mini sonuç, döngüsel açıklama, zorlama denge, erken bölünme, tutarlı hareket.
- **D. Belge:** tekrarlanan giriş ve sonuçlar, tek biçimli paragraf mimarisi, aynı gerekçenin tekrarı, yazarın sesini silen türdeş cila.
- **E. Yapı:** başlık sayısı ve derinliği, tek paragraflık bölümler, kopmuş yakınlık, çapraz gönderme sıklığı, yapay gerilim, gereksiz liste, mini giriş-sonuç; yapısal sınırlar kavramsal sınırlardan sık mı?
- **F. Çeviri kokusu:** yinelenen açık özne ve `bu + ad`; çekimli cümle zinciri ve fiilimsi dengesi; art niteleme ve `olan` zinciri; çerçeve yığını; `sahip olmak` ve `bulunmaktadır`; konu–odak sırası; yerli kaynak kullanımı; aşırı düzeltme.
- **G. Kanıt ve kesinlik:** her iddianın kaynağı ve statüsü; gözlem–çıkarım–olgu–nedensellik düzeyi; edilgen–etken dönüşümü ve aktör; atıf mesafesi; çekince–pekiştirici dengesi; kip bakış açısı; bölümler arası kesinlik; öneri–karar–uygulama; "gözlenmedi" ile "yoktur".
- **H. Sözcük uyumu:** eşdizim; hâl ve tümleç; edat izi; hafif ve genel fiil; eş anlamlı kayması; varlık adlandırma; seyrek ama geçerli birleşim.
- **I. Metinsel tutarlılık:** cümleler arası devir; olgu yığını; bağlaç geçerliliği; gönderge mesafesi; kapsam ve olumsuzluk bağlanması; kayıt; noktalama; iddia–dayanak yakınlığı.
- **J. Zamansal ankraj:** pasajın baskın ankrajı; her yüklemin olay statüsü; zamansal sürtünme ve genel kip doygunluğu; güncel durum, güncel yorum ve belgenin güncel işlevi zamansız geniş zamanda mı donmuş; kip değişiminin önermeyi genelleştirip daraltmadığı; geçmişe, `-miştir` ya da `-yor` biçimine zorlama.

Çıkardığın hiçbir şeyi daha sakin eş anlamlılarla geri koyma. Sonucu insanileştirmek için hata, argo, rastgelelik veya cümle uzunluğu gürültüsü üretme.

**6. Ses ve akış denetimi yap.** Metni bir kez anlam, bir kez doğal duraklar için oku. Her cümlenin öncekiyle ilişkisi açık mı? Yazarın tavrı, iletişim amacı veya yapısal ölçeği kaybolmuş mu? Özgün fakat doğal ifadeler yanlışlıkla düzleştirilmiş mi? Kullanıcının istediğinden fazla değişiklik yapılmış mı? Gerekli bir sınırlılık, koşul, kesinlik işareti, öğretici açıklama, tekrarlanabilirlik adımı veya gezinme başlığı dolgu sanılıp silinmiş mi? Raporda bulgu, yorum, sınırlılık, öneri veya karar yanlışlıkla birbirine dönüşmüş mü? Metin Türkçe düşünülmüş gibi okunuyor mu; her iddia kaynaktaki kişiye, kanıt statüsüne ve kesinlik düzeyine hâlâ bağlı mı; her cümle öncekinden yararlı bir şey alıp sonrakine yararlı bir şey bırakıyor mu?

## Referans yönlendirmesi

- Klişe, yapay ritim, gereksiz resmiyet, reklam dili veya çeviri kokusu baskınsa [Türkçe örüntüler](references/turkce-oruntuler.md).
- Cümleler doğru olduğu hâlde metin yapay okunuyorsa; önem cümleleri, savunmacı açıklama, tekrar döngüleri, yol haritası, kalıp giriş ve sonuç, soyut yüklem veya tek biçimli paragraf mimarisi varsa [Retorik yapılar](references/retorik-yapilar.md).
- Metin çok başlıklı, kısa paragraflı, sık çapraz göndermeli veya yapay gerilimliyse; bölümler birleştirilecek ya da korunacaksa [Yapısal bütünlük](references/yapisal-butunluk.md).
- Paragraf kopuksa, göndergeler belirsizse veya okuma akışı takılıyorsa [Akıcı Türkçe](references/akicilik.md).
- Metin çeviri gibi okunuyorsa; açık özne, `bu sonuç`, `ve` zinciri, `sahip olmak`, `olan` zinciri, çerçeve yığını, fazla `bir` ya da uzak yüklem ritmi varsa [Türkçe ritim ve çeviri kokusu](references/turkce-ritim-ve-ceviri-kokusu.md).
- Aktarım, çıkarım, çekince, pekiştirici, edilgen çatı, kip değişimi, öneri–karar–uygulama statüsü ya da bölümler arası kesinlik söz konusuysa [Kanıt ve kesinlik](references/kanit-ve-kesinlik.md).
- Tamamlanmış iş zamansız-genel kiple anlatılıyorsa; `bu çalışma inceler` ritmi, tarihli olayda geniş zaman, yöntem tanımı ile uygulama karışması ya da geçmişe zorlama varsa [Zamansal ankraj ve rapor kipi](references/zamansal-ankraj-ve-rapor-kipi.md).
- Sözcükler tuhaf birleşiyorsa; hafif fiil, yanlış hâl, edat izi, eş anlamlı kayması ya da terim kararsızlığı varsa [Sözcük birleşimleri](references/sozcuk-birlesimleri.md).
- Paragraflar iyi olduğu hâlde metin bir düşünceyi geliştirmiyorsa; olgu yığını, desteksiz bağlaç, uzak gönderge, kapsam ya da olumsuzluk kayması, kayıt kayması ya da noktalama yükü varsa [Metinsel tutarlılık](references/metinsel-tutarlilik.md).
- Metin rapor, inceleme notu veya yönetici özeti ise [Rapor yazımı](references/rapor-yazimi.md).
- Kullanıcı açıkça temel bir kavrama giriş yazılmasını istiyorsa [Kavramsal girişler](references/kavramsal-girisler.md).
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
