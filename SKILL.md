---
name: metinoskop
description: Türkçe metni net ve anlaşılır kılar; her önermeyi bir kez, doğru yerde ve kaynağın kesinliğiyle söyletir. Omurgası ASD-STE100 yazım ilkelerinden uyarlanmıştır (bir paragraf bir konu, kısa ve doğrudan cümle, bir terim bir anlam, şişirme ve döngüsel anlatım yok). Öncelikli alan bilimsel ve teknik metindir (makale, tez, rapor, teknik belge, README); kurallar her konuda geçerlidir. Metni belge, paragraf, cümle ve sözcük katmanlarında birlikte okur; sorunları kendisi teşhis edip düzeltir, kullanıcıya seçenek sunmaz. Olguları, sayıları, kanıt statüsünü ve yazarın tavrını korur. Türkçeye çevrilmiş metin için de kullanılır. Türkçe bir metin verilip yalnızca "geliştir", "iyileştir", "düzelt", "toparla", "akıcı yap", "AI slop gibi", "yapay duruyor", "netleştir", "sadeleştir", "doğal Türkçe yap", "çeviri gibi durmasın" dendiğinde kullan.
---

# Metinoskop

Türkçe metni net ve anlaşılır yap: okur her önermeyi bir kez, doğru yerde, kaynağın verdiği kesinlikle bulsun. Bu konu ne olursa olsun geçerlidir. Omurga, ASD-STE100'ün (Simplified Technical English) yazım ilkelerinden Türkçeye uyarlanmıştır; sözlüğü ve İngilizceye özgü dil bilgisi kuralları alınmamıştır. Netlik hiçbir zaman kaynak sadakatinin, kanıt statüsünün ya da kesinliğin önüne geçmez. Bu dosya ilkeleri ve karar noktalarını verir; katalog, örnek ve karşı örnekler `references/` altındadır.

## Kural önceliği

Çatışma olduğunda şu sırayı uygula:

1. Kullanıcının açık talebi ve belirttiği kapsam
2. Kaynak metindeki olgular, iddialar, belirsizlikler ve yazar tavrı
3. Kullanıcının sağladığı üslup örneği
4. Metnin iletişim amacı, türü ve muhatabı
5. Bu skill'deki netlik omurgası ve genel dil tercihleri

Bir alt sıradaki kural, üst sıradakini bozmasın.

## Görevin sınırı

- Mevcut metnin dilini, paragraf akışını ve gerekiyorsa bölüm yapısını düzenle. Kullanıcı açıkça kaynak bilgilerden bir giriş istemedikçe yeni bölüm üretme.
- Yeni olgu, tarih, sayı, alıntı, kaynak, özellik, sonuç, deneyim veya kişisel görüş üretme.
- Kaynak dilden Türkçeye çeviri yapma; Türkçeye çevrilmiş mevcut metni düzenle.
- Alıntıları, kodu, URL'leri, dipnotları, kaynak işaretlerini, tablo hücrelerini ve Markdown yapısını koru. Başlık hiyerarşisini yalnızca yapısal düzenleme istendiğinde ya da derin düzeyde, kavramsal sınırlara göre değiştir.
- Anlatı metninde olay sırasını, sahneyi, bakış açısını ve sonucu değiştirme.
- Bir metnin herhangi bir AI dedektöründen geçeceğini vaat etme; dedektör için hata veya yapay çeşitlilik üretme.

## Bağlamı çıkar

Yazmadan önce sessizce belirle: **tür** (bilimsel, teknik, rapor, kurumsal, gündelik ya da kenar tür); **amaç** (bilgi, açıklama, talimat, ikna, kayıt); **muhatap** (uzman, genel okur, yeni başlayan); **yapısal ölçek** (yazarın paragraf ve bölüm ölçeği, dışarıdan dayatılmış yapı); **istenen değişiklik** (yalnızca belirtilen sorun mu, genel editörlük mü); raporsa her bölümün **işlevi** (bağlam, yöntem, bulgu, yorum, sınırlılık, öneri). Muhatabın bilgi düzeyi hangi açıklamanın gerekli, hangisinin dolgu olduğunu belirler.

**Kenar türler ayrı tutulur.** Hukuki metin, tanıtım ve pazarlama, deneme, köşe yazısı ve sosyal medya, kişisel yazışma, edebî metin ve üslup eşleme için ek kurallar [Kenar türler](references/kenar-turler.md) dosyasındadır. Metin bu türlerden biri değilse o dosyayı okuma ve oradaki istisnaları (hukuki kalıp, ikna amacı, yazara özgü imge) bilimsel ya da teknik metne taşıma. Bilimsel metindeki alıntılanmış yasa maddesi ya da formül alıntı kuralıyla korunur.

## Kısa talep, tam iş

Kullanıcı çoğu zaman yalnızca "bunu geliştir", "çok AI slop gibi", "toparla" der. Bu, eksik talimat değil, tam yetkidir: düzey, kapsam, ton ya da hangi sorunun düzeltileceğini sorma. Metni bütüncül oku (aşağıdaki bölüm), sorunları kendin teşhis et, düzeyi teşhise göre seç ve tek bir son metin ver.

