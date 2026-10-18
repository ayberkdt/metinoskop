---
name: metinoskop
description: AI ajanının Türkçe metni insan ritmiyle yazmasını ve düzenlemesini sağlar; her önerme bir kez, doğru yerde ve kaynağın kesinliğiyle söylenir, olgular, sayılar, kanıt statüsü ve yazarın tavrı korunur. Dayanağı ASD-STE100 yazım ilkeleri ve AI–insan metnini karşılaştıran araştırmalardır. Öncelikli alan bilimsel ve teknik metindir (makale, tez, rapor, README); Türkçeye çevrilmiş metin de düzenlenir. Metin konuşmayı görmemiş son okura gider. Ajan kullanıcı için Türkçe metin yazarken (rapor, özet, e-posta, belge) ya da Türkçe bir metin verilip "geliştir", "düzelt", "toparla", "akıcı yap", "AI slop gibi", "yapay duruyor", "netleştir", "sadeleştir", "çeviri gibi durmasın", "okura hazırla" dendiğinde kullan.
---

# Metinoskop

Türkçe metni, yazarken de düzenlerken de, net ve insan ritmiyle kur: okur her önermeyi bir kez, doğru yerde, kaynağın verdiği kesinlikte bulsun. Netlik kaynak sadakatinin, kanıt statüsünün ve kesinliğin önüne geçmez. Katalog ve örnekler **Referans yönlendirmesi**ndeki dosyalardadır.

## Kural önceliği

Çatışma olduğunda şu sırayı uygula:

1. Kullanıcının açık talebi ve belirttiği kapsam
2. Kaynak metindeki olgular, iddialar, belirsizlikler ve yazar tavrı
3. Kullanıcının sağladığı üslup örneği
4. Metnin iletişim amacı, türü ve okuru
5. Bu skill'deki netlik omurgası ve genel dil tercihleri

Alt sıradaki kural üst sıradakini bozmaz. Açık talep kapsamı, amacı ve okuru belirler; olgu uydurma izni vermez. Kullanıcının talepte verdiği bilgi (`pilot iptal edildi, düzelt`) kaynağın parçasıdır.

## Görevin sınırı

**Yazma ve düzenleme.** Kurallar iki kipte aynıdır. **Yazma:** kullanıcı istek ve bilgi verir (not, veri, dosya, konuşma); kaynak bu bilgidir, metni sen kurarsın. Kuralları ilk taslakta uygula. Eksik bilgiyi uydurma, yer tutucu koyma; metnin dışında sor. Notun sonucunu da çıkarma: `veri henüz gelmedi` notu `etkisi değerlendirilemiyor` cümlesine dönmez. Yazarın kanaati birinci şahısla kalır (`sanırım`, `bence`); öznesiz kanaat (`düşünülüyor`, `bir tahmin var`) kimin düşündüğünü siler. **Düzenleme:** kaynak verilen metindir; kullanıcı istemedikçe yeni bölüm ya da giriş üretme.

- Yeni olgu, tarih, sayı, alıntı, kaynak, özellik, sonuç, deneyim veya görüş üretme.
- Kaynak dilden çeviri yapma; Türkçeye çevrilmiş metni düzenle.
- Alıntıyı, kodu, URL'yi, dipnotu, kaynak işaretini, tablo hücresini ve Markdown yapısını koru. Başlık hiyerarşisini yalnızca yapısal düzenleme istendiğinde ya da derin düzeyde, kavramsal sınırlara göre değiştir.
- Anlatıda olay sırasını ve bakış açısını değiştirme.
- AI dedektöründen geçme vaadi verme; metni "insanileştirmek" için hata, argo, rastgelelik ya da uzunluk gürültüsü üretme.

## Okura doğrudan metin

Metin konuşmayı görmemiş son okura gider. Kullanıcıyla konuşma, talimat ve `/goal` istemi, önceki taslaklar, araç çıktıları ve ajanın çalışma sırası okurun dünyasında yoktur; metinde bunlara gönderme kalmaz. Kural düzenlediğin ve ürettiğin her metne, her düzeyde uygulanır. Kullanıcı okuru başka tanımlarsa (kendisine not, konuşmanın tarafına yanıt) o tanım geçerlidir.

**Sızıntıyı tanı.** Konuşmaya gönderme (`konuştuğumuz gibi`, `verdiğin dosyaya göre`), kullanıcıya teklif (`şunu yapabiliriz`, `istersen eklerim`), çalışma süreci (`önce X'e baktım`), düzenleme geçmişi (`önceki taslakta`, `(düzeltildi)`), teslim ambalajı ve ajan kimliği (`İşte rapor:`, `bir yapay zekâ olarak`). Test: konuşmayı görmemiş okur `ben`, `biz`, `sen` kim, anlıyor mu; cümle ona bilgi veriyor mu?

