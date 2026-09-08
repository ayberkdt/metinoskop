# Davranışsal değerlendirmeler

Bu klasördeki vakalar tek bir beklenen metni dayatmaz. Amaç, farklı geçerli düzenlemelerin aynı kaynak sadakati ve editoryal sınırlar içinde kalıp kalmadığını değerlendirmektir.

Her vaka için:

1. `Kaynak` ve `Talep` bölümlerini `$metinoskop` ile çalıştırın.
2. Çıktıyı `Korunması gerekenler` maddeleriyle karşılaştırın.
3. `Kaçınılması gerekenler` bölümündeki ihlallerden herhangi biri varsa vakayı başarısız sayın.
4. Tek bir cümle yapısını veya sözcük seçimini zorunlu tutmayın.

Yeni bir davranış kuralı eklenirken en az bir mevcut vaka güncellenmeli veya yeni bir vaka eklenmelidir.

## Vaka grupları

**Kaynak sadakati ve kapsam:** `akademik`, `belirsizlik`, `bicim-koruma`, `hukuki`, `kapsam-ve-kosul`, `kaynak-sadakati`, `teknik`, `rapor-bulgu-yorum-oneri`, `rapor-yapisal-butunluk`, `yonetici-ozeti`.

**Ton, ses ve değişiklik bütçesi:** `kurumsal`, `kisisel`, `uslup-eslestirme`, `degisiklik-butcesi`, `kavramsal-giris`.

**Retorik mimari:** cümle, paragraf ve belge düzeyindeki yapay düzyazıyı sınar.

| Vaka | Sınanan davranış |
|---|---|
| `savunmaci-akademik` | Dayanaksız savunma çerçevesini silerken ölçülmüş yöntem gerekçesini korumak |
| `iddia-tekrar-dongusu` | Olgu → açımlama → önem → mini sonuç dizisini kaynağın kurduğu önermeye indirmek |
| `yol-haritasi` | Bölüm duyurusu ve ileri göndermeleri silip olguyu doğrudan söylemek |
| `yapay-denge` | Adlandırılmamış denge cümlelerini silerken adlandırılmış sınırlılığı korumak |
| `giris-hunisi` | Kalıp giriş hunisini atıp kaynaktaki somut gerekçeyle başlamak |
| `sonuc-ve-gelecek-calisma` | Kalıp sonuç ve üretilmiş gelecek çalışmayı silip gerçek sınırlılığı korumak |
| `soyut-yuklem` | Soyut yüklemi ölçülmüş ilişkiyle değiştirmek, türetilmiş sayı eklememek |
| `paragraf-simetrisi` | Tek biçimli paragraf mimarisini bilgi yapısına göre yeniden kurmak |
| `gerekli-ifade` | Yüzeyde yapay görünen ama teknik ayrım taşıyan içeriği korumak (yanlış pozitif) |
| `egitsel-aciklama` | Yeni başlayan için öğretici açıklamayı korumak (muhatap duyarlılığı) |
| `iyi-metin` | Zaten iyi yazılmış metni neredeyse hiç değiştirmemek |

**Yapısal bütünlük:** başlık, paragraf ve bölüm sınırlarının kavramsal sınırları izleyip izlemediğini ve okur yorgunluğunu sınar.

| Vaka | Sınanan davranış |
|---|---|
| `asiri-bolumleme` | Beş mikro başlığı tek bölüme indirirken yöntem gerekçesini ve sınırlılığı korumak |
| `derin-baslik` | Dördüncü düzey hiyerarşiyi içeriğin gerektirdiği derinliğe indirmek |
| `tek-paragraf-bolumler` | Tek paragraflık bölümleri kavramsal sınıra göre birleştirmek |
| `kisa-paragraf-yigini` | Erken bölünmüş tek cümlelik paragrafları baskın hareketlere göre toplamak; bulgu → öneri sınırını koruyabilmek |
| `yapay-gerilim` | Anlatı dramasını silip nicel ödünleşimi doğrudan yazmak |
| `tekrarlanan-bolum-girisleri` | Bölüm duyurularını ve düzenek hatırlatmalarını kaldırırken başlıkları korumak |
| `tekrarlanan-bolum-sonuclari` | Her bölümde yinelenen mini sonucu kaldırmak |
| `asiri-capraz-gonderme` | Göndermeleri silmek yerine birleştirme ve yeniden sıralamayla gereksiz kılmak |
| `uzun-cerceve-ifadeleri` | Yığılmış nitelemeyi özne, yüklem ve gerekli nitelemeye indirmek |
| `ayrilmis-kanit` | Sınırlılığı sınırladığı sonucun yanına taşımak |
| `gereksiz-listeleme` | Nedensel zinciri listeden düzyazıya çevirmek |
| `korunacak-basliklar` | Uzun belgenin gezinme başlıklarını ve yönlendirme cümlesini korumak |
| `yontem-ayrimi` | Tekrarlanabilirlik için ayrı deney bölümlerini korumak |
| `uzun-paragraf-korunur` | Tek hareket taşıyan uzun paragrafı bölmemek |
| `kisa-paragraf-korunur` | İşlevsel olarak yalıtılmış tek cümlelik uyarıyı birleştirmemek |
| `yapisal-iyi-metin` | Yapısı iyi metne dokunmamak |

