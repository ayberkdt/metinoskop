# AGENTS.md

Bu depo `metinoskop` agent skill'ini içerir: Türkçe metni kaynak sadakatini, kanıt statüsünü ve okuru koruyarak netleştirir.

## Dosyalar

- `SKILL.md`: her çağrıda yüklenen sözleşme; yalnızca karar noktaları.
- `references/`: gerektiğinde okunan kataloglar. `insan-ve-yapay-metin.md` AI–insan metni araştırmalarının bulgularını, güven düzeyini ve Türkçe karşılığını tutar; yeni bir "AI izi" kuralı oraya kaynağıyla girer. Hangi belirtide hangisinin okunacağı `SKILL.md` › Referans yönlendirmesi'ndedir; `kenar-turler.md` yalnızca o türlerde okunur.
- `evals/`: davranış vakaları (`## Kaynak`, `## Talep`, `## Korunması gerekenler`, `## Kaçınılması gerekenler`, isteğe bağlı `## Yapısal beklenti`, `## Serbest değişmezler` ve `## Serbest eklemeler`), `evals/outputs/` altındaki gold çıktılar ve 15–36 vakalık canlı regresyon seti `critical-cases.txt`. Gruplar ve vaka adları `evals/README.md`'dedir.
- `scripts/validate-package.py`: paket yapısı, `SKILL.md` bütçesi ve başlık pinleri, eval bölümleri ve işaretleri, lisans.
- `scripts/eval-runner.py`: çıktıda kaynak değişmezlerinin (sayı, tarih, kod, kapsam sözcüğü) korunduğunu ve kaynakta olmayan epistemik işaretin (olumsuzluk, çekince, nedensellik, pekiştirici, karşılaştırma, tümel nicelik, zorunluluk, gelecek) eklenmediğini denetler.
- `scripts/style-lint.py`: retorik, yapı, netlik, çeviri kokusu, söylem ve konuşma sızıntısı bulgularını inceleme işareti olarak raporlar; `--source` yeni eklenen kalıpları sert/bağlamsal ayırır, `--son-okur` sızıntı adaylarını sert sayar.
- `scripts/eval-suite.py`: gold çıktıları değişmez, sert kalıp ve yapısal beklenti açısından denetler (CI: `--require-all`).
- `scripts/behavioral-regression.py`: kritik vakaları gerçek modelde taze üretip deterministik denetimden ve model hakeminden geçirir; `.github/workflows/behavioral.yml` haftalık çalıştırır.
- `agents/openai.yaml`: istemci metadata'sı. `LICENSE` CC BY 4.0, `NOTICE` atıf biçimi; lisans değişirse README rozeti, `## Lisans ve atıf` ve doğrulayıcının lisans denetimi birlikte değişir.

## Bakım sözleşmesi

### Paket ve SKILL.md