**Bilgiyi kurtar, ambalajı at.** Sızıntıyı sil, taşıdığı önermeyi kaynağın statüsüyle yaz: `Verdiğin 2024 dosyasına göre` → `2024 verilerine göre`; `X'i varsaydım` → `hesap X varsayımına dayanır`; `doğrulayamadım` → `doğrulanmadı`; `önce cache.py'ye baktım, testi çalıştırdım` → `cache.py incelendi, test çalıştırıldı` (yöntem silinmez). `Yapabiliriz` → `yapılabilir`, `yapılmalıdır` değil; `biz` yerine aktör uydurma. Bilgi vermeyen teklif ve ambalaj gider; çekince ve varsayım kalır. Okurun tarafı olduğu yazışmadaki ortak geçmiş ve okura yapılan teklif (`istersen ayrı sayfa eklerim`), kurumsal yanıtta `talebiniz doğrultusunda`, sürüm notunda önceki sürüm sızıntı değildir.

**Not metnin dışına yazılır.** Soru ya da kapsam dışı uyarı metne girmez (`[?]`, `TODO` dahil); gerekiyorsa metinden sonra `---` ile ayrılmış kısa nottur. Neyi sildiğini anlatan not, inceleme istenmedikçe yazılmaz.

## Bağlamı çıkar

Yazmadan önce sessizce belirle: **tür** ve **amaç**; **okur** (uzman, genel okur, yeni başlayan; kullanıcı değil, metni okuyacak kişi); **yapısal ölçek** (dayatılmış yapı dahil); **istenen değişiklik**; raporsa her bölümün **işlevi** (bağlam, yöntem, bulgu, yorum, sınırlılık, öneri).

**Kenar türler ayrı tutulur.** Hukuki metin, tanıtım ve pazarlama, deneme, köşe yazısı ve sosyal medya, kişisel yazışma, edebî metin ve üslup eşleme için ek kurallar [Kenar türler](references/kenar-turler.md) dosyasındadır. Metin bu türlerden biri değilse o dosyayı okuma ve oradaki istisnaları (hukuki kalıp, ikna amacı, yazara özgü imge) bilimsel ya da teknik metne taşıma.

## Kısa talep, tam iş

"Bunu geliştir", "çok AI slop gibi", "toparla" eksik talimat değil, tam yetkidir: düzey, kapsam ya da ton sorma; sorunları kendin teşhis et ve tek bir son metin ver.

- **Düzeyi teşhis seçer.** Kullanıcı sorun ya da düzey söylemediyse varsayılan standarttır. Teşhis yapısal parçalanma gösteriyorsa (dağılmış konu, tek paragraflık bölüm, ilk cümleyi yineleyen başlık) derin düzeyin yapı kurallarını yalnızca o bölümlere uygula. Dışarıdan dayatılmış yapı her durumda korunur.
- **Seçenek sunma.** Alternatif sürüm, "şunu da ister misiniz" teklifi, düzey menüsü ya da soru listesi ekleme.
- **Soru yalnızca yorum seçimi için.** Bkz. **Belirsizlik ve yorum seçimi**. Üslup ya da yapı tercihi soru gerekçesi değildir.

## Bütüncül düzenleme

Metni dört katmanda birlikte düzenle: **belge** (konular nerede, hangi sırayla açılıyor), **paragraf** (tek konu, cümle rolleri ve sırası, komşu paragrafla bağ), **cümle** (önerme, yapı, uzunluk), **sözcük** (eşdizim, terim, yakın tekrar).

**Yukarıdan aşağı teşhis, aşağıdan yukarı doğrulama.** Belgeden başla, sözcüğe in. Her değişiklikten sonra bir üst katmanı yeniden oku: devir, özne, zaman, bağlaç ya da gönderge bozuldu mu; konu başka yerde yeniden açılıyor mu?

**Paragraf testi.** Her paragraf için sessizce sor:

1. Özü tek cümleyle söylenebiliyor mu? Söylenemiyorsa paragraf iki konu taşıyor ya da konuyu bitirmiyor.
2. Her cümlenin rolü ne: iddia, kanıt, yorum, sınırlılık, örnek, geçiş? Rolü olmayan cümle silinir.
3. Roller doğru sırada mı? Bilinen bilgi yeniden önce gelir; iddia ile kanıt, sonuç ile sınırlılık bitişik durur.
4. İlk cümle önceki paragrafın son cümlesinden doğal olarak çıkıyor mu?

**Yerinde olmayan cümle yeniden yazılmaz, taşınır.** Doğru ama yanlış yerdeki cümleyi ait olduğu yere taşı ya da ilişkili cümleyle birleştir. Taşıma düzeye bağlıdır: hafif düzeyde yapılmaz, standartta paragraf içinde ya da komşu paragrafa, derinde bölümler arasında yapılır. Göndermeler, numaralar ve dayatılmış bölüm ayrımı bozulmaz.

## Netlik omurgası

Yedi kural ASD-STE100 yazım kurallarından Türkçeye uyarlanmıştır; sözlüğü ve İngilizceye özgü kuralları alınmamıştır. Sayısal eşikler inceleme işaretidir, kesme kuralı değildir: tek ilişki taşıyan uzun cümle ve tek hareketi yürüten uzun paragraf korunur.

**1. Bir paragraf, bir konu.** Paragraf tek konuyu ya da tek düşünce hareketini (iddia → kanıt → yorum, ölçüm → sınırlılık) taşır; konu başta belli olur. Söylem işlevi sert biçimde değişince (bulgu → öneri, yöntem → sonuç) yeni paragraf açılır. Belgeye dağılmış konuyu tek yerde topla; okur bitirdiği konuya geri çağrılmasın. Altı cümleyi aşan paragrafta iki konu olup olmadığına bak; tek hareketse bölme.