**Zamansal ankraj ve rapor kipi:** tamamlanmış işin tamamlanmış olay olarak anlatılıp anlatılmadığını, genel davranışın genel kalıp kalmadığını ve düzeltmenin geçmişe zorlamaya dönüşmediğini sınar. `algoritma-genel-davranis-korunur`, `bilimsel-genelleme-korunur`, `prosedur-kilavuz-korunur`, `teknik-sistem-davranisi-korunur`, `tablo-sekil-zaman-korunur` ve `gecmise-zorlama-yok` vakalarının kayıtlı çıktısı kaynağın kendisidir.

| Vaka | Sınanan davranış |
|---|---|
| `raporda-genis-zaman-yigini` | Tamamlanmış saha çalışmasını geniş zaman yığınından tamamlanmış olay anlatımına taşımak |
| `bu-calisma-inceler` | `Bu çalışma inceler` ritmini `Çalışmada ... incelendi` eksenine çevirmek |
| `sonuclarda-genis-zaman` | Gözlenen sonucun geniş zamanla genel yasaya dönüşmesini önlemek |
| `tarihli-olay-genis-zaman` | Tarihli ve sınırlı olayı tamamlanmış anlatmak, planı gelecekte bırakmak |
| `metot-uygulamasi-gecmis` | Fiilen uygulanan yöntem adımlarını tamamlanmış olay olarak anlatmak |
| `metot-ve-uygulama-ayrimi` | Aynı paragrafta yöntem tanımını geniş zamanda, uygulamayı geçmişte tutmak |
| `sonuc-ve-yorum-kip-ayrimi` | Bulgu ile yorumu tek biçimlilik uğruna aynı kipe zorlamamak |
| `durum-raporu-uc-zaman` | Tamamlanan, süren ve planlanan işi ayrı statülerde tutmak |
| `her-seyi-edildi-yapma` | Düzeltmenin tek biçimli edilgen geçmiş zincirine dönüşmesini önlemek |
| `mistir-yigini-yapma` | Geniş zamanı yaygın `-mıştır` ile değiştirmemek |
| `gecmis-genel-yasa-bozmasin` | Geçmişe çevirirken genel bilimsel ilişkiyi bozmamak |
| `algoritma-genel-davranis-korunur` | Algoritma tanımını geniş zamanda bırakmak (yanlış pozitif) |
| `bilimsel-genelleme-korunur` | Genel bilimsel ilişkiyi geçmişe çekmemek |
| `prosedur-kilavuz-korunur` | Yeniden kullanılabilir prosedürü tek seferlik bakıma indirmemek |
| `teknik-sistem-davranisi-korunur` | Ürün belirtimini test kaydına çevirmemek |
| `tablo-sekil-zaman-korunur` | Belge göndermelerinin farklı kiplerini korumak |
| `gecmise-zorlama-yok` | Gerekçeli kip çeşitliliğine dokunmamak |

**Çeviri gölgesi ve Türkçe ritim:** dil bilgisi doğru olduğu hâlde İngilizce cümle iskeleti taşıyan metinde ilişkinin Türkçe kaynaklarla yeniden kurulup kurulmadığını ve yerli yapıya dokunulmadığını sınar. Her "korunur" vakasının kayıtlı çıktısı kaynağın kendisidir.

