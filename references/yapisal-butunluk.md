# Yapısal bütünlük ve okur yorgunluğu

## İçindekiler

1. [Kullanım ilkesi](#kullanım-ilkesi)
2. [Üç ilke](#üç-ilke)
3. [Bölme testleri](#bölme-testleri)
4. [Parçalanma yoğunluğu](#parçalanma-yoğunluğu)
5. [Paragraf hareketi ve zihinsel model](#paragraf-hareketi-ve-zihinsel-model)
6. [Yakınlık kuralı](#yakınlık-kuralı)
7. [Yapay gerilim ve paragraf askısı](#yapay-gerilim-ve-paragraf-askısı)
8. [Bağlam yeniden başlatma ve çapraz gönderme](#bağlam-yeniden-başlatma-ve-çapraz-gönderme)
9. [Başlık tekrarı, sarmalayıcı ve zorlama geçiş](#başlık-tekrarı-sarmalayıcı-ve-zorlama-geçiş)
10. [Listeleştirme](#listeleştirme)
11. [Uzun ifadeler ve yığılmış çerçeve](#uzun-ifadeler-ve-yığılmış-çerçeve)
12. [Cümle birleştirme ve şişkin cümle](#cümle-birleştirme-ve-şişkin-cümle)
13. [Yinelenme haritası](#yinelenme-haritası)
14. [Yapısal onarım örnekleri](#yapısal-onarım-örnekleri)
15. [Karşı örnekler: kalması gereken yapı](#karşı-örnekler-kalması-gereken-yapı)

## Kullanım ilkesi

Bu dosya, cümleleri temiz olduğu hâlde okurun içinde kalamadığı metinler içindir. Metin sürekli yeni alt bölüm açıyor, paragrafı erken kesiyor, ilişkili fikirleri ayırıyor, açıklamayı yeniden başlatıyor, gerilim üretiyor, her geçişten sonra bağlamı tekrarlıyor, basit ilişkileri fazla açıklıyor ve okuru bağlantıları yapısal sınırların ötesinde yeniden kurmaya zorluyorsa doğru cümlelerle de yorucudur.

Hedef "her şeyi kısaltmak" değildir. Paragraf uzun diye bölünmez, başlık sayıyı azaltmak için birleştirilmez, cümle mekanik olarak kısaltılmaz. Her yapısal değişiklik, anlamı bozmadan süreklilik, anlama, gezinme, anlamsal yakınlık, okur emeği veya yinelenme açısından bir kazanç sağlamalıdır. Örneklerdeki "sonra" metinleri "önce" metninde bulunmayan olgu eklemez.

## Üç ilke

1. **Yapı kavramsal sınırları izler; modelin her şeyi düzenleme isteğini değil.** Yeni bir başlık, paragraf veya liste bilişsel maliyet yaratır. Bu maliyeti yalnızca anlama veya gezinme kazancı karşılıyorsa yükle.
2. **Okur, bir kavramı zihninde sabitleyecek kadar bilgi birikmeden o kavramdan tekrar tekrar ayrılmak zorunda kalmamalıdır.** Açıklama bitmeden yeni yapısal birime geçme.
3. **Görsel parçalanma açıklık değildir.** Kısa paragraf, çok başlık ve madde işareti tek başına okumayı kolaylaştırmaz; çoğu zaman okurun kendi kuracağı bağlantıları artırır.

## Bölme testleri

### Süreklilik testi

Yeni paragraf, alt bölüm veya başlık açmadan önce şu soruları sor. Cevapların çoğu "hayır" ise bölme.

| Soru | "Evet" örneği | "Hayır" örneği |
|---|---|---|
| Konu gerçekten değişti mi? | Depo verisinden taşıma verisine geçiliyor. | Aynı depo verisinin ikinci sayısı veriliyor. |
| Argüman işlevi değişti mi? | Yöntemden sonuca, sonuçtan yoruma geçiliyor. | Aynı sonucun bir nitelemesi ekleniyor. |
| Aynı paragrafta devam etmek ilişkiyi zorlaştırır mı? | İki farklı deney karıştırılacak. | Neden ile sonuç yan yana daha iyi okunuyor. |
| Bölme gezinmeye yarıyor mu? | Okur bu bölümü tek başına arayacak. | Bölüm yalnızca metni düzenli gösteriyor. |

### Başlık testi

Yararlı başlık şunlardan en az birini yapar:

- büyük bir kavramsal geçişi işaretler,
- uzun bölümde gezinmeyi sağlar,
- gerçekten ayrı yöntem aşamalarını ayırır,
- aksi hâlde bulunması güç bulguları ayırır,
- dışarıdan dayatılan belge yapısını yansıtır,
- altında anlamlı bir birim oluşturacak kadar malzeme taşır.

Yüksek riskli başlık biçimleri:

- her küçük kavrama açılan başlık,
- altında tek kısa paragraf bulunan başlık,
- tek bir geniş bölümde doğal olarak duracak birden çok başlık,
- altındaki ilk cümleyi yineleyen başlık,
- bir iki cümlelik işlev değişimi için açılan başlık,
- aşırı `###` ve `####` derinliği,
- mühendislik ürünü gibi görünen simetrik başlık ağacı.

Bir paragrafa etiket verilebiliyor olması başlık gerekçesi değildir.

### Derinlik testi

`###` veya `####` açmadan önce ayrımın belge yapısına ait olacak kadar önemli olup olmadığını sor. Şu desen okuru her birkaç cümlede bir sıfırlar:

```text
## Bölüm
### Alt bölüm
#### Alt-alt bölüm
bir paragraf
#### Başka bir alt-alt bölüm
iki cümle
```

Okur her yeni başlıkta konuyu, üst bölümle ilişkiyi, bunun yeni bir argüman mı yoksa yalnızca yeni bir ayrıntı mı olduğunu ve hangi varsayımların hâlâ geçerli olduğunu yeniden kurar. Bu sıfırlamayı gerçek bir kazanç olmadan dayatma. Daha az, daha geniş bölüm ve içinde tutarlı paragraflar tercih et.

### Başlık sıkıştırma

Belge düzeyinde komşu başlıklara bak:

- İki bölüm gezinme kaybı olmadan birleşebilir mi?
- İki başlık aynı önermenin farklı yüzlerini mi anlatıyor?
- Bir başlık öncekinin yalnızca örneği, sınırlılığı, sonucu veya devamı mı?
- Bir geçiş cümlesi sürekliliği yapısal kesintiden daha iyi korur mu?
- Hiyerarşi içeriği mi, yoksa modelin düşünme sırasını mı yansıtıyor?

Bitişik iki bölüm tek sürekli argüman olarak daha kolay anlaşılıyorsa birleştir. Kullanıcı derin yapısal düzenleme istediyse başlıkları sırf mevcut oldukları için koruma. Kullanıcı hafif düzenleme veya yapı koruma istediyse başlıklara dokunma; yalnızca bölünmenin ürettiği dolgu cümlelerini sil.

## Parçalanma yoğunluğu

Belge düzeyinde şu ölçüleri sessizce çıkar. Bunlar sınır değil, uyarı işaretidir:

- başlık sayısı ve derinliği,
- başlık başına ortalama paragraf,
- tek paragraflık bölüm sayısı,
- bir veya iki cümlelik paragraf sayısı,
- konu sıfırlama sıklığı,
- çapraz gönderme sıklığı,
- bölüm duyurusu sıklığı,
- mini sonuç sıklığı.

Özellikle şüpheli:

- her biri tek paragraflı çok sayıda başlık,
- tekrarlayan üçüncü ve dördüncü düzey başlıklar,
- paragraflarının çoğu iki cümlelik uzun teknik belge,
- aynı mimariyle tekrarlayan alt bölüm desenleri (duyuru → içerik → mini sonuç).

Sayısal eşik dayatma; uyarı işaretini gördüğünde bölme testlerini uygula. `scripts/style-lint.py` bu ölçüleri raporlar, karar vermez.

## Paragraf hareketi ve zihinsel model

Kısa paragrafın otomatik olarak daha kolay okunduğu varsayımını reddet. Paragraf, cümleleri baskın ve tutarlı bir düşünce hareketini yürüttüğü sürece bütün kalır; hareket, gözlem → yorum → çekince gibi birbirine bağlı birkaç alt işlev taşıyabilir:

- iddia → kanıt → yorum,
- gözlem → açıklama,
- koşul → sonuç,
- yöntem → gerekçe,
- sonuç → sınırlılık,
- bağlam → özgül sorun,
- mekanizma → çıkarım,
- karşılaştırma → sonuç.

**Erken bölünmüş**

> Yöntem hata oranını düşürdü.
>
> Bunun temel nedeni örnekleme stratejisiydi.
>
> Örnekleme özellikle düşük yoğunluklu bölgelerde etkiliydi.
>
> Bu durum sonuçların yorumlanması açısından önemlidir.

**Tek paragraf**

> Yöntem hata oranını düşürdü. Bunun temel nedeni örnekleme stratejisiydi; örnekleme özellikle düşük yoğunluklu bölgelerde etkiliydi.

İlk üç cümle gözlem → açıklama → niteleme hareketidir ve tek paragrafta kalır; birleştirme paragraf düzeyindedir, üç cümleyi tek noktalı virgüllü cümleye sıkıştırmak zorunlu değildir. Dördüncü cümle hiçbir önerme taşımadığı ve önceki bilgiyi sentezlemediği için silinir.

Aynı konu üzerinde olmak tek paragraf için yeterli değildir. Söylem işlevi sert biçimde değişiyorsa, özellikle bulgu → öneri, betimleme → karar ve yöntem → sonuç geçişlerinde, paragraf sınırı meşrudur. Parçalanmayı önlemek, bulgu, yorum ve öneriyi tek yoğun blokta paketlemek değildir.

Her paragraf veya bölüm sınırında sor: okur, etkin kalabilecek bağlamı yeniden mi kuracak? Sonraki birim aynı özneyi, yöntemi, deneyi, değişkeni, nedensel zinciri, çerçeveyi, sınırlılığı veya karşılaştırmayı yeniden tanıtmak zorunda kalıyorsa bölme zararlıdır. Bölümü kapatmadan önce okurun iddiayı, gerekli kanıtı, gerekiyorsa yorumu ve temel sınırlılığı ya da koşulu edinip edinmediğini sor; açıklama bitmemişse sürdür.

## Yakınlık kuralı

Bir cümle başka bir cümleyi niteliyor, sınırlıyor, açıklıyor veya doğrudan yorumluyorsa belge yapısı ayrılmayı gerçekten gerektirmedikçe ikisini yakın tut. Şu çiftler temiz alt bölümler uğruna ayrılmaz:

| Çift | Ayrıldığında okurun taşıdığı yük |
|---|---|
| iddia ↔ kanıt | İddiayı kanıtsız kabul etmek veya aramak |
| yöntem ↔ gerekçe | Tercihi keyfî sanmak |
| sonuç ↔ belirsizliği | Sonucu kesin sanmak |
| ölçüm ↔ yorum | Yorumun hangi sayıya dayandığını hatırlamak |
| sınırlılık ↔ sınırladığı iddia | İddiayı yanlış genellemek |
| karşılaştırma ↔ iki tarafı | Tabanı hatırlamak |
| değişken tanımı ↔ ilk kullanımı | Tanımı geri dönüp aramak |

Bilimsel sınırlılık, koşul, belirsizlik, istisna, yöntemsel varsayım, karşılaştırma tabanı ve kapsam kısıtı için bu kural özellikle geçerlidir. Okur bir sonucu sınırlılığına ulaşmak için birkaç başlık boyunca aklında tutmamalıdır. Dergi veya kurum kuralı sınırlılıkları ayrı bölüme koymayı dayatıyorsa bölümü koru; sonucun yanına yalnızca kapsamı belirten kısa bir niteleme bırak.

## Yapay gerilim ve paragraf askısı

Dil modelleri malzeme gerektirmese de momentum üretmeye çalışır. Bilgi veren metinde ilgi, gerçek problemden veya sonuçtan gelir.

### Gerilim kataloğu

- Ancak burada işler değişmektedir.
- Fakat asıl sorun bundan sonra ortaya çıkmaktadır.
- İlk bakışta her şey yolunda görünmektedir.
- Tam da bu noktada yeni bir problem ortaya çıkar.
- Burada beklenmedik bir durumla karşılaşılır.
- Fakat hikâye burada bitmez.
- Asıl şaşırtıcı olan ...
- İşin ilginç yanı ...
- Daha da önemlisi ...
- Sorun tam olarak burada başlıyor.
- Görünüşte basit olan bu durum aslında ...
- Bu noktaya kadar tablo nettir. Ancak ...
- Burada kritik bir kırılma meydana gelir.
- Ve asıl mesele burada ortaya çıkar.

### Askı kataloğu

- Bu sorunun yanıtı bir sonraki bölümde görülecektir.
- Ancak burada önemli bir sorun ortaya çıkmaktadır.
- Bunun nedenini anlamak için bir sonraki adıma geçmek gerekir.
- Bu durum bizi daha temel bir soruya götürmektedir.
- Asıl cevap ise bir sonraki bölümde ortaya çıkmaktadır.

### Karar

Gerçek bir tersine dönüş, çelişki, beklenmedik bulgu ya da kavramsal gerilim yoksa üretme. Gerçek karşıtlık bilgi taşır ve zayıflatılmaz; anlatı draması aynı bilginin ambalajıdır ve atılır.

**Dramatik**

> İlk bakışta yeni denetleyici başarılı görünmektedir: kuvvet hatası %12 azalmıştır. Ancak hikâye burada bitmez. Uzun dönem davranışa bakıldığında tablo değişmektedir. Yedi günlük konum hatası %8 artmıştır. Sorun tam olarak burada başlamaktadır.

**Doğrudan**

> Yeni denetleyici kuvvet hatasını %12 azaltmış, yedi günlük konum hatasını ise %8 artırmıştır.

Beş cümle bir cümle oldu; iki ölçüm ve ödünleşim korundu. Askı cümlesi yerine de ilişki doğrudan söylenir: "Bunun nedeni bir sonraki bölümde açıklanacaktır" yerine neden buradaysa buraya yazılır, burada yoksa askı silinir.

## Bağlam yeniden başlatma ve çapraz gönderme

Parçalanmış metin açıklamayı tekrar tekrar başlatır:

- aynı değişkenin yeniden tanımlanması,
- aynı deney düzeneğinin hatırlatılması,
- aynı yöntemin yeniden tanıtılması,
- her alt bölüm başında "bu çalışmada ...",
- her alt bölüm başında aynı amacın tekrarı,
- aynı "bu sonuç neden önemli" hatırlatması.

Olgu okurun çalışma belleğinde hâlâ etkinse ve belirsizlik doğmayacaksa yeniden söyleme.

Sık çapraz gönderme aynı belirtidir:

- yukarıda belirtildiği gibi
- önceki bölümde açıklandığı üzere
- aşağıda görüleceği üzere
- ilerleyen bölümde ele alınacağı gibi
- daha önce değinildiği üzere
- bir önceki başlıkta belirtildiği gibi
- bu konuya ileride tekrar dönülecektir

Uzun teknik belgede birkaç gönderme yararlıdır. Her göndermeden önce sor: malzemeyi birleştirmek veya yeniden sıralamak göndermeyi gereksiz kılar mı? Gezinme yaması yerine yapısal onarımı tercih et. Tablo, şekil, ek, denklem ve kaynak göndermeleri ile sabit numaralı bölümlere yapılan zorunlu göndermeler bu kuralın dışındadır.

**Yamalı**

> ### 2.2 Yöntem
>
> Önceki bölümde açıklanan 1.200 kayıt, teslim süresine göre üç gruba ayrılmıştır. Grupların tanımı aşağıda görüleceği üzere 2.3'te verilmiştir.
>
> ### 2.3 Gruplar
>
> Yukarıda değinilen üç grup şunlardır: 2 günden kısa, 2–5 gün ve 5 günden uzun teslimatlar.

**Onarılmış**

> ### 2.2 Yöntem
>
> 1.200 kayıt teslim süresine göre üç gruba ayrılmıştır: 2 günden kısa, 2–5 gün ve 5 günden uzun teslimatlar.

Grupların tanımı yöntemin parçası olduğu için yöntemin yanına taşındı; üç gönderme kendiliğinden gereksizleşti.

## Başlık tekrarı, sarmalayıcı ve zorlama geçiş

**Başlık ile içerik tekrarı.** "Doğrulamanın Önemi" başlığının altında "Doğrulama önemlidir; çünkü ..." ya da "Analiz Sonuçları" altında "Analiz şu sonuçları vermiştir" ile başlama. Başlık yönlendirmeyi zaten veriyorsa ilk cümle içerik taşır.

**Boş sarmalayıcılar.** Yaygın yapay bölüm yapısı şudur: konuyu duyur, konuyu açıkla, sonucu yeniden söyle, bölümü özetle. Çoğu zaman yalnızca ikinci adım yararlıdır.

| Açılış sarmalayıcısı | Kapanış sarmalayıcısı |
|---|---|
| Bu bölümde X ele alınmaktadır. | Dolayısıyla X'in önemi açıkça görülmektedir. |
| X bu çalışmanın önemli bileşenlerinden biridir. | Bu değerlendirmeler X'in kritik rolünü göstermektedir. |
| X'in anlaşılması için birkaç noktaya değinmek gerekir. | Sonuç olarak bu bölüm X'in temel önemini ortaya koymaktadır. |

Her bölümün kendi girişi ve sonucu olmak zorunda değildir.

**Zorlama geçişler.** Yeni paragraf başlıyor diye "Bununla birlikte", "Öte yandan", "Bu doğrultuda", "Bu bağlamda", "Bu noktada", "Buna ek olarak", "Ayrıca", "Dolayısıyla" ekleme. Anlamsal süreklilik zaten açıksa doğrudan cümle daha iyidir. Konu değişimini de üç cümleyle anlatma:

**Fazla**

> Bu sonuçlar yöntemin kısa dönem davranışını göstermektedir. Ancak uzun dönem davranış ayrı bir değerlendirme gerektirir. Bu nedenle bir sonraki aşamada yedi günlük hata incelenmiştir.

**Yeterli**

> Yedi günlük hata ise uzun dönem davranışı gösterir.

Kaynağın izin verdiği en kısa geçişi kullan; kaynak yalnızca "yedi günlük hata da ölçülmüştür" diyorsa uzun dönem yorumunu da ekleme.

## Listeleştirme

Mantıksal sürekliliği olan akıl yürütmeyi sırf maddelenebiliyor diye listeye çevirme. Liste şu durumlarda uygundur: ögeler gerçekten paralel; sıra veya karşılaştırma taramadan yararlanıyor; kullanıcı liste istedi; belge türü liste bekliyor. Fikirler arasındaki ilişki maddelenmeden önemliyse düzyazı kullan.

**Listeleştirilmiş**

> Önbellek şu nedenlerle devre dışı bırakılmıştır:
>
> - Sorgular arasında tekrar oranı %2'nin altındaydı.
> - Bu nedenle önbellek isabet oranı düşük kaldı.
> - Düşük isabet oranı 4 GB'lık bellek maliyetini haklı çıkarmıyordu.
> - Sonuç olarak önbellek kapatıldı.

**Düzyazı**

> Sorgular arasında tekrar oranı %2'nin altında kaldığı için önbellek isabet oranı düşük kaldı ve 4 GB'lık bellek maliyetini haklı çıkarmadı; önbellek bu nedenle devre dışı bırakıldı.

Maddeler bir nedensel zincirdi; liste zinciri dört bağımsız olguya bölüyordu. Gerçekten paralel ögeler (üç deney koşulu, beş yapılandırma alanı, adım sırası önemli bir kurulum) listede kalır.

## Uzun ifadeler ve yığılmış çerçeve

Daha kısa biçim aynı anlam ve tonu taşıyorsa uzun biçimi bırak. Tam biçimi ayrı anlam taşıyan teknik ifadeyi sıkıştırma.

| Uzun | Kısa |
|---|---|
| bu durumun ortaya çıkmasına neden olmaktadır | buna neden oluyor |
| uygulanabilir durumda bulunmaktadır | uygulanabilir |
| bir değerlendirme yapılması gerekmektedir | değerlendirilmelidir |
| bu konuda bir açıklama yapılmasına ihtiyaç vardır | bu konu açıklanmalıdır |
| söz konusu yöntemin kullanılması durumunda | yöntem kullanıldığında |
| gerçekleştirilen analiz sonucunda elde edilen bulgular | analiz sonuçları |
| ... açısından değerlendirildiği zaman | ... açısından |
| ... bakımından ele alındığında | çoğu zaman gereksiz |
| dikkate alınması gereken bir husus olarak karşımıza çıkmaktadır | meselenin kendisini yaz |
| bu kapsamda değerlendirilmesi mümkün olan | gerçek ilişkiyi yaz |

**Yığılmış çerçeve.** Üst üste nitelemelerde gerçek özneyi, gerçek yüklemi ve gerçekten gerekli nitelemeyi bul; gerisini at.

**Önce**

> Bu bağlamda, söz konusu yöntemin mevcut çalışma kapsamında uygulanabilirliği açısından göz önünde bulundurulması gereken temel hususlardan biri, veri kümesinin büyüklüğünün yetersiz kalması durumunun ortaya çıkmasına neden olabilecek koşulların dikkate alınması gereken bir husus olarak karşımıza çıkmasıdır.

**Sonra**

> Yöntemin bu çalışmada uygulanabilirliği için veri kümesinin yetersiz kalabileceği koşullar dikkate alınmalıdır.

Özne: uygulanabilirlik koşulu. Yüklem: dikkate alınmalı. Gerekli niteleme: veri kümesinin yetersiz kalabileceği koşullar. Geri kalan yirmi sözcük çerçeveydi. Akademik ses veriyor diye karmaşıklığı ödüllendirme.

## Cümle birleştirme ve şişkin cümle

Birkaç ardışık cümle yalnızca tek bir düşüncenin yapay olarak parçalanmasından doğuyorsa birleştir:

> İlk aşamada veri temizlenmiştir. Daha sonra normalize edilmiştir. Ardından modele aktarılmıştır.

> Veri temizlenip normalize edildikten sonra modele aktarılmıştır.

Sıra, vurgu veya yöntemsel tekrarlanabilirlik ayrı adım gerektiriyorsa birleştirme; numaralı işlem adımları listede kalabilir.

Tersine, parçalanmayı dev cümlelerle çözme. Bir cümle birkaç ilgisiz iddiayı, iç içe nitelemeleri, birden çok parantez dalını ya da bir argümanı sınırlılığı ve çıkarımıyla birlikte taşımamalıdır.

**Kaynak**

> Veri iki kaynaktan gelmektedir ve %4 eksik değer içermektedir. Bu nedenle temizlenip z-puanıyla normalize edilmiştir. İlk denemede ıraksama görülmüş, öğrenme oranı 0,001'e düşürülmüştür. Yeniden eğitilen model doğrulama kümesinde %91 doğruluk vermiştir.

**Şişkin**

> Veri, iki kaynaktan geldiği ve %4 eksik değer içerdiği için temizlenip z-puanıyla normalize edildikten sonra, ilk denemede ıraksama görüldüğünden öğrenme oranı 0,001'e düşürülerek yeniden eğitilen ve doğrulama kümesinde %91 doğruluk veren modele aktarılmıştır.

**Doğal birim**

> Veri iki kaynaktan geldiği ve %4 eksik değer içerdiği için temizlenip z-puanıyla normalize edilmiştir. İlk denemede ıraksama görülünce öğrenme oranı 0,001'e düşürüldü; yeniden eğitilen model doğrulama kümesinde %91 doğruluk verdi.

Kaynaktaki dört cümle iki düşünce taşır: veri hazırlığı ve eğitim. İki cümle bu iki birime karşılık gelir; tek cümle ise dört olguyu, iki nedeni ve bir sonucu aynı anda taşımaya zorlar. Ölçüt cümle sayısı değil kavramsal birliktir.

## Yinelenme haritası

Uzun metinde aynı önermenin nerede tekrar ettiğini sessizce izle: giriş, bölüm girişi, sonuçlar, tartışma, sonuç, alt bölüm sonları. Tür gereği özet meşru olabilir; öz, giriş ve sonuç bölümlerinde aynı ana bulgunun görünmesi beklenir. Ayır:

- **Gerekli özet:** Önerme yeni bir rol kazanıyor (özde bulgu, tartışmada yorum, sonuçta sınırlılıkla birlikte).
- **Hacim üreten tekrar:** Aynı önerme yeni rol, nitelendirme veya yorum kazanmadan yeniden açımlanıyor.

İkincisini azalt; birincisini koru.

## Yapısal onarım örnekleri

Aşağıdaki örneklerde ana iyileşme sözcük değişiminden değil birleştirme ve yeniden düzenlemeden gelir.

### Akademik: dört mikro bölüm tek bölüm oluyor

**Önce**

> ### Temel çizginin seçimi
>
> Karşılaştırma için temel çizgi olarak 2023 sürümü seçilmiştir.
>
> ### Temel çizginin önemi
>
> Temel çizgi, yöntemin katkısının ölçülebilmesi açısından kritik bir rol oynamaktadır. Uygun bir temel çizgi olmadan iyileşmenin kaynağı belirsiz kalır.
>
> ### Ana deneyle ilişkisi
>
> Yukarıda belirtilen 2023 sürümü, ana deneyde kullanılan veri kümesinin aynısıyla eğitilmiştir; böylece fark yalnızca yöntemden kaynaklanır.
>
> ### Yorum
>
> Bu durum, karşılaştırmanın adil olduğunu göstermektedir. Ancak temel çizginin sınırlılıkları bir sonraki bölümde ele alınacaktır.

**Sonra**

> ### Temel çizgi
>
> Karşılaştırma için temel çizgi olarak 2023 sürümü seçilmiştir. Bu sürüm, ana deneyde kullanılan veri kümesinin aynısıyla eğitilmiştir; böylece iki sonuç arasındaki fark yalnızca yöntemden kaynaklanır.

Dört başlık ve altı cümle, bir başlık ve iki cümle oldu. Sürüm, veri kümesi eşleşmesi ve "yalnızca yöntemden" iddiası korundu. "Kritik rol" ve "adil olduğunu göstermektedir" cümleleri kaynaktaki iddiayı yeniden ifade ediyordu; "temel çizgi olmadan iyileşmenin kaynağı belirsiz kalır" uzman okur için olağan bilgidir; askı cümlesi ise sınırlılıkların kendisini taşımıyordu. Sınırlılıklar bu bölümde varsa aynı paragrafın sonuna gelir.

### Teknik belge: dördüncü düzey başlıklar düzleşiyor

**Önce**

> ## 3. Yapılandırma
>
> ### 3.1 Bağlantı ayarları
>
> #### 3.1.1 Zaman aşımı
>
> `timeout` alanı saniye cinsinden bekleme süresidir; varsayılan 30'dur.
>
> #### 3.1.2 Yeniden deneme
>
> `retries` alanı deneme sayısıdır; varsayılan 3'tür.
>
> ### 3.2 Önbellek ayarları
>
> #### 3.2.1 Süre
>
> `cache_ttl` alanı sonuçların kaç saniye tutulacağını belirler; varsayılan 300'dür.

**Sonra**

> ## 3. Yapılandırma
>
> Bağlantı ayarları iki alandan oluşur: `timeout` saniye cinsinden bekleme süresidir (varsayılan 30), `retries` deneme sayısıdır (varsayılan 3). Önbellek ayarında `cache_ttl` alanı sonuçların kaç saniye tutulacağını belirler; varsayılan 300'dür.

Beş başlık bir başlık oldu; üç alan, üç varsayılan ve iki ayar grubu korundu. Belge başka yerden `3.1` veya `3.2` numarasına gönderme yapıyorsa ya da kullanıcı numaralı yapıyı koruyorsa `### 3.1` ve `### 3.2` kalır, yalnızca `####` düzeyi düzleşir.

### Rapor: tek cümlelik paragraflar hareketlere göre toplanıyor

**Önce**

> Kuzey depoda iade oranı %6,2 olarak ölçülmüştür.
>
> Diğer depolarda bu oran %3,1'dir.
>
> Fark, çalışan görüşmelerinde manuel veri girişine bağlanmıştır.
>
> Görüşmeler bu bağı kanıtlamaz.
>
> Yönetim üç aylık bir barkod pilotu önermektedir.

**Sonra**

> Kuzey depoda iade oranı %6,2, diğer depolarda %3,1 olarak ölçülmüştür. Çalışan görüşmeleri farkı manuel veri girişine bağlamaktadır; görüşmeler bu bağı kanıtlamaz.
>
> Yönetim üç aylık bir barkod pilotu önermektedir.

Beş paragraf iki paragraf oldu: bulgu → yorum ve sınırı bir hareket, öneri ayrı bir söylem işlevi. Öneriyi aynı paragrafa almak yanlış olmazdı; ama bulgu → öneri geçişi sert bir işlev değişimi olduğu için sınır meşrudur ve okur öneriyi bulgudan ayrı görür. Kanıt düzeyleri korundu; yorum olguya, öneri karara çevrilmedi.

### Yönetim notu: tekrarlanan bölüm giriş ve sonuçları

**Önce**

> ### 4.1 Sıcaklık etkisi
>
> Bu bölümde sıcaklığın hata oranı üzerindeki etkisi ele alınmaktadır. Hata 20 °C'de %3, 40 °C'de %11 ölçülmüştür. Dolayısıyla sıcaklığın önemi açıkça görülmektedir.
>
> ### 4.2 Nem etkisi
>
> Bu bölümde nemin hata oranı üzerindeki etkisi ele alınmaktadır. Hata %30 nemde %4, %80 nemde %9 ölçülmüştür. Dolayısıyla nemin önemi açıkça görülmektedir.
>
> ### 4.3 Birleşik etki
>
> Bu bölümde iki etkenin birlikte etkisi ele alınmaktadır. 40 °C ve %80 nemde hata %19 ölçülmüştür. Bu değerlendirmeler çevresel koşulların kritik rolünü göstermektedir.

**Sonra (derin düzenleme)**

> ### 4. Çevresel koşulların etkisi
>
> Hata 20 °C'de %3, 40 °C'de %11; %30 nemde %4, %80 nemde %9 ölçülmüştür. 40 °C ve %80 nemde hata %19'a çıkmıştır.

**Sonra (başlıklar korunuyor)**

> ### 4.1 Sıcaklık etkisi
>
> Hata 20 °C'de %3, 40 °C'de %11 ölçülmüştür.
>
> ### 4.2 Nem etkisi
>
> Hata %30 nemde %4, %80 nemde %9 ölçülmüştür.
>
> ### 4.3 Birleşik etki
>
> 40 °C ve %80 nemde hata %19 ölçülmüştür.

İki sürüm de altı sarmalayıcı cümleyi siler ve beş ölçümü korur. Hangi sürümün seçileceğine kullanıcının müdahale düzeyi ve numaralı bölümlere yapılan göndermeler karar verir.

### Rapor: sonuçla sınırlılığı yakınlaşıyor

**Önce**

> ### 3.1 Doğruluk
>
> Model, doğrulama kümesinde %91 doğruluk elde etmiştir.
>
> ### 3.2 Dağıtım
>
> Model haziran ayında üretim ortamına alınmıştır.
>
> ### 3.3 Sınırlılıklar
>
> 3.1'deki %91 doğruluk yalnızca 2024 verisiyle ölçülmüştür; 2025 verisinde ölçüm yapılmamıştır. Üretim ortamındaki doğruluk izlenmemektedir.

**Sonra**

> ### 3.1 Doğruluk
>
> Model, doğrulama kümesinde %91 doğruluk elde etmiştir. Bu ölçüm yalnızca 2024 verisiyle yapılmıştır; 2025 verisinde ölçüm yapılmamıştır.
>
> ### 3.2 Dağıtım
>
> Model haziran ayında üretim ortamına alınmıştır. Üretim ortamındaki doğruluk izlenmemektedir.

Her sınırlılık sınırladığı iddianın yanına taşındı; üç bölüm iki bölüm oldu. Kurum şablonu ayrı bir "Sınırlılıklar" bölümü dayatıyorsa bölüm kalır ve 3.1'de yalnızca "2024 verisiyle" kapsam nitelemesi bırakılır.

## Karşı örnekler: kalması gereken yapı

Sorun başlık değil, hak edilmemiş yapısal sınırdır. Aşağıdaki yapılar korunur.

### Bağımsız tekrarlanabilir deneyler

> ### Deney 1: Sabit sıcaklık
>
> Sensör 25 °C'de 6 saat boyunca dakikada bir örneklenmiştir. Kalibrasyon deneyden hemen önce yapılmıştır.
>
> ### Deney 2: Sıcaklık taraması
>
> Sensör 10 °C'den 50 °C'ye 5 °C'lik adımlarla ısıtılmış, her adımda 30 dakika beklenmiştir. Kalibrasyon yalnızca deney başında yapılmıştır.

İki bölüm kısadır, ama her biri kendi başına tekrarlanabilir olmalıdır. Kalibrasyon cümleleri benzer görünse de farklı bilgi taşır; "tekrar" diye silinmez. Bölümler birleştirilmez.

### Hukuki hükümler

> **7.1** Sağlayıcı, bildirimin kendisine ulaştığı tarihten itibaren on iş günü içinde yazılı yanıt vermekle yükümlüdür.
>
> **7.2** Bu süre, tarafların yazılı mutabakatı olmaksızın uzatılamaz.

Numaralı hükümler ayrı ayrı atıf alır; tek paragrafa birleştirilmez.

### Dergi kuralıyla ayrılan bölümler

Dergi "Yöntem", "Bulgular" ve "Tartışma" bölümlerini dayatıyorsa "Bulgular" tek paragraf olsa da bölüm kalır. Yakınlık kuralı bölüm sınırını değil bölüm içini düzenler: bulgunun kapsam nitelemesi bulgunun yanına, yorumu tartışmaya gider.

### Güvenlik açısından kritik adımlar

> 1. Ana şalteri kapatın.
> 2. Kapasitörlerin boşalması için 5 dakika bekleyin.
> 3. Voltmetreyle gerilimin sıfır olduğunu doğrulayın.
> 4. Kapağı açın.

Adım sırası güvenlik taşır; düzyazıya çevrilmez, adımlar birleştirilmez.

### Uzun belgenin gezinme çıpaları

Kırk sayfalık kılavuzdaki on iki `##` başlığı, her biri birkaç paragraf taşıyorsa gezinme içindir. Girişteki "Bu kılavuz dört bölümden oluşur; mevcut kurulumu güncelliyorsanız üçüncü bölüme geçebilirsiniz" cümlesi okurun nereden başlayacağını değiştirdiği için bilgi taşır. Başlık sayısına bakıp birleştirme.

### Uzun kalması gereken paragraf

Ölçüm → dağılım → yorum → karşı veri → belirsizlik hareketini yedi cümlede tamamlayan analitik bir paragraf tek baskın hareketi taşır. Okur bu paragrafın içinde kalarak sayıların, yorumun ve çekincenin ilişkisini görür; üç kısa paragrafa bölmek her çekinceyi dayandığı sayıdan uzaklaştırır. Uzunluk gerekçesiyle bölünmez.

### Kısa kalması gereken paragraf

> `--purge` seçeneği bütün yedekleri geri alınamaz biçimde siler.

Tek cümlelik bu paragraf komşularıyla birleştirilmez: yalıtılmışlığı işlevseldir, uyarının görülmesini sağlar. Kısa olduğu için "erken bölünmüş" sayılmaz; kavramsal sınır gerçekten buradadır.

### Sabit numaralı bölümler

Belge başka belgelerden `Bölüm 3.2` biçiminde atıf alıyorsa ya da kullanıcı numaralı hiyerarşiyi koruyorsa bölümler birleştirilmez; yalnızca bölünmenin ürettiği duyuru, askı ve gönderme cümleleri silinir.
