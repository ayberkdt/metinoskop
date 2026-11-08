# Türkçe dil bilgisi ve kullanım literatürü

Bu dosya Metinoskop kurallarının dayandığı ya da dayanabileceği Türkçe dil bilgisi, derlem, akademik yazı, çeviri ve dil modeli çalışmalarını tarar. Kayıtlar [`turkce-dil-literaturu.csv`](turkce-dil-literaturu.csv) veritabanındadır; her kaydın künyesi, tek cümlelik bulgusu, ilgili Metinoskop dosyası, doğrulama düzeyi ve bağlantısı vardır. Burada bulgular konuya göre sentezlenir ve her birinin kurallara etkisi yazılır.

Veritabanı kural kitabı değildir. Bir bulgu Metinoskop kuralına ancak ilgili referans dosyasına kaynağıyla yazıldıktan ve dönüşüm ve korunur vakasıyla sınandıktan sonra dönüşür; `SKILL.md` değişikliği ayrıca kör A/B ölçümü ister (`AGENTS.md`).

## İçindekiler

- [Yöntem ve sınırlar](#yöntem-ve-sınırlar)
- [Veritabanının kullanımı](#veritabanının-kullanımı)
- [Sözcük dizimi ve bilgi yapısı](#sözcük-dizimi-ve-bilgi-yapısı)
- [Özne düşürme ve gönderge](#özne-düşürme-ve-gönderge)
- [Kanıtsallık: -DI ve -mIş](#kanıtsallık--di-ve--miş)
- [Zarf-fiil, ilgi yan cümlesi ve bağlayıcılar](#zarf-fiil-ilgi-yan-cümlesi-ve-bağlayıcılar)
- [Tamlama, biçim bilgisi ve ses uyumu](#tamlama-biçim-bilgisi-ve-ses-uyumu)
- [Akademik Türkçe: kaçınma, vurgulayıcı, üstsöylem, edilgen](#akademik-türkçe-kaçınma-vurgulayıcı-üstsöylem-edilgen)
- [Derlem, sıklık ve eşdizim kaynakları](#derlem-sıklık-ve-eşdizim-kaynakları)
- [Okunabilirlik](#okunabilirlik)
- [Çeviri kokusu ve çeviri kaymaları](#çeviri-kokusu-ve-çeviri-kaymaları)
- [Dil modelleri ve yapay zekâ Türkçesi](#dil-modelleri-ve-yapay-zekâ-türkçesi)
- [Aday kurallar](#aday-kurallar)
- [Boşluklar ve doğrulanamayanlar](#boşluklar-ve-doğrulanamayanlar)

## Yöntem ve sınırlar

Tarama 2026-11-08'de üç kümede yapıldı: temel dil bilgisi kaynakları ve sözdizimi; derlem, sıklık ve akademik Türkçe; çeviri ve dil modeli çalışmaları. Kayıtların hepsi web aramasının döndürdüğü yayıncı, katalog, depo ve kaynakça kayıtlarıyla karşılaştırıldı. Bu oturumun ağ ayarı `dergipark.org.tr`, `aclanthology.org`, `arxiv.org`, `tdk.gov.tr` ve birkaç yayıncı sitesinin doğrudan okunmasına izin vermedi. Bu yüzden:

- **Tam metin okunmadı.** Bulgular özetlerden, yayıncı tanıtımlarından ve ikincil kaynakların aktarımından gelir; hangisi olduğu her kaydın `dogrulama` alanında yazılıdır.
- **`künye+içerik`** (51 kayıt): künye ve bulgu görülen bir kaynakla doğrulandı. **`künye`** (16 kayıt): yalnızca künye doğrulandı; bulgu alanı boş bırakıldı ("Künye doğrulandı; içerik özetlenmedi."). `scripts/literatur.py --check` bu ayrımı denetler.
- **Sayısal bulgular özetteki değerdir.** Tablo düzeyinde değer, model başına yüzde ve formül katsayısı alınmadı.
- İngilizce derlemle yapılmış çalışmalar (Türk yazarların İngilizce makaleleri) bulgu alanında belirtilir; Türkçe yazıma aktarımı çıkarımdır.

## Veritabanının kullanımı

```bash
python scripts/literatur.py                          # kayıt, tür, konu ve doğrulama sayıları
python scripts/literatur.py --konu ozne-dusurme      # konuya göre
python scripts/literatur.py --kural kanit-ve-kesinlik.md
python scripts/literatur.py --ara "odak"
python scripts/literatur.py --id enc-1986 --tam
python scripts/literatur.py --check                  # şema; validate-package.py de çalıştırır
```

Alanlar: `id`, `yazarlar`, `yil`, `baslik`, `yayin`, `tur`, `konular` (noktalı virgülle), `bulgu`, `metinoskop` (ilgili referans dosyaları ya da `—`), `dogrulama` (`künye+içerik: …` ya da `künye: …`), `url`. Yeni kayıt için: künyeyi görülen bir kaynakla doğrula, bulguyu yalnızca okuduğun yerden tek cümleyle yaz, okumadıysan bulgu yazma. Kayıt bu dosyanın ilgili bölümünde `id`siyle anılır; doğrulayıcı her `id`nin burada geçtiğini denetler.

## Sözcük dizimi ve bilgi yapısı

Kayıtlar: `erguvanli-1984`, `issever-2003`, `goksel-ozsoy-2000`, `kilicaslan-2004`, `kural-1992`, `kural-1997`, `underhill-1976`.

Erguvanlı (1984) Türkçede yüklemin sonda kaldığını, cümle başının konuyu, yüklemin hemen önünün yeni ve önemli bilgiyi, yüklem sonrasının arka plan bilgisini taşıdığını gösterir. İşsever (2003) bilgi yapısını sözcük dizimiyle ezginin birlikte işaretlediğini, arka plan ögelerinin dizimde serbestçe yer değiştirdiğini ekler. Göksel ve Özsoy (2000) yüklemin hemen önünün odağın tek yeri değil cümle vurgusunun yeri olduğunu, odağın yüklem öncesi alanın başka bir yerinde de durabildiğini savunur; Kılıçaslan (2004) da konumu söylem işlevine bire bir eşleyen açıklamanın eksik kaldığını söyler.

**Metinoskop'a etkisi.** `turkce-ritim-ve-ceviri-kokusu.md` › Bilgi yapısı ve sözcük sırası yüklem önünü "odak konumu" diye veriyordu; bu tarama sonrasında eğilim olarak yazıldı: yeni bilgi çoğunlukla yüklem önüne yakın durur, ama yüklem öncesi alanda başka yerde duran odak yanlış değildir. Düzenleme sırayı yalnızca "yüklem önü odak olmalı" diye değiştirmez. Yazılı metinde ezgi yoktur; okur odağı yalnızca sözcük dizimi ve bağlamdan kurar, bu yüzden yazıda dizimin yükü konuşmadakinden fazladır (çıkarım).

## Özne düşürme ve gönderge

Kayıtlar: `enc-1986`, `erguvanli-taylan-1986`, `turan-1996`, `cinar-2026`, `altinok-2025-trglue`.

Enç (1986) Türkçede özne adılının düşmesini olağan durum, açık özne adılını konu değişimi, karşıtlık ya da vurgu işareti sayar. Turan (1996) yayımlanmış anlatılarda açık adılın öncülüyle aynı göndergeyi paylaştığını, gönderimsel olmayan öncüle yalnızca boş adılın bağlanabildiğini bulur. Altınok (2025), İngilizceden çevrilen veride çıplak adılın (`o`, `onu`) Türkçede belirsiz kaldığını, doğal Türkçenin ad öbeğini yinelediğini ya da hâl ekine başvurduğunu bildirir. Çınar ve Karayel Çınar (2026) ChatGPT'nin konu sürekliliği ve karşıtlık koşullarında boş ve açık özne dağılımına duyarlı olduğunu özetler; istatistik görülmedi.

**Metinoskop'a etkisi.** `turkce-ritim-ve-ceviri-kokusu.md` › Özne düşürme ve açık özne fazlası ile `SKILL.md` › Çeviri kokusunu ilişkide ara ("ardışık cümlelerde yinelenen açık özne") Enç ve Turan'la uyumludur. Altınok'un bulgusu `gerekli-ad-tekrari-korunur` ve `belirsizligi-onleyen-ozne-korunur` vakalarının dayanağını güçlendirir: belirsizlik doğacaksa adılı değil adı yinele. Çınar ve Karayel Çınar'ın sonucu, özne fazlasının bütün modellerde aynı güçte olmayabileceğini düşündürür; kural sayımla değil bağlamla karar verir.

## Kanıtsallık: -DI ve -mIş

Kayıtlar: `slobin-aksu-1982`, `aksu-koc-slobin-1986`, `johanson-2000`, `karakas-simsek-2026`.

Slobin ve Aksu (1982) ile Aksu-Koç ve Slobin (1986) `-DI`'nın doğrudan yaşanmış geçmişi, `-mIş`'ın çıkarım ya da duyumla edinilen bilgiyi işaretlediğini; `-mIş`'ın konuşur için yeni ya da beklenmedik bilgiyi de sunduğunu gösterir. Karakaş ve Şimşek (2026) anadil konuşucularının güvenilir kaynak bağlamında `-DI`'yı, güvenilmez kaynak bağlamında `-mIş`'ı görece daha çok seçtiğini, on dil modelinde bu duyarlılığın tutarlı olmadığını bildirir.

**Metinoskop'a etkisi.** `-DI` ile `-mIş` arasındaki seçim kanıt statüsüdür: `Toplantı ertelenmiş` (duyum) → `Toplantı ertelendi` (doğrudan bilgi) aktarımı olguya çevirir; ters yön gözlemi duyuma indirir. Bu, `SKILL.md` › Bilginin kaynağı ve statüsü ile `kanit-ve-kesinlik.md`'deki "aktarım olguya çevrilmez" ilkesinin biçim bilgisi düzeyidir. Raporlardaki `-mıştır` resmî bitmişlik kipidir, duyum bildirmez (`zamansal-ankraj-ve-rapor-kipi.md` › `-mıştır` biçimi); kanıtsallık kuralı yalnızca kaynak bilginin geliş yolunu söylüyorsa uygulanır. Bkz. [Aday kurallar](#aday-kurallar).

## Zarf-fiil, ilgi yan cümlesi ve bağlayıcılar

Kayıtlar: `johanson-1995`, `kornfilt-1997-ilgi`, `kornfilt-2000`, `zeyrek-webber-2008`, `zeyrek-2009-tdb-yan-cumle`, `zeyrek-2013-tdb`, `zeyrek-kurfali-2018`, `kamaci-gencer-2023`, `sen-bartan-2022`.

Johanson (1995) Türk dillerinde zarf-fiil yapısını özne ortaklığına ve sıkılığa göre dört düzeyde ayırır; ortak özneli yapı ile iki ayrı özneli yapı aynı şey değildir. Kornfilt (1997, 2000) ilgi yan cümlesinin iki ekle kurulduğunu gösterir: özne ilgilendiğinde `-(y)An`, özne dışı öge ilgilendiğinde `-DIK` + iyelik (`benim okuduğum kitap`). Türkçe Söylem Bankası çalışmaları (Zeyrek ve Webber 2008; Zeyrek ve ark. 2009, 2013; Zeyrek ve Kurfalı 2018) Türkçede söylem ilişkisinin yalnızca sözcüksel bağlaçla değil zarf-fiil ve ilgeç tabanlı bağlayıcılarla da kurulduğunu, işaretleme biçeminin bu yüzden genişletildiğini, yan cümle bağlayıcılarının cümleler arası bağlaçların seçmediği bazı anlamları yeğlediğini gösterir; `karşın`, `rağmen`, `halde` karşıtlık–ödün ilişkisinin yan cümle bağlayıcılarıdır. Kamacı Gencer (2023) `için`in derlemde neden–sonuç ve amaç–sonuç ilişkisini birlikte taşıdığını bulur. Şen Bartan (2022) İngilizce konuşmalardaki yapısal tekrarların Türkçe çeviride büyük ölçüde örtük aktarıldığını, cümle başı tekrarların çoğunlukla düşürüldüğünü bildirir.

**Metinoskop'a etkisi.** `SKILL.md` › Türkçenin bağlayıcı kaynaklarını kullan ve `turkce-baglayicilar.md`'nin "ek, ilgeç, bağlaç, bağlaçsız" ayrımı Türkçe Söylem Bankası'nın derlem bulgusuyla örtüşür: ilişkiyi ekle kurmak çeviri kokusunu gidermenin yerli yoludur, süs değildir. Johanson'un düzeyleri `-erek` kuralına dayanak verir: `-erek` aynı özneyi varsayar (`turkce-baglayicilar.md` › Araç ve yol); özne değişiyorsa kullanılmaz. Kamacı Gencer'in bulgusu `için`in amaç mı neden mi bildirdiğinin bağlamdan çözülmesi gerektiğini gösterir; `için` → `nedeniyle` dönüşümü ilişkiyi tek okumaya sabitler ve ancak kaynak nedeni kuruyorsa yapılır (`evals/README.md`'deki `için` → `nedeniyle` yanlış alarmı bu yüzden ayrıca okunur). Şen Bartan'ın bulgusu yapısal paralelliği Türkçede örtükleştirmenin çevirmen davranışı olduğunu düşündürür; `SKILL.md` › Paragraf simetrisi ile uyumludur.

## Tamlama, biçim bilgisi ve ses uyumu

Kayıtlar: `van-schaaik-2002`, `kunduraci-2013`, `goksel-haznedar-2007`, `clements-sezer-1982`, `korkmaz-2003`, `banguoglu-turkcenin-grameri`, `goksel-kerslake-2005`, `kornfilt-1997`, `lewis-2000`, `csato-johanson-1998`, `kara-2023-gecturk`.

Van Schaaik (2002) Türkçede ad birleşiminin çok üretken olduğunu inceler; Kunduracı (2013) `-(s)I` ekli ad + ad birleşimlerinin (belirtisiz tamlama) sözdiziminden ayrı biçim bilgisi bileşeninde üretildiğini savunur. Clements ve Sezer (1982) ünlü uyumu istisnalarının altta yatan gösterimden kestirilebildiğini, ince `/l/`'li alıntıların ön ünlülü ek almasının bunun örneği olduğunu gösterir. GECTurk (Kara ve ark. 2023) uzmanlarca seçilmiş 20'yi aşkın Türkçe yazım ve dil bilgisi kuralıyla sentetik hata verisi üretir.

**Metinoskop'a etkisi.** `yazim-ve-dil-bilgisi.md` › Sözcüğün kökeni bölümündeki `alkolü`, `kontrolü`, `protokolde` örüntüsü Clements ve Sezer'in açıklamasıyla uyumludur. Belirtisiz tamlamanın biçim bilgisi düzeyinde üretilmesi (Kunduracı), adlaşmış öbeklerde içteki iyeliğin düşmesini (`veri analiz yöntemleri`) "eksik tamlama" saymamanın dayanağını güçlendirir; bu dosyadaki kayıtlar `yazim-ve-dil-bilgisi.md`'nin doğrulama tablosundaki "dil bilgisi önerisi" satırlarının yerine geçmez, yanına eklenir. Dil bilgisi kitaplarının (Göksel ve Kerslake, Kornfilt, Lewis, Korkmaz, Banguoğlu) yalnızca künyesi doğrulandı; kurallar bu kitaplara sayfa numarasıyla bağlanmadan atıf yapılmaz.

## Akademik Türkçe: kaçınma, vurgulayıcı, üstsöylem, edilgen

Kayıtlar: `fidan-2002`, `dag-tarcan-2020`, `sen-iseri-2023`, `oflaz-koleci-uzun-2021`, `erk-emeksiz-2015`, `cakir-2011`, `akbas-hardman-2018`, `kafes-2017`, `bal-gezegin-2019`.

Fidan (2002) psikoloji, dilbilim ve tıp alanlarındaki Türkçe araştırma yazılarında kaçınmanın, alanlar arasında oranı benzer kalan tek üstsöylem ulamı olduğunu bulur. Şen ve İşeri (2023) Türkçe makale özetlerinde en sık etkileşimli belirleyicinin vurgulayıcı olduğunu, sosyal bilim özetlerinin fen özetlerinden daha çok üstsöylem belirleyicisi kullandığını bildirir. Erk Emeksiz (2015) Türkçe bilimsel söylemde edilgeni en çok bilginin kaynağının belirlediğini gösterir: kaynak yazarsa edilgen araştırma aşamasını, okura yönlendirmeyi, iddia ve öneriyi; kaynak başkalarıysa alanyazın aktarımını ve genel kabul görmüş bilgiyi taşır. Çakır (2011) Türkçe özetlerde nesnel duruşun çoğunlukla etkeni belirtilmemiş edilgen ve cansız özneyle kurulduğunu, özgün İngilizce özetlerin daha çok kişi zamiri ve etken çatı kullandığını, fen özetlerinin edilgeni daha çok yeğlediğini bulur. Akbaş ve Hardman (2018) ile Kafes (2017) Türk yazarların İngilizce metinlerini inceler; Türkçe yazıma aktarımı çıkarımdır.

**Metinoskop'a etkisi.** `SKILL.md` kural 6 ("bilimsel betimlemede edilgen çatı ... meşrudur; edilgenliği yalnızca aktör belli diye etkene çevirme") Erk Emeksiz ve Çakır'la doğrudan uyumludur: Türkçe bilimsel metinde edilgen İngilizceden gelen bir iz değil, yerleşik duruş biçimidir. `SKILL.md` › Çekince kanıttır ile Fidan'ın bulgusu uyumludur: kaçınma Türkçe bilimsel yazının alanlar arası sabit ögesidir, AI izi sayılıp silinmez. Şen ve İşeri'nin bulgusu bir uyarıdır: Türkçe özetlerde vurgulayıcı sıktır, yani vurgulayıcının varlığı tek başına yapaylık işareti değildir. `SKILL.md` vurgulayıcıyı yasaklamaz, "hangi kanıt bunu hak ediyor" diye sorar; bu soru doğru kalır, ama özet türünde vurgulayıcıyı otomatik silmek insan normunu bozar.

## Derlem, sıklık ve eşdizim kaynakları

Kayıtlar: `aksan-2012-tnc`, `aksan-2017-siklik-sozlugu`, `goz-2003`, `say-2002-odtu-derlemi`, `oflazer-2003-agac-bankasi`, `turk-2022-boun`, `aksan-aksan-2015`, `aksan-2016-iliskisel-kaliplar`.

Türkçe Ulusal Derlem (TNC; Aksan ve ark. 2012) British National Corpus tasarımını izleyen 50 milyon sözcüklük dengeli derlemdir; Türkçe sıklık sözlüğü (Aksan ve ark. 2017) bu derlemden 5000 madde çıkarır. Göz (2003) 1995–2000 yazılı Türkçesinden yaklaşık 1 milyon sözcükle 22.693 başsözcüğün sıklığını verir. ODTÜ Türkçe Derlemi (Say ve ark. 2002) yaklaşık 2 milyon sözcüktür; ODTÜ-Sabancı (Oflazer ve ark. 2003) ve BOUN (Türk ve ark. 2022) ağaç bankaları sözdizimsel işaretli kaynaklardır. Aksan ve Aksan (2015) ile Aksan, Mersinli ve Altunay (2016) TNC'den çok sözcüklü birimleri türlere ve ilişkisel kalıplara göre sınıflar.

**Metinoskop'a etkisi.** `sozcuk-birlesimleri.md` › Eşdizim denetimi ve `AGENTS.md`'deki "derlem sıklığı tek başına norm değildir, genel ve alan derlemi ayrı değerlendirilir" ilkesi için başvurulacak kaynaklar bunlardır. TNC genel derlemdir; teknik alan terminolojisi için tek başına yeterli değildir. Aksan ve Aksan'ın tür karşılaştırması, aynı birimin kurmaca ve kurmaca dışı metinde farklı sıklıkta olduğunu gösterir; eşdizim kararı türe bakar (`sozcuk-birlesimleri.md` › Türe göre eşdizim).

## Okunabilirlik

Kayıtlar: `atesman-1997`, `bezirci-yilmaz-2010`.

Ateşman (1997) Flesch formülünü Türkçeye uyarlar (yalnızca künye doğrulandı); Bezirci ve Yılmaz (2010) Türkçe için hece sayısına dayanan yeni bir ölçüt önerir.

**Metinoskop'a etkisi.** Formüller cümle ve sözcük uzunluğunu ölçer, anlamı ve bağlamı ölçmez. `netlik-omurgasi.md` sayısal eşikleri kesme kuralı saymaz; okunabilirlik puanı da kural değil, en fazla inceleme işaretidir. Türkçede sözcük uzunluğu eklemeli yapıdan ötürü yüksektir; puanı düşürmek için ekli biçimi açmak (`-dığından` → `-dığı için`) ya da cümleyi bölmek tek ilişkili uzun cümle kuralını bozar.

## Çeviri kokusu ve çeviri kaymaları

Kayıtlar: `sen-bartan-2022`, `baser-2025`, `cakir-2011`, `umutlu-2025`, `yuksel-2024-turkishmmlu`, `altinok-2025-trglue`.

Umutlu ve ark. (2025) İngilizceden çevrilmiş ya da uyarlanmış 17 Türkçe veri kümesinin yaklaşık %70'inin kalite standardını karşılamadığını, en sorunlu ölçütün teknik terim doğruluğu olduğunu bulur. Yüksel ve ark. (2024) çevrilmiş kıyaslama setlerini güvenilmez bulduğu için özgün Türkçe soru kullanır. Altınok (2025) çeviride İngilizce belirsizliği korumanın doğal olmayan Türkçe ürettiğini söyler.

**Metinoskop'a etkisi.** Bu çalışmalar Türkçe çeviri metnin sorunlu olduğunu doğrular ama hangi yapının çeviri kokusu taşıdığını derlemle ölçmez. `turkce-ritim-ve-ceviri-kokusu.md`'deki ailelerin (`sahip olmak`, `olan` zinciri, `bir` fazlası, açık özne) Türkçe çeviri derlemiyle ölçülmüş dayanağı bu taramada bulunamadı; bu kurallar dil bilgisi bilgisine ve depo vakalarına dayanan çıkarımlardır. Umutlu ve ark.'nın "teknik terim doğruluğu en sorunlu ölçüt" bulgusu `SKILL.md` › Aşırı Türkçeleştirme'deki terim koruma kuralını destekler.

## Dil modelleri ve yapay zekâ Türkçesi

Kayıtlar: `basar-2025-turblimp`, `ismayilzada-2025`, `er-2025-cetvel`, `safaya-2022-mukayese`, `karakas-simsek-2026`, `cinar-2026`, `cosar-2025`, `simsek-ozdemir-2026`, `kocagul-2026`, `kayabas-2025`, `ozdemir-2026`.

TurBLiMP (Başar ve ark. 2025) en iyi modellerin bile sözcük sırası değiştiğinde ve biçimbilimsel yan cümlede doğruluk kaybettiğini; Ismayilzada ve ark. (2025) ek sayısı arttıkça biçimbilimsel bileşim başarısının keskin biçimde düştüğünü gösterir. Cetvel (Er ve ark. 2025) Türkçe modelleri en iyi ayıran görevler arasında dil bilgisi hatası düzeltmeyi sayar. Kocagül (2026) özete göre yapay zekânın yazdığı Türkçe metinleri yüksek noktalı virgül ve virgül yoğunluğu, cümle başı söylem belirleyicileri, yinelenen `-ArAk` zincirleri ve kalıplaşmış kapanış sözcükleriyle ayırır; başkasının düzenlediği melez metinlerde 61 özelliğin 41'i yapay zekâ profilinde kalır. Coşar (2025) GPT-4'ün incelenen örneklerde yazım ve noktalama kusurunu seyrek yaptığını bildirir. Şimşek ve Özdemir (2026) ChatGPT metnini anadil yazarıyla değil Türkçe öğrenicisiyle karşılaştırır.

**Metinoskop'a etkisi.** `insan-ve-yapay-metin.md` 2026-10'da AI ve insan Türkçesini üslup bakımından karşılaştıran hakemli çalışma bulamamıştı; bu tarama 2025–2026'dan dergi makaleleri buldu ve dosyanın girişi buna göre güncellendi. Kocagül'ün özeti dört izi sayar ve bunların üçü Metinoskop'ta zaten vardır: cümle başı söylem belirleyicisi (`SKILL.md` › Çeviri kokusunu ilişkide ara), `-ArAk` zinciri (`SKILL.md` › Cümle sonu kuyruğu, `turkce-ritim-ve-ceviri-kokusu.md` › Türkçenin fiilimsi kaynakları), kalıp kapanış (`SKILL.md` › Kalıp giriş ve kalıp sonuç). Noktalı virgül ve virgül yoğunluğu Metinoskop'ta denetlenmiyor; Metinoskop'un kendi gold'ları noktalı virgülü bağlaçsız ilişki için sık kullanır, bu yüzden tam metin okunmadan kural yapılmaz ([Aday kurallar](#aday-kurallar)). TurBLiMP ve Ismayilzada ve ark., düzenleme sırasında sözcük sırası ve ek dizisi değişen her yerin yeniden okunmasını gerektirir: modelin en çok yanıldığı yer düzeltmenin kendisidir (`SKILL.md` › Yerine yazdığın ifade yeni bir iddiadır). Tespit çalışmaları (Kayabaş ve ark. 2025; Özdemir 2026) sınıflandırıcı başarısı raporlar, dil özelliği raporlamaz; Metinoskop dedektör atlatmayı hedeflemez.

## Aday kurallar

Literatürden çıkan ama henüz Metinoskop kuralı olmayan öneriler. Her biri girmeden önce referans dosyasına kaynağıyla yazılır, dönüşüm ve korunur vakasıyla sınanır; `SKILL.md`'ye girecekse kör A/B ile ölçülür.

| Aday | Dayanak | Gereken vaka | Risk |
|---|---|---|---|
| Duyum `-mIş`'ı `-DI`'ya, doğrudan `-DI`'yı `-mIş`'a çevirme; kanıtsallık kanıt statüsüdür | `aksu-koc-slobin-1986`, `slobin-aksu-1982`, `karakas-simsek-2026` | dönüşüm: duyuma dayalı haber notu; korunur: rapordaki resmî `-mıştır` | `-mıştır`'ı duyum sanıp `-dı`'ya çevirmek |
| Odak eğilimi: düzenleme sırayı yalnızca "yüklem önü odak olmalı" diye değiştirmez | `goksel-ozsoy-2000`, `kilicaslan-2004` | korunur: odağı yüklem öncesi alanın başında olan doğru cümle | yeni bilgiyi yüklemden uzaklaştıran çeviri sırasını korumak |
| Türkçe özette vurgulayıcıyı türün normu say, yalnızca dayanaksızsa sil | `sen-iseri-2023` | korunur: ölçümle desteklenen vurgulayıcılı özet | dayanaksız `açıkça`yı bırakmak |
| Noktalı virgül ve virgül yoğunluğunu AI izi olarak incele | `kocagul-2026` (yalnızca özet) | tam metin okunmadan vaka yazılmaz | Metinoskop gold'larının bağlaçsız ilişki için kullandığı noktalı virgülü silmek |

## Boşluklar ve doğrulanamayanlar

**Bulunamayan çalışma türleri.**

- Türkçe çeviri metni özgün Türkçeyle derlemde karşılaştıran (açıklaştırma, sadeleştirme, girişim) hakemli bir çalışma. Yalnızca künyesi görülen ilgili kayıtlar: Yazıcı, "Simplification as a Translation Universal" (13. Dil, Yazın ve Halkbilim Sempozyumu, 2013, 1131–1138); bir İstanbul Üniversitesi çeviribilim tezinde önerilen derlem modeli (yazar ve yıl doğrulanmadı).
- `sahip olmak` kalkısı üzerine akademik çalışma.
- İngilizce→Türkçe makine çevirisinde MQM türü sistemli hata sayımı.

**Künyesi eksik kaldığı için veritabanına alınmayanlar.**

- Zeyrek (2014), `ama` ve `fakat` üzerine bölüm, John Benjamins, Studies in Language Companion Series 164: bölüm adı ve editörler doğrulanamadı. Katalog özetine göre `ama` ödünü ve edimbilimsel yorumları `fakat`'tan daha kolay işaretler; `fakat` daha resmî türlerde yeğlenir.
- Yıldız, İpek, Türkçe bilimsel metinlerde çok sözcüklü birimler üzerine doktora tezi (YÖK Açık Bilim 20.500.12812/220663): yıl ve üniversite doğrulanamadı.
- Bozkurt Güvenek, "Türkçede Makine Çevirisinin Söz Dizimsel ve Anlamsal Hataları: Google Translate ve DeepL Örnekleri", HUMANITAS 14(27), 35–57: yayın yılı doğrulanamadı. Özete göre iki sistemin Türkçe çıktısı kiplik, zaman, vurgu (tema–rema) ve mecazda yetersiz kalır.
- Er ve Çoğalmış (2024), yapay zekâ ve insan Türkçe metni tespiti (IEEE ICMI): yalnızca künye görüldü.
- Akdağ ve ark. (2026), "Retranslation at the intersection of style, machines, and plagiarism" (StyGenAI, EAMT): bulgu doğrulanamadı.
- Alimen (2023), ChatGPT çevirisi üzerine deneysel çalışma (RumeliDE 36): sonuçlar görülemedi.
- Uzun ve Huber (ed.), *Türkçede Bilgi Yapısı ve Bilimsel Metinler*: yıl ve içerik doğrulanamadı.

**Kayıtlardaki belirsizlikler.** Banguoğlu'nun ilk baskı yılı (1974 ya da 1986), Csató ve Johanson (1998) bölümünün sayfa aralığı, Oflazer ve ark. (2003) bölümünün yer aldığı kitabın adı, Ateşman (1997) makalesinin sayfa aralığı ve Kocagül (2026) yazarının tam adı kaynaklarda çelişiyor ya da bulunamadı; ayrıntı ilgili kaydın `yayin` ve `dogrulama` alanlarındadır.