- Ad her yüzeyde `metinoskop`, açık çağrı `$metinoskop`. Frontmatter'da yalnızca `name` ve `description`; `description` katalog değil tetikleyicidir.
- `SKILL.md` dikkat bütçesine tabidir: doğrulayıcı 300 satır, 34 KB ve 900 karakterlik frontmatter sınırı koyar (60 KB → 40 KB → 34 KB). Yeni kural için ana dosyaya "ne zaman fark et → hangi kararı ver → neyi bozma" düzeyinde birkaç cümle yazın; ayrıntı, örnek ve karşı örnek referansa gider. Bir kuralı ikinci bir bölümde yeniden anlatmayın, bölüm adıyla gönderin.
- `SKILL.md` kendi yapı kuralına uyar: dördüncü düzey başlık yok, her küçük kavrama `###` açılmaz, ilişkili kurallar kalın başlangıçlı paragraflardır. Doğrulayıcı başlıkları sabitler; başlık değişirse pin listesi de değişir.
- Yeni davranış kuralı yedi netlik kuralından birine ya da değişmezlere (kaynak sadakati, kanıt statüsü, zamansal ankraj, okura doğrudan metin) bağlanır; bağlanamıyorsa önce gerekliliğini sorgulayın. Netlik kuralı kesinliği, kapsamı ya da kanıt statüsünü değiştiremez.
- STE100'den yalnızca yazım ilkeleri alınır; sözlük ve İngilizce fiil kısıtları alınmaz. STE alıntısı resmî metinden doğrulanmalıdır; `netlik-omurgasi.md` bugün ikincil kaynağa dayandığını söyler. Sayısal eşikler kesme kuralı değildir.
- Tür özelindeki kurallar (hukuki kalıp, ikna, görüş ambalajı, yazara özgü imge, kişisel eksilti, üslup eşleme) `kenar-turler.md`'ye gider; doğrulayıcı birkaçını `SKILL.md`'de yakalar. Kenar tür vakaları kritik sete girmez; kritik set bilimsel-teknik davranışı ve netlik omurgasını korur.
- Yeni örüntünün yeri: sözcük ve kalıp `turkce-oruntuler.md`; cümle, paragraf, belge `retorik-yapilar.md`; İngilizce iskelet `turkce-ritim-ve-ceviri-kokusu.md`; kanıt ve kip `kanit-ve-kesinlik.md`; eşdizim `sozcuk-birlesimleri.md`; konu ilerleyişi ve bağlaç geçerliliği `metinsel-tutarlilik.md`; ankraj seçimi `zamansal-ankraj-ve-rapor-kipi.md`; konuşma sızıntısı `okura-dogrudan-metin.md`. Retorik dolguyu eşdizimden, yapısal sınırı söylem tutarlılığından, ankraj seçimini ankraj içi kip tutarlılığından ayrı tutun.
- Kapsam Türkçeye çevrilmiş metni düzenlemektir; çeviri yapacak biçimde genişletmeyin. Kavramsal giriş yalnızca açık istekle devreye girer. Skill'i belirli bir agent ürününe bağlamayın; ürün metadata'sı `agents/` altındadır.
- Davranış değişince README'yi, ilgili eval'i ve `CHANGELOG.md`'yi güncelleyin.

### Davranış sözleşmesi

- Varsayılan çağrı kısa taleptir: "geliştir", "AI slop gibi" dendiğinde ajan düzey, kapsam ya da ton sormaz, seçenek sunmaz, tek metin verir. Soru yalnızca yorum seçimi gerektiğinde, metnin dışında sorulur. `SKILL.md`'ye kullanıcıya seçim yaptıran adım eklemeyin.
- Skill iki kipte çalışır: ajanın kullanıcı isteğinden metin **yazması** ve verilen metni **düzenlemesi**. Yazma kipinde kaynak kullanıcının verdiği bilgidir; kurallar ilk taslakta uygulanır, eksik bilgi uydurulmaz, yer tutucu konmaz. Bir kuralı yalnızca düzenleme diliyle yazmayın.
- "AI izi" kuralı ölçülmüş bir farka dayanır ve `insan-ve-yapay-metin.md`'de kaynağıyla durur. İngilizce bulgunun Türkçe karşılığı çıkarımdır; depo vakasıyla sınanmadan sert denetime dönüşmez. Değişkenliği rastgelelikle, çeşitliliği eş anlamlı döndürmeyle üreten kural eklemeyin; cümle uzunluğu değişkenliği eşiği iyi Türkçe metni işaretlediği için denetime konmadı.
- Düzenleme bütüncüldür. Cümle düzeyinde kural eklerken paragraf ölçeğinde neyi bozabileceğini (devir, yakın tekrar, gönderge, rol sırası) da yazın. Yanlış yerdeki doğru cümle taşınır, yeniden yazılmaz.
- Metin konuşmayı görmemiş son okura gider. Açık talep kapsamı ve okuru belirler, olgu uydurma izni vermez; talepte verilen bilgi kaynağın parçasıdır. Anlam kalkısı ve konuşma sızıntısı her düzeyde düzeltilir; kapsam açıkça daraltıldıysa dokunulmaz, metnin dışında bildirilir. `---` sonrası not kanalı tek soru ve gerektiği zamanla sınırlıdır.

### Örnek ve gold yazımı