| Vaka | Sınanan davranış |
|---|---|
| `tekrarlanan-acik-ozne` | Ardışık cümlelerde yinelenen açık özneyi tek aktörlü paragrafta düşürmek veya birleştirmek |
| `bu-sonuc-ritmi` | `Bu sonuç / bu bulgu / bu durum` paketini çözüp önermeyi doğrudan söylemek |
| `asiri-bir` | Tanımlık kalkısı `bir` sözcüklerini azaltırken sayı ve gerçek tekillik bildirenleri korumak |
| `sahip-olmak-kalkisi` | `X, Y'ye sahiptir` kalkısını ilişki türüne göre iyelik, sıfat veya fiille kurmak; mülkiyet ve yetki dilini korumak |
| `bulunmaktadir-kalkisi` | `Bulunmaktadır / yer almaktadır / mevcuttur / içermektedir` kalıplarını doğrudan varlık veya iyelik ilişkisiyle kurmak |
| `ve-zinciri` | Bağımsız çekimli cümle zincirini `-ip`, noktalı virgül ve aktör değişimine göre yeniden kurmak |
| `dogal-ve-korunur` | Eş düzeyli iki olguyu bağlayan `ve` bağlacını sıraya veya karşıtlığa çevirmemek |
| `yararli-ip-yapisi` | Belirteçle dizilmiş sıralı adımları `-ip` ve `-dikten sonra` ile kurmak |
| `asiri-ip-zinciri` | Tek yükleme asılı yedi fiilimsiyi kavramsal sınırda bölmek |
| `art-niteleme` | Adın ardına eklenen İngilizce nitelemeyi ad önü ortaçla kurmak |
| `gerekli-olan` | Koşulu sınırlayan tek `olan` yapısını korumak |
| `gereksiz-olan` | `Olan` zincirini ve `sahip olan` kalkılarını sıfat ve iyelikle çözmek |
| `cerceve-yigini` | `Açısından / kapsamında / bağlamında / noktasında` yığınını hâl eki, iyelik veya fiille kurmak |
| `gerekli-acisindan` | Gerçek karşılaştırma eksenini kuran `açısından` çiftini korumak |
| `soyut-ad-yuklemi` | Soyut ad yüklemlerini ve hafif yüklemleri kaynağın desteklediği fiille kurmak; ölçülmemiş etkiyi ölçülmüş gibi yazmamak |
| `teknik-adlastirma-korunur` | Teknik işlemi ve tablo büyüklüğünü adlandıran isim-fiil ve iyelik zincirini korumak |
| `ozne-dusurme-akisi` | Tek aktörlü sürüm notunda özne düşürerek akışı kurmak |
| `belirsizlik-icin-acik-ozne` | Dönüşümlü iki aktörde açık özne tekrarını korumak |
| `dogal-uzun-cumle-korunur` | Tek ana önerme ve denetimli tümleç taşıyan uzun cümleyi bölmemek |
| `asiri-yuklu-cumle` | İç içe çerçeve ve uzak yüklemli cümleyi kavramsal sınırda bölmek, sonucu uydurmamak |
| `ingilizce-soylem-belirtecleri` | Belirteçle etiketlenmiş ilişkileri `ise`, `de/da` ve `-dığından` ile kurmak; kapsam sınırını korumak |
| `hukuki-kalip-korunur` | Sözleşme dilinde yinelenen tarafı, `işbu`, `söz konusu`, `takdirde` kalıplarını korumak |
| `teknik-ozne-tekrari-korunur` | Ayrı kaydedilen adımlarda açık özne tekrarını korumak |
| `yerli-turkce-metin` | Zaten Türkçe düşünülmüş metne dokunmamak |

**Epistemik mimari:** kimin bildiğini, nasıl bildiğini, ne kadar kesin iddia ettiğini ve her iddianın statüsünü düzenleme boyunca koruyup korumadığını sınar.

| Vaka | Sınanan davranış |
|---|---|
| `edilgen-korunur` | Aktörü adlandırmayan yöntem paragrafında edilgen çatıyı korumak, aktör uydurmamak |
| `edilgen-etkene` | Aktörü açık olan "tarafından" zincirini etkene çevirmek |
| `bilinmeyen-aktor` | Belirsiz aktörü tek özneye çözmemek |
| `aktarim-olgu-olmaz` | İki ayrı kaynağa atıflı iddiaları atıflı tutmak, ölçümü olgu olarak bırakmak |
| `olcum-ile-cikarim` | Ölçüm ile çıkarımı ayırmak; çıkarımı nedensel olguya çevirmemek |
| `cekince-korunur` | Kanıt düzeyi taşıyan çekince ve kapsam sınırını korumak |
| `kiplik-yigini` | Aynı şeyi söyleyen üç kiplik işaretini teke indirmek; atıf ile olasılığı birlikte korumak |
| `dayanaksiz-pekistirici` | "Açıkça kanıtlamaktadır" pekiştiricisini kaynağın sınırlı gözlemine indirmek |
| `mesru-guclu-iddia` | Ölçümle desteklenen kesin iddiaya çekince eklememek |
| `gerekceli-kip-degisimi` | Dört işlevli dört kipi korumak |
| `uslup-kip-nobetlesmesi` | Tek bakış açısına ait beş cümledeki kip nöbetleşmesini gidermek |
| `oneri-karar-degil` | Öneriyi karara, beklentiyi taahhüde çevirmemek |
| `karar-uygulama-degil` | Kararı uygulamaya, planı sonuca çevirmemek |
| `gozlenmedi-yoktur-degil` | "Gözlenmedi", "sınanmadı", "çözümsüz" statülerini ayrı tutmak |
| `atif-kapsami` | Atıflı yorumdan sonra gelen "bu nedenle" olgusunu kaldırmak |
| `kapsam-isareti-baglanmasi` | `Yalnızca` işaretinin bağlandığı ögeyi korumak |
| `sonuc-sonuclardan-guclu` | Tartışma ve sonuç bölümlerini sonuçlar bölümünün kanıt düzeyine indirmek |
| `iyi-akademik-paragraf` | Kanıt düzeyini zaten doğru taşıyan paragrafa dokunmamak |

