<p align="center"><img src="assets/banner.svg" alt="Metinoskop: dağınık metin satırları büyüteç camının içinde düzgün satırlara dönüşüyor." width="100%"></p>

# Metinoskop

[![Validate package](https://github.com/ayberkdt/metinoskop/actions/workflows/validate.yml/badge.svg)](https://github.com/ayberkdt/metinoskop/actions/workflows/validate.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-2e7d32)](LICENSE)
![Agent Skill](https://img.shields.io/badge/agent-skill-2563eb)
![Language: Türkçe](https://img.shields.io/badge/language-T%C3%BCrk%C3%A7e-c62828)

Metinoskop, yapay zekâ ajanının Türkçe metni yazarken ve düzenlerken uyduğu kuralları taşıyan bir skill'dir. Ajan her önermeyi bir kez, doğru yerde ve kaynağın verdiği kesinlikte yazar; olguları, sayıları, kanıt düzeyini ve yazarın tavrını korur. Zaten net ve doğal olan metni olduğu gibi bırakır.

Kurallar iki kaynağa dayanır. Netlik kuralları, havacılık belgeleri için geliştirilmiş ASD-STE100 (Simplified Technical English) standardının yazım ilkelerinden uyarlandı; standardın İngilizceye özgü sözlüğü ve fiil kısıtları alınmadı. AI metnini insan metniyle karşılaştıran on dört araştırmanın bulguları ve Türkçe karşılıkları [`references/insan-ve-yapay-metin.md`](references/insan-ve-yapay-metin.md) dosyasındadır. Öncelikli alan bilimsel ve teknik metindir.

## Örnekler

Her örnek bir vakadan alındı: sol sütun vakanın kaynağı, sağ sütun kayıtlı çıktısıdır. Kalın yerler değişen kısımlardır.

### Aynı ölçümü dört kez söylemek

`evals/dongusel-tanim.md`

| Kaynak | Kayıtlı çıktı |
|---|---|
| **Kalibrasyon, ölçüm sisteminin kalibre edilmesi işlemidir.** | *silindi* |
| Bu çalışmada kuvvet sensörü 12 referans ağırlıkla kalibre edildi **ve** doğrusallık hatası %0,8'den %0,2'ye indi. | Bu çalışmada kuvvet sensörü 12 referans ağırlıkla kalibre edildi**;** doğrusallık hatası %0,8'den %0,2'ye indi. |
| **Başka bir deyişle, kalibrasyondan sonra sensörün doğrusallık hatası azaldı.** | *silindi* |
| **Bu sonuç, kalibrasyonun ölçüm doğruluğu açısından kritik önemini açıkça ortaya koymaktadır.** | *silindi* |
| **Sonuç olarak, kalibrasyon sensörün doğrusallık hatasını düşürmektedir.** | *silindi* |

Birinci cümle terimi kendisiyle tanımlıyor. Son üç cümle aynı ölçümü açımlama, önem ve sonuç olarak yineliyor; sonuncusu tek bir ölçümü genel bir yasaya çeviriyor. Kalan cümlede bütün sayılar duruyor.

### Yapılmış işi kılavuz gibi anlatmak

`evals/raporda-genis-zaman-yigini.md`

| Kaynak | Kayıtlı çıktı |
|---|---|
| **Bu çalışmada** 12 Ağustos'ta toplanan 1.200 kayıt incele**nir**. | 12 Ağustos'ta toplanan 1.200 kayıt incele**ndi**. |
| Çalışma üç veri kümesi**ni kullanır**. Her kümeye aynı filtre uygula**nır** ve sonuçlar karşılaştırıl**ır**. | Üç veri kümesi **kullanıldı**; her kümeye aynı filtre uygula**ndı** ve sonuçlar karşılaştırıl**dı**. |
| Ortalama hata %4 olarak hesapla**nır**. | Ortalama hata %4 olarak hesapla**ndı**. |
| Yalnızca düşük yoğunluklu bölgelerde hata %6'ya **çıkar**. | Yalnızca düşük yoğunluklu bölgelerde hata %6'ya **çıktı**. |

Tarih ve ölçümler tamamlanmış bir işi bildiriyor, geniş zamanlı yüklemler ise genel bir prosedür anlatıyordu. Kayıtlı çıktı yüklemleri geçmişe alıyor; `Yalnızca` kapsam işareti yerinde kalıyor.

### İngilizce `have` iskeleti

`evals/sahip-olmak-kalkisi.md`

| Kaynak | Kayıtlı çıktı |
|---|---|
| Önerilen yöntem yüksek bir hesaplama maliyeti**ne sahiptir**. | Önerilen yöntem**in** hesaplama maliyeti **yüksektir**. |
| Model üç katman**a sahiptir** ve her katman 64 birim**e sahiptir**. | Model üç katman**lıdır**; her katman**da** 64 birim **bulunur**. |
| Cihaz IP67 koruma sınıfı**na sahiptir**. | Cihaz**ın** koruma sınıfı **IP67'dir**. |
| Sistem ayrıca bir hata günlüğü**ne sahiptir**. | Sistem ayrıca hata günlüğü **tutar**. |

Dört cümle de İngilizce `have` iskeletini taşıyordu; ilişki iyelik, sıfat ve yüklemle yeniden kuruldu. Aynı vakada gerçek mülkiyet (`şirketin sahip olduğu iki fabrika`) ve yükümlülük (`yönetici yetkisine sahip olmalıdır`) bildiren `sahip` korunuyor.

### Etiketle açılan cümle ve anons

`evals/etiket-ve-anons.md`

**Kaynak**

> **Kısa cevap:** İkisi farklı işler yapar.
>
> **Kavramsal ayrım:** Önbellek sık okunan veriyi saklar. Tampon ise veriyi iki bileşen arasında aktarırken geçici olarak tutar.
>
> **Sezgisel açıklama:** Aynı veri ikinci kez istendiğinde önbellek onu yeniden hesaplatmaz.
>
> **Detaylı açıklama:** Sistemimizde önbellek Redis üzerinde çalışır ve kayıtları 10 dakika tutar. Tampon, günlük yazıcısının önünde 4 MB'lık bir kuyruk olarak durur.
>
> Merak etmeyin, ikisini de yapılandırmak kolay. Bu yazıda ikisinin ayarlarını adım adım öğreneceksiniz.

**Kayıtlı çıktı**

> Önbellek sık okunan veriyi saklar; aynı veri ikinci kez istendiğinde onu yeniden hesaplatmaz. Tampon ise veriyi iki bileşen arasında aktarırken geçici olarak tutar.
>
> Sistemimizde önbellek Redis üzerinde çalışır ve kayıtları 10 dakika tutar. Tampon, günlük yazıcısının önünde 4 MB'lık bir kuyruk olarak durur.

Etiketler cümlenin türünü adlandırıyordu; ayrımı ve açıklamayı cümlelerin kendisi kuruyor. `Kısa cevap` cümlesi ayrım yazıldığında bilgi taşımadığı için silindi, öteki etiketlerin altındaki cümleler etiketsiz kaldı. Okura seslenen son paragraf da silindi.

### Konuşmayı görmemiş okura rapor

`evals/konusma-sizintisi-rapor.md`

**Kaynak**

> İstediğin gibi önbellek sorununu inceledim. Önce `cache.py` dosyasına baktım, sonra yük testini çalıştırdım. Verdiğin günlük dosyasına göre 14 Ekim'deki 37 zaman aşımının 29'u önbellek yenilemesiyle aynı dakikada oluştu. Burada sunucu saatlerinin senkron olduğunu varsaydım; bunu doğrulayamadım.
>
> Yenileme aralığını 5 dakikadan 15 dakikaya çıkarırsak zaman aşımları azalabilir. İstersen bir sonraki adımda bunu deneyebilirim ya da yük testini tekrarlayabiliriz. Umarım faydalı olur!

**Kayıtlı çıktı**

> `cache.py` incelendi ve yük testi çalıştırıldı. Günlük kayıtlarına göre 14 Ekim'deki 37 zaman aşımının 29'u önbellek yenilemesiyle aynı dakikada oluştu. Bu eşleşme, sunucu saatlerinin senkron olduğu varsayımına dayanır; varsayım doğrulanmadı.
>
> Yenileme aralığı 5 dakikadan 15 dakikaya çıkarılırsa zaman aşımları azalabilir.

Konuşmaya gönderme, çalışma sırası ve kullanıcıya teklif silindi. Taşıdıkları yöntem, varsayım ve doğrulanmamışlık okura yazıldı; `azalabilir` önerisi karara yükselmedi.

### Dokunulmayan cümleler

198 vakanın 79'unda doğru davranış hiçbir şeyi değiştirmemektir. Bu korunur vakalarının kayıtlı çıktısı kaynağın kendisidir ve doğrulayıcı bu eşitliği denetler. Aşağıdaki cümlelerin her biri bir korunur vakasının kaynağından alındı.

| Cümle | Vaka | Neden kalır |
|---|---|---|
| `RK4 her adımda türevi dört kez değerlendirir.` | `algoritma-genel-davranis-korunur` | Algoritmanın genel davranışı; makalede geçiyor diye geçmişe çevrilmez. |
| `Sıcaklık yükseldikçe direnç artar; bu ilişki 20 °C ile 80 °C arasında doğrusaldır.` | `bilimsel-genelleme-korunur` | Genel bilimsel ilişki; geçmişe çevrilirse tek seferlik gözleme iner. |
| `Bakımdan önce şalter kapatılır ve hattaki basınç boşaltılır.` | `prosedur-kilavuz-korunur` | Yeniden kullanılabilir güvenlik prosedürü. |
| `Filtre ölçümü 50 Hz'de alır. Gözlemci durumu günceller.` | `belirsizligi-onleyen-ozne-korunur` | İki aktör var; özne düşerse kimin ne yaptığı belirsizleşir. |
| `Kalman kazancının hesaplanması, yenilik kovaryansının tersinin alınmasını gerektirir.` | `teknik-adlastirma-korunur` | İki isim-fiil iki teknik işlemin adıdır. |
| `... iade etmeyi kabul ve taahhüt eder.` | `hukuki-formul-korunur` | Hukuki formül; sadeleştirmek hukuki etkiyi değiştirir. |
| `Model, baseline ile aynı pipeline üzerinde üç benchmark'ta değerlendirildi.` | `odunc-terim-korunur` | Alanın yerleşik ödünç terimleri. |
| `... ancak çalışma gözlemsel olduğundan nedensellik göstermemektedir.` | `akademik-paragraf-korunur` | Kanıt düzeyini bildiren çekince; AI izi değildir. |
| `Güneşsiz bir günde panel çıkışı 40 W'a düştü.` | `tetikleyici-iceren-sozcuk-korunur` | İçinde `eşsiz` dizisi geçiyor ama pazarlama dili değil. |
| `Başvurular her yıl 15 Ekim'de kapanır.` | `periyodik-takvim-genis-zaman-korunur` | Açık tarihle geniş zaman burada yinelenen bir takvim kuralıdır. |
| `14 Mayıs testinde basınç düşerken pompa hâlâ çalışıyordu.` | `gecmiste-surme-korunur` | Artalanda süren eylem; `çalıştı` onu bitmiş olaya çevirir. |
| `Hesaplamalar Dünya merkezli eylemsiz referans çerçevesinde yapıldı.` | `referans-cercevesi-korunur` | Fizik terimi; `framework` kalkısı değil. |
| `Uçuş test kampanyası 14 sortiden oluştu.` | `test-kampanyasi-korunur` | Havacılık terimi; `campaign` kalkısı değil. |
| `Denetleyici belleği 16 bitlik sayfalar hâlinde adresler.` | `bellek-adresleme-korunur` | `Adreslemek` burada gerçek teknik anlamında. |
| `Önceki sürümde istek zaman aşımı 30 saniyeydi; bu sürümde 60 saniyeye çıkarıldı.` | `sizinti-sanilan-icerik-korunur` | Sürüm notunun okuru önceki sürümü kullanmıştır; konuşma sızıntısı değil. |
| `Girdi: UTF-8 kodlamalı CSV dosyası.` | `alan-etiketi-korunur` | Belgenin alan etiketi; cümlenin türünü adlandırmıyor. |
| `Rapor, geçen ay konuştuğumuz gibi bayi bazında değil bölge bazında hazırlandı; ...` | `iyi-yazilmis-metin-korunur` | Okur yazışmanın tarafıdır; ortak geçmiş içeriktir. |

## Düzenleme kuralları

Kurallar çatıştığında kullanıcının açık talebi ve kapsamı önce gelir; onu kaynaktaki olgular ve yazarın tavrı, kullanıcının verdiği üslup örneği, metnin amacı ve okuru izler, skill'in dil tercihleri en sondadır. Alt sıradaki kural üst sıradakini bozmaz.

Ajan metni belge, paragraf, cümle ve sözcük katmanında birlikte okur: önce yukarıdan aşağı teşhis eder, her değişiklikten sonra bir üst katmanı yeniden okur. Doğru ama yanlış yerde duran cümleyi yeniden yazmaz, ait olduğu yere taşır. Teslimden önce son metindeki her sayı, tarih, nedensellik, karşılaştırma ve kapsam sözcüğünün kaynakta karşılığını arar.

### Netlik omurgası

Yedi kural ASD-STE100 yazım ilkelerinden uyarlandı ([`references/netlik-omurgasi.md`](references/netlik-omurgasi.md)):

1. Bir paragraf bir konu taşır; belgeye dağılmış konu tek yerde toplanır.
2. Her önerme bir kez söylenir; döngüsel tanım ve açımlama döngüsü kalkar.
3. Yalnızca gerekli bilgi yazılır: silindiğinde hiçbir önerme, ilişki ya da yazar tavrı kaybolmayan cümle çıkar.
4. Cümle bir ana önerme ya da bir ilişki taşır; talimatta bir cümle bir adımdır.
5. Bir kavramın tek adı olur; terim, tekrar olmasın diye eş anlamlıyla değişmez.
6. Aktör biliniyor ve okura bilgi veriyorsa somut özne ve somut yüklem kullanılır.
7. Başlık, paragraf ve liste okura hizmet eder; altında tek kısa paragraf olan başlık birleşir.

Sayısal eşikler (betimleyici cümlede 25 sözcük, paragrafta altı cümle) inceleme işaretidir, kesme kuralı değildir: tek ilişki taşıyan uzun cümle bölünmez.

### Değişmezler

Netlik kesinliği bozamaz. Kısaltırken, birleştirirken ya da somutlaştırırken ajan:

- Olumsuzluğu, istisnayı, koşulu ve `yalnızca`, `en az`, `henüz` gibi kapsam sözcüklerini korur; kaynaktaki sayılardan yeni oran ya da fark türetmez.
- Aktarımı olguya, ilişkiyi nedenselliğe, öneriyi karara, kararı uygulamaya çevirmez; `gözlenmedi` `yoktur` olmaz.
- Kanıt düzeyini bildiren çekinceyi korur; dayanağı olmayan `açıkça`, `tartışmasız` gibi pekiştiricileri kaldırır.
- Olumsuz bulguyu ve eleştiriyi yumuşatmaz (`başarısız oldu` → `beklenen düzeye ulaşamadı` olmaz).
- Tamamlanmış işi geçmişle anlatır; algoritmanın genel davranışını, bilimsel ilişkiyi, ürün belirtimini ve prosedürü geniş zamanda bırakır.
- Metne konuşmaya, talimata ya da çalışma sırasına gönderme bırakmaz; kullanıcıya soru gerekiyorsa metinden sonra `---` ile ayrılmış tek nottur.

### Sorunlar ve referans dosyaları

Ana kurallar `SKILL.md` dosyasındadır. Ajan `references/` altındaki katalogları yalnızca ilgili sorunu gördüğünde okur.

| Sorun | Ajan ne yapar | Referans |
|---|---|---|
| Önem cümlesi, savunma, döngüsel tekrar, kalıp giriş ve sonuç | Bilgi taşımayan cümleyi siler; silinen dolguyu daha sakin eş anlamlıyla geri koymaz. | `retorik-yapilar.md` |
| Etiketle açılan cümle, anons, eylem çağrısı | `Kavramsal ayrım:`, `Kısa cevap:` gibi etiketleri ve `Merak etmeyin`, `Hemen deneyin` gibi anonsları her türde siler; `Girdi:`, `Uyarı:` gibi alan etiketlerini korur. | `retorik-yapilar.md` |
| Fazla başlık, tek paragraflık bölüm, kısa paragraf yığını | Hak edilmemiş başlığı birleştirir; dergi kuralı, mevzuat, güvenlik adımı ve tekrarlanabilirlik için gereken ayrımı korur. | `yapisal-butunluk.md` |
| Kopuk paragraf, belirsiz gönderge | Devri ve göndergeyi onarır. | `akicilik.md` |
| Tekdüze bağlaç, yakın tekrar | İlişkiyi ek ve ilgeçle kurar (`-e rağmen`, `-dığından`, `-ken`); kaynağın kurmadığı ilişkiyi bağlaçla eklemez. | `turkce-baglayicilar.md` |
| Klişe, reklam dili, yapay ritim | Kalıbı siler ya da kaynağın somut bilgisiyle değiştirir. | `turkce-oruntuler.md` |
| Çeviri gibi okunan cümle | Yinelenen özneyi, `bu durum` paketini, `sahip olmak` ve `bulunmaktadır` kalıbını Türkçenin araçlarıyla yeniden kurar; alan terimini ve hukuki kalıbı korur. | `turkce-ritim-ve-ceviri-kokusu.md` |
| Kanıt statüsü, çekince, edilgen çatı | Her iddiayı kaynaktaki kişiye, statüye ve kesinliğe bağlı tutar. | `kanit-ve-kesinlik.md` |
| Zaman ve kip | Baskın zaman çizgisini bulur; `-yordu`, `-mıştı`, `-ardı` ilişkilerini ne düzleştirir ne uydurur. | `zamansal-ankraj-ve-rapor-kipi.md` |
| Tuhaf eşdizim, sözcüksel kalkı | `karar gerçekleştirmek`, `X hakkında odaklanmak` gibi birleşimleri düzeltir; `referans çerçevesi`, `hipotezi desteklemek` gibi yerleşik terimleri korur. | `sozcuk-birlesimleri.md` |
| Paragraflar bir düşünceyi geliştirmiyor | Desteksiz `bu nedenle`yi, kayan kapsam işaretini ve iddiasından uzak düşen sınırlılığı düzeltir; zaman sırasını nedenselliğe çevirmez. | `metinsel-tutarlilik.md` |
| Rapor, inceleme notu, yönetici özeti | Bulgu, yorum, öneri ve karar sınırını korur; yönetici özeti gövdede olmayan çıkarım üretmez. | `rapor-yazimi.md` |
| AI metnine özgü izler | Cümle sonu `-arak/-erek` kuyruğunu, biçem fiilini ve yumuşatılmış olumsuz bulguyu giderir; uzunluğu rastgeleleştirmez. | `insan-ve-yapay-metin.md` |
| Konuşma sızıntısı | Sızıntıyı siler, taşıdığı varsayımı ve yöntemi okura yazar. | `okura-dogrudan-metin.md` |
| İstenen kavramsal giriş | Kaynaktaki bağlamdan probleme, sorudan kavrama doğru bir akış kurar. | `kavramsal-girisler.md` |
| Hukuki, tanıtım, deneme, sosyal medya, kişisel ve edebî metin | Ek kurallar yalnızca metin o türdense okunur; istisnaları bilimsel metne taşımaz. | `kenar-turler.md` |

### Terimler

Bu terimler referans dosyalarında ve `style-lint.py` çıktısında geçer.

| Terim | Anlamı |
|---|---|
| Çeviri kokusu | Dil bilgisi doğru olduğu hâlde altında İngilizce bir cümle taşıyan Türkçe; sorun cümlenin kuruluşundadır. |
| Sözcüksel kalkı | Sözcükler Türkçe olduğu hâlde birleşme tercihinin İngilizceden taşınması: `iyileşme elde edildi` yerine `hata azaldı`. |
| Zamansal ankraj | Bir pasajın baskın zaman düzlemi: yapılmış iş, genel davranış, güncel durum ya da plan. |
| Zamansal sürtünme | Yüklemin genel davranış, çevresindeki metnin tamamlanmış olay bildirmesi: `12 Ağustos'ta ekip sistemi inceler`. |
| Kılavuz kokusu | Yapılmış işin geniş zamanla anlatılması yüzünden raporun kullanım kılavuzu gibi okunması. |
| Epistemik statü | Önermenin türü: gözlem, ölçüm, aktarım, çıkarım, tahmin, plan ya da yorum. |
| Sıfır bilgi cümlesi | Silindiğinde hiçbir önerme, ilişki ya da yazar görüşü kaybolmayan cümle. |
| Üretilmiş önem | Kaynağın gerekçelendirmediği "bu önemlidir" cümlesi. |
| Hafif fiil | Gerçek fiili bir adın arkasına saklayan yapı: `değerlendirme gerçekleştirmek` yerine `değerlendirmek`. |
| Eşdizim | Sözcüklerin birlikte kullanılma alışkanlığı: `karar almak` doğaldır, `karar gerçekleştirmek` değildir. |
| Etiket | Cümlenin türünü adlandıran giriş (`Sezgisel açıklama:`); belgenin dayattığı alan etiketinden (`Girdi:`) ayrıdır. |
| Anons | Okura seslenen duyuru, slogan ya da eylem çağrısı (`Merak etmeyin`, `Hemen deneyin`). |
| Korunur vakası | Doğru davranışın hiçbir şeyi değiştirmemek olduğu vaka; adı `-korunur` ile biter, kayıtlı çıktısı kaynağın kendisidir. |

## Kurulum

### Skills CLI

Desteklenen ajan ortamlarının hepsine kurmak için:

```bash
npx skills add ayberkdt/metinoskop --global
```

Kurulu sürümü güncellemek için:

```bash
npx skills update metinoskop --global
```

Yalnızca geçerli projeye kurmak için `--global` seçeneğini kaldırın. Kurulumdan sonra ajan oturumunu yenileyin ya da skill listesini yeniden yükleyin.

### Elle kurulum

Depoyu ajan ortamınızın skill dizinine klonlayın:

```bash
git clone https://github.com/ayberkdt/metinoskop.git /path/to/skills/metinoskop
```

Çalışma zamanında yüklenen dosya `SKILL.md`'dir; `references/` dosyaları gerektiğinde okunur. `agents/openai.yaml` destekleyen istemciler için arayüz bilgisini taşır.

## Kullanım

Metni verip ne istediğinizi kısaca yazın:

```text
Bu metni geliştir, çok AI slop gibi duruyor.

[metin]
```

Düzey, kapsam ya da ton belirtmeniz gerekmez. Ajan sorunları kendisi teşhis eder ve tek bir son metin verir; seçenek ya da alternatif sürüm sunmaz. Düzenleme kaynakta olmayan bir yorumu seçmeyi gerektirirse metni verir ve metinden sonra tek soru sorar. Skill'i adıyla çağırmak için `$metinoskop` yazın.

Açık talep varsayılanın önüne geçer: `Yalnızca dolguyu çıkar, cümle yapısına dokunma.` Metinoskop çeviri yapmaz; Türkçeye çevrilmiş metni düzenler.

### Müdahale düzeyi

| Düzey | Ne değişir |
|---|---|
| Hafif | Belirgin dolgu, konuşma sızıntısı, bölüm duyurusu, etiket, anons, üretilmiş önem ve anlamı değiştiren kalkı düzeltilir; cümle yapısı, paragraf sırası ve başlıklar kalır. |
| Standart (varsayılan) | Netlik omurgasının cümle ve paragraf kuralları ile Türkçe doğallık kuralları uygulanır; erken bölünmüş paragraflar birleşir, başlık hiyerarşisi kalır. |
| Derin | Bilgi sırası, paragraf ve bölüm yapısı kavramsal sınırlara göre yeniden kurulur; dergi şablonu, tekrarlanabilir deney bölümleri, güvenlik adımları ve numaralı göndermeler kalır. |

Düzeyi belirtmezseniz ajan standart düzeyde çalışır. Teşhis yapısal parçalanma gösterirse derin düzeyin yapı kurallarını yalnızca o bölümlere uygular.

### Odaklı talepler

| Amaç | Örnek talep |
|---|---|
| Rapor | `Bu raporu düzenle; bulgu, yorum, sınırlılık ve önerileri birbirine dönüştürme, tablo ve atıfları koru.` |
| Zaman ve kip | `Yapılan işi tamamlanmış olay olarak anlat; algoritmanın genel davranışını ve prosedürü geniş zamanda bırak.` |
| Retorik dolgu | `Bilgi taşımayan cümleleri ve bölüm duyurularını çıkar; yöntem gerekçelerini ve adlandırılmış sınırlılıkları koru.` |
| Yapı | `Derin düzeyde düzenle; hak edilmemiş başlıkları birleştir, numaralı göndermelerin gerektirdiği bölümleri koru.` |
| Çeviri kokusu | `Metin Türkçe düşünülmüş gibi okunsun; sayıları, terimleri ve kesinlik düzeyini koru.` |
| Kanıt düzeyi | `Her iddiayı kaynaktaki kanıt düzeyinde tut; çekinceleri koru, dayanaksız pekiştiricileri kaldır.` |
| Üslup eşleme | `Önce şu iki paragraftan üslubumu çıkar, sonra bu metni aynı resmiyet ve ritimle düzenle.` |

Üslup eşlemede yazım yanlışları ve tesadüfi tekrarlar üslup özelliği sayılmaz.

### Okura hazırlama ve teslim kapısı

Ajanın bir konuşma ya da `/goal` talimatı üzerine yazdığı rapor, konuşmayı görmemiş okura hazırlanabilir: `Bu raporu ekip liderine gönderilecek hâle getir.` Talepte verilen yeni bilgi (`pilot iptal edildi`) metne olgu olarak girer, `kullanıcının bildirdiğine göre` diye değil.

Son metni iki komut denetler:

```bash
python scripts/style-lint.py rapor.md --son-okur
python scripts/style-lint.py rapor.md --teslim
```

`--son-okur` tek bir konuşma sızıntısı adayı kalsa bile 1 ile çıkar. `--teslim` etiketle açılan cümleyi ya da anonsu konumuyla listeler ve 1 ile çıkar; alan etiketini ve `---` sonrası notu engellemez. Listede olmayan bir etiket biçimi (`Öğretmen gözüyle:`) kapıyı durdurmaz, `etiket adayı` uyarısı olarak listelenir.

### İsteğe bağlı kavramsal giriş

Açıkça istenirse ajan, verilen kaynak bilgilerden bir kavrama kısa giriş yazar: okurun bildiği bağlam, kavramı gerekli kılan problem, cevaplanacak soru ve cevap olarak kavram. Kaynakta problem yoksa problem uydurulmaz. Ajan bu kipe kendiliğinden geçmez.

```text
$metinoskop

Önbellek kavramını tanıtan kısa bir giriş yaz. Yeni risk ya da fayda ekleme.

[kaynak bilgiler]
```

## Kapsam ve sınırlar

Ajan şunları yapmaz:

- Olgu doğrulamak, kaynakta olmayan bilgi üretmek ya da sayılardan yeni sayı türetmek.
- Kaynak dilden Türkçeye çeviri yapmak.
- Birden fazla makul yorumu olan ifadede yorum seçmek.
- Anlatıda olay sırasını, sahne yapısını ya da bakış açısını değiştirmek.
- Hukuki, akademik ya da teknik terminolojiyi gündelikleştirmek.
- Bilgi taşıyan cümleyi kısalık için kesmek; yeni başlayana yazılmış açıklamayı, benzetmeyi ya da örneği silmek.
- Metni "insanileştirmek" için hata, argo, rastgelelik ya da uzunluk gürültüsü eklemek; metnin bir AI dedektöründen geçeceğini vaat etmek.
- Metne kullanıcıya yönelik not, soru, teklif ya da değişiklik açıklaması koymak.

Hukuki, tanıtım, deneme, sosyal medya, kişisel ve edebî metin desteklenir; bu türlerin kuralları ana dosyada değil, yalnızca o türde okunan `references/kenar-turler.md` dosyasındadır.

## Depo yapısı

```text
metinoskop/
├── SKILL.md                    Her çağrıda yüklenen kurallar
├── references/                 İlgili sorun görülünce okunan 16 katalog
├── evals/                      198 davranış vakası: 79 korunur, 119 dönüşüm
│   ├── outputs/                Her vakanın kayıtlı çıktısı
│   ├── critical-cases.txt      Canlı regresyondaki 36 kritik vaka
│   └── README.md               Vaka grupları, hakem ölçütleri, ölçüm sonuçları
├── scripts/
│   ├── validate-package.py
│   ├── eval-runner.py
│   ├── eval-suite.py
│   ├── style-lint.py
│   ├── behavioral-regression.py
│   ├── research-profile.py
│   ├── ab-score.py
│   ├── ab-case-score.py
│   └── ab-gorevler/            Kör A/B görev setleri
├── agents/openai.yaml          İstemci arayüz bilgisi
├── assets/banner.svg
├── .github/workflows/          validate.yml, behavioral.yml
├── AGENTS.md                   Bakım sözleşmesi
├── CHANGELOG.md
├── LICENSE
├── NOTICE
└── README.md
```

## Geliştirme ve doğrulama

Bu denetimler bağımlılık gerektirmez. GitHub Actions (`validate.yml`) hepsini `main` dalına her gönderimde ve her pull request'te çalıştırır:

```bash
python scripts/validate-package.py
python scripts/eval-runner.py --self-test
python scripts/style-lint.py --self-test
python scripts/eval-suite.py --require-all
npx --yes skills@1.5.20 add . --list
```

| Betik | Ne denetler |
|---|---|
| `scripts/validate-package.py` | Paket yapısını, `SKILL.md` bütçesini (300 satır, 34 KB) ve başlıklarını, vaka biçimini, korunur vakalarında kayıtlı çıktının kaynağa eşitliğini ve lisansı. |
| `scripts/eval-runner.py VAKA ÇIKTI` | Kaynaktaki sayı, tarih, URL, kod, dipnot, kapsam sözcüğü ve terimlerin çıktıda korunduğunu; çıktıya kaynakta olmayan olumsuzluk, çekince, nedensellik, pekiştirici, karşılaştırma, tümel nicelik, zorunluluk ya da gelecek işareti eklenmediğini. Akıcılığa ve tona hakem karar verir. |
| `scripts/eval-suite.py` | Bütün kayıtlı çıktıları değişmez, sert kalıp ve yapısal beklenti açısından. `--export-judge-prompts DIR` her vaka için model hakem istemi yazar. |
| `scripts/style-lint.py METİN` | Retorik, yapı, netlik, çeviri kokusu ve söylem bulgularını inceleme işareti olarak listeler; tek bir işaret metni reddetmez. `--source` kaynakta olmayıp çıktıda beliren kalıpları ayırır; `--fail-on-introduced-hard` sert aile, `--fail-on-introduced-any` herhangi bir aile eklendiyse 1 ile çıkar. |
| `scripts/behavioral-regression.py` | Kritik vakaları gerçek modelde taze üretip deterministik denetimden ve model hakeminden geçirir. `ANTHROPIC_API_KEY` ister ve her çalıştırma ücretlidir; `--dry-run` API çağırmadan planı yazar. `behavioral.yml` haftalık ve elle çalıştırır, raporlar `build/behavioral/` altına yazılır. |
| `scripts/research-profile.py` | Kayıtlı çıktıları kaynaklarına karşı AI–insan metni farklarıyla ölçer; `--list` iz taşıyan çıktıları listeler. |
| `scripts/ab-score.py`, `scripts/ab-case-score.py` | Skill sürümlerini kör A/B ile karşılaştırır. Görev setleri `scripts/ab-gorevler/` altında, yöntem ve sonuçlar `evals/README.md` › Kör A/B ölçümü bölümündedir. |

Tek bir çıktıyı denetlemek için:

```bash
python scripts/eval-runner.py evals/teknik-gosterim-korunur.md cikti.txt
python scripts/style-lint.py cikti.txt --source evals/iddia-tekrar-dongusu.md
```

### Vaka biçimi

Her vaka korunması gereken olguları, kesinliği ve biçimi, ayrıca kaçınılması gereken davranışları tanımlar; tek bir doğru çıktı dayatmaz. Dönüşüm vakaları cümle sayısını üst sınırla verir (`cümle: <= 4`), çünkü önermeleri farklı gruplayan bir düzenleme de geçerlidir. Kesin sayı yalnızca korunur vakalarında ve talebin yapı dayattığı vakada yazılır. Doğrulayıcı bu ayrımı ve korunur vakalarının `-korunur` adını denetler.

## Sürümleme

Proje anlamsal sürümlemeyi izler. Son sürüm etiketi `v0.4.1`'dir; sonraki değişiklikler [CHANGELOG.md](CHANGELOG.md) dosyasının `Unreleased` bölümünde birikir.

## Katkı

Hata örneklerini ve önerileri [GitHub Issues](https://github.com/ayberkdt/metinoskop/issues) üzerinden paylaşabilirsiniz. Davranışı değiştiren pull request'te `SKILL.md`, README ve ilgili vakalar birbiriyle uyumlu kalmalıdır; bakım kuralları [AGENTS.md](AGENTS.md) dosyasındadır.

## Lisans ve atıf

Metinoskop, Creative Commons Atıf 4.0 Uluslararası (CC BY 4.0) lisansıyla dağıtılır. Kopyalayabilir, dağıtabilir, uyarlayabilir ve ticari olarak kullanabilirsiniz. Tek şart atıftır: eseri kullandığınız ya da uyarladığınız her yerde kaynağı makul biçimde belirtin ve değişiklik yaptıysanız bunu söyleyin.

Atıf için şu satırı kullanabilirsiniz:

```text
"Metinoskop" (Ayberk Demirkanat, https://github.com/ayberkdt/metinoskop), CC BY 4.0
```

Skill'i bir ajan ürününe gömüyorsanız bu satırı skill listesinde, dokümantasyonda ya da ürünün künye bölümünde görünür tutun. Atıf, lisans verenin sizi ya da kullanımınızı onayladığı izlenimini veremez.

Lisansın tam metni [LICENSE](LICENSE), telif ve atıf ayrıntısı [NOTICE](NOTICE) dosyasındadır.