- **Düzeyi teşhis seçer.** Varsayılan standarttır. Teşhis yapısal parçalanma gösteriyorsa (dağılmış konu, tek paragraflık bölümler, ilk cümleyi yineleyen başlıklar) derin düzeyin yapı kurallarını yalnızca o bölümlere uygula. Dışarıdan dayatılmış yapı her durumda korunur.
- **Seçenek sunma.** Alternatif sürüm, "şunu da ister misiniz" teklifi, düzey menüsü ya da soru listesi ekleme. Kullanıcı tek metin istedi, tek metin ver.
- **Yalnızca anlam gerektirirse sor.** Soru, düzenlemenin kaynakta olmayan bir yorum seçmeyi gerektirdiği durumla sınırlıdır (bkz. **Belirsizlik ve yorum seçimi**). Üslup ya da yapı tercihi soru gerekçesi değildir; bunları bu dosyanın kuralları belirler.
- **Açık talep önceliklidir.** Kullanıcı belirli bir sorun ya da düzey söylediyse bu bölüm değil, o talep geçerlidir.

## Bütüncül düzenleme

Tek başına kusursuz bir cümle, paragrafında yanlış yerde durabilir; doğru yerdeki bir cümle de komşusuyla aynı sözcüğü tekrarlayabilir. Bu yüzden metni cümle cümle değil, dört katmanı birlikte düşünerek düzenle: **belge** (konular nerede açılıyor, hangi sırayla), **paragraf** (tek konu, cümlelerin rolü ve sırası, komşu paragraflarla bağ), **cümle** (önerme, yapı, uzunluk), **sözcük** (eşdizim, terim, yakın tekrar).

**Yukarıdan aşağı teşhis, aşağıdan yukarı doğrulama.** Önce belgeyi ve paragrafları teşhis et, sonra cümle ve sözcüğe in. Her cümle düzeltmesinden sonra paragrafı yeniden oku: devir bozuldu mu, aynı bağlayıcı ya da fiil komşu cümleye mi geçti, düşürülen özne belirsizlik mi yarattı? Her paragraf değişikliğinden sonra belgeyi yeniden oku: bir konu başka yerde hâlâ açılıyor mu?

**Paragraf testi.** Her paragraf için sessizce sor:

1. Paragrafın özünü tek cümleyle söyleyebiliyor musun? Söyleyemiyorsan paragraf iki konu taşıyor ya da bir konuyu bitirmiyor.
2. Her cümlenin bu paragraftaki rolü ne: iddia, kanıt, yorum, sınırlılık, örnek, geçiş? Rolü olmayan cümle silinir; rolü başka paragrafta olan cümle oraya taşınır.
3. Roller doğru sırada mı? Bilinen bilgi yeni bilgiden önce gelir; iddia ile kanıtı, sonuç ile sınırlılığı bitişik durur; sonucu açıklamadan sınırlılığa geçilmez.
4. Paragrafın ilk cümlesi öncekinin son cümlesinden doğal olarak çıkıyor mu?
5. Cümleler arası bağ, Türkçenin bağlayıcı kaynaklarıyla mı kurulmuş, yoksa her cümle aynı etiketle mi açılıyor; aynı fiil ya da sıfat peş peşe mi geliyor?

**Yerinde olmayan cümle yeniden yazılmaz, taşınır.** Bir cümle doğru ama yanlış yerdeyse çözüm sözcüklerini değiştirmek değil, onu ait olduğu paragrafa ya da konuma taşımak, ilişkili cümleyle birleştirmek ya da rolü yoksa silmektir. Taşımanın da göndermeleri, numaraları ve dışarıdan dayatılmış bölüm ayrımını bozmaması gerekir.

**Değişiklik bütçesi katmanlarda da geçerlidir.** Bütüncül okumak, her katmanda bir şey değiştirmek demek değildir. Teşhis bir katmanda sorun bulmuyorsa o katmana dokunma.

## Netlik omurgası

Yedi kural, STE100'ün yazım kurallarından Türkçeye uyarlanmıştır. Sayısal eşikler (cümle başına sözcük, paragraf başına cümle, ad öbeği uzunluğu) inceleme işaretidir, kesme kuralı değildir: tek bir ilişkiyi taşıyan uzun cümle ve tek hareketi yürüten uzun paragraf korunur. Uyarlamanın gerekçesi, STE100 ile eşleme tablosu ve örnekler [Netlik omurgası](references/netlik-omurgasi.md) dosyasındadır.

**1. Bir paragraf, bir konu.** Her paragraf tek bir konuyu ya da tek bir düşünce hareketini (iddia → kanıt → yorum, ölçüm → sınırlılık) taşır; konu, paragrafın başında belli olur. Söylem işlevi sert biçimde değişiyorsa (bulgu → öneri, yöntem → sonuç) yeni paragraf açılır. Aynı konu belgenin birkaç yerine dağılmışsa onu tek yerde topla; okur bir konuyu bitirmeden ondan ayrılmamalı, bitirdiği konuya geri çağrılmamalıdır. Altı cümleyi aşan paragrafta iki konu olup olmadığına bak; tek hareketse bölme.

**2. Her önermeyi bir kez söyle.** Döngüsel anlatımı kaldır: olgu → aynı olgunun başka sözcüklerle tekrarı → genel önem cümlesi → soyut mini sonuç dizisini, kaynağın kurduğu önermeye indir. Aynı önermenin girişte, bölüm başında, sonuçta ve özette yeniden açımlanmasını; terimi kendisiyle tanımlayan döngüsel tanımı (`kalibrasyon, ölçümlerin kalibre edilmesidir`); sözcükleri farklı, işlevi aynı cümleleri (`Bu sonuç önemlidir`, `Bu bulgu dikkat çekicidir`) ara. Yinelenme yalnızca önerme yeni bir rol kazandığında (ölçüm → yorum → sınırlı öneri) ya da çok uzun belgede mesafe gerektirdiğinde meşrudur. Terimin kendisini yinelemek tekrar değildir (kural 5).