**Eşdizim ve istem:** sözcüklerin doğal Türkçedeki gibi birleşip birleşmediğini ve teknik ayrımların korunup korunmadığını sınar.

| Vaka | Sınanan davranış |
|---|---|
| `tuhaf-esdizim` | Dil bilgisi doğru ama deyimsel olmayan eşdizimleri alışılmış eşleşmeyle kurmak |
| `teknik-esdizim-korunur` | Alanın terim eşdizimlerini korumak |
| `yanlis-hal-cercevesi` | İngilizce edat izini taşıyan hâl çerçevelerini fiilin doğal istemiyle kurmak |
| `dogru-alisilmadik-hal` | Farklı ilişki kuran çıkma ve yönelme hâllerini korumak |
| `edat-aktarimi` | Çift ilgeçleri kaldırmak, gerçek ilişki kuran `üzerinden` ifadesini korumak |
| `hafif-fiil-sismesi` | Hafif fiilleri gerçek yüklemle kurmak, prosedür adını korumak |
| `surec-adi-korunur` | Süreç adı olan hafif fiil kuruluşunu korumak |
| `genel-fiil-kesin-iliski` | Dört "göstermektedir" yükleminin gizlediği dört ilişkiyi yazmak |
| `epistemik-guvensiz-fiil` | Hafif yüklemi kurarken nedensel fiil eklememek |
| `esanlam-kaymasi-teknik` | Aynı büyüklüğe gönderen teknik terimleri tek terimde toplamak |
| `kanonik-terim-tekrari` | Yinelenen kanonik terimi çeşitlendirmemek |
| `varlik-yeniden-adlandirma` | Beş adla anılan tek varlığı tek adla kurmak |
| `hukuki-formul-korunur` | "Kabul ve taahhüt eder" formülünü korumak |
| `dogal-is-epostasi` | Zaten doğal e-postaya kurumsal eşdizim dayatmamak |
| `odunc-terim-korunur` | Alanın ödünç terimlerini (`baseline`, `pipeline`, `benchmark`) korumak |

**Metinsel tutarlılık ve konu ilerleyişi:** metnin bir düşünceyi geliştirip geliştirmediğini, bağlaçların gerçek ilişki taşıyıp taşımadığını ve kapsam, olumsuzluk, kayıt ve noktalamanın korunup korunmadığını sınar.

| Vaka | Sınanan davranış |
|---|---|
| `olgu-yigini` | Olgu yığınını işlevlere göre gruplamak, ilişki uydurmamak |
| `sabit-konu-korunur` | Prosedürdeki sabit konu ilerleyişini korumak |
| `dogrusal-ilerleyis-korunur` | Doğrusal ilerleyişi yeniden sıralamamak |
| `desteksiz-bu-nedenle` | Önermelerin desteklemediği "bu nedenle" ilişkisini kaldırmak, öncül uydurmamak |
| `gecerli-nedensel-baglac` | Kaynağın kurduğu nedensel bağlacı korumak |
| `esanlam-donusu` | Sonuç, bulgu, çıktı, gözlem dönüşünü tek terimde toplamak |
| `gerekli-ad-tekrari` | Karşıtlık kuran grup adlarının yinelenmesini korumak |
| `uzak-bu` | Dört olası öncüle sahip "bu" göndergesini rastgele çözmemek |
| `kisa-mesafe-eksilti` | Tek ve yakın öncülde yeniden tanıtım eklememek |
| `bolum-basi-sifirlama` | Her bölümde yinelenen düzenek cümlesini teke indirmek, başlıkları korumak |
| `temiz-devir` | Doğal paragraf devrine duyuru eklememek |
| `islev-kaymasi` | Sonuçtan öneriye kayan paragraftaki dayanaksız öneriyi kaldırmak |
| `kronoloji-nedensellik` | Kronolojiyi nedenselliğe çeviren bağlacı kaldırmak |
| `kapsam-isareti-tasinmasi` | Kapsam işaretinin bağlandığı ögeyi korumak |
| `olumsuzluk-kapsami` | Cümle birleştirirken olumsuzluğun kapsamını korumak |
| `kayit-kaymasi` | Üç mikro kaydı tek akademik kayıtta kurmak |
| `bilincli-kayit-degisimi` | Uyarı kutusunun bilinçli kayıt değişimini korumak |
| `ingilizce-noktalama` | Uzun çizgili ara söz ve özne–yüklem virgülünü Türkçe gruplamaya çevirmek |
| `teknik-noktalama-korunur` | Ondalık listedeki noktalı virgülü ve parantez içi göndermeyi korumak |
| `uzak-sinirlilik` | Sınırlılığı sınırladığı iddianın yanına getirmek |
| `ayni-iddia-yeni-rol` | Üç bölümde üç rol taşıyan aynı ölçümü korumak |
| `ayni-iddia-hacim` | Aynı önermenin açımlamalarını kaldırmak |
| `tutarli-metin-korunur` | Zaten tutarlı metne dokunmamak |