Her örnekte: "sonra" sürümündeki her önermenin "önce"de karşılığı vardır; hedeflenen ilke görünür biçimde uygulanır (noktalama ya da tek bağlaç değişikliği yetmez); kaynakta olmayan olgu, tarih, sayı, alıntı, nedensellik, aktör ya da kişisel ayrıntı eklenmez; olumsuzluk, koşul, istisna, nicelik sınırı ve kapsam belirleyicisi dolgu gibi silinmez; terim, kısaltma, sembol, birim, denklem numarası ve büyük-küçük harf korunur; belirsizlik korunabiliyorsa korunur, gönderge açıklaştırılırken cevap uydurulmaz; silinen dolgu daha sakin eş anlamlıyla geri gelmez; cümle silen örnek, silinen her cümlenin önerme taşımadığını açıklamada gösterir. Aileye göre ek yasaklar:

- **Netlik ve yapı:** tek ilişkili uzun cümleyi ya da tek hareketli uzun paragrafı bölmeyin (`dogal-uzun-cumle-korunur`, `uzun-paragraf-korunur`); bölümü sayıyı azaltmak için birleştirmeyin; tekrarlanabilirlik, mevzuat, dergi kuralı ve güvenlik adımlarının gerektirdiği ayrımı kaldırmayın; her birleştirmenin dayandığı kavramsal sınırı gösterin.
- **Retorik:** yeni kalıp sözcük yasağı olarak değil, işlev ailesi olarak eklenir. Adlandırılmış sınırlılığı, ölçülmüş yöntem gerekçesini, yazar değerlendirmesini ve öğretici açıklamayı silmeyin. Görüş koruma hazır ambalajı korumanın gerekçesi değildir: görüşün önermesi ve gücü kalır; imge, formül, üçlü ve vecize gider. İmgeyi yumuşatan (`adeta bir pencere` → `bir pencere gibidir`), görüşü öneriye çeviren ya da yazara özgü imgeyi silen örnek yok.
- **Bağlayıcı:** kaynakta kurulmamış ilişkiyi bağlayıcıyla kuran (`sayesinde`, `-e rağmen`, `dolayısıyla`, `nitekim`), zaman sırasını nedenselliğe çeviren, gündelik kaynağı resmîleştiren ya da teknik metne mecazlı çerçeve (`merceği altında`) sokan örnek yok. Yakın tekrar terimi kapsamaz; terimi eş anlamlıyla değiştiren örnek yok.
- **Çeviri kokusu:** kara liste değildir; `bir`, `olan`, `ve`, `açısından`, `sahip`, `bulunmaktadır` tek başına işaret değildir ve her ailenin kalması gereken karşı örneği vardır. Kesinliği güçlendiren fiil (`ilişkili` → `neden olur`), öz Türkçe hevesiyle terim değişimi, tek yükleme dört beş fiilimsi, iki aktörlü paragrafta özne düşürme ve yapay yerlilik (arkaik sözcük, konuşma edatı, gereksiz devriklik) yok. Türe göre davranış (akademik adlaştırma, teknik özne tekrarı, hukuki kalıp, kişisel eksilti) korunur.
- **Kanıt:** aktarımı olguya, çıkarımı ölçüme, ilişkiyi nedenselliğe, öneriyi karara, kararı uygulamaya, `gözlenmedi`yi `yoktur`a çeviren; aktör uyduran; çekinceyi "AI gibi" diye silen ya da ölçümle desteklenen iddiaya çekince ekleyen; kipleri üslup için nöbetleştiren örnek yok. Raporda bulgu–yorum–öneri–karar sınırı ve tablo, atıf, dipnot, çapraz gönderme korunur; yönetici özeti gövdede olmayan çıkarım, fayda, risk ya da eylem üretmez.
- **Eşdizim ve kalkı:** yeni kalkı ailesi dönüşüm ve korunur vakasıyla birlikte eklenir. Karar birimi sözcük + tümleç + bağlam + tür + alandır; tek sözcük yasağı yok. Alan terminolojisi denetlenmeden teknik birleşim değişmez; derlem sıklığı tek başına norm değildir, genel ve alan derlemi ayrı değerlendirilir. Daha doğal fiil epistemik gücü artırmaz (`ilişkili` → `etkiliyor` yok). Kalkıyı kaldırırken yeni tuhaf eşdizim üretmeyin ve anlamın yönünü denetleyin (`hata oranı azaldı`, `iyileşti` değil; `operatöre görünürlük sağladı` ≠ `operatörün görünürlüğünü artırdı`). Hâl değişimiyle ilişkiyi değiştiren, teknik terimi ya da hukuki formülü "doğallaştıran", seyrek ama kesin birleşimi genelleştiren, süreç adını yalın fiile çeviren örnek yok. Anlam kalkısı (`bulgular ... önermektedir`, `deney ... yer aldı`, p değerli `önemli fark`) doğallık kalkısından ayrıdır: her düzeyde düzeltilir ama sözcük yasağı değildir; her örnekle doğru kullanımı da ekleyin. Düzeltme statüyü yükseltmez (`düşündürüyor`, `gösteriyor` değil), test yoksa `anlamlı` yazılmaz, öznesiz `-dığı tartışılmaktadır` için anlam seçilmez.
- **Tutarlılık:** kronolojiyi nedenselliğe çeviren, eksik öncül uyduran, kapsam işaretini ya da olumsuzluğu başka ögeye bağlayan, gerekli yinelemeyi silen, bilinçli kayıt değişimini düzleştiren ya da ondalık listedeki noktalı virgülü kaldıran örnek yok.
- **Zamansal ankraj:** algoritma tanımını, genel ilişkiyi, ürün belirtimini, yeniden kullanılabilir prosedürü ya da belgenin güncel işlevini geçmişe çeviren; tek gözlemi geniş zamanla genel yasaya, genel ilişkiyi tek seferlik olaya çeviren; planı tamamlanmış işleme dönüştüren; bütün yüklemleri `-dı` ya da `-mıştır` zincirine indiren örnek yok. Geniş zaman "profesyonel", `-yor` "gündelik" varsayılan değildir; karar göndergeye bakar. Yeni zamansal davranışa dönüşüm ve koruma vakası birlikte eklenir.
- **İnsan ritmi:** virgülden sonra `-arak/-erek` ile biten cümle bırakan ya da yüklemden önceki doğal zarf-fiili (`alarak denetledi`) kuyruk sanıp bölen örnek yok. Kuyruğu ayrı cümleye çevirirken kaynakta ilişkilendirilmemiş iki ölçümü tek özneye bağlamayın. Olumsuz bulguyu yumuşatan, çekinceyi AI izi diye silen ya da tek ilişkili uzun cümleyi uzunluk için bölen örnek yok.
- **Okura doğrudan metin:** konuşmaya, talimata, taslağa ya da çalışma sırasına gönderen, kullanıcıya teklif yapan ya da metne not koyan örnek yok. Sızıntıyı silerken varsayımı, `doğrulanmadı`yı, çekinceyi ya da yöntemi silen, `yapabiliriz`i öneriye ya da karara yükselten, `biz` yerine aktör yazan örnek de yok. Okurun tarafı olduğu yazışma, kurumsal yanıtta `talebiniz doğrultusunda`, sürüm notunda önceki sürüm, gereksinim metninde ürünün kullanıcısı ve dil modeli metninde `istem` içeriktir.