**2. Her önermeyi bir kez söyle.** Döngüsel anlatımı kaldır: olgu → başka sözcüklerle aynı olgu → önem cümlesi → soyut mini sonuç dizisini kaynağın kurduğu önermeye indir. Aynı önermenin girişte, bölüm başında ve sonuçta yeniden açımlanmasını, döngüsel tanımı (`kalibrasyon, ölçümlerin kalibre edilmesidir`) ve sözcükleri farklı, işlevi aynı cümleleri (`Bu sonuç önemlidir`, `Bu bulgu dikkat çekicidir`) ara. Yineleme yalnızca önerme yeni rol kazandığında (ölçüm → yorum → sınırlı öneri) ya da çok uzun belgede mesafe gerektirdiğinde meşrudur. Özet ve yönetici özetinin gövdeyle örtüşmesi tekrar sayılmaz; özetin içinde her önerme bir kez geçer. Terimi yinelemek tekrar değildir (kural 5).

**3. Yalnızca gerekli bilgiyi yaz.** Her cümle yeni bir olgu, gerekli bir nitelendirme, açık olmayan bir ilişki, kaynağın desteklediği bir yorum, yorumu değiştiren bir sınırlılık ya da önceki bilgiyi birleştiren bir sentez taşır. Silme testi: cümle çıkınca önerme, akıl yürütme, kronoloji, yorum veya yazar tavrı değişiyor mu; değişmiyorsa cümle okurun çıkarım yükünü azaltıyor mu? İkisine de hayırsa sil.

**4. Kısa ve doğrudan cümle.** Cümle bir ana önerme ya da bir ilişki taşır; talimatta bir cümle bir adımdır. İlgisiz önermeleri tek cümleye yığma, yapay olarak parçalanmış tek düşünceyi birleştir: ölçüt kavramsal birliktir. LLM cümleleri orta uzunlukta toplanır: tek ilişkili uzun cümleyi bölme, ana bulguyu kısa cümleyle verebilirsin. Varsayılan yüklem çekimli fiildir, adlaştırma değil. Uzun biçimi kısa eşdeğeriyle değiştir (`bir değerlendirme yapılması gerekmektedir` → `değerlendirilmelidir`); yığılmış çerçeveyi, isim-fiil zincirini, üçten uzun ad ya da iyelik zincirini çöz. Cümle ögesi düşürüp telgraf diline inme.

**5. Bir terim, bir anlam.** Bir kavrama bir ad ver ve onu kullan; aynı varlığı `yöntem`, `yaklaşım`, `yapı`, `sistem` arasında kaydırma, aynı sözcüğü iki anlamda kullanma. Kısaltmayı ilk geçtiği yerde aç. Sembol, birim, değişken ve bölüm numarasını değiştirme; kaynakta ayrı anlamlı iki terimi birleştirme; terimi tekrar olmasın diye eş anlamlıyla değiştirme.

**6. Somut özne, somut yüklem.** Aktör hem belli hem okur için bilgi taşıyorsa (kim onayladı, kim uygulayacak) etken çatı ve somut fiil kullan; talimatta etken çatı ya da emir kipi tercih edilir. Bilimsel betimlemede edilgen çatı yöntem merkezli kaydı ve konu sürekliliğini taşıyorsa meşrudur. Edilgenliği yalnızca aktör belli diye etkene çevirme; kaynağın adlandırmadığı aktörü uydurma. `ortaya koymak`, `rol oynamak`, `katkı sağlamak`, `ışık tutmak` gibi soyut yüklemde kodlanan somut ilişkiyi yaz; daha somut fiil kaynağın kurmadığı nedenselliği kurmasın. Tekrarlanan `bu durum`, `söz konusu süreç` öznesini somut göndergeye çöz ya da cümleyi sil.

**7. Yapı okura hizmet eder.** Başlık büyük kavramsal geçişi işaretler, uzun belgede gezinmeyi sağlar ya da dayatılmış yapıyı yansıtır; altında tek kısa paragraf olan, ilk cümleyi yineleyen ya da simetri için kurulan başlık birleşir. Liste yalnızca paralel ögeler ve sıralı adımlar içindir; `bu nedenle` ile bağlanan maddeler zincirdir, düzyazıya döner. İddia ile kanıtı, sonuç ile sınırlılığı ayrı bölümlere dağıtma. Görsel parçalanmayı açıklık sanma; parçalanmayı tek dev paragrafla da çözme.

## Şişirme kataloğu

Klişe sözcük içermeyen metin de her olgudan sonra önem cümlesi kuruyor ve her bölümü duyuruyla açıyorsa şişkindir. Yargı birimi sözcük değil, sözcüğün bağlamdaki işlevidir: `ancak`, `önemli`, `göstermektedir`, `-maktadır`, edilgen çatı, üçlü liste, alt başlık, `bir`, `olan`, `sahip olmak`, `bulunmaktadır`, `olabilir` incelenir, otomatik silinmez.

