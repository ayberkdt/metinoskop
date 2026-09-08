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

Rapor ayrıca çeviri gölgesi ölçülerini verir: `sahip olmak` ve varlık kalıbı işaretleri, tek cümlede iki farklı (ya da üç) çerçeve adı, tek cümlede iki `olan`, aynı bir iki sözcükle başlayan üç ardışık cümle, tek cümlede üç `ve`, tek yükleme asılı dört fiilimsi, üç ardışık iyelik eki, söylem belirteciyle başlayan cümle oranı ve 100 sözcük başına `bir`. Bunların hiçbiri sert aile değildir; hepsi "bu yapı Türkçede bağımsız olarak doğal mı?" sorusu için inceleme işaretidir. Tek `bir`, `olan`, `ve` ya da `açısından` hiçbir zaman işaretlenmez; `gerekli-acisindan` vakasındaki "maliyet açısından ucuz, süre açısından pahalı" çifti paralel eksen sayılır, yığın sayılmaz. `--source` ile kaynakta olmayıp çıktıda beliren çeviri gölgesi bulguları uyarı olarak listelenir; bunlar yeni bir kalkı ya da aşırı düzeltme (fiilimsi yığını) işareti olabilir.

### Kayıtlı çıktılar üzerinde regresyon

`evals/outputs/<vaka>.txt` dosyaları referans düzenlemelerdir: tek doğru çıktı değil, skill'in belgelenen davranışını sessizce kaybetmemek için sabitlenmiş örneklerdir. Yapısı korunması gereken vakalarda kayıtlı çıktı kaynağın kendisidir. `python scripts/eval-suite.py` her kayıtlı çıktı için üç deterministik denetim yapar ve CI'da çalışır:

1. `eval-runner.py` ile kaynak değişmezleri (sayı, tarih, kod, kapsam belirleyicisi); başlık satırlarındaki noktalı bölüm numaraları (`2.3`, `3.1.1`) olgu sayılmaz.
2. `style-lint.py` ile kaynakta olmayan sert kalıp eklenip eklenmediği; bağlamsal aileler uyarı olarak listelenir.
3. Vakanın isteğe bağlı `## Yapısal beklenti` bölümündeki ölçüler: `- başlık: <= 1`, `- en derin düzey: <= 3`, `- düzyazı paragrafı: 4`, `- liste ögesi: 0`, `- çapraz gönderme: 0`, `- duyuru/sarmalayıcı: 0`, `- sert işaret: 0`, `- cümle: 4` gibi satırlar (`=`, `<=`, `>=`, `<`, `>`). Çeviri gölgesi ölçüleri de kullanılabilir: `- sahip olmak: 0`, `- varlık kalıbı: <= 1`, `- çerçeve yığını: 0`, `- olan zinciri: 0`, `- ardışık özne: 0`, `- ve zinciri: 0`, `- fiilimsi yığını: 0`, `- iyelik zinciri: 0`, `- bağlaçla başlayan cümle: <= 1`, `- bir / 100 sözcük: <= 6`.

Yeni bir vaka eklerken mümkünse kayıtlı bir referans çıktı ve yapısal beklenti de ekleyin; yapı korunacaksa kaynağı olduğu gibi kaydedin. `python scripts/eval-suite.py --export-judge-prompts build/judge` her vaka için kaynak, talep, kayıtlı çıktı ve ölçütleri içeren bir model hakem istemi üretir; sabit bir model üzerinde tam davranışsal regresyon (taze çıktı üretip hakemle puanlama) bu depoda henüz otomatik değildir ve sonraki olgunluk adımıdır.

Rapor vakalarında ayrıca bulgu, yorum, sınırlılık, öneri ve karar statülerinin korunup korunmadığını; tablo, başlık ve çapraz göndermelerin doğru içeriğe bağlı kalıp kalmadığını inceleyin. Bu ilişkiler yalnızca sözcük varlığıyla güvenilir biçimde ölçülemediği için değerlendirme insan veya model hakemi gerektirir.