**3. Yalnızca gerekli bilgiyi yaz.** Her cümle yeni bir olgu, gerekli bir nitelendirme, açık olmayan bir mantıksal ilişki, kaynağın desteklediği bir yorum, yorumu değiştiren bir sınırlılık ya da önceki bilgiyi birleştiren bir sentez taşır. Silme testi: cümleyi çıkarınca önermeler, akıl yürütme, kronoloji, yorum veya yazar tavrı değişiyor mu; değişmiyorsa cümle bilgiyi birleştiriyor ya da okurun çıkarım yükünü azaltıyor mu? İkisine de hayırsa sil. Bu sınıfa girenler ve tanıları aşağıdaki **Şişirme kataloğu** bölümündedir.

**4. Kısa ve doğrudan cümle.** Bir cümle bir ana önerme ya da bir ilişki taşır; talimatta bir cümle bir adımdır. İlgisiz önermeleri tek cümleye yığma, yapay olarak parçalanmış tek düşünceyi de birleştir: ölçüt cümle sayısı değil kavramsal birliktir. 25 sözcüğü aşan betimleyici cümle ve 20 sözcüğü aşan talimat cümlesi incelenir. Uzun biçimi aynı anlamı taşıyan kısa biçimle değiştir (`bir değerlendirme yapılması gerekmektedir` → `değerlendirilmelidir`). Yığılmış çerçeveyi, isim-fiil zincirini ve üçten uzun ad ya da iyelik zincirini çöz. Kısaltmak için cümle ögesi düşürüp telgraf diline inme.

**5. Bir terim, bir anlam.** Bir kavrama bir ad ver ve metin boyunca onu kullan; aynı varlığı `yöntem`, `yaklaşım`, `yapı`, `sistem` arasında kaydırma, aynı sözcüğü iki ayrı anlamda kullanma. Kısaltmayı ilk geçtiği yerde aç, sonra tutarlı kullan. Sembol, birim, değişken ve bölüm numaralarını değiştirme. Kaynakta ayrı anlam taşıyan iki terimi birleştirme. Aynı terimi sırf tekrar olmasın diye eş anlamlıyla değiştirme.

**6. Somut özne, somut yüklem.** Aktör biliniyor ve ilgiliyse etken çatı ve somut fiil kullan. Talimat ve prosedürde etken çatı ya da emir kipi tercih edilir. Bilimsel betimlemede edilgen çatı yöntem merkezli kaydı ve konu sürekliliğini taşıyorsa meşrudur. Edilgenliği yalnızca aktör belli diye etkene çevirme; kaynağın adlandırmadığı aktörü uydurma. `ortaya koymak`, `rol oynamak`, `katkı sağlamak`, `ışık tutmak` gibi soyut yüklemlerde hangi somut ilişkinin kodlandığını sor ve onu yaz; daha somut fiil kaynağın kurmadığı nedenselliği kurmasın. Tekrarlanan `bu durum`, `bu yaklaşım`, `söz konusu süreç` öznelerini somut göndergeye çöz ya da cümleyi sil.

**7. Yapı okura hizmet eder.** Başlık hakkını kazanmalıdır: büyük kavramsal geçişi işaretler, uzun belgede gezinmeyi sağlar ya da dışarıdan dayatılmış yapıyı yansıtır. Altında tek kısa paragraf olan, ilk cümleyi yineleyen ya da simetri için kurulan başlıklar birleşir. Liste yalnızca gerçekten paralel ögeler ve sıralı adımlar içindir; `bu nedenle` ile birbirine bağlanan maddeler zincirdir, düzyazıya döner. İddia ile kanıtı, sonuç ile sınırlılığını, ölçüm ile yorumunu ayrı bölümlere dağıtma. Görsel parçalanmayı açıklık sanma; parçalanmayı tek dev paragrafla da çözme.

## Şişirme kataloğu

Hiçbir klişe sözcük içermeyen metin, her olgudan sonra önem cümlesi kuruyor ve her bölümü duyuruyla açıyorsa yine şişkindir. Sözcük tek başına yasak değildir; yargı birimi sözcüğün bağlamdaki işlevidir. `ancak`, `bu nedenle`, `önemli`, `göstermektedir`, edilgen çatı, `-maktadır`, üçlü liste, retorik soru, alt başlık, madde işareti, akademik ihtiyat, `bir`, `olan`, `ve`, `açısından`, `sahip olmak`, `bulunmaktadır` ve `olabilir` gibi çekinceler incelenir ama otomatik silinmez. Katalog ve karşı örnekler [Retorik yapılar](references/retorik-yapilar.md) dosyasındadır.

**Dolguyu başka dolguya çevirme.** Kesin kural: önem şişirmesi, retorik çerçeve, savunmacı açıklama, boş geçiş veya kalıp sonuç çıkarılırken aynı işlev daha sakin eş anlamlılarla korunmaz. `çığır açan sonuç` → `oldukça önemli sonuç`, `bu noktada vurgulamak gerekir` → `burada belirtmek gerekir` yanlıştır. Cümlenin bağımsız bilgi işlevi yoksa sil; varsa yalnızca o bilgiyi bırak. "Model 120. derecede en düşük hatayı verdi. Bu sonuç, yöntemin anlaşılması açısından önemli bir bulgudur" örneğinde ikinci cümle silinir, "ışık tutmaktadır" diye yeniden kurulmaz.

**Üretilmiş önem.** `... açısından önemlidir`, `kritik rol oynamaktadır`, `değerli içgörüler sunmaktadır`, `literatürdeki boşluğu doldurmaktadır` kaynak gerekçelendirmiyorsa çıkar; somut sonucun kendisini bırak. Kaynak önemi dayanağıyla kuruyorsa tam o güçte koru. Bir kişiye ya da kuruma atfedilmiş açık değerlendirme (`Bu proje bizim için bir dönüm noktasıdır`) yazar tavrıdır, korunur. Her konuya yapıştırılabilen hazır imge ve formül (`kilit rol`, `temel taşı`, `X'ten çok daha fazlası`) önerme değil ambalajdır: önermeyi aynı güçte yalın sözcüklerle bırak, ambalajı at.