**Dolguyu başka dolguya çevirme.** Önem şişirmesi, retorik çerçeve, savunma, boş geçiş ya da kalıp sonuç çıkarılırken aynı işlev daha sakin eş anlamlıyla korunmaz: `çığır açan sonuç` → `oldukça önemli sonuç`, `bu noktada vurgulamak gerekir` → `burada belirtmek gerekir` yanlıştır. Cümlenin bağımsız bilgisi yoksa sil; varsa yalnızca o bilgiyi bırak.

**Üretilmiş önem.** `... açısından önemlidir`, `kritik rol oynamaktadır`, `değerli içgörüler sunmaktadır`, `literatürdeki boşluğu doldurmaktadır` ve dayanaksız sağlamlık ya da genellenebilirlik iddiası kaynak gerekçelendirmiyorsa çıkar; somut sonucu bırak. Kaynak önemi dayanağıyla kuruyorsa o güçte koru. Kişiye ya da kuruma atfedilmiş değerlendirme (`Bu proje bizim için bir dönüm noktasıdır`) yazar tavrıdır; atıfsız olumlu çerçeve (`ulaşamadı, ancak bu bir fırsat sunuyor`) tavır değil, olumluya çekmedir. Her konuya yapışan imge ve formül (`kilit rol`, `temel taşı`, `X'ten çok daha fazlası`) ambalajdır: önermeyi aynı güçte yalın sözcüklerle bırak. LLM'in fazla sözcükleri çoğunlukla biçem fiili ve sıfatıdır (`altını çizmek`, `vurgulamak`, `gözler önüne sermek`, `kapsamlı`): yerine gösterilen değeri ya da farkı yaz.

**Savunmacı düzyazı.** `Burada amaç ... değildir`, `Bu tercih tesadüfi değildir` için sor: okurun hangi somut yanlış anlamasını önlüyor? Cevap yoksa çıkar. Tercih değişince yorum, tekrarlanabilirlik ya da geçerlilik değişecekse yöntem gerekçesi meşrudur. Uzman okura olağan uygulamayı savunma; yeni başlayana yazılmış öğretici açıklamayı silme, okur belirsizse koru.

**Üretilmiş karşıtlık ve zorlama denge.** `X değil, Y`, `yalnızca ... değil, aynı zamanda ...` karşıtlığını reddedilen taraf kaynakta yoksa kurma. `Güçlü olmakla birlikte bazı sınırlamaları da vardır` adlandırılmış sınırlılık yoksa çıkar. Kanıt düzeyi bildiren çekince (`çalışma gözlemseldir`) denge değil kesinlik bilgisidir.

**Okur yönlendirmesi ve sarmalayıcı.** `Bu bölümde ... ele alınacaktır`, `Şimdi ... bakalım` gibi duyuru ve askıları sil; olguyu doğrudan söyle. Yol haritası uzun ve karmaşık belgede, bir kez meşrudur. Tablo, şekil, ek ve kaynak göndermeleri korunur.

**Etiket ve anons yok.** Cümlenin türünü adlandıran etiket (`Kavramsal ayrım:`, `Detaylı açıklama:`, `Sezgisel açıklama:`, `Kısa cevap:`, `Özetle:`, `Kural şudur:`) kalın ya da başlık olsa da yazılmaz; ayrımı ya da açıklamayı cümlenin kendisi kurar (`Önbellek veriyi saklar, tampon yalnızca aktarır.`). Okura seslenen anons, slogan ve eylem çağrısı (`Merak etmeyin`, `çözümümüzü hazırladık`, `Hemen deneyin`, `Sizi bekliyoruz`) her türde silinir; emir yalnızca somut adımsa kalır (`Ayarlar > Depolama'dan açın`). Belgenin dayattığı alan etiketi (`Girdi:`, `Uyarı:`, `Konu:`, sözlükte terim) kalır.

**Kalıp giriş ve kalıp sonuç.** Giriş hunisini (geniş dünya → hızla değişen ortam → `giderek önem kazanıyor`) at; kaynaktaki somut nedenle başla. Sonuç sentez yapabilir, girişi ya da özeti yeniden anlatamaz.

**Yapay gerilim.** `Ancak burada işler değişmektedir`, `İşin ilginç yanı`, `Daha da önemlisi` gibi momentum kalıplarını sil; gerçek karşıtlığı nicel olarak yaz (`Yöntem kuvvet hatasını düşürdü ama yedi günlük konum hatasını artırdı`).

**Paragraf simetrisi.** Her paragrafın konu cümlesiyle açılıp mini sonuçla kapanması, eşit uzunluklar ve tekrarlayan "nokta → açıklama → sonuç" mimarisi yapaylık işaretidir. Her metni aynı açılışla, `İlk olarak … Son olarak` sırasıyla ve `Sonuç olarak` kapanışıyla kurma; ardışık cümleleri aynı söz dizimi kalıbıyla açıp kapama.

## Değişmezler: netlik kesinliği bozmaz

Kısaltırken, birleştirirken ya da somutlaştırırken bu bölüm her netlik kuralının üstündedir.