## Hakem ölçütleri

İnsan veya model hakemi her çıktıda şu soruları ayrıca sorar:

1. **Sıfır bilgi cümlesi:** Çıktıda, silindiğinde hiçbir önerme, ilişki, kronoloji, yorum veya yazar tavrı kaybolmayacak ve önceki bilgiyi sentezlemeyen cümle kaldı mı? Yeni önerme eklemeyen ama birden çok bulguyu tek karar cümlesinde toplayan ya da okurun çıkarım yükünü azaltan cümle yanlışlıkla silinmiş mi?
2. **İşlev tekrarı:** Sözcükleri farklı ama işlevi aynı cümleler (önem bildirme, yeniden ifade, mini sonuç) tekrarlanıyor mu?
3. **Savunmacı düzyazı:** Somut bir yanlış anlamayı önlemeyen savunma cümlesi kaldı mı? Dayanaklı yöntem gerekçesi yanlışlıkla silindi mi?
4. **Dolguyu dolguya çevirme:** Silinmesi gereken önem, karşıtlık, duyuru veya denge cümlesi daha sakin eş anlamlılarla geri konmuş mu?
5. **Paragraf ve belge mimarisi:** Paragraflar tek biçimli mi? Her paragraf önem cümlesiyle mi bitiyor? Giriş ve sonuç kalıp mı? Uzunluklar insan gibi görünsün diye rastgeleleştirilmiş mi?
6. **Muhatap duyarlılığı:** Uzman metninde açık olanın açıklaması kaldı mı? Yeni başlayan metninden öğretici açıklama silindi mi?
7. **Koruma:** Kesinlik düzeyi, kapsam, adlandırılmış sınırlılık, atıf, biçim ve yazar sesi korunmuş mu? Metin gündelikleşmiş veya telgraf diline dönmüş mü?
8. **Başlık ve bölüm sınırları:** Her başlık hakkını kazanıyor mu; tek paragraflık bölümler, gereksiz derinlik veya "başlık → kısa açıklama" slayt deseni kaldı mı? Kullanıcının istediği düzey aşılarak başlıklar değiştirilmiş mi? Tekrarlanabilirlik, mevzuat, dergi kuralı, güvenlik adımları veya gezinme gerektiren bölümler korunmuş mu?
9. **Paragraf ve yakınlık:** Paragraflar erken bölünmüş mü, tek baskın hareket taşıyan uzun paragraf bölünmüş mü, işlevsel kısa paragraf birleştirilmiş mi? Bulgu, yorum ve öneri sırf aynı konu diye tek yoğun blokta paketlenmiş mi? Sonuç ile sınırlılığı, iddia ile kanıtı, yöntem ile gerekçesi yakın mı? Bağlam her birimde yeniden başlatılıyor mu; çapraz gönderme, askı, yapay gerilim, boş sarmalayıcı veya zorlama geçiş kaldı mı?
10. **Parçalanma ve şişkinlik dengesi:** Uzun çerçeve ifadeleri kısaltılmış mı; birleştirme tek cümleye birkaç iddia, niteleme ve sonuç yığmış mı; nedensel akıl yürütme listeye çevrilmiş mi? Değişiklik yalnızca kısaltma mı, yoksa süreklilik, anlama, gezinme veya yakınlık kazancı mı sağlıyor?
11. **Kaynak dil gölgesi:** Çıktı hâlâ belirgin bir İngilizce iskelet taşıyor mu? Açık özne gereksiz yere yineleniyor mu; `bu sonuç`, `bu durum` söylem adları paragrafı her seferinde yeniden başlatıyor mu; tanımlık gibi `bir` yinelemesi kalmış mı; `have` daha doğal bir iyelik ilişkisi varken `sahip olmak` olarak kalmış mı; cümleler hâlâ İngilizce tarzı bağımsız birimler olarak `ve`, `ancak`, `sonra` ile dizili mi; çerçeve adları yığılı mı? Cümle İngilizceye geri çevrildiğinde özgün iskelet neredeyse değişmeden çıkıyor mu?
12. **Türkçe kaynak kullanımı:** Düzenleme Türkçe biçim bilgisini (özne düşürme, eksilti, `-ip`, `-ince`, `-dığından`, ortaç, iyelik, hâl eki, `de/da`, sözcük sırası) doğal biçimde kullanmış mı? Konu → odak → yüklem akışı doğal mı? Metin Türkçeye çevrilmiş gibi değil, Türkçe düşünülmüş gibi okunuyor mu?
13. **Gölge avında aşırı düzeltme:** Fiilimsi fazlası var mı; iki aktörlü paragrafta özne düşürülüp belirsiz eksilti yaratılmış mı; gerekli `olan`, `açısından`, `ve` ya da açık özne silinmiş mi; hukuki kalıp, teknik adlaştırma veya terim değiştirilmiş mi; bilimsel kesinlik ("ilişkili" → "neden olur") zayıflatılmış mı; yapay yerlilik (arkaik sözcük, zorlama deyim, konuşma edatı, gereksiz devriklik) eklenmiş mi; zaten yerli metne dokunulmuş mu?
14. **Epistemik mimari:** Her önemli iddianın kaynağı kim? Düzenleme gözlemi çıkarıma, çıkarımı olguya, ilişkiyi nedenselliğe çevirdi mi? Edilgen–etken dönüşümü sorumluluğu değiştirdi ya da aktör uydurdu mu? Atıf kayboldu ya da yönettiği önermeden uzaklaştı mı? Çekince–pekiştirici dengesi taahhüdü değiştirdi mi? Kip değişimi zamansal bakış açısını değiştirdi mi? İddia tartışma ya da sonuçta güçlendi mi? "Gözlenmedi" "yoktur", öneri karar ya da uygulama oldu mu?
15. **Sözcük uyumu:** Sözcükler doğal birleşiyor mu? Her ana fiil doğru hâl ve tümleci alıyor mu? İngilizce edat tuhaf bir ilgeç üretmiş mi? Hafif fiil daha yalın yüklemi gizliyor mu? Yeniden yazım anlam ilişkisini güçlendirdi mi? Eş anlamlı değişimi teknik ayrımı bulanıklaştırdı mı? Ana varlıklar tutarlı adlandırılıyor mu? Seyrek ama geçerli bir birleşim yanlışlıkla normalleştirildi mi?
16. **Metinsel tutarlılık:** Her cümle etkin olandan mı büyüyor? Paragraf konu mu geliştiriyor, olgu mu yığıyor? Her bağlaç gerçek bir ilişkiye mi karşılık geliyor? Sözcük zincirleri kararlı mı? Göndergeler mesafelerinde geri kazanılabilir mi? Paragraflar birbirine doğal devrediyor mu? Sözcük sırası değişimi kapsam ya da odağı değiştirdi mi? Olumsuzluk aynı önermeye bağlı mı? Kayıt kaydı mı? Noktalama Türkçe gruplamaya yardım ediyor mu? İddia ile dayanağı yeterince yakın mı?