**Savunmacı düzyazı.** `Burada amaç ... değildir`, `Bu tercih tesadüfi değildir`, `Bu durum bir eksiklik olarak görülmemelidir` için sor: okurun hangi somut yanlış anlamasını önlüyor? Cevap yoksa çıkar. Tercih değiştiğinde yorum, tekrarlanabilirlik veya geçerlilik değişecekse yöntem gerekçesi meşrudur; somut dayanağıyla koru. Olağan bilimsel uygulamayı önceden savunma; uzman okura olağan olanı açıklama. Yeni başlayana yazılmış öğretici açıklamayı silme; muhatap belirsizse koru.

**Üretilmiş karşıtlık ve zorlama denge.** `X değil, Y`, `Asıl mesele X`, `yalnızca ... değil, aynı zamanda ...` karşıtlığı reddedilen taraf kaynakta yoksa kurma. Her iddiaya karşı iddia ekleme; `güçlü olmakla birlikte bazı sınırlamaları da vardır` adlandırılmış sınırlılık yoksa çıkar. Kanıt düzeyini bildiren çekince (`çalışma gözlemseldir`) denge değil kesinlik bilgisidir, korunur.

**Okur yönlendirmesi ve sarmalayıcı.** `Bu bölümde ... ele alınacaktır`, `Şimdi ... bakalım`, `Bu noktaya daha sonra döneceğiz`, `Bu sorunun yanıtı bir sonraki bölümde görülecektir`, `Sonuç olarak bu bölüm X'in önemini ortaya koymaktadır` gibi duyuru, askı ve kapanışları sil; ilişkiyi ya da olguyu doğrudan söyle. Yol haritası uzun ve yapısı zor belgede, genellikle bir kez meşrudur. `Yukarıda belirtildiği gibi` sıklığı ve her bölümde düzeneği yeniden tanıtma metnin yanlış bölündüğünü gösterir; birleştir ya da yeniden sırala. Tablo, şekil, ek ve kaynak göndermeleri korunur.

**Kalıp giriş ve kalıp sonuç.** Giriş hunisini (geniş dünya → hızla değişen ortam → `giderek önem kazanıyor` → `bu nedenle`) at; kaynaktaki somut nedenle başla. Sonuç bölümü sentez yapabilir, özeti ya da girişi başka sözcüklerle tekrar edemez. Metin akademik diye `gelecek çalışmalar` cümlesi ekleme.

**Yapay gerilim.** Bilgi veren metinde `Ancak burada işler değişmektedir`, `İşin ilginç yanı`, `Daha da önemlisi` gibi momentum kalıplarını sil; gerçek karşıtlığı nicel olarak doğrudan yaz (`Yöntem kuvvet hatasını düşürdü ama yedi günlük konum hatasını artırdı`). Yeni paragraf başlıyor diye `Bununla birlikte`, `Bu doğrultuda` ekleme.

**Paragraf simetrisi.** Her paragrafın konu cümlesiyle açılıp mini sonuçla kapanması, eşit uzunlukta paragraflar ve tekrarlayan "nokta → açıklama → sonuç" mimarisi yapaylık işaretidir. Uzunlukları rastgeleleştirme; paragraf boyutunu bilgi yapısı belirlesin.

## Değişmezler: netlik kesinliği bozmaz

Netleştirme olguyu, kapsamı ve kanıt statüsünü değiştiremez. Kısaltırken, birleştirirken ya da somutlaştırırken bu bölüm her netlik kuralının üstündedir.

**Kaynak sadakati.** Önermeleri sessizce ayır: olgu veya ölçüm; amaç, plan veya vaat; görüş ya da değerlendirme; duygu veya kişisel tavır; belirsizlik ve çekince; tekrar ve dolgu. İlk beşinin anlamını ve kesinliğini koru, sonuncusunu başka sözcüklerle yeniden üretme. Hedefi sonuç, değerlendirmeyi ölçüm, kronolojiyi nedensellik gibi yazma; ilişkiye etki iddiası ekleme. Karşılaştırma zemini yoksa `daha`, ölçüt yoksa `en` ekleme. Olumsuzluğu, istisnayı, koşulu ve nicelik sınırını koru: `bazı` → `tüm`, `en az` → kesin sayı, `yalnızca` → genel kapsam olmaz; `henüz`, `artık`, `genellikle` dolgu değildir. Kaynaktaki sayılardan oran, fark veya ortalama türetme.

**Belirsizlik ve yorum seçimi.** Bir ifade birden fazla makul yoruma açıksa anlamı kendin seçme. Belirsizlik korunarak düzenleme yapılabiliyorsa koru; düzenleme yorum seçmeyi gerektiriyorsa kullanıcıya sor. Belirsiz göndergeyi açıklaştırırken kaynakta olmayan bir cevap seçme.

**Bilginin kaynağı ve statüsü.** Her önemli önermenin statüsünü belirle: gözlem, ölçüm, aktarım, çıkarım, tahmin, plan, varsayım, yorum. `Gözlendi`, `bildirildi`, `düşündürüyor`, `ölçüldü` farklı statü kodlar; düzenlenmiş cümle aynı düzeyde kalır. Ölçüm, ilişki, çıkarım ve nedensellik dört ayrı düzeydir: rastgele atanmamış iki grup arasındaki fark `etkiler` olmaz. Atıflı iddia (`rapora göre`, `yazarlar öne sürmektedir`) atıflı kalır. Şişmiş iddiayı indirirken yerine olumsuz iddia ya da yeni çekince yazma. Katalog: [Kanıt ve kesinlik](references/kanit-ve-kesinlik.md).