**Kaynak sadakati.** Önermeleri ayır: olgu veya ölçüm; amaç, plan veya vaat; görüş ya da değerlendirme; duygu veya tavır; belirsizlik ve çekince; tekrar ve dolgu. İlk beşinin anlamını ve kesinliğini koru, sonuncusunu yeniden üretme. Hedefi sonuç, değerlendirmeyi ölçüm, kronolojiyi nedensellik gibi yazma. Karşılaştırma zemini yoksa `daha`, ölçüt yoksa `en` ekleme. Olumsuzluğu, istisnayı, koşulu ve nicelik sınırını koru: `bazı` → `tüm`, `en az` → kesin sayı, `yalnızca` → genel kapsam olmaz; `henüz`, `artık`, `genellikle` dolgu değildir. Kaynaktaki sayılardan oran, fark ya da ortalama türetme. Olumsuz bulguyu ve eleştiriyi yumuşatma (`başarısız oldu` → `beklenen düzeye ulaşamadı`); LLM tonu nötre ve olumluya çeker.

**Belirsizlik ve yorum seçimi.** Birden fazla makul yoruma açık ifadede anlamı kendin seçme. Belirsizlik korunarak düzenlenebiliyorsa koru, soru sorma. Düzenleme yorum seçmeyi gerektiriyorsa o yeri kaynaktaki hâliyle bırak, metni ver ve metnin dışında tek soru sor.

**Bilginin kaynağı ve statüsü.** Her temel önermenin statüsünü belirle: gözlem, ölçüm, aktarım, çıkarım, tahmin, plan, varsayım, yorum. `Gözlendi`, `bildirildi`, `düşündürüyor`, `ölçüldü` farklı statü kodlar; düzenlenmiş cümle aynı düzeyde kalır. Ölçüm, ilişki, çıkarım ve nedensellik ayrı düzeylerdir: rastgele atanmamış iki grup arasındaki fark `etkiler` olmaz. Atıflı iddia (`rapora göre`, `yazarlar öne sürmektedir`) atıflı kalır. Şişmiş iddiayı indirirken yerine olumsuz iddia ya da yeni çekince yazma; ölçülmemiş iddia (`güvenilirlik arttı`) `düşündürüyor` diye yumuşatılmaz, silinir.

**Çekince kanıttır.** `Olabilir`, `görünmektedir`, `kısmen`, `bu verilerle sınırlı olarak` belirsizlik ya da kapsam kodluyorsa korunur. LLM metni insan metninden daha az çekince taşır; çekinceyi AI izi sanıp silme. `Açıkça`, `tartışmasız`, `kanıtlamaktadır` için hangi kanıtın bunu hak ettiğini sor. Kısalık için iddiayı güçlendirme, kontrollü deneyle kurulmuş iddiayı zayıflatma.

**Statü zinciri ilerlemez.** Bulgu yorum, yorum öneri, öneri karar, karar uygulama, beklenti taahhüt olmaz. İddia yeni kanıt olmadan sonraki bölümde güçlenmez. `Gözlenmedi` `yoktur`, `sınanmadı` `geçersizdir` olmaz.

**Yerine yazdığın ifade yeni bir iddiadır.** Hata çoğu zaman silinende değil, yerine yazılanda doğar. Dolguyu, kalkıyı ya da şişmiş iddiayı değiştirdiğin her yerde yeni ifadeyi kaynağa karşı beş soruyla sına:
- **Güç:** İndirirken olumsuz iddia ya da çekince eklemedin mi? Şişmiş iddia kaynağın düzeyine iner (`açıklamaktadır` → `zayıf bir ilişkiye işaret ediyor`); statü kaymaz (`karar sürecinde` kalır).
- **Yön:** Kim neyi yapıyor, aynı mı (`operatöre görünürlük sağladı` → `operatörün görünürlüğünü artırdı` operatörü görülen yapar)?
- **Eşdizim:** Yeni birleşim doğal mı (`hata oranı iyileşti` değil, `azaldı`)?
- **Derece:** Karşılaştırma ve kapsam aynı güçte mi (`her zamankinden` → `eskisinden` zayıflatır)?
- **Neden:** İki ölçümden çıkan sonuç tek nedene bağlandı mı (`gürültü arttığından ödünleşimdir`)?

**Zamansal ankraj.** Tamamlanmış çalışma `incelendi / kullanıldı / uygulandı` ekseninde anlatılır; açık geçmiş tarih ya da `bu çalışmada` çerçevesiyle zamansız geniş zaman (`inceler / kullanır`) yan yana gelince zamansal sürtünme vardır. Algoritmanın genel davranışı, bilimsel genel ilişki, ürün belirtimi, yeniden kullanılabilir prosedür ve normatif kural geniş zamanda kalır. Güncel durum, belgenin işlevi ve tartışılan bulgunun yorumu `-yor` alabilir (`Şekil 4 ... gösteriyor`). Kipi çeşitlilik için nöbetleştirme; düzeltmeyi `yapıldı / edildi` ya da `-miştir` zincirine çevirme. `-yordu`, `-mıştı`, `-ardı` ilişkilerini ne düzleştir ne uydur.

## Türkçe doğallık

Netlik İngilizce iskeletle kurulmaz; hedef Türkçe düşünülerek yazılmış düzyazıdır.

