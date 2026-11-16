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
- [Belirtme hâli, belirlilik ve `bir`](#belirtme-hâli-belirlilik-ve-bir)
- [Adlaştırma, `-DIr` ve `-mAktA`](#adlaştırma--dir-ve--makta)
- [Hafif fiil](#hafif-fiil)
- [Edilgen, `tarafından` ve yazar varlığı](#edilgen-tarafından-ve-yazar-varlığı)
- [Sayı uyumu](#sayı-uyumu)
- [Metin, kayıt ve gönderge](#metin-kayıt-ve-gönderge)
- [Yabancı etki, kalkı ve `ki`](#yabancı-etki-kalkı-ve-ki)
- [Ses bilgisi, ünsüz değişimi ve biçim çözümleyicileri](#ses-bilgisi-ünsüz-değişimi-ve-biçim-çözümleyicileri)
- [Odak, konu, eksilti ve söylem belirleyicileri](#odak-konu-eksilti-ve-söylem-belirleyicileri)
- [Kiplik, noktalama ve kibarlık](#kiplik-noktalama-ve-kibarlık)
- [Değerlendirme için hesaplamalı kaynaklar](#değerlendirme-için-hesaplamalı-kaynaklar)
- [Örüntü kararları](#örüntü-kararları)
- [Dil modelleri ve yapay zekâ Türkçesi](#dil-modelleri-ve-yapay-zekâ-türkçesi)
- [Aday kurallar](#aday-kurallar)
- [Boşluklar ve doğrulanamayanlar](#boşluklar-ve-doğrulanamayanlar)

## Yöntem ve sınırlar

İlk tarama 2026-11-08'de üç kümede yapıldı: temel dil bilgisi kaynakları ve sözdizimi; derlem, sıklık ve akademik Türkçe; çeviri ve dil modeli çalışmaları. İkinci tarama 2026-11-16'da örüntülere yönelik üç kümede yapıldı: biçim-sözdizimi (belirtme hâli, `bir`, adlaştırma, `-DIr`, `-mAktA`, hafif fiil, edilgen, sayı uyumu); metin, kayıt ve gönderge; yabancı etkili yapılar ve kalkı. İkinci turda her kayıt için bulgunun yanında örüntüye etkisi de soruldu; bu etki aşağıda ilgili bölümde ve [Örüntü kararları](#örüntü-kararları) tablosunda durur. İkinci turda web arama kotası doldu; bazı izler sürdürülemedi. Üçüncü tur 2026-11-16'da ses ve biçim bilgisi (ünsüz değişimi, ünlü uyumu istisnaları, vurgu, ek sırası, biçim çözümleyicileri), sözdizimi ve edimbilim (`de/da`, `ise`, eksilti, ilgi yan cümlesi işlemleme, söylem belirleyicileri, noktalama, kiplik, kibarlık) ve değerlendirmede kullanılabilecek hesaplamalı kaynaklar üzerine yapıldı. Kayıtların hepsi web aramasının döndürdüğü yayıncı, katalog, depo ve kaynakça kayıtlarıyla karşılaştırıldı. Bu oturumun ağ ayarı `dergipark.org.tr`, `aclanthology.org`, `arxiv.org`, `tdk.gov.tr` ve birkaç yayıncı sitesinin doğrudan okunmasına izin vermedi. Bu yüzden:

- **Tam metin okunmadı.** Bulgular özetlerden, yayıncı tanıtımlarından ve ikincil kaynakların aktarımından gelir; hangisi olduğu her kaydın `dogrulama` alanında yazılıdır.
- **`künye+içerik`** (165 kayıt): künye ve bulgu görülen bir kaynakla doğrulandı. **`künye`** (36 kayıt): yalnızca künye doğrulandı; bulgu alanı boş bırakıldı ("Künye doğrulandı; içerik özetlenmedi."). `scripts/literatur.py --check` bu ayrımı denetler.
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

## Belirtme hâli, belirlilik ve `bir`

Kayıtlar: `enc-1991`, `von-heusinger-kornfilt-2005`, `von-heusinger-kornfilt-2017`, `nakipoglu-2009`, `erguvanli-taylan-zimmer-1994`, `ozturk-2005`, `kornfilt-2007-inceleme`, `ketrez-2023`, `tat-2011`.

Belirtme hâli `-(y)I` Türkçede biçim değil anlam taşır: belirsiz nesneyi söylemde önceden kurulmuş bir kümeye bağlar (Enç 1991), belirliliği değil özgüllüğü kodlar (von Heusinger ve Kornfilt 2005, 2017); vurgu ve konum bilgi yapısını değiştirir (Nakipoğlu 2009). `Bir` tanımlık mı yoksa gönderimsellik işaretleyicisi mi, tartışmalıdır (Öztürk 2005; Kornfilt 2007); iki görüş de onu Türkçenin kendi dil bilgisine yerleştirir. Ketrez (2023) `bir`li nesnenin olumsuzluk üzerinde geniş kapsam alabildiğini, yalın nesnenin alamadığını deneyle gösterir; Tat (2011) sıfat + `bir` + ad sırasını açıklar; Öztürk (2005) yalın nesne + eylem birleşimlerini (`veri topladık`) sözde birleştirme olarak çözümler.

**Örüntü kararı.** `Bir` tek tek işaretlenmez; yoğunluk işaretlenir ve olumsuzluk, sıfat + `bir` + ad ve yalın nesne karşı örnektir (`turkce-ritim-ve-ceviri-kokusu.md` › `Bir` fazlası). Belirtme ekini eklemek ya da silmek önerme değişikliğidir, doğallaştırma değildir. Çeviri, öğrenici ya da makine Türkçesinde `bir` fazlasını ölçen derlem çalışması bulunamadı; yoğunluk eşiği çıkarımdır. Korunur vakası: `yerli-bir-edilgen-cogul-korunur`.

## Adlaştırma, `-DIr` ve `-mAktA`

Kayıtlar: `kaya-apaydin-2019`, `rentzsch-2024`, `caliskan-2019`, `turkkan-2009`, `sansa-tura-1986`, `kerimoglu-aksu-2015`, `erguvanli-taylan-2018`, `ozdemir-2023-dir`, `akaslan-2011`, `erguvanli-taylan-2001`, `kanik-2015`.

Öğretici fen metninde bile adlaştırma olağandır; `-mA` ve `-DIK` baskın, `-(y)Iş` seyrektir (Kaya ve Apaydın 2019). `-(y)Iş` `-mA`'nın serbest eş anlamlısı değildir, tarz anlamı ve sözlükselleşmiş biçimleri vardır (Rentzsch 2024); `-mA` ile `-DIK` ana eyleme göre seçilir (Çalışkan 2019); adlaştırma metnin sözbilimsel kipinin göstergesidir (Türkkan 2009). `-DIr` kişi eki değil önermeyi kuşatan bir kiplik belirleyicisidir (Kerimoğlu ve Aksu 2015; Erguvanlı Taylan 2018); tanımda yargıyı sabitler (Özdemir 2023), olay yükleminde varsayım okuması da verebilir (Sansa-Tura 1986). `-mAktA` ile `-(I)yor` karşıtlığı salt kayıt farkı değildir (Akaslan 2011); kip seçimi zarfla birlikte okunur (Erguvanlı Taylan 2001); sözlü dilde alışkanlık okuması `-(I)yor`'a kaymıştır (Kanık 2015).

**Örüntü kararı.** Adlaştırmayı toptan fiile çeviren kural kurulmaz; fiilimsi yığını ve iyelik zinciri işaretlenir. `-mA` ↔ `-(y)Iş` ve `-mA` ↔ `-DIK` otomatik değiştirilmez. `-mAktAdIr` yalnızca zincir ve yoğunlukta incelenir; tanım cümlesindeki `-DIr` silinmez (`zamansal-ankraj-ve-rapor-kipi.md` › Genel bilimsel önermeler). `-DIr`'ı eklenen işaret sayan bir değerlendirici kuralı eklenmedi: `-mAktAdIr` sadeleştirmesi `-DIr`'ı meşru biçimde siler ve aile ayrımı sayımla yapılamaz.

## Hafif fiil

Kayıtlar: `aksehirli-2013`, `ucar-2010`, `zulfikar-2023`, `un-2019`.

`Et-` Türkçenin en temel hafif eylemidir ve en sık işlevi adı eyleme çevirmektir (Akşehirli 2013); ad + `etmek`/`olmak` birleşimi yüzyıllardır yerleşiktir (Zülfikar 2023). Sözlükler bile hafif ve tam eylem kullanımını tutarlı ayırmaz (Uçar 2010).

**Örüntü kararı.** `analiz etmek`, `kabul etmek` işaretlenmez. `style-lint.py` hafif fiil denetimi lemma listesine değil birleşime bakar (`değerlendirme gerçekleştirmek`, `karar gerçekleştirmek`); bu karar Uçar'ın bulgusuyla uyumludur.

## Edilgen, `tarafından` ve yazar varlığı

Kayıtlar: `erdem-2007`, `sebzecioglu-oktar-2010`, `nakipoglu-demiralp-2001`, `guclu-2025`, `yilmaz-2022`, `konukman-2011`, `senoz-ayata-2008`, `cangir-can-2026`.

`Tarafından` ve `canibinden` eyleyen öbekleri Osmanlı Türkçesine 18. ve 19. yüzyılda girer (Erdem 2007); temel edilgen eyleyeni örtmekten çok olayı öne çıkarır ve `tarafından`lı edilgen modern Türkçede kurallı yapı sayılacak sıklıkta değildir (Sebzecioğlu ve Oktar 2010). Türkçe araştırma makalelerinde birinci çoğul kişi adılı seyrektir; açık yazar göndermesini biz ekleri, örtük göndermeyi eyleyensiz edilgen ve cansız özne taşır (Güçlü 2025); kendinden söz eki adlarda da görülür (`çalışmamızda`; Yılmaz 2022). Bir bildiri özetine göre L1 Türkçe akademik yazı etkileşimli üstsöylemi İngilizceden daha seyrek, pekiştirici zarfı daha sık kullanır (Cangir ve Can 2026; hakemli tam yayın değil).

**Örüntü kararı.** `style-lint.py`'ye bağlamsal `tarafindan` ailesi eklendi: eyleyen biliniyorsa etken çatı adaydır; kurumsal ve hukuki eyleyen vurgusu ile süreç eyleyeni (`başka bir süreç tarafından kullanılması`) meşrudur, bu yüzden aile sert değildir. Eyleyensiz edilgen işaretlenmez; düzeltme eyleyeni `tarafından` ile eklemez (`kanit-ve-kesinlik.md`). Biz ekleri sızıntı ya da öznel dil sayılmaz.

## Sayı uyumu

Kayıtlar: `bamyaci-2014`, `uygun-felser-2023`, `sag-2022`, `renans-2017`, `kerimoglu-2008`.

Cansız çoğul öznede çoğul yüklemin kabul edilebilirliği keskin biçimde düşer, insan öznede düşmez; tekil yüklem varsayılan biçimdir (Bamyacı, Häussler ve Kabak 2014). Uyum öznenin konumuna da bağlıdır (Uygun ve Felser 2023). Yalın tekil ad atomiktir ve sayıdan sonra çokluk eki gelmez (Sağ 2022); soru ve olumsuzlukta çoğul ad sayıdan bağımsızdır (Renans ve ark. 2017). Zamir yüklemli cümlelerde kişi uyumu farklı işler (Kerimoğlu 2008).

**Örüntü kararı.** `style-lint.py`'ye bağlamsal `sayi_uyumu` ailesi eklendi: cansız çoğul özne (`sonuçlar`, `veriler`, `sensörler` …) + çoğul yüklem ve sayı sıfatı (`iki`, `üç`, `birkaç`, `birçok` …) + çoğul ad. İnsan özne, `altı`/`yüz`/`on` (`yüz ifadeleri`, `on yıllardır`) ve rakam (`Tablo 3 sonuçları`) yanlış pozitif riski yüzünden dışarıda tutuldu; öz sınama bu karşı örnekleri tutar. Soru ve olumsuzluktaki çoğul ad tekile çevrilmez (`yazim-ve-dil-bilgisi.md` › Sayı uyumu).

## Metin, kayıt ve gönderge

Kayıtlar: `erten-johansson-2024`, `ari-2025`, `can-patton-2004`, `aydin-iseri-2023`, `aydin-2023-tez`, `balpinar-2019`, `sagin-simsek-2008`, `mete-2023`, `demirsahin-2008`, `onursal-2003`, `calisir-zenci-2020`, `furtun-borekci-2023`, `guclu-2020`, `atasoy-2016`, `ozmen-2024`, `tekin-2024`.

Türkçe web kayıtları ölçülebilir biçimde ayrışır; haber metinleri İngilizce haberlere benzer, etkileşimli tartışma ve tarif dile ve kültüre özgüdür (Erten-Johansson ve ark. 2024). 52 doktora tezi özetinde ortalama cümle uzunluğu 20,93 sözcüktür (Arı 2025). Özetlerde en sık üstsöylemsel ad metin adıdır ve `çalışmanın amacı` türü kalıp savları yönetir (Aydın ve İşeri 2023). Metne bağlı `bu` ile `o` ikili karşıtlık kurar (Balpınar 2019). Bağlacın konumu bağlacın sözdizimsel grubuna bağlıdır (Demirşahin 2008). Türkçe bilimsel metinde olumsuz tümce genelleme, çıkarım, araştırma boşluğu ve beklenmeyen sonuç edimlerini taşır (Çalışır Zenci 2020). Tez sonuç ve öneri bölümlerinde gönderim sürekliliği zayıf bulunmuştur (Mete 2023); Türkçe eğitimi makalelerinde en zayıf bölümler yöntem ve tartışmadır (Furtun ve Börekçi 2023). Özetlerde kanıtsal belirleyiciler zamanla artmıştır (Güçlü 2020). Teknik Türkçede terim katmanı genel akademik sözcük katmanından ayrı listelenebilir (Tekin 2024).

**Örüntü kararı.** `netlik-omurgasi.md` 25 sözcük eşiğini "zaten uzun" diye veriyordu; Arı (2025) ile ortalamanın üstü ama olağan diye düzeltildi. `çalışmanın amacı` türü kabuk adlar duyuru ya da etiket sayılmaz; `style-lint.py` bunları işaretlemiyor (denendi). `bu` ↔ `o` dönüşümü yapılmaz (`akicilik.md` › Gönderge açıklığı). Bağlacı mekanik olarak cümle başına taşıyan kural kurulmaz. Olumsuz tümce dolgu sayılmaz; bu, `SKILL.md` › Kaynak sadakati ile uyumludur.

## Yabancı etki, kalkı ve `ki`

Kayıtlar: `sari-2014`, `dogan-2020`, `ozkan-musa-2004`, `yarar-2020`, `sargin-2024`, `yalap-bicer-2022`, `yetkin-karakoc-2014`, `koca-2021`, `can-koksal-2025`, `duman-2013`, `erdem-2006`, `sas-2022`, `zulfikar-1991`, `aksan-1996`, `akalin-2002`.

`Ki` Farsçadan alınmıştır; Batı Türkçesinde `kim` Osmanlı Türkçesinin sonuna kadar onunla birlikte kullanılmış (Sarı 2014), `ki`li cümle Anadolu'da 14. yüzyılda Farsça çevirilerle yaygınlaşmıştır (Doğan 2020). Yabancı kökenli bağlaçların bir kısmı yüzyıllık alıntıdır (Özkan ve Musa 2004). `Sahip` ve `ait` resmî Türkçede iyelik türü varoluş tümcesinin yerleşik yüklemleridir (Yarar 2020). Makine çevirisinde sıfat yan cümleleri sistemli hata üretir (Sargın 2024). Akademik tezlerde öbek düzeyinde öyküntü terim yaygındır (Yalap ve Biçer 2022); öyküntü anlaşılırlık sorunu da doğurabilir (Yetkin Karakoç 2014). Anlam değişmesi eski alıntılarda da görülür (Koca 2021); bazı öyküntüler birden çok dilde ortaktır (Can ve Köksal 2025). Duman (2013), "doğru Türkçe" kitaplarındaki yasakların önemli bir bölümünün dilbilimin ilkeleriyle çeliştiğini gösterir.

**Örüntü kararı.** Kökeni yabancı diye bir yapı işaretlenmez: `ki`, `sahip`, `etmek` birleşimleri, eski alıntılar ve yerleşik öyküntü terim karşı örnektir. Aday, Türkçe kaynakla daha doğal kurulabilecek ve İngilizce sırayı izleyen kullanımdır (`that/which` sırasındaki `ki`, özellik bildiren `sahip olmak`, ad + `olan` zinciri). Duman'ın bulgusu bu deponun disiplinini destekler: popüler yasak listesi kanıt değildir, kural betimleyici ya da derlem kanıtına dayanır. `olarak`, `tarafından`'ın İngilizce kaynaklı yayılması, çeviride `bir` fazlası ve `adreslemek`, `deneyimlemek` türü kalkılar için hakemli çalışma bulunamadı; bu kalıplar çıkarımdır ve sert denetime girmez.

## Ses bilgisi, ünsüz değişimi ve biçim çözümleyicileri

Kayıtlar: `becker-ketrez-nevins-2011`, `inkelas-orgun-1995`, `sezer-1981-k`, `inkelas-2011-velar`, `chong-2019`, `kallestinova-2004`, `levi-2001`, `polgardi-1999`, `kabak-vogel-2001`, `inkelas-orgun-2003`, `sezer-1983`, `oflazer-1994`, `hankamer-1986`, `goksel-2006`, `coltekin-2010`, `coltekin-2014`, `sak-2008`, `sak-2011`, `oflazer-1996`, `kabak-2007`, `broadwell-2008`.

Sonu durak ünsüzle biten adların yaklaşık %54'ü yumuşar; oran tek heceli köklerde %12, çok heceli köklerde %59'dur ve konuşurlar boğumlanma yerine ve hece sayısına duyarlıdır (Becker, Ketrez ve Nevins 2011). İstisnalar köke özgü sözlük özelliğidir (Inkelas ve Orgun 1995); velar düşmesini tetikleyen kısıt sözlüğün ses dizimi örüntülerinden öğrenilemez (Chong 2019) ve ek sınırına bağlıdır (Sezer 1981; Inkelas 2011). Yazımda tek `l` iki sesi karşılar ve bazı alıntılarda ek ünlüsü bu yan ünsüze uyar (`rol-e`; Levi 2001). Türkçe ek dizimi az sayıda ses kuralı ve sonlu durum makinesiyle betimlenir (Oflazer 1994; Hankamer 1986); özgür çözümleyiciler (Çöltekin 2010, 2014), belirsizlik gidericiler (Sak, Güngör ve Saraçlar 2008, 2011) ve hata toleranslı tanıma (Oflazer 1996) vardır. Ek ortaklığında askıdaki ek bütün ögeler üzerinde kapsam taşır (Kabak 2007; Broadwell 2008).

**Örüntü kararı.** Ünsüz yumuşaması ve ünlü uyumu istisnaları için genel düzenli ifade kurulmaz; `yazim` ailesi listelenmiş sözcüklerle çalışır ve listede olmayan biçim yanlış sayılmaz (`yazim-ve-dil-bilgisi.md` › Sözcüğün kökeni). Ek örüntüleri arketip sınıflarıyla düşünülür (A = a/e, I = ı/i/u/ü, D = d/t); `style-lint.py` öz sınamasındaki `turet` işlevi bu arketiplerden biçim üretip zaman ve edilgen örüntülerini sınar. Biçim çözümleyicisi bağımlılık gerektirdiği için eklenmedi; aday kural olarak durur.

## Odak, konu, eksilti ve söylem belirleyicileri

Kayıtlar: `goksel-ozsoy-2003`, `ersoyleyen-2023`, `kamali-krifka-2020`, `gurer-2020`, `grigoras-2020`, `gurer-goksel-2019`, `hankamer-1971`, `slobin-bever-1982`, `hoffman-1995`, `ozge-bozsahin-2010`, `kahraman-2010`, `ozge-2010-ilgi`, `ozge-2015-ilgi`, `ruhi-2009-yani`, `yilmaz-2004`, `ozbek-2000`.

`dA` hem ekleyici odağı hem karşıtsal konuyu işaretleyebilir (Göksel ve Özsoy 2003); bağlaç olan ve olmayan kullanımları ayrıdır (Ersöyleyen, Zeyrek ve Öter 2023). Karşıtsal konu bürünle ayrılmaz, sözdizimsel ve anlamsal araçlarla işaretlenir (Gürer 2020); konu ve karşıtsal odak öge taşımasını tetikler (Grigoraş 2020); soru ekinin yeri odağı belirler (Kamali ve Krifka 2020). Yüklemi eksiltili sıralı cümle meşrudur ve kabul yargısını bilgi yapısı da belirler (Gürer ve Göksel 2019). Türkçe en serbest dizimli dillerden biridir ama kanonik şema işlemeyi kolaylaştırır (Slobin ve Bever 1982); dizim seçimi bağlama bağlıdır (Hoffman 1995; Özge ve Bozşahin 2010). Özne ilgi yan cümlesi nesne ilgi yan cümlesinden daha hızlı işlenir (Kahraman 2010) ve daha sık üretilir (Özge, Marinis ve Zeyrek 2010), ama işlem maliyeti iki türde de vardır (Özge ve ark. 2015). Yazılı Türkçede `yani` önerme düzeyinde açımlama yapar (Ruhi 2009); `işte` ve `şey` konuşmanın değerlendirme parçacıklarıdır (Yılmaz 2004; Özbek 2000).

**Örüntü kararı.** `de/da` ve `ise` akıcılık için silinmez, başka ögeye taşınmaz, `ayrıca` ile değiştirilmez (`turkce-baglayicilar.md` › Karşı örnekler). Eksilti açılmaz; açılırsa ortak yüklemin zamanı ve kipi korunur (`yazim-ve-dil-bilgisi.md` › Ortak öge uyumu). Sözcük dizimini "kanonik sıraya" çeviren kural kurulmaz; nedensiz devriklik yapay yerlilik olarak işaretlenebilir. `-(y)An` ↔ `-DIK` dönüşümü rolleri değiştirebileceği için yapılmaz; uzun nesne ilgi yan cümlesi bölünebilir. Açımlayıcı `yani` sızıntı değildir; `işte` ve söylem `şey`i bilimsel metinde sızıntı adayıdır (`okura-dogrudan-metin.md` › Sızıntı olmayanlar).

## Kiplik, noktalama ve kibarlık

Kayıtlar: `corcu-2005`, `kerslake-1990`, `doyuran-2009`, `kalfa-2020`, `sahin-aydogdu-2017`, `zeyrek-2001`, `ruhi-isik-guler-2007`.

`-Abil` olasılık, `-mAlI` gereklilik taşır (Erguvanlı Taylan 2018; Corcu 2005; Kerslake 1990). Türkçe bilimsel makalelerde kaçınma epistemik ve çıkarımsal kip, aktarma fiili, belirteç ve soyut özneyle yapılır ve disiplin uzlaşımına bağlıdır (Doyuran 2009). Virgülün geniş işlevi ve belli ölçüde seçim özgürlüğü vardır (Şahin ve Aydoğdu Yüksel 2017; Kalfa 2020). Türkçe kibarlık grup bilincini ve ilişki işini öne alır (Zeyrek 2001; Ruhi ve Işık-Güler 2007).

**Örüntü kararı.** `-mAlI` ↔ `-Abilir` ↔ geniş zaman dönüşümü kanıt statüsü değişikliğidir (`kanit-ve-kesinlik.md`); `eval-runner.py` zorunluluk ve çekince eklemesini zaten sayar. İsteğe bağlı virgül sert yazım bulgusu yapılmaz; yalnızca anlam karışıklığı yaratan virgül ve ondalık listedeki noktalı virgül ele alınır. Kurumsal yazışmada `siz` ve grup odaklı kalıplar korunur (`kenar-turler.md`, `okura-dogrudan-metin.md`).

## Değerlendirme için hesaplamalı kaynaklar

Kayıtlar: `sulubacak-2016-ud`, `sulubacak-2016-imst`, `turk-2019`, `kuzgun-2021`, `cesur-2024-atis`, `bakay-2021-kenet`, `marsan-2021-framenet`, `kara-2020-tropbank`, `torunoglu-eryigit-2014`, `eryigit-2017`, `arikan-2019`, `koksal-2020-turkishtweets`, `eyecioglu-keller-2018`, `karaoglan-2018`, `ilgen-biemann-2022`, `schweter-2020`, `uludogan-2024-turna`, `berk-2018-parseme`, `berk-2019`, `ozturk-2022-parseme`, `golynskaia-2022`, `ruhi-2010-std`.

Türkçe UD ağaç bankaları (IMST-UD, BOUN, Penn, ATIS, Kenet, Tourism, PUD) farklı türleri temsil eder: Kenet TDK sözlüğünün örnek cümlelerinden, Tourism müşteri yorumlarından, PUD profesyonel çeviriden oluşur (UD sayfaları; yayın yılı olmadığı için kayıt açılmadı). ATIS çiftinde aynı 5.432 cümle İngilizcede yaklaşık 61.900, Türkçede yaklaşık 45.900 belirteçtir (Cesur ve ark. 2024). KeNet anlam ağı (Bakay ve ark. 2021), TRopBank (17.673 fiil; Kara ve ark. 2020), normalleştirme verileri (Torunoğlu ve Eryiğit 2014; Eryiğit ve Torunoğlu-Selamet 2017), `de/da` hatası tespiti (Arıkan ve ark. 2019), yazım düzeltme verisi (Köksal ve ark. 2020), eşanlamlı ifade derlemleri (Eyecioğlu ve Keller 2018; Karaoğlan ve ark. 2018), karmaşık sözcük derlemi (İlgen ve Biemann 2022), Türkçe dil modelleri (BERTurk, TURNA), PARSEME çok sözcüklü fiil derlemi (Berk ve ark. 2018; Berk 2019; Öztürk ve ark. 2022), öğrenici hata kodlama sistemi (Golynskaia 2022) ve Sözlü Türkçe Derlemi (Ruhi ve ark. 2010) değerlendirmede kullanılabilecek kaynaklardır.

**Örüntü kararı.** Bu kaynaklar henüz depoya bağlanmadı; lisansları ve erişim koşulları kayıtların `dogrulama` alanında ya da UD sayfalarındadır. Kullanım yolları aday kurallar tablosundadır: kayıt karşıtlığında yanlış pozitif ölçümü (Kenet ↔ Tourism), çeviri Türkçesi örneklemi (PUD, ATIS), terim değişikliği adayları (KeNet; terim korumasının yerini tutmaz), fiil çerçevesi (TRopBank; TDK hâl normu değildir). İki arXiv çalışması geri çekildiği için kullanılmaz: Türkçe sözcüksel sadeleştirme (arXiv 2201.05878) ve zenginleştirilmiş Türkçe öğrenici derlemi (arXiv 2601.22875). Cümle düzeyinde paralel Türkçe sadeleştirme derlemi bulunamadı.

## Örüntü kararları

| Örüntü | Kanıt | Karar | Nerede |
|---|---|---|---|
| Dört biçimli ekler (`-DI`, `-DIr`, `-mIştI`, `-mIştIr`) | Türkçe ünlü uyumu (`goksel-kerslake-2005`, `clements-sezer-1982`) | Lint örüntüleri `u/ü` biçimlerini kapsar; `görülmüştür`, `görülmüştü`, `ölçüldü` doğru sınıflanır | `style-lint.py` zaman sınıfı ve edilgen örüntüsü |
| `-dığı için`, `olasılıkla` | Neden ve çekince bildiren yerli biçimler | Eklenen işaret ailelerine girdi; aile içi dönüşüm ekleme sayılmaz | `eval-runner.py` |
| Cansız çoğul özne + çoğul yüklem; sayı + çoğul ad | `bamyaci-2014`, `sag-2022`, `renans-2017` | Bağlamsal aday; insan özne, `yüz`/`on`/`altı`, rakam ve soru–olumsuzluk dışarıda | `style-lint.py` `sayi_uyumu` |
| `tarafından`lı edilgen | `erdem-2007`, `sebzecioglu-oktar-2010` | Bağlamsal aday; kurumsal ve süreç eyleyeni meşru, eyleyensiz edilgen işaretlenmez | `style-lint.py` `tarafindan`, `kanit-ve-kesinlik.md` |
| `bir` | `ozturk-2005`, `ketrez-2023`, `tat-2011` | Yalnız yoğunluk; olumsuzluk, sıfat + `bir` + ad ve yalın nesne korunur | `turkce-ritim-ve-ceviri-kokusu.md` |
| Belirtme hâli `-(y)I` | `enc-1991`, `von-heusinger-kornfilt-2005` | Eklemek ya da silmek önerme değişikliğidir | `turkce-ritim-ve-ceviri-kokusu.md` |
| `-DIr`, `-mAktA` | `kerimoglu-aksu-2015`, `ozdemir-2023-dir`, `akaslan-2011` | Tanım `-DIr`'ı kalır; `-mAktAdIr` yalnız zincirde incelenir | `zamansal-ankraj-ve-rapor-kipi.md` |
| Ad + `et-` | `aksehirli-2013`, `ucar-2010` | İşaretlenmez; yalnız listelenmiş birleşim | mevcut `hafif_fiil` ve `sozcuksel_kalki` |
| `ki`, `sahip` | `sari-2014`, `dogan-2020`, `yarar-2020` | Tek kullanım işaret değil; İngilizce sırayı izleyen ve özellik bildiren kullanım aday | `turkce-ritim-ve-ceviri-kokusu.md` |
| Kabuk ad (`çalışmanın amacı`) | `aydin-iseri-2023` | İşaretlenmez | lint davranışı denendi, değişiklik yok |
| Cümle uzunluğu eşiği | `ari-2025` | 25 sözcük inceleme işaretidir, "zaten uzun" değildir | `netlik-omurgasi.md` |
| `bu` ↔ `o` | `balpinar-2019` | Birbirine çevrilmez | `akicilik.md` |
| Ünsüz yumuşaması, ünlü uyumu istisnası | `becker-ketrez-nevins-2011`, `inkelas-orgun-1995`, `levi-2001` | Genel kural yok; yalnız listelenmiş sözcük | `style-lint.py` `yazim`, `yazim-ve-dil-bilgisi.md` |
| Ek arketipleri | `oflazer-1994` | Öz sınama biçimleri arketiplerden üretir | `style-lint.py` `turet` |
| `de/da`, `ise` | `goksel-ozsoy-2003`, `ersoyleyen-2023`, `gurer-2020` | Silinmez, taşınmaz, `ayrıca` olmaz; bitişik `de/da` için düzenli ifade yok | `turkce-baglayicilar.md`, `yazim-ve-dil-bilgisi.md` |
| Eksilti | `gurer-goksel-2019` | Bozukluk sayılmaz | `yazim-ve-dil-bilgisi.md` |
| `yani`, `işte`, `şey` | `ruhi-2009-yani`, `yilmaz-2004` | Açımlayıcı `yani` kalır; cümle başı `işte` ve söylem `şey`i bağlamsal sızıntı adayı, `bir şey`/`her şey` işaretlenmez | `style-lint.py` `sizinti`, `okura-dogrudan-metin.md` |
| Kip gücü | `erguvanli-taylan-2018`, `doyuran-2009` | `-mAlI` ↔ `-Abilir` statü değişikliği | `kanit-ve-kesinlik.md` |
| Kibarlık kalıpları | `zeyrek-2001`, `ruhi-isik-guler-2007` | Dolgu sayılmaz | `kenar-turler.md` |

## Aday kurallar

Literatürden çıkan ama henüz Metinoskop kuralı olmayan öneriler. Her biri girmeden önce referans dosyasına kaynağıyla yazılır, dönüşüm ve korunur vakasıyla sınanır; `SKILL.md`'ye girecekse kör A/B ile ölçülür.

| Aday | Dayanak | Gereken vaka | Risk |
|---|---|---|---|
| Duyum `-mIş`'ı `-DI`'ya, doğrudan `-DI`'yı `-mIş`'a çevirme; kanıtsallık kanıt statüsüdür | `aksu-koc-slobin-1986`, `slobin-aksu-1982`, `karakas-simsek-2026` | dönüşüm: duyuma dayalı haber notu; korunur: rapordaki resmî `-mıştır` | `-mıştır`'ı duyum sanıp `-dı`'ya çevirmek |
| Odak eğilimi: düzenleme sırayı yalnızca "yüklem önü odak olmalı" diye değiştirmez | `goksel-ozsoy-2000`, `kilicaslan-2004` | korunur: odağı yüklem öncesi alanın başında olan doğru cümle | yeni bilgiyi yüklemden uzaklaştıran çeviri sırasını korumak |
| Türkçe özette vurgulayıcıyı türün normu say, yalnızca dayanaksızsa sil | `sen-iseri-2023` | korunur: ölçümle desteklenen vurgulayıcılı özet | dayanaksız `açıkça`yı bırakmak |
| Noktalı virgül ve virgül yoğunluğunu AI izi olarak incele | `kocagul-2026` (yalnızca özet) | tam metin okunmadan vaka yazılmaz | Metinoskop gold'larının bağlaçsız ilişki için kullandığı noktalı virgülü silmek |
| `-DIr` eklenmesini ya da silinmesini kanıt statüsü değişikliği olarak denetle | `erguvanli-taylan-2018`, `sansa-tura-1986`, `ozdemir-2023-dir` | dönüşüm: tanım cümlesinde `-DIr` silen düzenleme; korunur: `-mAktAdIr` sadeleştirmesi | kaynaklar `-DIr`'ın anlamında ayrışıyor (kesinlik ya da varsayım); `-mAktAdIr` sadeleştirmesini yanlış alarm sayma |
| Cansız öznenin yüklemden sonra geldiği devrik cümlede sayı uyumu | `uygun-felser-2023` | dönüşüm ve korunur vakası | konuma bağlı uyum yargısı belirsiz |
| Ek ve ünsüz kurallarını biçim çözümleyicisiyle doğrula | `coltekin-2010`, `oflazer-1996`, `sak-2011` | dış bağımlılık kararı; listede olmayan biçimlerde yanlış pozitif ölçümü | bağımlılıksız paket ilkesini bozmak; çözümleyici belirsizliği |
| Lint yanlış pozitiflerini UD ağaç bankalarında ölç (Kenet ↔ Tourism, PUD) | `turk-2019`, `kuzgun-2021`, `cesur-2024-atis` | ölçüm betiği; lisans denetimi | CC BY-NC-SA ve CC BY-SA lisanslı veriyi depoya kopyalamak |

## Boşluklar ve doğrulanamayanlar

**Bulunamayan çalışma türleri.**

- Türkçe çeviri metni özgün Türkçeyle derlemde karşılaştıran (açıklaştırma, sadeleştirme, girişim) hakemli bir çalışma. Yalnızca künyesi görülen ilgili kayıtlar: Yazıcı, "Simplification as a Translation Universal" (13. Dil, Yazın ve Halkbilim Sempozyumu, 2013, 1131–1138); bir İstanbul Üniversitesi çeviribilim tezinde önerilen derlem modeli (yazar ve yıl doğrulanmadı).
- `sahip olmak` kalkısı üzerine akademik çalışma.
- İngilizce→Türkçe makine çevirisinde MQM türü sistemli hata sayımı.

- Biber türü çok boyutlu bir Türkçe kayıt karşılaştırması; `-mAktAdIr` sıklığını türlere göre ölçen derlem çalışması; Türkçe akademik yazıda `bu durum`, `söz konusu` sıklığını ölçen kabuk ad çalışması; `hakkında`, `ilişkin`, `üzerine`, `konusunda`, `ile ilgili` ilgeçlerinin anlam ve kayıt farkını karşılaştıran hakemli kaynak. İkinci turda arama kotası dolduğu için bu boşlukların bir kısmı gerçek boşluk olmayabilir.

**Künyesi eksik kaldığı için veritabanına alınmayanlar.**

- Zeyrek (2014), `ama` ve `fakat` üzerine bölüm, John Benjamins, Studies in Language Companion Series 164: bölüm adı ve editörler doğrulanamadı. Katalog özetine göre `ama` ödünü ve edimbilimsel yorumları `fakat`'tan daha kolay işaretler; `fakat` daha resmî türlerde yeğlenir.
- Yıldız, İpek, Türkçe bilimsel metinlerde çok sözcüklü birimler üzerine doktora tezi (YÖK Açık Bilim 20.500.12812/220663): yıl ve üniversite doğrulanamadı.
- Bozkurt Güvenek, "Türkçede Makine Çevirisinin Söz Dizimsel ve Anlamsal Hataları: Google Translate ve DeepL Örnekleri", HUMANITAS 14(27), 35–57: yayın yılı doğrulanamadı. Özete göre iki sistemin Türkçe çıktısı kiplik, zaman, vurgu (tema–rema) ve mecazda yetersiz kalır.
- Er ve Çoğalmış (2024), yapay zekâ ve insan Türkçe metni tespiti (IEEE ICMI): yalnızca künye görüldü.
- Akdağ ve ark. (2026), "Retranslation at the intersection of style, machines, and plagiarism" (StyGenAI, EAMT): bulgu doğrulanamadı.
- Alimen (2023), ChatGPT çevirisi üzerine deneysel çalışma (RumeliDE 36): sonuçlar görülemedi.
- Uzun ve Huber (ed.), *Türkçede Bilgi Yapısı ve Bilimsel Metinler*: yıl ve içerik doğrulanamadı.
- Çokal, "Turkish discourse anaphors: bu and o" (Köln Üniversitesi): yıl ve künye görülmedi. Arama özetine göre ODTÜ Türkçe Derlemi'nde `bu` ve `o` çoğunlukla hemen önceki tümceye gönderme yapar.
- Özyıldırım (2010), Türkçe haber metinlerinde çok boyutlu çözümleme: yalnızca bir aktarımda görüldü.
- Karaköse, `ki` bağlacı ve Batı dillerinden çeviri üzerine metin (Pamukkale Üniversitesi deposu): yayın yeri ve yılı kesin değil.
- Kan (2021), fen ve sosyal bilim makalelerinde etkileşimli belirleyiciler (EPASR 16(3)): yazarın adı ve tam başlık görülmedi.
- Kornfilt, "Two evidentials or two commitment phrases in Turkish?": konuşma metni, yıl ve yer görülmedi.
- Kabak (2011), "Turkish vowel harmony", Blackwell Companion to Phonology: yazar listesi ve sayfalar çelişkili. Akın ve Akın (2007), Zemberek: yayın yeri doğrulanamadı. Kamali (2011), soru ekinin konumu üzerine doktora tezi: kurum ve yıl doğrulanamadı.
- Bozşahin (2000), Türkçede eksilti ve sözcük dizimi: hiçbir sonuçta görülmedi. `ise` üzerine müstakil bir makale ve akademik metin gövdesinde virgül sıklığını veren bir derlem çalışması bulunamadı.
- Demir ve ark. (2012), Turkish Paraphrase Corpus (LREC 2012) ve Sözlü Türkçe Derlemi'nin LREC 2010 ve CILC-10 bildirileri: tam yazar listeleri görülmedi.
- Göksu, Türkçede `-DIK`, `-mA`, `-(y)Iş`, `-Im` adlaştırmalarının tipolojisi (IULC Working Papers) ve Predolac, Türkçede dilek ve bildirme kipleri (IULC Working Papers): yayın yılları görülmedi.

**Kayıtlardaki belirsizlikler.** Banguoğlu'nun ilk baskı yılı (1974 ya da 1986), Csató ve Johanson (1998) bölümünün sayfa aralığı, Oflazer ve ark. (2003) bölümünün yer aldığı kitabın adı, Ateşman (1997) makalesinin sayfa aralığı ve Kocagül (2026) yazarının tam adı kaynaklarda çelişiyor ya da bulunamadı; ayrıntı ilgili kaydın `yayin` ve `dogrulama` alanlarındadır.