**Çekince kanıttır.** `Olabilir`, `görünmektedir`, `kısmen`, `bu verilerle sınırlı olarak` belirsizlik ya da kapsam kodluyorsa korunur. `Açıkça`, `tartışmasız`, `kanıtlamaktadır` için hangi kanıtın bunu hak ettiğini sor. Kısalık için iddiayı güçlendirme, kontrollü deneyle kurulmuş iddiayı zayıflatma. Kiplik yığınında (`muhtemelen ... olabileceği düşünülebilir`) her işaretin ne kodladığını sor ve gereksizi kaldır.

**Statü zinciri ilerlemez.** Öneri karar, karar uygulama, beklenti taahhüt olmaz. Bir iddia yeni kanıt olmadan sonraki bölümde güçlenemez. `Gözlenmedi` `yoktur`, `sınanmadı` `geçersizdir` olmaz. Bulguyu yoruma, yorumu öneriye çevirme.

**Zamansal ankraj.** Tamamlanmış çalışma, deney ya da süreç `incelendi / kullanıldı / uygulandı` ekseninde anlatılır; açık geçmiş tarih ya da `bu çalışmada` çerçevesiyle zamansız geniş zaman (`inceler / kullanır`) yan yana gelince zamansal sürtünme vardır. Algoritmanın genel davranışı, bilimsel genel ilişki, ürün belirtimi, yeniden kullanılabilir prosedür ve normatif kural geniş zamanda kalır. Güncel durum, okurun önündeki belgenin işlevi ve şu an tartışılan bulgunun yorumu doğal olarak `-yor` alabilir (`Şekil 4 ... gösteriyor`). Kipi çeşitlilik için nöbetleştirme; düzeltmeyi `yapıldı / edildi` ya da `-miştir` zincirine çevirme, tekdüzeliği sözdizimiyle çöz. `-yordu`, `-mıştı`, `-ardı` ilişkilerini ne düzleştir ne uydur. Ayrıntı: [Zamansal ankraj ve rapor kipi](references/zamansal-ankraj-ve-rapor-kipi.md).

## Türkçe doğallık

Netlik İngilizce iskeletle kurulmaz. Hedef, güçlü bir Türkçe yazarın doğrudan Türkçe düşünerek kurabileceği düzyazıdır.

**Çeviri kokusunu ilişkide ara.** Bilgi yapısı, özne kullanımı, yan cümle mimarisi ve bağlaç seçimi İngilizceden miras kalmışsa metin çeviri gibi okunur. Sık işaretler: ardışık cümlelerde yinelenen açık özne; `bu sonuç`, `bu durum` diye yeniden öznelenen önceki önerme; `ve`, `ancak` ile dizilmiş çekimli cümleler; her cümle başında söylem belirteci; `sahip olmak`, `bulunmaktadır` gibi hafif yüklemler; `açısından`, `kapsamında` çerçeve yığını; `olan ... olan` zinciri; her adın önünde `bir`. Sözcükleri bir kez daha çevirme; taşınan ilişkiyi bul ve Türkçenin kaynaklarıyla kur: özne düşürme, eksilti, `-ip`, `-ince`, `-dığından`, `-ken`, `-erek`, önden niteleyen ortaç, iyelik, hâl eki, `de/da`. Şüpheli cümle için yapısal olarak farklı iki seçenek üret, anlamı ve vurguyu en iyi koruyanı seç. Özne iki aktör arasında belirsizlik doğuracaksa açık kalır. Katalog: [Türkçe ritim ve çeviri kokusu](references/turkce-ritim-ve-ceviri-kokusu.md).

**Aşırı Türkçeleştirme.** `İlişkili`yi `neden olur`, `olumsuz etki`yi `bozuldu` yapma. Alan terimini (`parametre`, `pipeline`, `baseline`) öz Türkçe hevesiyle değiştirme. Tek yükleme asılmış dört beş fiilimsi, arkaik sözcük, zorlama deyim ve gereksiz devriklik aşırı düzeltmedir. Akademik metin adlaştırma ve edilgenliğe, teknik belge güvenlik için açık özne yinelemesine hak sahibidir. Peş peşe `-maktadır` yüklemlerini doğal kiplerle sadeleştir ama sırf çeşitlilik için kip değiştirme; teknik işlemi adlandıran isim-fiili koru.

**Eşdizim ve istem.** Şüpheli öbekte sor: bu ad bu fiille normalde kullanılır mı; fiil tümlecini doğru hâlde mi alıyor; İngilizce edat harfiyen ilgeç mi üretmiş (`X hakkında odaklanmak` → `X'e odaklanmak`); hafif fiil (`değerlendirme gerçekleştirmek`) yalın yüklemi mi gizliyor? Hâl değişimi ilişkiyi değiştirebilir (`gürültüden etkilenmez` ≠ `gürültüyü etkilemez`). Gerçek süreç adını (`risk değerlendirmesi yapmak`) bırak. Katalog: [Sözcük birleşimleri](references/sozcuk-birlesimleri.md).

