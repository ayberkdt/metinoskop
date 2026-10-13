# Netlik omurgası

Metinoskop'un ana sözleşmesi tek cümledir: okur her önermeyi bir kez, doğru yerde, kaynağın verdiği kesinlikle bulmalıdır. Bu dosya, `SKILL.md`'deki yedi netlik kuralının nereden geldiğini, Türkçeye nasıl uyarlandığını, eşiklerin nasıl okunacağını ve her kural için dönüşüm ve korunma örneklerini verir.

## Kaynak: ASD-STE100

ASD-STE100 (Simplified Technical English, STE), havacılık ve savunma sanayisinde teknik belgeler için geliştirilmiş, ASD'nin sahibi olduğu kontrollü bir İngilizce standardıdır. Standardın iki parçası vardır: yazım kuralları ve onaylı sözcükleri içeren bir sözlük. Güncel sürüm Issue 9'dur (2025). Standart iki metin türünü ayırır: **prosedür** (okura ne yapacağını söyleyen talimat) ve **betimleme** (bir şeyin ne olduğunu, nasıl çalıştığını anlatan metin).

Bu depoda kullanılan kural özetleri ikincil kaynaklara dayanır (Wikipedia'nın "Simplified Technical English" maddesi ve standardı özetleyen kamu sayfaları). Resmî metin bu dosya yazılırken okunamadı. Aşağıdaki maddeler STE'nin kendi kuralı ile Metinoskop'un uyarlamasını ayrı tutar. Bir STE kuralı alıntılanacaksa resmî metinden doğrulanmalıdır.

**Alınanlar.** Yazım ilkeleri: kısa cümle, paragraf başına tek konu, kısa paragraf, uzun ad öbeğinden kaçınma, etken çatı, bir sözcüğe bir anlam, talimatta cümle başına bir adım, karmaşık içerik için dikey liste, kısaltmak için cümle ögesi düşürmeme.

**Alınmayanlar.** Onaylı sözcük sözlüğü, İngilizce fiil biçimi kısıtları ve tanımlık kuralları. Bunlar İngilizceye özgüdür ve Türkçe için bir karşılığı yoktur. Türkçe eklemeli bir dildir: aynı ilişki ekle, ortaçla ya da zarf-fiille kurulabilir. Bu yüzden STE'nin sözcüğe bağlı kuralları değil, işleve bağlı kuralları uyarlanmıştır.

**Uyarlamanın gerekçesi.** STE'nin ilkeleri metnin türünden bağımsız olarak okurun yükünü azaltır: okur bir cümlede bir şeyi, bir paragrafta bir konuyu izler; aynı kavrama hep aynı adla rastlar. Metinoskop'un önceki kuralları (sıfır bilgi cümlesi, açımlama döngüsü, işlev tekrarı, yinelenme haritası, terim tutarlılığı, yapısal bütünlük) zaten bu ilkelerin yerel biçimleriydi; omurga onları tek bir sözleşme altında toplar. STE'de "döngüsel anlatım yasağı" diye ayrı bir kural yoktur. Metinoskop'un ikinci kuralı (her önermeyi bir kez söyle), STE'nin "paragraf başına tek konu" ilkesinin belge düzeyindeki sonucudur: bir konu tek paragrafta bitirilirse başka yerde yeniden açılmasına gerek kalmaz.

## Eşleme tablosu

| STE ilkesi (ikincil özet) | Metinoskop kuralı | Türkçe uyarlama | Ayrıntı |
|---|---|---|---|
| Paragraf başına tek konu; paragraf en çok altı cümle | 1. Bir paragraf, bir konu | Altı cümle inceleme eşiğidir; tek hareketi yürüten uzun paragraf korunur. Dağılmış konu toplanır. | `yapisal-butunluk.md`, `metinsel-tutarlilik.md` |
| (Tek konu ilkesinin belge düzeyi sonucu) | 2. Her önermeyi bir kez söyle | Açımlama döngüsü, işlev tekrarı, döngüsel tanım, bölüm başı ve sonu tekrarı | `retorik-yapilar.md` |
| Yalnızca gerekli bilgi (STE'nin açık ve özgül yazma ilkesi) | 3. Yalnızca gerekli bilgiyi yaz | Silme testi; üretilmiş önem, savunma, yol haritası, kalıp giriş ve sonuç | `retorik-yapilar.md` |
| Betimlemede en çok 25, prosedürde en çok 20 sözcük; talimatta cümle başına bir talimat; ad öbeği en çok üç sözcük; kısaltmak için öge düşürme | 4. Kısa ve doğrudan cümle | Eşikler inceleme işaretidir; ad öbeği eşiği Türkçede iyelik ve çerçeve zincirine uygulanır; telgraf dili yasaktır | `turkce-ritim-ve-ceviri-kokusu.md`, `yapisal-butunluk.md` |
| Bir sözcük, bir anlam | 5. Bir terim, bir anlam | Kavram başına tek ad; eş anlamlı kayması yok; kısaltma ilk geçişte açılır | `sozcuk-birlesimleri.md` |
| Etken çatı; betimlemede edilgen yalnızca aktör bilinmiyorsa | 6. Somut özne, somut yüklem | Talimatta etken ya da emir kipi. Bilimsel betimlemede edilgen, yöntem merkezli kayıtta ve konu sürekliliğinde meşrudur; aktör uydurulmaz | `kanit-ve-kesinlik.md` |
| Karmaşık içerik için dikey liste | 7. Yapı okura hizmet eder | Liste yalnızca paralel öge ve sıralı adım içindir; nedensel zincir düzyazıdır | `yapisal-butunluk.md` |

**Edilgen çatı neden STE'den gevşek?** STE betimlemede edilgeni yalnızca aktör bilinmediğinde kabul eder. Türkçe bilimsel yazımda edilgen çatı yöntem merkezli kaydın olağan biçimidir (`Örnekler 40 °C'de kurutuldu`) ve aktör çoğu zaman araştırma ekibinin kendisidir. Bu cümleyi `Biz örnekleri 40 °C'de kuruttuk` yapmak netlik kazandırmaz, kaydı değiştirir. Bu yüzden Metinoskop STE'nin etken çatı ilkesini talimat ve prosedürde uygular. Betimlemede ise kanıt ve kesinlik dosyasındaki karar çerçevesi geçerlidir.

## Eşikler nasıl okunur

Sayısal eşikler bir şeyin **incelenmesi** gerektiğini söyler, ne yapılacağını söylemez.

- **Cümle uzunluğu.** STE'nin eşikleri İngilizce sözcük sayısıyla tanımlanmıştır. Türkçede ekler ilişkiyi sözcük içinde taşıdığı için aynı içerik çoğu zaman daha az sözcükle yazılır. Bu yüzden 25 sözcüğü aşan Türkçe betimleyici cümle zaten uzundur ve incelenir. İnceleme sorusu: bu cümle bir ilişki mi taşıyor, yoksa ilgisiz önermeler mi yığılmış? Tek ilişki taşıyan uzun cümle korunur (`dogal-uzun-cumle-korunur`).
- **Paragraf uzunluğu.** Altı cümleyi aşan paragrafta iki ayrı konu olup olmadığına bak. Tek bir düşünce hareketiyse bölme (`uzun-paragraf-korunur`).
- **Ad öbeği.** Türkçede STE'nin "noun cluster" sorunu iyelik zinciri (`sistemin bakım sürecinin planlama aşamasının`) ve çerçeve yığını (`... kapsamında ... açısından`) olarak görünür. Üç halkayı aşan zinciri çöz.
- **Talimat.** Talimatta bir cümle bir adımdır. Uyarı ve koşul adımın başına gelir. Sıralı adımlar numaralı listedir.

`scripts/style-lint.py` bu eşikleri `netlik` bulguları olarak raporlar: uzun cümle, kalabalık paragraf ve döngüsel tekrar adayı. Bulgular bağlamsaldır; hiçbiri tek başına hata değildir.

## Kurallar ve örnekler

Örneklerde "sonra" sürümündeki her önermenin "önce" sürümünde karşılığı vardır. Hiçbir örnek sayı türetmez ya da kanıt statüsünü yükseltmez.

### 1. Bir paragraf, bir konu

**Dağılmış konu.** Aynı konu belgenin birkaç yerinde açılıyorsa okur onu her seferinde yeniden kurar.

> Önce: (Yöntem bölümünde) Sensörler her ölçümden önce sıfırlandı. (…iki paragraf sonra, sonuçlarda) Sıfırlamanın etkisini görmek için sıfırlanmamış bir seri de kaydedildi. (…bir paragraf sonra) Sıfırlanmamış seride kayma 0,4 mV'a ulaştı.
>
> Sonra: (Yöntem bölümünde) Sensörler her ölçümden önce sıfırlandı; sıfırlamanın etkisini görmek için sıfırlanmamış bir seri de kaydedildi. (Sonuçlarda) Sıfırlanmamış seride kayma 0,4 mV'a ulaştı.

Yöntem bilgisi yöntemde toplandı; ölçüm sonucu sonuçlarda kaldı. Bölüm sınırı korundu, çünkü yöntem ile sonuç ayrı işlevdir.

**Korunur.** Bulgu ile öneri aynı konuyu işlese de ayrı paragraflardadır; söylem işlevi değiştiği için sınır meşrudur.

### 2. Her önermeyi bir kez söyle

**Döngüsel tanım.** Terimi kendisiyle tanımlayan cümle okura bilgi vermez.

> Önce: Kalibrasyon, ölçüm sisteminin kalibre edilmesi işlemidir. Kalibrasyonda sistemin çıktısı bilinen referans değerlerle karşılaştırılır.
>
> Sonra: Kalibrasyonda ölçüm sisteminin çıktısı bilinen referans değerlerle karşılaştırılır.

**Açımlama döngüsü.** Olgu → açımlama → önem → mini sonuç dizisi tek önermeye iner (`SKILL.md` kısa örneği; eval `iddia-tekrar-dongusu`).

**Korunur.** Aynı önerme yeni bir rol kazanıyorsa yinelenir: bulgularda ölçüm olarak (`hata %9'dan %4'e indi`), tartışmada yorumun dayanağı olarak (`%4'lük hata, ... için yeterli düzeydedir`). Eval: `ayni-iddia-yeni-rol`.

### 3. Yalnızca gerekli bilgiyi yaz

**Silme testi.** Cümleyi çıkar; önermeler, akıl yürütme, kronoloji, yorum ya da yazar tavrı değişiyor mu? Değişmiyorsa ve cümle bir sentez de yapmıyorsa sil.

> Önce: Ölçümler üç tekrarla alındı. Bu, ölçümlerin güvenilirliği açısından önemli bir adımdır. Tekrarlar arasındaki en büyük fark %1,2 oldu.
>
> Sonra: Ölçümler üç tekrarla alındı; tekrarlar arasındaki en büyük fark %1,2 oldu.

**Korunur.** Yeni başlayana yazılmış öğretici açıklama, adlandırılmış sınırlılık ve ölçülmüş yöntem gerekçesi bilgi taşır (`egitsel-aciklama`, `savunmaci-akademik`).

### 4. Kısa ve doğrudan cümle

**Çok önermeli cümle.** İlgisiz önermeler tek cümleye yığılmışsa okur hangisinin ana önerme olduğunu çözemez.

> Önce: Yeni pompa, eski pompaya göre daha az enerji tüketen ve bakım aralığı 600 saatten 900 saate çıkarılmış olan, ayrıca tedarikçisi değiştirilmiş ve montajı iki kişi yerine tek kişiyle yapılabilen bir model olarak 2024'te hatta takıldı.
>
> Sonra: Yeni pompa 2024'te hatta takıldı. Eski pompaya göre daha az enerji tüketiyor ve bakım aralığı 600 saatten 900 saate çıkarıldı. Tedarikçisi değişti; montajı iki kişi yerine tek kişiyle yapılabiliyor.

Karşılaştırma zemini (`eski pompaya göre`) yalnızca enerji tüketimine bağlı kaldı; kaynak bunu bakım aralığına bağlamıyordu.

**Korunur.** Tek ilişkiyi (koşul, neden, karşıtlık) taşıyan uzun cümle bölünmez; bölmek ilişkiyi koparır (`dogal-uzun-cumle-korunur`).

**Telgraf dili yasaktır.** `Pompa takıldı. 2024. Enerji düşük.` kısadır ama net değildir; ögeler ve ilişki kaybolmuştur.

### 5. Bir terim, bir anlam

> Önce: Önerilen yöntem üç aşamadan oluşur. Yaklaşımın ilk aşamasında veri temizlenir. Sistemin ikinci aşaması özellik seçimidir. Çözümün son aşamasında model eğitilir.
>
> Sonra: Önerilen yöntem üç aşamadan oluşur: veri temizleme, özellik seçimi ve model eğitimi.

`Yöntem`, `yaklaşım`, `sistem`, `çözüm` aynı varlığı adlandırıyordu; okur dört ayrı şey olup olmadığını soracaktı. Eval: `varlik-yeniden-adlandirma`, `kanonik-terim-tekrari`.

**Korunur.** Terimin yinelenmesi tekrar değildir. `Hata`, `sapma` ve `belirsizlik` ayrı kavramlarsa üçü de kalır.

### 6. Somut özne, somut yüklem

> Önce: Önbellek eklendikten sonra ortalama yanıt süresi 180 ms'den 95 ms'ye indi. Bu yaklaşım, sistem performansının iyileştirilmesinde önemli bir rol oynamaktadır.
>
> Sonra: Önbellek eklendikten sonra ortalama yanıt süresi 180 ms'den 95 ms'ye indi.

İkinci cümle ölçümü soyut yüklemle (`rol oynamaktadır`) ve boş özneyle (`bu yaklaşım`) yineliyordu. `Önbellek yanıt süresini indirdi` yazmak daha somut görünür ama kaynağın kurduğu zaman ilişkisini nedenselliğe çevirir; değişmezler buna izin vermez. Kaynak ölçüm vermiyorsa ölçüm uydurulmaz: cümle ya kaynağın kendi iddiası olarak kalır ya da dolguysa silinir. Eval: `soyut-yuklem`.

**Talimat.** `Vananın kapatılması gerekmektedir` → `Vanayı kapatın`. Bilimsel betimlemede `Örnekler 40 °C'de kurutuldu` korunur.

### 7. Yapı okura hizmet eder

**Sıralı adım listedir.** Okurun sırayla uygulayacağı adımlar numaralı listeye girer. Uyarı, adımın başına yazılır.

**Zincir düzyazıdır.** Maddeler `bu nedenle`, `dolayısıyla` ile birbirine bağlanıyorsa paralel değil nedenseldir; düzyazıya dön (`gereksiz-listeleme`).

**Başlık hakkını kazanır.** Altında tek kısa paragraf olan başlık, komşusuyla aynı konuyu işliyorsa birleşir (`tek-paragraf-bolumler`). Uzun belgenin gezinme başlıkları ve tekrarlanabilirlik için ayrılmış deney bölümleri korunur (`korunacak-basliklar`, `yontem-ayrimi`).

## Aşırı uygulama belirtileri

Omurga "her şeyi kısalt" demek değildir. Şunlar aşırı uygulamadır:

- Kesinlik işaretini (`yaklaşık`, `henüz`, `bu verilerle sınırlı olarak`) kısalık için silmek.
- Tek ilişkiyi taşıyan cümleyi bölüp `bu`, `bu durum` göndergeleriyle yeniden bağlamak.
- Gerekli terim tekrarını eş anlamlıyla ya da zamirle değiştirmek.
- Uzun belgenin gezinme başlıklarını ya da tekrarlanabilirlik bölümlerini birleştirmek.
- Yeni başlayan okur için yazılmış açıklamayı uzman okura göre silmek.
- Bilimsel betimlemeyi etken çatıya zorlayıp aktör uydurmak.
- Cümleleri eşit uzunluğa ya da eşiklerin hemen altına göre kesmek.