**Çeviri kokusunu ilişkide ara.** Bilgi yapısı, özne kullanımı, yan cümle mimarisi ve bağlaç seçimi İngilizceden kalmışsa metin çeviri gibi okunur. İşaretler: ardışık cümlelerde yinelenen açık özne; `bu sonuç`, `bu durum` diye yeniden öznelenen önerme; `ve`, `ancak` ile dizilmiş çekimli cümleler; her cümle başında söylem belirteci; `sahip olmak`, `bulunmaktadır`; `açısından`, `kapsamında` yığını; `olan ... olan` zinciri; her adın önünde `bir`. Sözcükleri yeniden çevirme; ilişkiyi bul ve Türkçenin kaynaklarıyla kur (özne düşürme, eksilti, zarf-fiil, ortaç, hâl eki). Özne iki aktör arasında belirsizlik doğuracaksa açık kalır.

**Cümle sonu kuyruğu.** Virgülle cümle sonuna eklenen `-arak/-erek` öbeği (`yanıt süresini 240 ms'ye indirdi, kullanıcı deneyimini iyileştirerek.`) ve `, bu da … sağlamaktadır` eki İngilizce `-ing` ve `, which` iskeletidir ve LLM metninin en sık izlerindendir. Kuyruk yeni önerme taşıyorsa öznesi ve yüklemiyle ayrı cümle yap; kaynakta olmayan değerlendirme taşıyorsa sil. Yüklemden önce gelen zarf-fiil (`ölçümleri iki kez alarak denetledi`) doğaldır.

**Aşırı Türkçeleştirme.** `İlişkili`yi `neden olur`, `olumsuz etki`yi `bozuldu` yapma. Alan terimini (`parametre`, `pipeline`, `baseline`) öz Türkçe hevesiyle değiştirme. Tek yükleme asılmış dört beş fiilimsi, arkaik sözcük, zorlama deyim ve gereksiz devriklik aşırı düzeltmedir. Akademik metin adlaştırmaya ve edilgenliğe, teknik belge güvenlik için açık özne yinelemesine hak sahibidir. Peş peşe `-maktadır` yüklemlerini sadeleştir ama sırf çeşitlilik için kip değiştirme; teknik işlemi adlandıran isim-fiili koru.

**Eşdizim ve istem.** Şüpheli öbekte sor: bu ad bu fiille kullanılır mı; fiil tümlecini doğru hâlde mi alıyor; İngilizce edat ilgece mi dönmüş (`X hakkında odaklanmak` → `X'e odaklanmak`); hafif fiil (`değerlendirme gerçekleştirmek`) yalın yüklemi mi gizliyor? Hâl değişimi ilişkiyi değiştirebilir (`gürültüden etkilenmez` ≠ `gürültüyü etkilemez`). Gerçek süreç adını (`risk değerlendirmesi yapmak`) bırak.

**Sözcüksel kalkı.** `framework→çerçeve`, `provide→sağlamak`, `perform→gerçekleştirmek`, `capture→yakalamak`, `address→adreslemek`, `enable→mümkün kılmak` eşleşmelerini otomatik kabul etme; sor: anadili Türkçe bir uzman bu ilişkiyi İngilizce cümleyi görmeden bu sözcüklerle mi kurardı? Karar birimi sözcük + tümleç + bağlam + alandır; teknik terimi (`referans çerçevesi`, `belleği adreslemek`), yerleşik eşdizimi (`hipotezi desteklemek`) ve alan jargonunu değiştirme. Daha doğal fiil daha güçlü iddia olmasın.

**Anlamı değiştiren kalkıyı her düzeyde düzelt.** Bazı kalkılar okura başka önerme verir: `bulgular ... olduğunu önermektedir` (→ `düşündürüyor`), `yazarlar ... olduğunu tartışmaktadır` (→ `savunuyor`), `deney Mart'ta yer aldı` (→ `yapıldı`), p değerli karşılaştırmada `önemli fark` (→ `istatistiksel olarak anlamlı`), tıp dışı deneyde `tedavi grubu`, Hz ile `örnekleme oranı`. Bunlar anlam hatasıdır; hafif düzeyde de düzelt. Kullanıcı kapsamı açıkça başka bir işe daralttıysa (`yalnızca noktalama`) dokunma, metnin dışında tek satırla bildir; konuşma sızıntısı için de aynısı geçerlidir. Statüyü koru (`düşündürüyor`, `gösteriyor` değil; test yoksa `anlamlı` yazma). Doğru kullanımı (`yöntem önermek`, `sonuçlar tartışılmıştır`, klinik `tedavi grubu`) koru.

**Türkçenin bağlayıcı kaynaklarını kullan.** İlişkiyi yalnızca cümle başı etiketle (`Ayrıca`, `Ancak`, `Bu nedenle`) kurma; Türkçe aynı ilişkiyi ek ve ilgeçle daha sıkı kurar (`-e rağmen`, `-mesinin yanı sıra`, `-dığından`, `ise`, `-ken`, `-erek`, `-e kıyasla`). Önce ilişkiyi adlandır, sonra kaynağı seç. Bağlayıcı yalnızca kaynağın kurduğu ilişkiyi kodlar: `sayesinde` ve `yüzünden` nedensellik ve değer yargısı, `-e rağmen` beklenti ekler; kaynak yalnızca sıra ya da birliktelik bildiriyorsa bunları yazma. Mecazlı çerçeve (`merceğinden`, `ışığında`) teknik metne girmez.

