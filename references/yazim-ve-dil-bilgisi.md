# Yazım ve dil bilgisi

Bu dosya Türkçe metnin biçim doğruluğunu tutar: TDK Yazım Kılavuzu'na dayanan yazım kuralları, alıntı sözcüklerin ses ve ek davranışı, tamlama kuruluşu, özne–yüklem ve ortak öge uyumu, sık kullanılan fiillerin hâl çerçevesi. Bunlar "AI izi" değildir; insan metninde de, model metninde de aynı ölçütle düzeltilir. Yazım yanlışı önermeyi değiştirmez ama okuru durdurur ve metnin güvenilirliğini düşürür; ortak öge ve tamlama hatası ise önermeyi bulanıklaştırabilir.

Kurallar `SKILL.md`'deki kural 4'e (cümle ögesi düşürülmez, birleştirilen cümle kurallı kalır) ve kural 5'e (bir terim, bir anlam; aynı sözcük tek yazımla geçer) bağlıdır. Her bölüm doğru biçimi, dokunulmayacak karşı örneği ve aşırı düzeltme belirtisini birlikte verir.

## İçindekiler

- [Kullanım ilkesi](#kullanım-ilkesi)
- [Dokunulmayacaklar](#dokunulmayacaklar)
- [Bitişik ve ayrı yazım](#bitişik-ve-ayrı-yazım)
- [`ki`, `de/da`, `mi`](#ki-deda-mi)
- [Kesme işareti](#kesme-işareti)
- [Sayılar, yüzde ve kısaltmalar](#sayılar-yüzde-ve-kısaltmalar)
- [Büyük harf ve düzeltme işareti](#büyük-harf-ve-düzeltme-işareti)
- [Sözcüğün kökeni: alıntıların ses ve ek davranışı](#sözcüğün-kökeni-alıntıların-ses-ve-ek-davranışı)
- [Kökenden gelen anlam tekrarı](#kökenden-gelen-anlam-tekrarı)
- [Söz varlığı katmanları ve kayıt](#söz-varlığı-katmanları-ve-kayıt)
- [Tamlamalar](#tamlamalar)
- [Sayı uyumu ve çokluk eki](#sayı-uyumu-ve-çokluk-eki)
- [Ortak öge uyumu](#ortak-öge-uyumu)
- [Fiil–hâl çerçevesi listesi](#fiilhâl-çerçevesi-listesi)
- [Örnekler](#örnekler)
- [Aşırı düzeltme belirtileri](#aşırı-düzeltme-belirtileri)
- [Kaynaklar ve doğrulama düzeyi](#kaynaklar-ve-doğrulama-düzeyi)

## Kullanım ilkesi

1. **Kesin yazım yanlışı her düzeyde düzeltilir.** TDK Yazım Kılavuzu'nun açık kuralına aykırı yazım hafif düzeyde de doğru biçime (`Türkçede`, `Türk Dil Kurumuna`, `fark etti`, `her şey`, `hakkı`, `8'inci`) getirilir; bu düzeltme önermeyi, statüyü ve kesinliği değiştirmez. Kullanıcı kapsamı açıkça başka bir işe daralttıysa (`yalnızca noktalama`) dokunma, metnin dışında tek satırla bildir.
2. **Tercih yanlış değildir.** Kılavuzun izin verdiği ya da kaynağın tutarlı biçimde uyguladığı tercih (şapkasız yazım, teknik tabloda ondalık nokta, kurumsal yazım kılavuzu) düzeltme konusu değildir. Yalnızca aynı metinde aynı sözcüğün iki yazımı varsa kaynağın baskın yazımına göre birleştir.
3. **Yazma kipinde kurala uy.** Kullanıcı için yazdığın metinde Kılavuz'un yazımını kullan; ondalık virgül, `%25`, `TDK'nin`, `Türkçede`, `hâlâ`.
4. **Dil bilgisi düzeltmesi önerme eklemez.** Ortak ögeyi açarken (`ona güveniyor`) yalnızca kaynakta zaten bulunan ögeyi yinele; yeni aktör, nesne ya da ilişki yazma. Çatı uyuşmazlığını giderirken kaynakta adı geçmeyen aktörü uydurma.
5. **Belirsiz yazımda yorum seçme.** `1.500` Türkçede bin beş yüz, İngilizce biçimde bir buçuktur; ayırıcının anlamı belli değilse sayıya dokunma, metnin dışında sor (**Belirsizlik ve yorum seçimi**).

## Dokunulmayacaklar

Yazım kuralı şu alanlara girmez; yanlış görünse de olduğu gibi kalır:

- doğrudan alıntı, kullanıcı geri bildirimi ve tanık ifadesi (`“yazılım herşeyi siliyor” yazdı`),
- kod, komut, değişken, dosya adı, URL, sürüm numarası (`sürüm 3.5`, `v2.10`),
- tescilli ya da resmî ad: kurumun kendi yazımı (`Türk Standardları Enstitüsü`, `Makina Mühendisleri Odası`), marka, ürün, kitap ve dergi adı,
- tablo hücresi ve dayatılmış biçim (dergi şablonu, mevzuat metni),
- yazarın bilinçli biçem tercihi (edebî metin, ağız taklidi; [Kenar türler](kenar-turler.md)).

Teknik metindeki ad (`cache.py`, `GitHub`) Türkçe ek alır; ek kesmeyle ve okunuşa göre gelir (`cache.py'ye`, `GitHub'a`, `Linux'ta`). Adın kendisi değişmez.

## Bitişik ve ayrı yazım

**Yardımcı fiille kurulan birleşik fiil.** `etmek`, `edilmek`, `eylemek`, `olmak`, `olunmak` ile kurulan birleşik fiilde ilk sözcük ses düşmesine, ses değişmesine ya da ses türemesine uğruyorsa bitişik, uğramıyorsa ayrı yazılır (TDK › Bitişik Yazılan Birleşik Kelimeler, Ayrı Yazılan Birleşik Kelimeler).

| Ses olayı var: bitişik | Ses olayı yok: ayrı |
|---|---|
| `affetmek` (af), `hissetmek` (his), `reddetmek` (ret), `zannetmek` (zan) — ünsüz ikizleşir | `fark etmek`, `ayırt etmek`, `farz etmek` |
| `kaybetmek`, `kaybolmak` (kayıp), `kaydetmek`, `kaydolmak` (kayıt), `sabretmek` (sabır), `keşfetmek` (keşif), `emretmek` (emir), `seyretmek` (seyir), `hapsetmek` (hapis), `şükretmek` (şükür), `kahrolmak` (kahır) — ünlü düşer | `yardım etmek`, `kabul etmek`, `terk etmek`, `ilan etmek`, `dert etmek`, `alt etmek`, `var olmak` |

Test: yardımcı fiili çıkar; kalan sözcük kendi biçimini koruyor mu (`fark` → `fark etmek`) yoksa ses değiştiriyor mu (`kayıp` → `kayb-`)? Değişiyorsa bitişik.

**Belgisiz sözcükler.** `biraz`, `birçok`, `birçoğu`, `birkaç`, `birkaçı`, `birtakım`, `herhangi`, `hiçbir`, `hiçbiri` gelenekleşmiş biçimde bitişik yazılır (TDK › Bitişik Yazılan Birleşik Kelimeler). Sözcüklerden hiçbiri anlam değiştirmiyorsa birleşik ayrı yazılır; `bir şey`, `her şey`, `her biri`, `pek çok`, `ya da` bu ilkeye göre ayrıdır. `Bir takım elbise` (sayı + ad) ile `birtakım sorunlar` (belgisiz) aynı yazılmaz.

**Terim birleşikleri.** Birleşik terimler (`dil bilgisi`, `bilgi işlem`) Türkçe Sözlük'teki madde başına göre yazılır; sezgiyle bitiştirilmez ya da ayrılmaz. Kaynakta terim tutarlı yazılmışsa (`veri tabanı` ya da `veritabanı`) terimi değiştirme; aynı metinde ikisi varsa baskın olanı kullan.

## `ki`, `de/da`, `mi`

**Bağlaç `ki` ayrı yazılır:** `demek ki`, `kaldı ki`, `bilmem ki`, `öyle zor ki`. Kalıplaşmış birkaç sözcükte bitişiktir: `belki`, `çünkü`, `hâlbuki`, `mademki`, `meğerki`, `oysaki`, `sanki` (TDK › Bağlaç Olan ki'nin Yazılışı). İlgi zamiri ve sıfat yapan `-ki` bitişiktir ve ünlü uyumuna girmez (`akşamki`, `yarınki`, `benimki`); yalnızca `bugünkü`, `dünkü`, `öbürkü` uyuma girer (TDK › Küçük Ünlü Uyumu).

**Bağlaç `de/da` ayrı yazılır**, önceki sözcüğün son ünlüsüne uyar, hiçbir zaman `te/ta` olmaz ve kesmeyle ayrılmaz: `Ayşe de geldi`, `sensör de`; `ya da` ayrıdır (TDK › Bağlaç Olan da, de'nin Yazılışı). Bulunma eki `-de/-da/-te/-ta` bitişiktir: `laboratuvarda`, `2025'te`. Ayırma testi: sözcüğü çıkar; cümle anlamını koruyorsa bağlaçtır (`Sensör de arızalandı` → `Sensör arızalandı`), bozuluyorsa ektir. Bağlaç `de` kapsam taşır; düzenlemede bağlandığı ögeyle birlikte taşınır (**Bağlaç ilişki kuramaz**).

**Soru eki `mi` ayrı yazılır**, kişi ve zaman ekleri ona bitişir: `geldi mi`, `hazır mısınız`, `doğru muydu`. Soru eki zarf tümleci olan yan cümledeyse cümle sonuna soru işareti konmaz (`Çalışır mı çalışmaz mı, ölçüm gösterecek.`).

## Kesme işareti

TDK › Kesme İşareti ve Noktalama İşaretleri (Açıklamalar) sayfalarına göre:

- **Özel ada gelen çekim eki ayrılır:** `Ankara'da`, `Yunus Emre'yi`, `Python'da`. Yabancı özel ada ek okunuşa göre gelir: `Cannes'a`.
- **Yapım eki ve çokluk eki ayrılmaz; ardından gelen ekler de ayrılmaz:** `Türkçe`, `Türkçenin`, `Türkçede`, `İngilizceye`, `Avrupalı`, `Türklük`, `Ahmetler`. Dil adı yapım ekiyle türediği için `Türkçe'de` yanlıştır.
- **Kurum, kuruluş, kurul, birleşim, oturum ve iş yeri adlarına gelen ekler ayrılmaz:** `Türk Dil Kurumundan`, `Türkiye Büyük Millet Meclisine`, `Rektörlüğe`. TDK bu kuralın 1985'ten beri kılavuzlarda olduğunu, 1996'da "çoklukla" sözcüğünün kaldırılarak kesinleştiğini bildirir.
- **Unvana gelen ek ayrılır:** `Nihat Bey'e`, `Türk Dil Kurumu Başkanı'na` (başkan kişidir, kurum değildir).
- **Kısaltmaya gelen ek ayrılır ve kısaltmanın okunuşuna uyar:** `TDK'nin` (te-de-ke), `TBMM'ye`, `ABD'de`, `NATO'ya`. Sonunda nokta olan kısaltmaya gelen ek kesmesiz yazılır.
- **Rakama gelen ek ayrılır:** `1985'te`, `8'inci`, `7,65'lik`, `%40'ı`. Sıra sayısı ekle gösterilince rakamdan sonra nokta konmaz: `8'inci`, `8.` ya da `sekizinci`; `8.'inci` yanlıştır.
- **Sonu 3. teklik iyelik ekli özel ada başka iyelik gelirse kesme konmaz:** `Boğaz Köprümüzün`, `Amik Ovamızın`.

## Sayılar, yüzde ve kısaltmalar

- **Ondalık virgül, binlik nokta.** `38,6`, `4.567`, `1.500.000 lira` (TDK › Sayıların Yazılışı). Düzenlemede ayırıcıyı değiştirme: sayı değişmezdir ve kaynak kod, tablo ya da uluslararası biçim kullanıyor olabilir. Yazma kipinde Türkçe biçimi kullan; kodda, sürüm numarasında ve çıktı günlüğünde kaynağın biçimi kalır.
- **Yüzde işareti sayıdan önce ve bitişik yazılır:** `%25`, `‰50`; ek okunuşa göre gelir: `%25'i` (yüzde yirmi beşi), `%40'ı`, `%3'ü`.
- **Bayağı kesre gelen ek alttaki sayının okunuşuna uyar:** `1/2'si`, `4/8'i`.
- **Saat, para, ölçü ve istatistik verisinde rakam kullanılır:** `17.30'da`, `25 kilogram`. Sayıyı yazıya ya da yazıyı rakama çevirmek değişiklik bütçesine girer; gerekçesiz yapılmaz.
- **Kısaltma ilk geçtiği yerde açılır** (kural 5). Ek kısaltmanın okunuşuna uyar (`TDK'nin`, `NATO'ya`); okunuş belirsizse kaynağın biçimini koru.

## Büyük harf ve düzeltme işareti

**Büyük harf.** Dil ve lehçe adları büyük harfle başlar (`Türkçe`, `Kazakça`). Belirli bir tarih bildiren ay ve gün adı büyük, tarih bildirmeyen küçük yazılır: `29 Ekim 1923`, `Festival 25 Haziran'da başlayacak`; `eylülün ikinci haftasında`, `perşembe günleri` (TDK › Büyük Harflerin Kullanıldığı Yerler). Tarih değişmezdir; yalnızca büyük harfi düzeltirken gün, ay ve yılı koru.

**Düzeltme işareti kaldırılmadı.** TDK'ye göre işaret üç yerde kullanılır (TDK › Düzeltme İşareti; SSS "Düzeltme işareti kaldırıldı mı?"):

1. Yazılışı aynı, anlamı ve okunuşu farklı sözcükleri ayırmak için: `hâlâ` (henüz) / `hala`, `kâr` / `kar`, `âdet` / `adet`, `âlem` / `alem`, `hâl` / `hal`.
2. Alıntı sözcüklerde ince `g` ve `k`'den sonra gelen `a` ve `u` için: `kâğıt`, `dükkân`, `rüzgâr`.
3. Nispet `-î`'sini iyelik ve belirtme ekinden ayırmak için: `resmî` (resmî yazı) / `resmi` (onun resmi), `millî`, `askerî`, `dinî`; Türkçe ek gelince işaret kalır: `millîleştirmek`, `resmîlik`.

Kaynak işareti tutarlı biçimde kullanmıyorsa düzenlemede bütün metne ekleme; yalnızca okurun yanlış okuyacağı çiftte (`hala` ↔ `hâlâ`, `kar` ↔ `kâr`) ekle. Kaynak işareti kullanıyorsa silme.

## Sözcüğün kökeni: alıntıların ses ve ek davranışı

Türkçe Türk dilleri ailesindendir, sondan eklemelidir ve ünlü uyumu ile ünsüz benzeşmesi Türkçe kökenli sözcüklerde düzenli işler. Ek seçimi sözcüğün yazılışına değil söylenişine bakar; Arapça, Farsça, Fransızca ve İngilizceden gelen sözcüklerde söyleyiş Türkçe kurala uymadığı için ek de uymaz. Türkçe Sözlük madde başında köken dilini ve ekli biçimi (`hak, -kkı`) verir; şüpheli ek orada denetlenir.

**İnce söylenen son ünsüz.** Son ünlüsü kalın olduğu hâlde son sesi ince söylenen alıntılar ince ünlülü ek alır (TDK › Büyük Ünlü Uyumu): `saat` → `saate`, `saatler`; `alkol` → `alkolü`; aynı örüntüyle `kontrolü`, `protokolü`, `sembolü`, `rolü`, `petrolü`, `kabulü`, `usulü`, `hayali`, `hâli`. Teknik metinde en sık geçenler `kontrol`, `protokol`, `sembol` ve `rol` sözcükleridir.

**Küçük ünlü uyumu aranmaz.** Alıntılarda küçük ünlü uyumu çoğu zaman yoktur ve ek bu yüzden kökün son ünlüsüne göre seçilir (TDK › Küçük Ünlü Uyumu): `alkollü`, `saatlik`.

**Ünsüz ikizleşmesi.** Arapçada sonu ikiz ünsüzlü olup Türkçede tek ünsüzle yazılan sözcüklerde ünlüyle başlayan ek ya da yardımcı fiil gelince ünsüz ikizleşir (TDK › Ünsüz Türemesi): `hak` → `hakkı`, `his` → `hissi`, `hissetmek`, `ret` → `reddi`, `reddetmek`, `tıp` → `tıbbı`, `zam` → `zammı`, `zan` → `zannı`, `af` → `affetmek`, `şer` → `şerri`. Teknik metinde sık geçen `hat` (iletim hattı, üretim hattı) ve `üs` (üssü) aynı örüntüdedir; Türkçe Sözlük madde başıyla denetle.

**Ünsüz yumuşaması alıntıda düzensizdir.** Çok heceli sözcüklerde sondaki `p, ç, t, k` ünlüyle başlayan ek alınca çoğunlukla yumuşar (`kitap` → `kitabı`, `grup` → `grubu`, `metot` → `metodu`, `süreç` → `süreci`); ama `hukuk` → `hukuku`, `ahlak` → `ahlakı` gibi yumuşamayan alıntılar vardır. Ekli biçimi sezgiyle değil sözlükle karar ver; kaynak tutarlı yazıyorsa dokunma.

**Yazılışı yerleşmiş alıntı.** Türkçe Sözlük'teki yazım esastır: `laboratuvar`, `makine`, `metot`, `orijinal`, `entelektüel`, `standart`. Resmî adda kurumun yazımı kalır (`Makina Mühendisleri Odası`, `Türk Standardları Enstitüsü`; bkz. **Dokunulmayacaklar**).

## Kökenden gelen anlam tekrarı

Alıntı sözcüğün ya da kısaltmanın anlamı bilinmeyince aynı anlam Türkçe sözcükle bir kez daha söylenir. Bu, kural 3'ün (yalnızca gerekli bilgi) sözcük düzeyindeki biçimidir.

| Tekrar | Neden | Doğal biçim |
|---|---|---|
| `iade etmek` önüne `geri` | `iade` geri verme demektir | `iade etmek` |
| `optimum` önüne `en`; `maksimum`, `minimum` önüne `en` | `optimum` en uygun demektir | `optimum eşik`, `en uygun eşik` |
| `PIN` sonrası `numarası` | PIN: personal identification **number** | `PIN` |
| `ATM` sonrası `makinesi` | ATM: automated teller **machine** | `ATM` |
| `API` sonrası `arayüzü` | API: application programming **interface** | `API` |
| `LCD` sonrası `ekran` | LCD: liquid crystal **display** | `LCD` |

Test: kısaltmayı açılımıyla oku; arkasındaki Türkçe ad açılımın baş sözcüğünü (İngilizcede son ad) yineliyorsa tekrardır. Yinelemiyorsa tekrar değildir ve kalır: `IP adresi` (Internet **Protocol**), `SQL sorgusu` (Structured Query **Language**; sorgu dilin kendisi değil, o dille yazılan şeydir), `SMS mesajı` (Short Message **Service**; mesaj servisin kendisi değildir), `DNS sunucusu`, `USB bellek`, `HTTP isteği`. Alanda yerleşmiş ve kurumların resmî metninde geçen kullanım (`HIV virüsü` tıp yayınlarında yaygındır) düzenlemede zorlanmaz; yazma kipinde tekrarsız biçimi seç.

## Söz varlığı katmanları ve kayıt

Türkçenin söz varlığında Türkçe kökenli sözcüklerin yanında Arapça ve Farsça (Osmanlı Türkçesi döneminden), Fransızca (19. ve 20. yüzyıl kurum ve bilim dili) ve İngilizce (güncel teknik dil) katmanları ile 1932'de kurulan Türk Dili Tetkik Cemiyetinin (bugünkü Türk Dil Kurumu) yürüttüğü dil devriminin türetmeleri (`bilim`, `yöntem`, `kuram`, `örneklem`) bir arada durur. Aynı kavramın birden çok katmandan karşılığı olabilir: `yöntem` / `metot`, `kuram` / `teori`, `bilim` / `ilim`, `olasılık` / `ihtimal`.

- **Katmanı değiştirmek kayıt değiştirmektir.** `İhtimal` → `olasılık` ya da `teori` → `kuram` dönüşümü sadeleştirme değil, kayıt ve çoğu zaman alan tercihidir; gerekçesiz yapılmaz (**Aşırı Türkçeleştirme**). Osmanlıcalaştırma da aynı ölçüde yasaktır.
- **Aynı metinde katman nöbetleşmez.** Bir kavrama bir ad (kural 5): metin `yöntem` dediyse aynı nesne için `metot`a geçmez. Kaynakta iki ad iki ayrı şeyi adlandırıyorsa birleştirme.
- **Kalıp tamlamalar formüldür.** Arapça–Farsça kuruluşlu tamlamalar ve ekler (`-î`, `-âne`, `bi-`, `na-`) hukuki ve kurumsal metinde terimdir; açılmaz, Türkçe kuruluşa çevrilmez ([Kenar türler](kenar-turler.md)).
- **Arapça çokluk biçimi.** `evrak`, `esnaf`, `eşya` köken dilinde çokluktur; Türkçede tekil gibi kullanılır ve `-lar` alabilir. Bu düzeltme konusu değildir.

## Tamlamalar

**Belirtili ve belirtisiz tamlama başka göndergedir.** Belirtili tamlama (`projenin bütçesi`) belirli bir varlığın parçasını, belirtisiz tamlama (`proje bütçesi`) bir türü ya da kavramı adlandırır. `Kullanıcının deneyimi` o kullanıcıyı, `kullanıcı deneyimi` alan kavramını söyler. İngilizce `the` her ada belirtililik yükleyince metin `sistemin performansının değerlendirilmesinin sonuçları` zincirine döner ([Türkçe ritim › İyelik zinciri](turkce-ritim-ve-ceviri-kokusu.md#iyelik-zinciri)). Belirtisizliği gönderge değişmiyorsa seç; belirli bir varlık kastediliyorsa belirtili kalır.

**Son tamlanan iyelik ekini taşır.** Serbest öbekte belirtisiz tamlamanın başı iyelik alır: `proje yönetimi`, `veri analizi`, `hata oranı`. `Proje yönetim ekipte kaldı` eksik tamlamadır. Zincirin içindeki ögenin iyeliği düşebilir ve adlaşmış öbekte düşer: `Türk Dil Kurumu`, `veri analiz yöntemleri`, `risk değerlendirme raporu`. İçteki eksik iyeliği "düzeltme"; yalnızca öbeği bitiren başa bak.

**Terim tamlaması sabittir.** `Doğal dil işleme`, `görüntü işleme`, `sinyal işleme`, `makine öğrenmesi`, `derin öğrenme` alanın yerleşmiş adlarıdır; iyelik ekleyerek (`görüntü işlemesi`) ya da belirtili yaparak değiştirilmez (kural 5).

**İyelik üst üste gelmez.** Tamlanan zaten iyelikli birleşik adsa ikinci iyelik eklenmez: `Türk Dil Kurumu Başkanı`, `hava durumu raporu`, `kullanıcı arayüzü tasarımı`.

**Ek ortaklığı meşrudur.** Türkçe aynı eki sıralanan ögelerin sonuncusuna bağlayabilir: `sistemin hız ve güvenilirliği`, `Ankara ve İstanbul'da`. Bunu eksik ek sanıp açma; kapsam belirsizleşiyorsa (`eski öğrenci ve öğretmen evi`) yorum seçme, kaynağı koru.

**Sıfat ile tamlayan aynı değildir.** `Bilimsel araştırma` (niteleme) ile `bilim araştırması` (tür) ya da `toplumsal sorun` ile `toplum sorunu` eş anlamlı değildir; çeşitlilik için birinden ötekine geçme.

**Sıfat tamlaması kapsam belirsizliği taşıyabilir.** `Eski öğrenci evi` hem `[eski öğrenci] evi` hem `eski [öğrenci evi]` okunur. Kaynakta tek okuma açık değilse yeniden kurma; belirsizliği koru ya da metnin dışında sor.

## Sayı uyumu ve çokluk eki

**Sayı sıfatı ve çokluk bildiren sıfattan sonra ad çokluk eki almaz:** `üç sensör`, `birkaç cümle`, `birçok kullanıcı`, `her deney`. `Bazı`, `tüm`, `bütün`, `çeşitli`, `farklı` ile çoğul ad doğaldır (`bazı sorunlar`, `farklı yöntemler`).

**İnsan dışı çoğul özneyle yüklem çoğunlukla teklik kalır:** `Sonuçlar bu ilişkiyi gösteriyor`, `Sensörler 12 Mart'ta değiştirildi`. `Sonuçlar ... göstermektedirler` İngilizce sayı uyumunun izidir. İnsan öznede iki biçim de doğrudur; yüklemdeki `-lar` bireyleri öne çıkarır (`Katılımcılar formu doldurdular`). `Bazıları`, `başkaları` gibi belgisiz zamir öznede yüklem çokluk eki almaz. Kurum adı özne tekildir.

**Düzeltme sayı uyumuyla sınırlıdır.** `Üç sensörler` → `üç sensör` düzeltmesi sayıyı korur; `sensörlerin üçü` (bir bütünün parçası) ile `üç sensör` aynı önerme değildir, kaynak bütün kurmuyorsa ekleme.

## Ortak öge uyumu

İki yüklem bir ögeyi paylaşıyorsa öge iki yüklemin de çerçevesine uymalıdır. Bu, kural 4'ün "cümle ögesi düşürülmez" ilkesinin sözdizimsel karşılığıdır ve en çok iki cümleyi birleştirirken bozulur: birleştirme her zaman ortak öge kurar.

| Uyumsuzluk | Kurallı | Neden |
|---|---|---|
| hâl: `Kullanıcılar uygulamayı seviyor ve güveniyor` | `Kullanıcılar uygulamayı seviyor ve ona güveniyor` | `sevmek -i`, `güvenmek -e` |
| hâl: `Ekip protokolü inceledi ve itiraz etti` | `Ekip protokolü inceledi ve protokole itiraz etti` | `incelemek -i`, `itiraz etmek -e` |
| çatı: `Veriler toplandı ve analiz ettik` | `Veriler toplandı; verileri analiz ettik` | edilgen ile etken yüklem aynı özneyi paylaşamaz; kaynak toplayanı adlandırmıyor |
| ek-fiil: `Sistem hızlı ve verileri şifreliyor` | `Sistem hızlı; verileri şifreliyor` | ad cümlesi ile fiil cümlesi `ve` ile tek yüklemmiş gibi bağlanmaz; zaman değişmez |

**Onarım yeni bilgi eklemez.** Açılan öge kaynaktaki ögenin kendisidir (`protokole`, `ona`). Çatı uyuşmazlığında edilgen yüklemi etkene çevirip ona kaynakta olmayan aktör (`araştırmacılar`, `biz`) verme; etken yüklemi edilgene çevirip kaynaktaki aktörü de silme. İki yargıyı ayrı tutmak çoğu zaman tek güvenli onarımdır. Ek-fiil uyumsuzluğunda zamanı değiştirme (`şifreliyor` → `şifreler` zamansal ankrajı değiştirir); en güvenli onarım iki cümleye ayırmaktır.

**Cümle birleştirirken denetle.** Düzenleme iki cümleyi `ve`, `-ip`, `-erek` ile bağladığında sor: ortak özne, nesne ve tümleç iki yüklemle de aynı hâlde mi; çatı ve kişi aynı mı? Değilse ögeyi ikinci yüklemde yinele ya da cümleleri ayrı bırak.

## Fiil–hâl çerçevesi listesi

Bilimsel ve teknik düzyazıda sık geçen fiillerin tümleç hâli. Yakın anlamlı iki fiil farklı hâl istiyorsa ortak öge kuramaz; bu çiftler aynı satırdadır. Liste kapalı değildir; hâl değişince anlam da değişebilir ([Sözcük birleşimleri › Hâl seçimi](sozcuk-birlesimleri.md#hâl-seçimi-ve-fiilhâl-çerçevesi)).

| Fiil ve hâl | Yakın anlamlı, başka hâl | Not |
|---|---|---|
| `X'i etkilemek` | `X'e etki etmek` | `X üzerine etki etmek` edat izidir |
| `X'i kullanmak` | `X'ten yararlanmak`, `X'e başvurmak` | |
| `X'i ele almak`, `X'i incelemek` | `X'e değinmek`, `X'ten söz etmek / bahsetmek` | `değinmek` kısa geçiştir, `incelemek` ayrıntılıdır; eş anlamlı değildir |
| `X'i gerektirmek` | `X'e ihtiyaç duymak`, `X'e gereksinim duymak` | |
| `X'i desteklemek` | `X'e katkı sağlamak / katkıda bulunmak`, `X'e destek olmak` | `hipotezi desteklemek` yerleşik eşdizimdir |
| `X'i doğurmak` | `X'e neden olmak`, `X'e yol açmak` | üçü de nedensellik kurar; ilişki kaynaktan gelir |
| `X'i karşılamak` | `X'e uymak`, `X'e uygun olmak` | `gereksinimi karşılamak`, `standarda uymak` |
| `X'i içermek`, `X'i kapsamak` | `X'ten oluşmak` | `oluşmak` bütünün tamamını söyler, `içermek` parçasını |
| `X'i temel almak` | `X'e dayanmak` | |
| `X'i sınamak / test etmek / doğrulamak` | `X'e güvenmek` | `modeli sınadık ve ona güveniyoruz`; ortak nesne kendiliğinden kurulmaz |
| `X'i Y ile karşılaştırmak / kıyaslamak` | `X'ten farklı olmak`, `X'e benzemek` | |
| `X'i Y'ye dönüştürmek`, `X'i Y'ye uygulamak` | `X'ten Y'ye geçmek` | |
| `X'i Y'den ayırmak`, `X'i Y'den çıkarmak` | `X'ten ayrılmak` | |
| `X'e erişmek`, `X'e ulaşmak` | `X'i elde etmek` | `başarı, sonuç, derece elde etmek` yerleşiktir; ölçüm cümlesinde doğrudan fiil (`hata %20 azaldı`) yeğlenir ([Sözcük birleşimleri](sozcuk-birlesimleri.md)) |
| `X'e odaklanmak`, `X'e yönelmek` | `X'i hedeflemek` | `X hakkında odaklanmak` edat izidir |
| `X'ten kaynaklanmak` | `X'e bağlı olmak` | `bağlı olmak` bağımlılık, `kaynaklanmak` köken söyler |
| `X'le ilgilenmek`, `X'le uğraşmak` | `X'i ele almak` | |
| `X'e itiraz etmek`, `X'e karşı çıkmak` | `X'i reddetmek` | `itiraz` süreç, `ret` karardır; statü değişir |
| `X'e karar vermek` | `X'i kararlaştırmak` | |
| `X'e katılmak` | `X'i paylaşmak` (görüş) | yakın anlamlıdır ama ortak nesne kuramaz: `görüşü paylaşıyor ve ona katılıyor` |

## Örnekler

**Önce**

> Raporun Türkçe'si 3 Mart 2025'te Bilgi Teknolojileri Kurumu'na gönderildi. Taslakta herşey tamam değildi; veri hatı kesintisine ilişkin bölüm hâlâ boştu ve ekip bunu geç farketti.

**Sonra**

> Raporun Türkçesi 3 Mart 2025'te Bilgi Teknolojileri Kurumuna gönderildi. Taslakta her şey tamam değildi; veri hattı kesintisine ilişkin bölüm hâlâ boştu ve ekip bunu geç fark etti.

Yalnızca yazım değişti: dil adı yapım ekli olduğu için kesmesiz, kurum adına gelen ek kesmesiz, `her şey` ve `fark etmek` ayrı, `hat` ünlüyle başlayan ek alınca ikizleşir. Tarih, `hâlâ` ve `geç` kaldı; cümle yapısına dokunulmadı.

**Önce**

> Üç sensörler iki hafta boyunca ölçüm aldı. Veriler toplandı ve analiz ettik. Ekip yeni kalibrasyon protokolünü inceledi ve itiraz etti; sonuçlar sapmanın sensör yaşıyla ilişkili olduğunu göstermektedirler.

**Sonra**

> Üç sensör iki hafta boyunca ölçüm aldı. Veriler toplandı; verileri analiz ettik. Ekip yeni kalibrasyon protokolünü inceledi ve protokole itiraz etti; sonuçlar sapmanın sensör yaşıyla ilişkili olduğunu gösteriyor.

Sayı sıfatından sonraki çokluk eki ve insan dışı öznedeki yüklem çokluğu kalktı. Çatı uyuşmazlığı iki yargıya ayrılarak giderildi: toplayan kaynakta adlandırılmadığı için `biz`e bağlanmadı, analizi yapan `biz` silinmedi. `İtiraz etmek` yönelme hâli istediği için ortak nesne ikinci yüklemde yinelendi. `İlişkili` nedenselliğe dönmedi; itirazın gerekçesi eklenmedi.

**Önce**

> Kullanıcı ATM makinesinde PIN numarasını üç kez yanlış girdi; sistem SMS mesajıyla uyarı gönderdi ve kartı geri iade etmedi. En optimum eşik 0,35 olarak belirlendi.

**Sonra**

> Kullanıcı ATM'de PIN'i üç kez yanlış girdi; sistem SMS mesajıyla uyarı gönderdi ve kartı iade etmedi. Optimum eşik 0,35 olarak belirlendi.

Kısaltmanın açılımının başını yineleyen ad (`makine`, `numara`) ve alıntının anlamında bulunan `geri`, `en` silindi. `SMS mesajı` kaldı: açılımın başı `service`tir, mesaj o servisin iletisidir. Olumsuzluk (`etmedi`), sayı ve `üç kez` korundu.

**Dokunulmaz**

> Kurul Başkanı'na sunulan taslak Türk Standardları Enstitüsünün TS 13298 belgesine dayanıyor. Sunucu sürüm 3.5'te IP adresini `herSeyiSil()` çağrısından önce kaydediyor; kullanıcı “sistem herşeyi siliyor” diye yazdı.

Unvana gelen ek kesmeyle ayrılır; kurumun resmî adı (`Standardları`) kendi yazımıyla kalır; sürüm numarası ondalık sayı değildir; `IP adresi` tekrar değildir; kod ve doğrudan alıntı düzeltilmez.

## Aşırı düzeltme belirtileri

- Alıntıdaki, koddaki ya da resmî addaki yazımın "düzeltilmesi".
- Kaynağın tutarlı tercihinin (şapkasız yazım, ondalık nokta) bütün metne yayılmış değişiklikle ters çevrilmesi.
- `1.500` ya da `3.5` gibi ayırıcısı belirsiz sayının yeniden biçimlenmesi.
- Terim tamlamasına iyelik eklenmesi (`görüntü işlemesi`) ya da zincir içi düşmüş iyeliğin geri konması (`Türk Dili Kurumu`).
- Ek ortaklığının (`hız ve güvenilirliği`) açılıp metnin uzatılması.
- Ortak ögeyi onarırken aktör, nesne ya da gerekçe eklenmesi; ek-fiil onarımı için zamanın değiştirilmesi.
- `metot` → `yöntem`, `ihtimal` → `olasılık` gibi katman değişiminin yazım düzeltmesi sanılması.
- İnsan öznede yüklemdeki çokluk ekinin yanlış sayılıp silinmesi.
- Yazım düzeltmesi bahanesiyle cümle yapısının değiştirilmesi: hafif düzeyde yalnızca yazım değişir.

## Kaynaklar ve doğrulama düzeyi

Kural metinleri TDK'nin çevrim içi yazım sayfalarından alınmıştır (2026-11 erişimi). Oturumun ağ ayarı `tdk.gov.tr`'ye doğrudan erişime izin vermediği için sayfa metinleri arama motoru özetlerinden okunmuştur; kesin madde numarası ve güncel ifade için kılavuzun kendisine bakın.

- TDK, Yazım Kuralları: Bitişik Yazılan Birleşik Kelimeler; Ayrı Yazılan Birleşik Kelimeler; Kesme İşareti; Noktalama İşaretleri (Açıklamalar); Sayıların Yazılışı; Büyük Harflerin Kullanıldığı Yerler; Düzeltme İşareti; Büyük Ünlü Uyumu; Küçük Ünlü Uyumu; Ünsüz Türemesi; Bağlaç Olan ki'nin Yazılışı; Bağlaç Olan da, de'nin Yazılışı. https://tdk.gov.tr/kategori/icerik/yazim-kurallari/
- TDK Yazım Kılavuzu (çevrim içi). https://yazim.tdk.gov.tr/
- TDK, Sıkça Sorulan Sorular: "Kurum ve kuruluş adlarından sonra gelen ekler kesme işareti ile ayrılır mı?", "Düzeltme işareti (^) kaldırıldı mı?", "Yüzde işaretiyle sayı arasında boşluk bırakılır mı?", "Yabancı özel adlara ekler nasıl getirilir?". https://tdk.gov.tr/kategori/icerik/sikca-sorulan-sorular/
- TDK, Kamuoyuna Duyuru (2016; kurum adlarındaki kesme kuralının geçmişi). https://tdk.gov.tr/icerik/duyurular/kamuoyuna-duyuru-2/
- Türk Dili dergisi (2013), "Çokluk Kavramı ve -lar (-ler) Ekinin Kullanımı" (sayı ve çokluk sıfatından sonra çokluk eki, belgisiz zamir öznede yüklem). https://tdk.gov.tr/wp-content/uploads/2013/04/20130409.pdf
- Zülfikar H. (2013), "Anlatım Bozukluğuyla Ne Anlıyoruz?", *Türk Dili*. https://tdk.gov.tr/wp-content/uploads/2013/09/20130906.pdf

Doğrulama düzeyi:

| Kural | Düzey |
|---|---|
| Birleşik fiil, belgisiz sözcükler, `ki`, `de/da`, kesme işareti, sayı, yüzde, büyük harf, düzeltme işareti, ünlü uyumu istisnası, ünsüz ikizleşmesi örnekleri (`hak`, `his`, `ret`, `tıp`, `zam`, `zan`, `af`, `şer`) | TDK sayfası |
| `-ki`'nin yalnızca `bugünkü`, `dünkü`, `öbürkü`de uyuma girmesi | TDK › Küçük Ünlü Uyumu |
| `bir şey`, `her şey`, `pek çok`, `her biri` ayrı | TDK'nin ayrı yazım ilkesinden çıkarım; madde listesinde bu taramada görülmedi |
| `hat` → `hattı`, `üs` → `üssü`; `kontrol`, `protokol`, `sembol`, `rol`, `kabul`, `usul`, `hayal` için ince ek | aynı kuralın örneği; Türkçe Sözlük madde başıyla denetlenmeli |
| Sayı ve çokluk sıfatından sonra çokluk eki yok; insan dışı öznede teklik yüklem | Türk Dili makalesi (2013); Kılavuz kuralı değil, dil bilgisi önerisi |
| Ortak öge, çatı ve ek-fiil uyumu | Türkçe dil bilgisi ve anlatım bozukluğu öğretiminin yerleşik konusu (Zülfikar 2013); depo vakalarıyla sınanır |
| Kısaltma ve alıntıda anlam tekrarı | açılım ve sözlük anlamından çıkarım (`iade`: alınmış bir şeyi geri verme; `optimum`: en uygun); bağlamsal kural. Yaygın kullanım kılavuzları `SMS mesajı`nı da tekrar sayar; baş sözcük testi saymaz ve bu dosya testi izler |
| Söz varlığı katmanları | dil tarihine ilişkin genel bilgi; sayısal oran verilmedi, çünkü güncel ve tutarlı bir döküm bulunamadı |