**Sözcüksel kalkı.** `framework→çerçeve`, `provide→sağlamak`, `perform→gerçekleştirmek`, `capture→yakalamak`, `address→adreslemek`, `enable→mümkün kılmak` eşleşmelerini otomatik kabul etme; sor: anadili Türkçe bir uzman, İngilizce cümleyi görmeden bu ilişkiyi bu sözcüklerle mi kurardı? Karar birimi sözcük + tümleç + bağlam + alandır; teknik terimi (`referans çerçevesi`, `belleği adreslemek`), yerleşik akademik eşdizimi (`hipotezi desteklemek`) ve alan jargonunu yabancı kökenli göründüğü için değiştirme. Daha doğal fiil daha güçlü iddia olmasın.

**Anlamı değiştiren kalkıyı her düzeyde düzelt.** Bazı kalkılar okura başka bir önerme verir: `bulgular ... olduğunu önermektedir` (→ `düşündürüyor`), `yazarlar ... olduğunu tartışmaktadır` (→ `savunuyor`), `deney Mart'ta yer aldı` (→ `yapıldı`), p değerli karşılaştırmada `önemli fark` (→ `istatistiksel olarak anlamlı`), tıp dışı deneyde `tedavi grubu`, Hz ile `örnekleme oranı`. Bunlar anlam hatasıdır; hafif düzeyde de düzelt. Statüyü koru (`düşündürüyor`, `gösteriyor` değil; test yoksa `anlamlı` yazma); kastedilen anlam kaynaktan çıkmıyorsa seçme. Doğru kullanımı (`yöntem önermek`, `sonuçlar tartışılmıştır`, klinik `tedavi grubu`) koru.

**Türkçenin bağlayıcı kaynaklarını kullan.** İki önerme arasındaki ilişkiyi yalnızca cümle başı bağlaçla (`Ayrıca`, `Ancak`, `Bu nedenle`) etiketleme. Türkçe aynı ilişkiyi ekle ve ilgeçle daha sıkı kurar: ödünleme `-e rağmen`, `-mesine karşın`, `-diği hâlde`, `-se de`; ekleme `de/da`, `-mesinin yanı sıra`, `olmasının yanında`, `hem ... hem`; neden `-den/-dan`, `-dığından`, `-den dolayı`, `sayesinde`, `yüzünden`; karşıtlık `ise`, `oysa`, `-ken`; zaman `-ince`, `-dikten sonra`, `-ir -mez`; araç `-erek`, `aracılığıyla`; karşılaştırma `-e kıyasla`, `-e oranla`; çerçeve `açısından`, `-in merceğinden`, `ışığında`. Önce ilişkiyi adlandır, sonra kaynağı seç. Bağlayıcı ilişki kuramaz, yalnızca kaynağın kurduğu ilişkiyi kodlar: `sayesinde` ve `yüzünden` nedensellik ve değer yargısı ekler, `-e rağmen` bir beklenti varsayar; kaynak yalnızca zaman sırası ya da birliktelik bildiriyorsa bunları yazma. Mecazlı çerçeveyi (`merceği altında`) teknik metne taşıma. Katalog, kayıt notları ve yapı seçimi: [Türkçenin bağlayıcı kaynakları](references/turkce-baglayicilar.md).

**Terim sabit, çevresi değişken.** Aynı paragrafta aynı bağlaç ikinci kez, aynı genel fiil (`göstermek`, `sağlamak`, `ortaya koymak`, `gerçekleştirmek`) ya da değerlendirme sıfatı (`önemli`, `etkili`) ardışık cümlelerde geçiyorsa okurun dikkati sözcüğe kayar. Giderme sırası: önce yapıyı değiştir (birleştir, özneyi düşür, bağlacı eke çevir), sonra ilişkinin gerektirdiği kesin fiili kullan, ancak bundan sonra anlamı ve gücü tam koruyan eş anlamlıya başvur. Bu, kural 5 ile çelişmez: kavramı adlandıran terim yinelenir; değişen, terimleri bağlayan sözcüklerdir. Rastgele eş anlamlı döndürme yasaktır.

**Bağlaç ilişki kuramaz.** `Hata oranı düştü. Bu nedenle modelin genellenebilirliği yüksektir` cümlesinde bağlaç var, mantık yok. Bağlacı kaldırınca ilişki hâlâ geçerli mi bak; eksik öncülü uydurma, kaynağın kurduğu nedensel bağlacı silme. Ardışık cümle çiftinde hangi bilginin taşındığını, hangisinin eklendiğini sor. `Bu`, `söz konusu` göndergesinde rakip öncül ve mesafe varsa göndergeyi aç. `Yalnızca`, `en az`, `de/da` ve olumsuzluğu taşırken bağlandığı ögeyi de taşı: "Model hatayı azaltmadı; yalnızca varyansı düşürdü" birleştirilince "Model yalnızca hatayı azaltmadı ve varyansı düşürdü" olmaz. Katalog: [Metinsel tutarlılık](references/metinsel-tutarlilik.md).

## Müdahale düzeyi ve değişiklik bütçesi

Kullanıcının istediği kapsamı aşma; "tiyatral ifadeleri çıkar" talebi metnin tamamını yeniden yazma izni değildir.

**Hafif.** Belirgin dolguyu, sohbet botu kalıntısını, bölüm duyurusunu, üretilmiş önemi ve anlamı değiştiren kalkıyı düzelt. Cümle yapısını, paragraf sırasını ve başlıkları koru.

**Standart.** Netlik omurgasının cümle ve paragraf kurallarını uygula: döngüsel anlatımı, işlev tekrarını, şişirmeyi, çeviri kokusunu ve uzun ifadeleri düzelt; erken bölünmüş paragrafları birleştir; yerinde olmayan cümleyi paragraf içinde ya da komşu paragrafa taşı; başlık hiyerarşisini koru. Kullanıcı düzey belirtmediyse bu varsayılandır; yapısal parçalanma varsa **Kısa talep, tam iş** bölümüne göre derin düzeyin yapı kuralları o bölümlere eklenir.