**Terim sabit, çevresi değişken.** Aynı paragrafta aynı bağlaç ikinci kez ya da aynı genel fiil (`göstermek`, `sağlamak`, `gerçekleştirmek`) veya değerlendirme sıfatı (`önemli`, `etkili`) ardışık cümlelerde geçiyorsa dikkat sözcüğe kayar. Önce yapıyı değiştir (birleştir, özneyi düşür, bağlacı eke çevir), sonra ilişkinin gerektirdiği kesin fiili kullan, en son anlamı ve gücü koruyan eş anlamlıya başvur. Terim yinelenir (kural 5); değişen, terimleri bağlayan sözcüklerdir. Rastgele eş anlamlı döndürme yasaktır.

**Bağlaç ilişki kuramaz.** `Hata oranı düştü. Bu nedenle modelin genellenebilirliği yüksektir` cümlesinde bağlaç var, mantık yok. Bağlacı kaldırınca ilişki hâlâ geçerli mi bak; eksik öncülü uydurma, kaynağın kurduğu nedensel bağlacı silme. `Bu`, `söz konusu` göndergesinde rakip öncül ve mesafe varsa göndergeyi aç. `Yalnızca`, `en az`, `de/da` ve olumsuzluğu bağlandığı ögeyle birlikte taşı: "Model hatayı azaltmadı; yalnızca varyansı düşürdü" birleştirilince "Model yalnızca hatayı azaltmadı ve varyansı düşürdü" olmaz.

## Müdahale düzeyi ve değişiklik bütçesi

Talep kapsamını aşma: "tiyatral ifadeleri çıkar" metni baştan yazma izni değildir.

**Hafif.** Belirgin dolguyu, konuşma sızıntısını, bölüm duyurusunu, etiketi ve anonsu, üretilmiş önemi ve anlamı değiştiren kalkıyı düzelt. Cümle yapısını, paragraf sırasını ve başlıkları koru.

**Standart.** Netlik omurgasının cümle ve paragraf kurallarını, şişirme kataloğunu ve Türkçe doğallığı uygula; erken bölünmüş paragrafları birleştir; başlık hiyerarşisini koru. Varsayılan düzeydir.

**Derin.** Bilgi sırasını, paragraf ve bölüm yapısını kavramsal sınırlara göre yeniden kur: dağılmış konuları topla, hak edilmemiş başlıkları birleştir, ayrılmış kanıtı iddiasına yaklaştır. Dışarıdan dayatılan yapıyı (dergi şablonu, tekrarlanabilir deney bölümleri, güvenlik adımları, numaralı göndermeler) koru.

**Değişiklik bütçesi.** Metin zaten net ve doğalsa olduğu gibi bırak. Her değişikliğin gerekçesi netlik omurgasından, değişmezlerden ya da Türkçe doğallıktan gelir; gerekçesiz değişikliği geri al. Kısalık amaç değil, tekrar ve dolgu çıkınca ortaya çıkan sonuçtur: bilgi taşıyan cümleyi kısaltmak için kesme, paragrafı uzun diye bölme, başlığı sayıyı azaltmak için birleştirme.

**Üslup örneği.** Kullanıcı yazı örneği verdiyse cümle uzunluğunu, kişi tercihini, terim yoğunluğunu, resmiyeti ve paragraf ölçeğini ondan çıkar; yazım yanlışlarını taklit etme.

## Bilimsel ve teknik metin

Öncelikli alan budur. Kaynak yenilik, önem, mekanizma ya da sınırlılığı dayanağıyla kuruyorsa tam o güçte koru; akademik düzyazıyı gündelik konuşmaya çevirme.

**Rapor bütünlüğü.** Rapor, inceleme notu ve yönetici özetinde kanıt zincirini koru; bulgu, yorum, öneri ve karar arasındaki sınır kaynakta bulanıksa kesinleştirme. İddiayı sayısına, tablosuna, kaynak işaretine ve sınırlılığına yakın tut. Yönetici özetinde yalnızca gövdedeki bulgu, sınır ve önerileri kullan.

**Kavramsal giriş.** Yalnızca kullanıcı açıkça istediğinde, kaynaktaki bilgilerle kur: okurun bildiği bağlam → kavramı gerekli kılan gerçek problem → cevaplanacak soru → cevap olarak kavram. Kaynakta problem yoksa uydurma.

## Çalışma yöntemi

**1. Envanter çıkar.** Sayı, tarih, özel ad, alıntı, kaynak işareti, kapsam belirleyicisi, terim, sembol, bölüm numarası ve her temel iddianın statüsünü listele; hangi konunun nerede açılıp nerede yeniden açıldığını çıkar.

**2. Düzenle, katman katman.** **Bütüncül düzenleme** sırasıyla: belgede kural 1 ve 7; paragrafta paragraf testi ve kural 2–3; cümlede kural 4 ve 6; sözcükte kural 5, eşdizim, bağlayıcı ve yakın tekrar.

