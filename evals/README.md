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
| `kisa-paragraf-yigini` | Erken bölünmüş tek cümlelik paragrafları tek harekete toplamak |
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

## Hakem ölçütleri

İnsan veya model hakemi her çıktıda şu soruları ayrıca sorar:

1. **Sıfır bilgi cümlesi:** Çıktıda, silindiğinde hiçbir önerme, ilişki, kronoloji, yorum veya yazar tavrı kaybolmayacak cümle kaldı mı?
2. **İşlev tekrarı:** Sözcükleri farklı ama işlevi aynı cümleler (önem bildirme, yeniden ifade, mini sonuç) tekrarlanıyor mu?
3. **Savunmacı düzyazı:** Somut bir yanlış anlamayı önlemeyen savunma cümlesi kaldı mı? Dayanaklı yöntem gerekçesi yanlışlıkla silindi mi?
4. **Dolguyu dolguya çevirme:** Silinmesi gereken önem, karşıtlık, duyuru veya denge cümlesi daha sakin eş anlamlılarla geri konmuş mu?
5. **Paragraf ve belge mimarisi:** Paragraflar tek biçimli mi? Her paragraf önem cümlesiyle mi bitiyor? Giriş ve sonuç kalıp mı? Uzunluklar insan gibi görünsün diye rastgeleleştirilmiş mi?
6. **Muhatap duyarlılığı:** Uzman metninde açık olanın açıklaması kaldı mı? Yeni başlayan metninden öğretici açıklama silindi mi?
7. **Koruma:** Kesinlik düzeyi, kapsam, adlandırılmış sınırlılık, atıf, biçim ve yazar sesi korunmuş mu? Metin gündelikleşmiş veya telgraf diline dönmüş mü?
8. **Başlık ve bölüm sınırları:** Her başlık hakkını kazanıyor mu; tek paragraflık bölümler, gereksiz derinlik veya "başlık → kısa açıklama" slayt deseni kaldı mı? Kullanıcının istediği düzey aşılarak başlıklar değiştirilmiş mi? Tekrarlanabilirlik, mevzuat, dergi kuralı, güvenlik adımları veya gezinme gerektiren bölümler korunmuş mu?
9. **Paragraf ve yakınlık:** Paragraflar erken bölünmüş mü, tek hareket taşıyan uzun paragraf bölünmüş mü, işlevsel kısa paragraf birleştirilmiş mi? Sonuç ile sınırlılığı, iddia ile kanıtı, yöntem ile gerekçesi yakın mı? Bağlam her birimde yeniden başlatılıyor mu; çapraz gönderme, askı, yapay gerilim, boş sarmalayıcı veya zorlama geçiş kaldı mı?
10. **Parçalanma ve şişkinlik dengesi:** Uzun çerçeve ifadeleri kısaltılmış mı; birleştirme tek cümleye birkaç iddia, niteleme ve sonuç yığmış mı; nedensel akıl yürütme listeye çevrilmiş mi? Değişiklik yalnızca kısaltma mı, yoksa süreklilik, anlama, gezinme veya yakınlık kazancı mı sağlıyor?

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

`scripts/style-lint.py` üretilmiş önem, savunmacı açıklama, yol haritası, kalıp giriş ve sonuç, üretilmiş karşıtlık, zorlama denge, soyut yüklem, boş özne ve sohbet botu kalıntısı ailelerini işaretler; paragraf uzunluğu tek biçimliliği, önem cümlesiyle kapanış oranı, `-maktadır` zinciri ve işlev tekrarı gibi yapı bulgularını raporlar. `--source` verildiğinde kaynakta olmayıp çıktıda beliren kalıpları kalıp düzeyinde ayrıca listeler; aynı aileden farklı bir kalıp da yeni sayılır. Bu, dolgunun başka dolguya çevrildiğine ilişkin güçlü bir deterministik işarettir; kaynakta olup çıktıda kalan sert aileler ise hakemin silme testiyle incelemesi için listelenir. `--fail-on-introduced` ile yalnızca yeni kalıp durumunda başarısız çıkış kodu verir. Rapor ayrıca parçalanma yoğunluğunu (başlık sayısı ve derinliği, başlık başına paragraf, tek paragraflık bölüm, kısa paragraf oranı, liste ögesi, çapraz gönderme) özetler ve `--source` ile bu ölçülerdeki değişimi gösterir; `korunacak-basliklar` veya `yontem-ayrimi` gibi vakalarda başlık sayısının düşmesi hata işaretidir, `asiri-bolumleme` gibi vakalarda beklenen sonuçtur.

Denetim tek bir sözcüğe bakarak metni reddetmez. `gerekli-ifade` ve `iyi-metin` vakalarında işaretlenen ifadelerin çoğu kalmalıdır; işaret, hakemin işlevi incelemesi içindir.

Rapor vakalarında ayrıca bulgu, yorum, sınırlılık, öneri ve karar statülerinin korunup korunmadığını; tablo, başlık ve çapraz göndermelerin doğru içeriğe bağlı kalıp kalmadığını inceleyin. Bu ilişkiler yalnızca sözcük varlığıyla güvenilir biçimde ölçülemediği için değerlendirme insan veya model hakemi gerektirir.