Bu ölçütler `Kaçınılması gerekenler` maddelerinin üstünde, bütün vakalara uygulanan genel denetimdir.

## Deterministik ön denetimler

### Kaynak değişmezleri

Bir model çıktısını kaynakta açıkça korunan değişmezler bakımından denetlemek için:

```bash
python scripts/eval-runner.py evals/teknik.md outputs/teknik.txt
```

Çalıştırıcı sayı, tarih, URL, kod, dipnot, kapsam belirleyicisi, teknik ad, sembol, denklem numarası ve ölçüm kayıplarını yakalar. Birebir çıktı karşılaştırması yapmaz. Akıcılık, ton, gönderge yorumu ve genel anlam uyumu elle veya model hakemiyle değerlendirilmelidir.

### Stil denetimi

Çıktıdaki şüpheli retorik örüntüleri işlev ailesine göre işaretlemek için:

```bash
python scripts/style-lint.py outputs/iddia-tekrar-dongusu.txt --source evals/iddia-tekrar-dongusu.md
```

`scripts/style-lint.py` üretilmiş önem, savunmacı açıklama, yol haritası, kalıp giriş ve sonuç, üretilmiş karşıtlık, zorlama denge, soyut yüklem, boş özne ve sohbet botu kalıntısı ailelerini işaretler; paragraf uzunluğu tek biçimliliği, önem cümlesiyle kapanış oranı, `-maktadır` zinciri ve işlev tekrarı gibi yapı bulgularını raporlar. `--source` verildiğinde kaynakta olmayıp çıktıda beliren kalıpları kalıp düzeyinde ayrıca listeler; aynı aileden farklı bir kalıp da yeni sayılır. Bu, dolgunun başka dolguya çevrildiğine ilişkin güçlü bir deterministik işarettir; kaynakta olup çıktıda kalan sert aileler ise hakemin silme testiyle incelemesi için listelenir. Çıkış kodu sert ve bağlamsal aileleri ayırır: `--fail-on-introduced-hard` yalnızca kaynakta olmayan bir sert bastırma kalıbı eklenmişse 1 döndürür; `yani`, `öte yandan`, `işaret etmek` gibi bağlamsal aileler yalnızca uyarı olarak listelenir, çünkü skill bunları otomatik silmeyi yasaklar. `--fail-on-introduced-any` katı moddur. Rapor ayrıca parçalanma yoğunluğunu (başlık sayısı ve derinliği, başlık başına paragraf, tek paragraflık bölüm, kısa paragraf oranı, liste ögesi, çapraz gönderme) özetler ve `--source` ile bu ölçülerdeki değişimi gösterir; `korunacak-basliklar` veya `yontem-ayrimi` gibi vakalarda başlık sayısının düşmesi hata işaretidir, `asiri-bolumleme` gibi vakalarda beklenen sonuçtur.