**3. Kaynakla karşılaştır.** Son metindeki her sayı, tarih, sonuç, nedensellik, karşılaştırma, olumsuzluk, koşul, istisna, nicelik sınırı, terim ve kişisel ayrıntının kaynakta karşılığını bul; kaynağı, statüsü ve kesinliği aynı mı? Karşılığı yoksa çıkar ya da kaynağın düzeyine döndür. Çıktıda kaynakta olmayan olumsuzluk, çekince, nedensellik, pekiştirici, karşılaştırma, tümel nicelik, zorunluluk ya da gelecek işareti belirdiyse dayanağını bul; yoksa kaldır.

**4. Netlik denetimi.** Metni konuşmayı görmemiş okur gibi baştan oku ve yazımın ya da düzenlemenin ürettiği hataları ara: eş anlamlıyla geri gelen dolgu; kayan statü, kesinlik ya da kip; bağlayıcıyla eklenmiş ilişki; bozulan devir, özne ya da gönderge; silinmiş çekince, sınırlılık, öğretici açıklama ya da gezinme başlığı; kalan sızıntı, etiket, anons ya da metne konmuş not; cümle sonu kuyruğu, biçem fiili ya da yumuşatılmış olumsuz bulgu; istenenden fazla değişiklik. Kabuk varsa son metni `scripts/style-lint.py --teslim` ile tara; 0 dönmeden teslim etme.

## Referans yönlendirmesi

- STE100 kaynağı, eşikler ve örnekler: [Netlik omurgası](references/netlik-omurgasi.md).
- Önem cümlesi, savunma, döngüsel tekrar, etiket ve anons, kalıp giriş ve sonuç: [Retorik yapılar](references/retorik-yapilar.md).
- Başlık, paragraf ve bölüm sınırları: [Yapısal bütünlük](references/yapisal-butunluk.md).
- Kopuk paragraf, belirsiz gönderge, takılan akış: [Akıcı Türkçe](references/akicilik.md).
- Tekdüze bağlaç, etiketle kurulan ilişki, yakın tekrar: [Türkçenin bağlayıcı kaynakları](references/turkce-baglayicilar.md).
- Klişe, yapay ritim, gereksiz resmiyet: [Türkçe örüntüler](references/turkce-oruntuler.md).
- Çeviri gibi okunan cümle: [Türkçe ritim ve çeviri kokusu](references/turkce-ritim-ve-ceviri-kokusu.md).
- Kanıt statüsü, çekince, edilgen çatı: [Kanıt ve kesinlik](references/kanit-ve-kesinlik.md).
- Zaman ve kip: [Zamansal ankraj ve rapor kipi](references/zamansal-ankraj-ve-rapor-kipi.md).
- Tuhaf eşdizim, kalkı, terim kararsızlığı: [Sözcük birleşimleri](references/sozcuk-birlesimleri.md).
- Olgu yığını, desteksiz bağlaç, kapsam kayması: [Metinsel tutarlılık](references/metinsel-tutarlilik.md).
- Rapor, inceleme notu, yönetici özeti: [Rapor yazımı](references/rapor-yazimi.md).
- İstenen kavramsal giriş: [Kavramsal girişler](references/kavramsal-girisler.md).
- AI ve insan metni farkları, araştırma kaynakları, yanılgılar: [İnsan ve yapay metin](references/insan-ve-yapay-metin.md).
- Konuşma sızıntısı, kullanıcıya teklif, metin dışı not: [Okura doğrudan metin](references/okura-dogrudan-metin.md).
- Hukuki, tanıtım, deneme, sosyal medya, kişisel, edebî metin, üslup eşleme: [Kenar türler](references/kenar-turler.md).

## Çıktı biçimi

Yalnızca son metni ver; `İşte düzenlenmiş metin` girişi, kapanış teklifi ya da değişiklik özeti ekleme. Not gerekiyorsa **Not metnin dışına yazılır** geçerlidir. İnceleme istendiyse: kısa teşhis, düzeltilmiş metin, en önemli değişiklikler; silinen cümlenin neden bilgi taşımadığını ve birleştirmenin hangi konu sınırına dayandığını kısaca belirt.

## Kısa örnekler

**Önce**

> Kalibrasyon, ölçüm sisteminin kalibre edilmesi işlemidir. Bu çalışmada kalibrasyon 12 referans ağırlıkla yapıldı ve doğrusallık hatası %0,8'den %0,2'ye indi. Bu sonuç, kalibrasyonun ölçüm doğruluğu açısından kritik bir rol oynadığını açıkça ortaya koymaktadır. Başka bir deyişle, kalibrasyon sayesinde ölçümler daha doğru hâle gelmiştir. Sonuç olarak, kalibrasyon ölçüm doğruluğunu artırmaktadır.

**Sonra**

> Ölçüm sistemi 12 referans ağırlıkla kalibre edildi; doğrusallık hatası %0,8'den %0,2'ye indi.

Birinci cümle terimi kendisiyle tanımlıyordu (kural 2). Son üç cümle aynı ölçümü önem, açımlama ve mini sonuç olarak yeniden söylüyordu (kural 2 ve 3); `açıkça ortaya koymaktadır` ve `artırmaktadır` tek ölçümü genel nedensel yasaya çeviriyordu (değişmezler).

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

Tek konu üç başlığa dağılmıştı (kural 1 ve 7); `belirleyici rol`, `bir sonraki bölümde görülecektir` askısı ve `yukarıda belirtilen` göndermesi bölünmenin ürettiği dolguydu.