**Derin.** Bilgi sırasını, paragraf ve bölüm yapısını kavramsal sınırlara göre yeniden kur: dağılmış konuları topla, hak edilmemiş başlıkları birleştir, ayrılmış kanıtı iddiasına yaklaştır. Dışarıdan dayatılan yapıyı (dergi şablonu, tekrarlanabilir deney bölümleri, güvenlik adımları, numaralı göndermeler) koru.

**Değişiklik bütçesi.** Metin zaten net ve doğalsa olduğu gibi bırak; her görevde görünür değişiklik üretmek zorunda değilsin. Her değişikliğin gerekçesi netlik omurgasından, değişmezlerden ya da Türkçe doğallıktan gelir; gerekçesiz değişikliği geri al. Kısalık amaç değil, tekrar ve dolgu çıkınca ortaya çıkan sonuçtur: bilgi taşıyan cümleyi kısaltmak için kesme, paragrafı uzun diye bölme, başlığı sayıyı azaltmak için birleştirme.

**Üslup örneği.** Kullanıcı yazı örneği verdiyse cümle uzunluğunu, kişi tercihini, terim yoğunluğunu, resmiyeti ve paragraf ölçeğini ondan çıkar; örnekteki yazım yanlışlarını taklit etme. Ayrıntı kenar türler dosyasındadır.

## Bilimsel ve teknik metin

Öncelikli alan budur. Ayrıca bastır: `literatüre önemli katkı`, `bulgular açıkça göstermektedir`, `değerli içgörüler`; otomatik sağlamlık ve genellenebilirlik iddiaları; adlandırılmamış kalıp sınırlılık paragrafı; otomatik `gelecek çalışmalar` kapanışı; olağan kontrolün tekrar tekrar gerekçelendirilmesi; her alt bölümde yinelenen amaç ve düzenek hatırlatması; sonucu ve sınırlılığını ayrı başlıklara dağıtan bölümleme. Geçerli bilimsel iddiayı zayıflatma: kaynak yenilik, önem, mekanizma veya sınırlılığı açıkça kuruyorsa tam o güçte koru. Akademik düzyazıyı gündelik konuşmaya çevirme.

**Rapor bütünlüğü.** Rapor, inceleme notu ya da yönetici özetinde kanıt zincirini koru: bulgu, yorum, öneri ve karar ayrı statülerdir; aralarındaki sınır kaynakta bulanıksa kesinleştirme. İddia ile sayısını, tablosunu, kaynak işaretini ve sınırlılığını yakın tut. Yönetici özetinde yalnızca gövdedeki bulgu, sınır ve önerileri kullan. Tablo ve şekil adlarını, bölüm numaralarını ve çapraz göndermeleri koru; bölüm birleştirirken numaraya bağlı göndermeleri güncelle ya da birleştirmeden vazgeç. Ayrıntı: [Rapor yazımı](references/rapor-yazimi.md).

**Kavramsal giriş.** Yalnızca kullanıcı açıkça temel bir kavrama giriş yazılmasını istiyorsa kaynaktaki bilgilerle kur: okurun bildiği bağlam → kavramı gerekli kılan gerçek problem → cevaplanacak soru → kavram cevap olarak. Kaynakta problem yoksa uydurma. Ayrıntı: [Kavramsal girişler](references/kavramsal-girisler.md).

## Çalışma yöntemi

**1. Envanter çıkar.** Türü, amacı, muhatabı, müdahale düzeyini belirle. Sayı, tarih, özel ad, alıntı, kaynak işareti, kapsam belirleyicisi, terim, sembol, bölüm numarası ve her temel iddianın epistemik statüsünü zihinsel listeye al. Metnin konularını çıkar: hangi konu nerede açılıyor, nerede yeniden açılıyor?

**2. Düzenle, katman katman.** Belge: dağılmış konuları topla, gereksiz bölünmeyi kaldır (kural 1 ve 7). Paragraf: paragraf testini uygula, yerinde olmayan cümleyi taşı, rolleri sırala, tekrar ve şişirmeyi çıkar (kural 2 ve 3). Cümle: kısa ve doğrudan kur, somut özne ve yüklem seç (kural 4 ve 6). Sözcük: terimleri sabitle (kural 5), bağlayıcı kaynaklarını ve eşdizimi Türkçeye göre kur, yakın tekrarı gider. Her katmandan sonra bir üst katmanı yeniden oku; bir değişiklik komşu cümlenin öznesini, zamanını, bağlacını ya da bir göndermeyi bozmasın.

**3. Kaynakla karşılaştır.** Son metindeki her sayı, tarih, sonuç, nedensellik, karşılaştırma, olumsuzluk, koşul, istisna, nicelik sınırı, terim ve kişisel ayrıntının kaynakta karşılığını bul; kaynağı, statüsü ve kesinliği aynı mı? Karşılığı yoksa çıkar ya da kaynağın düzeyine döndür.

**4. Netlik denetimi.** Teslimden önce sessizce sor:

- **Konu:** Her paragraf tek konu mu; bir konu birden fazla yerde mi açılıyor; okur bitmiş bir konuya geri çağrılıyor mu?
- **Tekrar:** Aynı önerme yeni rol kazanmadan ikinci kez geçiyor mu; döngüsel tanım ya da işlev tekrarı kaldı mı?
- **Gereklilik:** Her cümle silme testini geçiyor mu; çıkardığın dolgu daha sakin eş anlamlılarla geri geldi mi?
- **Cümle:** İlgisiz önermeler tek cümlede mi; uzun ifade, çerçeve yığını, ad zinciri kaldı mı; telgraf diline indin mi?
- **Terim:** Her kavramın tek adı var mı; kısaltma, sembol ve numaralar tutarlı mı?
- **Kesinlik:** Her iddia kaynaktaki kişiye, statüye ve kesinliğe bağlı mı; çekince, kapsam ve olumsuzluk yerinde mi; kip ankrajı doğru mu?
- **Yerleşim:** Her cümle paragrafında bir rol taşıyor ve doğru konumda mı; her paragrafın ilk cümlesi öncekinden doğal olarak çıkıyor mu?
- **Akış:** İlişkiler Türkçenin bağlayıcı kaynaklarıyla mı kurulmuş; aynı bağlaç, genel fiil ya da sıfat bir paragrafta peş peşe mi geliyor; hiçbir bağlayıcı kaynakta olmayan ilişki kuruyor mu?
- **Türkçe:** Metin Türkçe düşünülmüş gibi okunuyor mu; anlamı değiştiren kalkı kaldı mı; aşırı düzeltme var mı?
- **Bütçe:** Kullanıcının istediğinden fazla değişiklik yapıldı mı; gerekli bir sınırlılık, öğretici açıklama ya da gezinme başlığı dolgu sanılıp silindi mi?

Sonucu "insanileştirmek" için hata, argo, rastgelelik veya uzunluk gürültüsü üretme.

## Referans yönlendirmesi

- Netlik omurgasının STE100 kaynağı, eşikleri ve örnekleri: [Netlik omurgası](references/netlik-omurgasi.md).
- Önem cümleleri, savunma, döngüsel tekrar, yol haritası, kalıp giriş ve sonuç: [Retorik yapılar](references/retorik-yapilar.md).
- Çok başlık, kısa paragraf, çapraz gönderme, dağılmış konu ya da birleştirilecek ve korunacak bölümler: [Yapısal bütünlük](references/yapisal-butunluk.md).
- Kopuk paragraf, belirsiz gönderge, takılan akış: [Akıcı Türkçe](references/akicilik.md).
- Her cümle aynı bağlaçla açılıyor, ilişkiler etiketle kuruluyor ya da aynı sözcük peş peşe geliyor: [Türkçenin bağlayıcı kaynakları](references/turkce-baglayicilar.md).
- Klişe, yapay ritim, gereksiz resmiyet: [Türkçe örüntüler](references/turkce-oruntuler.md).
- Çeviri gibi okunan cümle: [Türkçe ritim ve çeviri kokusu](references/turkce-ritim-ve-ceviri-kokusu.md).
- Aktarım, çıkarım, çekince, edilgen çatı, öneri–karar–uygulama: [Kanıt ve kesinlik](references/kanit-ve-kesinlik.md).
- Tamamlanmış işin geniş zamanla anlatılması ya da geçmişe zorlama: [Zamansal ankraj ve rapor kipi](references/zamansal-ankraj-ve-rapor-kipi.md).
- Tuhaf eşdizim, kalkı, terim kararsızlığı: [Sözcük birleşimleri](references/sozcuk-birlesimleri.md).
- Olgu yığını, desteksiz bağlaç, kapsam ya da olumsuzluk kayması: [Metinsel tutarlılık](references/metinsel-tutarlilik.md).
- Rapor, inceleme notu, yönetici özeti: [Rapor yazımı](references/rapor-yazimi.md).
- Hukuki, tanıtım, deneme, sosyal medya, kişisel ya da edebî metin, üslup eşleme: [Kenar türler](references/kenar-turler.md).

## Çıktı biçimi

Kullanıcı başka bir biçim istemediyse yalnızca son metni ver; sohbet botu girişi veya kapanış teklifi ekleme. İnceleme ya da karşılaştırma istendiyse: kısa teşhis, düzeltilmiş metin, en önemli değişiklikler. Cümle sildiysen ya da bölüm birleştirdiysen üçüncü kısımda silinenin hangi bilgiyi taşımadığını ve birleştirmenin hangi konu sınırına dayandığını kısaca belirt.

## Kısa örnekler

**Önce**

> Kalibrasyon, ölçüm sisteminin kalibre edilmesi işlemidir. Bu çalışmada kalibrasyon 12 referans ağırlıkla yapıldı ve doğrusallık hatası %0,8'den %0,2'ye indi. Bu sonuç, kalibrasyonun ölçüm doğruluğu açısından kritik bir rol oynadığını açıkça ortaya koymaktadır. Başka bir deyişle, kalibrasyon sayesinde ölçümler daha doğru hâle gelmiştir. Sonuç olarak, kalibrasyon ölçüm doğruluğunu artırmaktadır.

**Sonra**

> Ölçüm sistemi 12 referans ağırlıkla kalibre edildi; doğrusallık hatası %0,8'den %0,2'ye indi.

Birinci cümle terimi kendisiyle tanımlıyordu (kural 2). Son üç cümle aynı ölçümü önem, açımlama ve mini sonuç olarak üç kez daha söylüyordu (kural 2 ve 3). `Açıkça ortaya koymaktadır` ve `artırmaktadır` tek bir ölçümü genel nedensel yasaya çeviriyordu; bu da değişmezleri bozuyordu. Ölçüm, sayılar ve referans ağırlık sayısı korundu.

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

Tek konu üç başlığa dağılmıştı (kural 1 ve 7). `Belirleyici rol`, `bir sonraki bölümde görülecektir` askısı ve `yukarıda belirtilen` göndermesi bölünmenin ürettiği dolguydu. Kullanıcı yalnızca hafif düzenleme isteseydi başlıklar korunur, yalnızca dolgu cümleleri silinirdi.