### Eval'ler

- Her vakanın `evals/outputs/<vaka>.txt` gold çıktısı vardır. Gold bir sözleşmedir: kaydetmeden önce her iddianın statüsünü kaynakla karşılaştırın; rastgele atanmamış grup farkını nedensel fiille yazan, şişmiş iddiayı indirirken olumsuz iddia ya da çekince ekleyen, statüyü (süreç → karar, öneri → uygulama) kaydıran gold kabul edilmez. Kaynaktaki dolgunun silinmesi değişmez denetimine takılırsa `## Serbest değişmezler`de, gerekçeli bir epistemik ekleme (kalkı düzeltmesi, planın gelecek kipe taşınması) eklenen işaret denetimine takılırsa `## Serbest eklemeler`de gerekçesiyle muaf tutun; çıktıyı bükmeyin, muafiyeti gerekçesiz yazmayın. Eklenen işaret ailesi genişletilirken bütün gold'larda yeni bulgu sayısı ölçülür ve aile içi dönüşüm (`Sonuç olarak` → `Dolayısıyla`) ekleme sayılmaz.
- Korunur vakasının gold'u kaynağın kendisidir ve doğrulayıcının `SHOULD_REMAIN_CASES` listesinde durur; orada kesin cümle sayısı meşrudur. Dönüşüm vakasında `- cümle: <= N` yazın; vakanın talebi yapı dayatıyorsa `- cümle: = N`.
- Davranış değişince ilgili grubun dönüşüm ve korunur vakalarını birlikte güncelleyin; tek yönlü ekleme sistemi tek yöne kaydırır.
- Yanlış pozitif bekçileri; sezgiseli sıkılaştırırken bozmayın: `periyodik-takvim-genis-zaman-korunur` (yinelenen takvim kuralı iki zamansal sinyali de yakar ve doğrudur), `sizinti-sanilan-icerik-korunur`, `iyi-metin`, `anlam-kalkisi-korunur`, `dogal-baglayici-korunur`, `degisiklik-butcesi`.