Denetim tek bir sözcüğe bakarak metni reddetmez. `gerekli-ifade` ve `iyi-metin` vakalarında işaretlenen ifadelerin çoğu kalmalıdır; işaret, hakemin işlevi incelemesi içindir.

Rapor ayrıca çeviri gölgesi ölçülerini verir: `sahip olmak` ve varlık kalıbı işaretleri, tek cümlede iki farklı (ya da üç) çerçeve adı, tek cümlede iki `olan`, aynı bir iki sözcükle başlayan üç ardışık cümle (`tekrarlanan cümle başlangıcı`: özne tespiti değildir, "İlk deney ... İlk sonuç ..." de yakalanır; tekrarın özne tekrarı olup olmadığına hakem karar verir), tek cümlede üç `ve`, tek yükleme asılı dört fiilimsi, üç ardışık iyelik eki, söylem belirteciyle başlayan cümle oranı ve 100 sözcük başına `bir`. Bunların hiçbiri sert aile değildir; hepsi "bu yapı Türkçede bağımsız olarak doğal mı?" sorusu için inceleme işaretidir. Tek `bir`, `olan`, `ve` ya da `açısından` hiçbir zaman işaretlenmez; `gerekli-acisindan` vakasındaki "maliyet açısından ucuz, süre açısından pahalı" çifti paralel eksen sayılır, yığın sayılmaz. `--source` ile kaynakta olmayıp çıktıda beliren çeviri gölgesi bulguları uyarı olarak listelenir; bunlar yeni bir kalkı ya da aşırı düzeltme (fiilimsi yığını) işareti olabilir.

Söylem ölçüleri de yalnızca inceleme içindir: çekince (`olabilir`, `düşünülebilir`, `görünmektedir`), pekiştirici (`açıkça`, `kesin olarak`, `kanıtlamaktadır`), aktarım (`bildirdi`, `belirtti`, `-e göre`) ve hafif fiil (`gerçekleştirmek`, `iyileştirme sağlamak`) aileleri bağlamsaldır; tek cümlede iki çekince (kiplik yığını), pekiştirici ile çekince çatışması, atıflı cümleden sonra gelen "bu nedenle" (aktarım sonrası sonuç), bir paragrafta üç farklı kip ve üç geçiş (kip nöbetleşmesi), iki adlaştırma ile edilgen yüklem, iki ilgeç, üç genel ad (yöntem/yaklaşım/yapı ya da sonuç/bulgu/çıktı), "bu çalışmada" ile açılan iki paragraf, ara söz yükü ve sohbet gerilimi ile bürokratik kayıt çatışması bulgu olarak listelenir. Hiçbir regex epistemik doğruluğa karar vermez; `mesru-guclu-iddia` ve `gerekceli-kip-degisimi` gibi vakalarda işaretlenen yapı kalmalıdır.

### Kayıtlı çıktılar üzerinde regresyon

`evals/outputs/<vaka>.txt` dosyaları referans düzenlemelerdir: tek doğru çıktı değil, skill'in belgelenen davranışını sessizce kaybetmemek için sabitlenmiş örneklerdir. Yapısı korunması gereken vakalarda kayıtlı çıktı kaynağın kendisidir. `python scripts/eval-suite.py` her kayıtlı çıktı için üç deterministik denetim yapar ve CI'da çalışır:

1. `eval-runner.py` ile kaynak değişmezleri (sayı, tarih, kod, kapsam belirleyicisi); başlık satırlarındaki noktalı bölüm numaraları (`2.3`, `3.1.1`) olgu sayılmaz.
2. `style-lint.py` ile kaynakta olmayan sert kalıp eklenip eklenmediği; bağlamsal aileler uyarı olarak listelenir.
3. Vakanın isteğe bağlı `## Serbest değişmezler` bölümü: kaynakta geçen ama dolgu olduğu için silinmesi beklenen kapsam ya da kesinlik işaretini (`- bazı — "bazı sınırlılıkları bulunmaktadır" adlandırılmamış denge dolgusudur`) değişmez denetiminden muaf tutar; her muafiyet gerekçeli olmalıdır ve yalnızca `kapsam` ile `kesinlik` gruplarına uygulanır.
4. Vakanın isteğe bağlı `## Yapısal beklenti` bölümündeki ölçüler: `- başlık: <= 1`, `- en derin düzey: <= 3`, `- düzyazı paragrafı: 4`, `- liste ögesi: 0`, `- çapraz gönderme: 0`, `- duyuru/sarmalayıcı: 0`, `- sert işaret: 0`, `- cümle: 4` gibi satırlar (`=`, `<=`, `>=`, `<`, `>`). Çeviri gölgesi ölçüleri de kullanılabilir: `- sahip olmak: 0`, `- varlık kalıbı: <= 1`, `- çerçeve yığını: 0`, `- olan zinciri: 0`, `- tekrarlanan cümle başlangıcı: 0`, `- ve zinciri: 0`, `- fiilimsi yığını: 0`, `- iyelik zinciri: 0`, `- bağlaçla başlayan cümle: <= 1`, `- bir / 100 sözcük: <= 6`. Söylem ölçüleri: `- kiplik yığını: 0`, `- pekiştirici: 0`, `- pekiştirici çatışması: 0`, `- aktarım sonrası sonuç: 0`, `- kip nöbetleşmesi: 0`, `- edilgen adlaştırma: 0`, `- hafif fiil: 0`, `- ilgeç yoğunluğu: 0`, `- eş anlamlı kayması: 0`, `- konu sıfırlama: 0`, `- parantez yükü: 0`, `- kayıt kayması: 0`.

Her vakanın kayıtlı bir referans çıktısı vardır ve CI `--require-all` ile çalıştığından yeni vaka çıktısız eklenemez; yapı korunacaksa kaynağı olduğu gibi kaydedin. Kayıtlı çıktı ("gold") bir sözleşmedir: skill'in kendi kurallarını ihlal eden bir gold yanlış davranışı kilitler. Bu yüzden her gold, kaydedilmeden önce kaynağına karşı şu üç soruyla okunur: hangi iddia hangi epistemik statüde (gözlem, ölçüm, aktarım, çıkarım, öneri, karar) ve çıktıda aynı statüde mi; kaynağa olumsuz iddia ya da yeni çekince eklenmiş mi; daha doğrudan bir fiil nedensellik kurmuş mu? Rastgele atanmamış iki grup arasındaki farkı "etkiler" ya da "azaltır" diye yazan, "karar sürecine girdi"yi "henüz karar vermedi"ye çeviren ya da şişmiş iddiayı indirirken "mekanizma ortaya konmamıştır" ekleyen gold bu denetimde düzeltilmiştir. `python scripts/eval-suite.py --export-judge-prompts build/judge` her vaka için kaynak, talep, kayıtlı çıktı ve ölçütleri içeren bir model hakem istemi üretir.

### Gerçek model regresyonu

Kayıtlı çıktı denetimi fixture'ları sınar, skill'i değil: `SKILL.md` bozulsa da eski çıktılar yerinde durduğu için yeşil kalır. `scripts/behavioral-regression.py` bu boşluğu kapatır: `SKILL.md` ve referans dosyalarını sistem istemi olarak gerçek bir modele verir, her vakanın talebini kaynağına uygulatır, taze çıktıyı önce `eval-runner.py` değişmezleri ve `style-lint.py` sert kalıp denetiminden geçirir, sonra bir model hakemine vakanın koruma ve kaçınma maddeleri ile bu dosyadaki hakem ölçütlerine göre puanlatır. Hakem son satırda `SONUÇ: GEÇTİ` ya da `SONUÇ: BAŞARISIZ` yazar; her vaka hem deterministik hem hakem kapısından geçmelidir.

```bash
python scripts/behavioral-regression.py --dry-run
python scripts/behavioral-regression.py
python scripts/behavioral-regression.py --all
```

Varsayılan küme `evals/critical-cases.txt` dosyasındaki yirmi vakadır: beş epistemik, beş çeviri gölgesi, beş yapı, beş "doğal metni koru". Her çalıştırma gerçek para harcadığı için `.github/workflows/behavioral.yml` bu kümeyi haftalık ve elle tetiklemeyle çalıştırır (`ANTHROPIC_API_KEY` sırrı gerekir); her push'ta çalışan `validate.yml` yalnızca deterministik denetimleri içerir. Taze çıktılar, hakem raporları ve `summary.json` `build/behavioral/` altına yazılır.

Rapor vakalarında ayrıca bulgu, yorum, sınırlılık, öneri ve karar statülerinin korunup korunmadığını; tablo, başlık ve çapraz göndermelerin doğru içeriğe bağlı kalıp kalmadığını inceleyin. Bu ilişkiler yalnızca sözcük varlığıyla güvenilir biçimde ölçülemediği için değerlendirme insan veya model hakemi gerektirir.
