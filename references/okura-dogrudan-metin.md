# Okura doğrudan metin

Bir ajan çoğu zaman bir konuşmanın içinde yazar: kullanıcı bir hedef (`/goal`) ya da talimat verir, ajan dosya okur, araç çalıştırır, taslak üretir, kullanıcıyla düzeltmeler üzerinde konuşur. Bu dünyanın izleri teslim edilen metne kolayca sızar: `konuştuğumuz gibi`, `istersen ekleyebilirim`, `önce şu dosyaya baktım`, `bu bölümü daha net olsun diye yeniden yazdım`. Metni okuyacak kişi bu konuşmayı görmedi. Onun için bu cümleler ya anlamsızdır ya da metnin kime yazıldığını bulanıklaştırır.

Bu dosya, Metinoskop'un düzenlediği ya da ürettiği her metnin, konuşmayı görmemiş son okura doğrudan verilecekmiş gibi kurulmasını sağlar.

## İçindekiler

1. [Kullanıcı ile okur](#kullanıcı-ile-okur)
2. [Okuru belirle](#okuru-belirle)
3. [Sızıntı aileleri](#sızıntı-aileleri)
4. [Bilgiyi kurtar, ambalajı at](#bilgiyi-kurtar-ambalajı-at)
5. [Teklifi ve öneriyi okura çevirmek](#teklifi-ve-öneriyi-okura-çevirmek)
6. [Metin dışı not](#metin-dışı-not)
7. [Sızıntı olmayanlar](#sızıntı-olmayanlar)
8. [Tam örnek](#tam-örnek)
9. [Aşırı uygulama belirtileri](#aşırı-uygulama-belirtileri)
10. [Stil denetimi](#stil-denetimi)

## Kullanıcı ile okur

İki ayrı kişi vardır:

- **Kullanıcı** metni isteyen ya da düzenleten kişidir. Ajanla konuşur, talimat verir, taslakları görür.
- **Okur** metni teslimden sonra okuyan kişidir: raporu alan yönetici, README'yi açan geliştirici, makaleyi okuyan hakem, e-postanın alıcısı.

Konuşma, talimatlar, önceki taslaklar, araç çıktıları, ajanın çalışma dizini ve ajanın çalışma sırası kullanıcının dünyasındadır, okurun dünyasında değil. Metin yalnızca okurun dünyasındaki şeylere gönderme yapar: olgulara, belgenin kendisine, okurun erişebildiği kaynaklara.

## Okuru belirle

- **Varsayılan:** Okur konuşmayı görmedi. Kullanıcı aksini söylemedikçe bu geçerlidir.
- **Kullanıcı okuru tanımlarsa** ("bunu bana not olarak yaz", "Selin'e yanıt olarak düzenle") o tanım geçerlidir. Okur kullanıcının kendisiyse, kullanıcıyla paylaşılan bağlama gönderme sızıntı değildir.
- **Okurun da tarafı olduğu yazışma:** Bir e-postada `geçen ay konuştuğumuz gibi` yazarla alıcının ortak geçmişine gönderir; okur o konuşmanın tarafıdır. Bu sızıntı değil, içeriktir (`iyi-metin` vakası).
- **Kim kime konuşuyor testi:** Konuşmayı görmemiş okur cümleyi okuyunca `ben`, `biz`, `sen`, `siz` kimdir, anlıyor mu? Cümle ona bir bilgi veriyor mu? İkisine de evetse cümle kalır. `Biz` ajan ile kullanıcıysa, `sen` kullanıcıysa ve okur bunlardan biri değilse sızıntı vardır.

## Sızıntı aileleri

| Aile | Örnek | Ne yapılır |
|---|---|---|
| **Konuşmaya gönderme** | `konuştuğumuz gibi`, `isteğin üzerine`, `talimatta belirtildiği gibi`, `verdiğin dosyaya göre`, `yukarıdaki mesajda`, `kullanıcının istediği üzere` | Gönderme silinir; taşıdığı olgu ya da kaynak bilgisi okura yazılır. |
| **Kullanıcıya teklif** | `istersen ... ekleyebilirim`, `bir sonraki adımda ... bakabilirim`, `şunu da yapabiliriz`, `ister misiniz?` | Okura bilgi vermiyorsa silinir; içinde gerçek bir seçenek ya da öneri varsa statüsüyle okura çevrilir. |
| **Çalışma süreci anlatımı** | `önce X dosyasını inceledim, sonra testi çalıştırdım`, `analizi tamamladım`, `şimdi Y'ye bakalım` | Ajanın sırası ve ilk tekil şahıs atılır. Bulgunun dayanağı olan yöntem bilgisi yöntem cümlesi olarak kalır (`kayıtlar incelendi`). |
| **Düzenleme geçmişi** | `bu bölüm daha net olsun diye yeniden yazıldı`, `önceki taslakta ... yazıyordu`, `(düzeltildi)`, `Not: X kaldırıldı`, `güncelleme:` | Silinir. Okur önceki taslağı görmedi; metin yalnızca son hâlini söyler. Belge bir sürüm notuysa önceki sürüm içeriktir (bkz. [Sızıntı olmayanlar](#sızıntı-olmayanlar)). |
| **Teslim ambalajı** | `İşte düzenlenmiş rapor:`, `Aşağıda istediğin özeti bulabilirsin`, `Umarım faydalı olur`, `Başka bir şey ister misin?` | Silinir. Metin kendi başlığıyla ya da ilk önermesiyle başlar. |
| **Ajan kimliği** | `bir yapay zekâ olarak`, `bir dil modeli olarak bunu bilemem` | Silinir. Taşıdığı belirsizlik varsa olgunun statüsü olarak yazılır (`bu bilgi kaynakta yok`). |
| **Okurun erişemediği nesne** | ajanın çalışma dizinindeki geçici dosya, oturum ya da araç adı, `promptta`, `bağlam penceresinde` | Okur nesneye erişemiyorsa gönderme silinir; nesnenin taşıdığı bilgi okura yazılır. Okurun erişebildiği depo dosyası, URL ya da ek gönderme olarak kalır. |
| **Metin içine konmuş not** | `[?]`, `(kaynakta belirsiz)`, `TODO: kontrol et`, `(burayı netleştirmek gerek)` | Metinden çıkar; kullanıcıya söylenecekse metin dışı nota taşınır. Kaynakta zaten bulunan yer tutucu (`[tarih eklenecek]`) yazarındır, korunur. |

## Bilgiyi kurtar, ambalajı at

Sızıntılı cümle çoğu zaman gerçek bir önerme taşır. Kural, ambalajı atıp önermeyi kaynağın statüsü ve kesinliğiyle okura yazmaktır. Bu, değişmezlerin (kaynak sadakati, kanıt statüsü) altında çalışır: sızıntıyı temizlemek bir çekinceyi, varsayımı ya da kapsam sınırını silme gerekçesi değildir.

| Önce | Sonra | Korunan |
|---|---|---|
| Konuştuğumuz gibi bütçe 2 milyon TL. | Bütçe 2 milyon TL. | Olgu |
| Verdiğin 2024 satış dosyasına göre iade oranı %6,2. | 2024 satış verilerine göre iade oranı %6,2. | Veri kaynağı ve atıf |
| Burada sunucu saatlerinin senkron olduğunu varsaydım. | Bu hesap, sunucu saatlerinin senkron olduğu varsayımına dayanır. | Varsayım statüsü |
| Bunu doğrulayamadım. | Bu değer doğrulanmadı. | Belirsizlik |
| Emin değilim ama gecikme ağ kaynaklı olabilir. | Gecikme ağ kaynaklı olabilir. | Çekince düzeyi (`olabilir` kalır; `emin değilim` aynı belirsizliği ajanın ağzından söylüyordu) |
| Kullanıcının belirttiği üzere pilot iptal edildi. | Pilot iptal edildi. | Olgu (kullanıcının talepte verdiği bilgi kaynağın parçasıdır) |
| Önce `cache.py` dosyasına baktım, sonra yük testini çalıştırdım. | `cache.py` incelendi ve yük testi çalıştırıldı. | Yöntem |

Bilgi taşımayan sızıntı (teşekkür, teslim ambalajı, kullanıcıya teklif, okura hiçbir şey söylemeyen süreç anlatımı) karşılıksız silinir. Silme testi burada da geçerlidir: cümle çıkınca okurun bildiği bir şey eksiliyor mu?

İlk tekil şahıs süreç cümlesini yöntem cümlesine çevirirken zamansal ankrajı koru: yapılmış iş geçmişte anlatılır (`incelendi`), genel prosedür geniş zamanda kalır. Kaynağın adlandırmadığı aktörü uydurma: `inceledim` → `ekip inceledi` değil, `incelendi`.

## Teklifi ve öneriyi okura çevirmek

Ajanın kullanıcıya önerisi (`şunu böyle yapabiliriz`) içinde okur için gerçek bir seçenek taşıyabilir. Çevirirken üç şeyi koru:

- **Statü:** `yapabiliriz` bir olasılıktır, öneri ya da karar değildir. `Önbelleği kaldırabiliriz` → `Önbellek kaldırılabilir` ya da `Bir seçenek, önbelleğin kaldırılmasıdır`. `Önbellek kaldırılmalıdır` statüyü öneriye, `Önbellek kaldırılacak` karara yükseltir; ikisi de yanlıştır. Kaynak açıkça öneriyorsa (`önbelleğin kaldırılmasını öneririm`) öneri olarak kalır: `Önbelleğin kaldırılması önerilir`.
- **Aktör:** `biz` okurun dünyasında tanımsızdır. Kaynakta adı geçen bir aktör (ekip, yönetim) yoksa edilgen ya da adlaştırılmış yapı kur; aktör uydurma.
- **Koşul:** `yük testi temiz geçerse sürümü çıkarabiliriz` → `Yük testi temiz geçerse sürüm çıkarılabilir`. Koşul düşmez.

Okura hiçbir seçenek sunmayan teklif (`istersen tabloyu da güncellerim`, `bir sonraki adımda grafik ekleyebilirim`) ajanın kullanıcıyla işidir; silinir.

## Metin dışı not

Kullanıcıya söylenecek her şey (yorum seçimi gerektiren soru, kapsam dışı kalan bir anlam hatası, değişiklik açıklaması) metnin içine değil, dışına yazılır:

- Metin önce, eksiksiz gelir; olduğu gibi kopyalanıp okura gönderilebilmelidir.
- Not metinden sonra, yatay çizgiyle (`---`) ayrılmış kısa bir bölümdür. Soru tek ve somuttur.
- Not yalnızca gerektiğinde yazılır: yorum seçimi zorunluysa, kullanıcı kapsamı daralttığı için bir anlam hatası metinde kaldıysa ya da kullanıcı inceleme istediyse. Değişiklik yapıldı diye not yazılmaz.
- Belirsiz yer metinde kaynaktaki hâliyle kalır; nota yazılan soru onu çözmeyi kullanıcıya bırakır.

Kapsam daraltıldığında örnek: kullanıcı "yalnızca noktalama hatalarını düzelt" dediyse ve metinde `bulgular ... olduğunu önermektedir` kalkısı varsa kalkıya dokunulmaz. Metinden sonra tek satır: `önermektedir` Türkçede tavsiye bildirir; kastedilen çıkarımsa `düşündürüyor` yazılabilir.

## Sızıntı olmayanlar

Aynı yüzey biçimleri, okurun dünyasına gönderme yaptığında içeriktir:

- **Okurun da tarafı olduğu konuşma:** E-postada `dünkü toplantıda konuştuğumuz gibi`, `istersen ayrı bir sayfa ekleyebilirim` (teklif okura yapılıyor).
- **Kurumsal yanıt:** Müşteriye yazılan yanıtta `talebiniz doğrultusunda aboneliğiniz iptal edildi`. Okur talebin sahibidir.
- **Belgenin kendi parçaları:** `Tablo 2'de`, `3. bölümde`, `Ek A`. Belge içi gönderme okurun önündedir.
- **Sürüm notu ve değişiklik günlüğü:** `Önceki sürümde zaman aşımı 30 saniyeydi; bu sürümde 60 saniye.` Okur önceki sürümü kullanmıştır; karşılaştırma içeriktir.
- **Gereksinim ve davranış metni:** `Kullanıcının isteği üzerine silinen hesabın verisi 30 gün içinde yok edilir.` Buradaki kullanıcı ürünün kullanıcısıdır.
- **Dil modellerini konu edinen metin:** `Model, istemde belirtilen biçime 200 denemenin 11'inde uymadı.` İstem çalışmanın nesnesidir.
- **Akademik `biz`:** `Bu sonuçtan, ... olduğunu çıkarabiliriz` yazarın okurla kurduğu ortak akıl yürütmedir. Ajan ile kullanıcıyı göstermez; kayıt kararı ayrı bir sorudur.
- **Yöntem olarak yapılmış iş:** `Bu çalışmada 12 günlük kayıt incelendi.` Çalışmanın kendisi okurun konusudur.
- **Kaynaktaki yer tutucu:** `[tarih eklenecek]` yazarın kendi işaretidir; Metinoskop bilgi uyduramayacağı için onu doldurmaz ve silmez.

Bu vakaları `sizinti-sanilan-icerik-korunur` ve `iyi-metin` korur.

## Tam örnek

**Kaynak** (kullanıcı ajana "önbellek sorununu araştır, rapor yaz" demiş; ajanın taslağı):

> İstediğin gibi önbellek sorununu inceledim. Önce `cache.py` dosyasına baktım, sonra yük testini çalıştırdım. Verdiğin günlük dosyasına göre 14 Ekim'deki 37 zaman aşımının 29'u önbellek yenilemesiyle aynı dakikada oluştu. Burada sunucu saatlerinin senkron olduğunu varsaydım; bunu doğrulayamadım. Yenileme aralığını 5 dakikadan 15 dakikaya çıkarırsak zaman aşımları azalabilir. İstersen bir sonraki adımda bunu deneyebilirim ya da yük testini tekrarlayabiliriz. Umarım faydalı olur!

**Okura doğrudan metin**

> `cache.py` incelendi ve yük testi çalıştırıldı. Günlük kayıtlarına göre 14 Ekim'deki 37 zaman aşımının 29'u önbellek yenilemesiyle aynı dakikada oluştu. Bu eşleşme, sunucu saatlerinin senkron olduğu varsayımına dayanır; varsayım doğrulanmadı. Yenileme aralığı 5 dakikadan 15 dakikaya çıkarılırsa zaman aşımları azalabilir.

Konuşmaya gönderme (`istediğin gibi`, `verdiğin`), süreç sırası (`önce ... sonra`), kullanıcıya teklif ve kapanış nezaketi gitti. Yöntem, günlük kaynağı, sayılar, varsayım ve doğrulanmamış olması, öneri olmayan olasılık (`azalabilir`) ve koşul (`-ırsa`) korundu. Yük testinin sonucu kaynakta yok; sonuç uydurulmadı.

## Aşırı uygulama belirtileri

- Varsayımı, `doğrulanmadı` bilgisini ya da çekinceyi "ajanın sesi" diye silmek.
- Bulgunun dayanağı olan yöntem bilgisini süreç anlatımı sayıp silmek.
- `yapabiliriz` olasılığını `yapılmalıdır` önerisine ya da `yapılacak` kararına yükseltmek.
- `biz` yerine kaynakta olmayan bir aktör (`ekip`, `yönetim`) yazmak.
- Okurun tarafı olduğu yazışmadaki ortak geçmişe göndermeyi, kurumsal yanıttaki `talebiniz doğrultusunda` ifadesini ya da sürüm notundaki önceki sürümü silmek.
- Kaynaktaki yer tutucuyu silmek ya da doldurmak.
- Metin dışı notu her düzenlemeye eklemek; not yalnızca gerektiğinde yazılır.

## Stil denetimi

`scripts/style-lint.py` konuşma sızıntısı adaylarını `sizinti` ailesinde işaretler: konuşmaya gönderme, kullanıcıya teklif (`-ebilirim`, `-ebiliriz`, `istersen`), ilk tekil şahıs süreç fiilleri, önceki taslak ya da sürüm, parantez içi düzenleme işareti, `İşte ...` teslim ambalajı ve `prompt`. Aynı biçimler yazışmada, sürüm notunda ve gereksinim metninde içerik olduğu için aile varsayılan olarak bağlamsaldır. Ajan kimliği (`bir yapay zekâ olarak ben ...`) ve sohbet nezaketi `sohbet` sert ailesindedir.

Okurun konuşmayı görmediği biliniyorsa denetimi `--son-okur` ile çalıştırın:

```bash
python scripts/style-lint.py rapor.md --son-okur
```

Bu kipte `sizinti` adayları sert sayılır ve metinde tek bir aday kalsa bile betik 1 ile çıkar. Okurun da tarafı olduğu yazışmada (yanıt e-postası, müşteri yanıtı) bu kipi kullanmayın.