### Stil denetimi

- Aile eklerken öz sınamadaki yapay ve temiz metinleri güncelleyin; temiz metin sert ailede işaret üretmez. Kalıplar sözcük sınırına saygı gösterir (`eşsiz` ⊂ `güneşsiz`); yeni kalıbı `\b` ile başlatıp `INNOCENT_WORDS`'e karşı sınayın.
- Bağlamsal aileyi `sert`e taşımayın; `--fail-on-introduced-hard` yalnızca sert aileler için hata verir. Çeviri kokusu (`sahip`, `varlik`, `kalki`, `ceviri`), söylem (`kiplik`, `pekistirici`, `aktarim`, `hafif_fiil`, `soylem`), zamansal (`zamansal_surtunme`, `genis_zaman_doygunlugu`), `mecaz`, `sus`, `kuyruk` ve `sizinti` bağlamsaldır; `sizinti`yi yalnızca `--son-okur` sert sayar. Anlam kalkısında yalnızca veri öznesi + `-dığını önermek` serttir. Yeni sezgiselden sonra yerli, temiz, iyi yapılı ve iç içe öz sınama metinleri sıfır bulgu üretmeye devam etmelidir.
- Dar sezgiseller: `yakin_tekrar` kapalı bir bağlaç, genel fiil ve değerlendirme sıfatı listesine bakar, listeye terim olabilecek sözcük girmez (`NEAR_REPEAT_INNOCENT`), bilinçli paralellik bulgu üretebilir. `dongusel_tekrar` en az üç ortak kök ve 0,5 Jaccard ister; eşik değişince bütün gold'larda yeni bulgu sayısı ölçülür. `sozcuksel_kalki` yalnızca birleşim düzeyinde aday üretir (`referans çerçevesinde`, `belleği adresler`, `erişim sağlamaktadır` korunur). `genis_zaman_katiligi` yalnızca güncel gönderge + betimleyici yüklemde, `genis_zaman_doygunlugu` yalnızca tamamlanmış iş çıpası varken çalışır.
- Sezgisele yapabileceğinden fazlasını vaat eden ad vermeyin. `tense_class` biçim bilgiseldir: `inceler`/`uygular`ı çoğul addan, `üretir`i `-tır` koşacından, `yapardı`yı `sardı`dan ayıramaz; hakem karar verir.

## Değişiklik öncesi kontroller

```bash
python scripts/validate-package.py
python scripts/eval-runner.py --self-test
python scripts/style-lint.py --self-test
python scripts/eval-suite.py --require-all
python scripts/behavioral-regression.py --dry-run
npx --yes skills@1.5.20 add . --list
```

Davranışı değiştiren değişiklikten sonra, API anahtarı varsa `python scripts/behavioral-regression.py` ile kritik vakaları gerçek modelde çalıştırın; CI bunu haftalık yapar. Doğrulama başarısızsa commit oluşturmayın. Yeni ya da değişmiş örnekleri kaynak sadakati ve örtük nedensellik açısından ayrıca elle inceleyin.
