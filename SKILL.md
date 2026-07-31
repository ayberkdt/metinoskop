---
name: metinoskop
description: Türkçe metinlerde mekanik yapay zekâ ritmini, basmakalıp geçişleri, gereksiz resmiyeti, kurumsal ve pazarlamacı cilayı, tiyatral vurguyu ve çeviri kokusunu azaltır; anlamı, olguları, kesinlik düzeyini, iletişim amacını ve yazarın sesini koruyarak doğal Türkçeyle düzenler. Makale, deneme, haber, rapor, tanıtım metni, e-posta, sosyal medya metni, açıklama veya Türkçeye çevrilmiş metin için "insanileştir", "doğal Türkçe yap", "AI gibi görünmesin", "robotik ifadeleri temizle", "pazarlama dilini azalt" ya da "kendi üslubuma uyarla" dendiğinde kullan.
---

# Metinoskop

Türkçe metni bir sözcük yasaklama listesiyle değil; bağlam, iletişim amacı, kaynak sadakati ve doğal Türkçe ritmi üzerinden düzenle.

## Kural önceliği

Çatışma olduğunda şu sırayı uygula:

1. Kullanıcının açık talebi ve belirttiği kapsam
2. Kaynak metindeki olgular, iddialar, belirsizlikler ve yazar tavrı
3. Kullanıcının sağladığı üslup örneği
4. Metnin iletişim amacı, türü ve muhatabı
5. Bu skill'deki genel dil tercihleri

Bir alt sıradaki kural, üst sıradakini bozmasın.

## Görevin sınırı

- Ana görev olarak mevcut metnin dilini ve paragraf akışını düzenle.
- Kullanıcı açıkça kaynak bilgilerden bir giriş yazılmasını istemedikçe yeni bölüm üretme.
- Yeni olgu, tarih, sayı, alıntı, kaynak, özellik, sonuç, deneyim veya kişisel görüş üretme.
- Kaynak dilden Türkçeye çeviri yapma; Türkçeye çevrilmiş mevcut metni doğallaştır.
- Kullanıcı istemedikçe olay sırasını, sahne yapısını, bakış açısını veya anlatı sonucunu değiştirme. Anlatı yapısının yeniden kurulması bu skill'in kapsamı dışındadır.
- Alıntıları, kodu, URL'leri, dipnotları, kaynak işaretlerini, tablo hücrelerini, başlık hiyerarşisini ve Markdown yapısını koru. Kullanıcı biçim değişikliği istemişse yalnızca gerekli kısmı değiştir.
- Bir metnin herhangi bir AI dedektöründen geçeceğini vaat etme. Dedektör için hata veya yapay çeşitlilik üretme.

## Bağlam profilini çıkar

Yazmadan önce sessizce belirle:

- **Tür:** akademik, teknik, haber, hukuki, kurumsal, tanıtım, gündelik, kişisel veya edebî
- **Amaç:** bilgi verme, açıklama, ikna, talep, eleştiri, savunma, değerlendirme, duygu aktarma veya resmî kayıt
- **Muhatap:** uzman, genel okur, müşteri, çalışma arkadaşı, kurum veya kişisel çevre
- **Ses:** resmiyet, doğrudanlık, kişi tercihi, terim yoğunluğu ve duygusal sıcaklık
- **İstenen değişiklik:** yalnızca belirtilen sorun mu, yoksa genel editörlük mü?
- **Rapor işlevi:** metin raporsa bölüm veya paragraf bağlam mı, yöntem mi, bulgu mu, yorum mu, sınırlılık mı, öneri mi taşıyor?

Bir metin aynı anda birden fazla amaç taşıyabilir. Kurumsal bir duyuru hem bilgi verebilir hem ikna edebilir; ikna amacını otomatik olarak silme.

## İkincil kabiliyet: kavramsal giriş

Yalnızca kullanıcı açıkça temel bir kavramı tanıtan giriş yazılmasını istiyorsa kaynakta bulunan bilgilerle şu hareketi kur:

1. Okurun bildiği durumu veya somut bağlamı göster.
2. Kavramı gerekli kılan gerçek problemi ya da bilgi boşluğunu belirginleştir.
3. Bölümün cevaplayacağı soruyu doğal biçimde görünür kıl.
4. Kavramı, yöntemi veya yaklaşımı bu sorunun cevabı olarak sun.

Bu sıralamayı zorunlu şablon gibi uygulama. Kaynakta problem yoksa problem, risk veya aciliyet uydurma; doğrudan bağlamdan kavrama geç. Soruyu mutlaka soru işaretiyle yazma. Merakı retorik heyecanla değil, henüz cevaplanmamış somut noktayla kur.

## Müdahale düzeyi

Kullanıcının istediği kapsamı aşma.

### Hafif

- Belirgin klişeleri, sohbet botu kalıntılarını, tiyatral vurguyu ve gereksiz dolguyu temizle.
- Cümle yapısını, paragraf sırasını ve kelime tercihlerini mümkün olduğunca koru.

### Standart

- Cümleleri ve paragraf içi akışı gerektiğinde yeniden kur.
- Mekanik ritmi, gereksiz resmiyeti, belirsiz göndergeleri ve çeviri kokusunu düzelt.
- Kullanıcı bir düzey belirtmediyse bunu kullan.

### Derin

- Bilgi sırasını ve paragraf yapısını yeniden düzenle.
- Tekrarları birleştir; metin boyunca ton ve ritim tutarlılığı kur.
- Olguları, ayrıntıları, kesinlik düzeyini ve yazar tavrını koru.

Kullanıcı yalnızca belirli bir sorun söylediyse müdahaleyi o sorunla sınırla. "Tiyatral ifadeleri çıkar" talebi, metnin tamamını yeniden yazma izni değildir.

## Değişiklik bütçesi

Metin zaten doğal, açık ve kullanıcının istediği tona uygunsa metni olduğu gibi bırak veya yalnızca zorunlu düzeltmeleri yap. Her görevde görünür değişiklik üretmek zorunda değilsin.

Doğal, açık ve işlevini yerine getiren bir cümleyi sırf farklı görünsün diye değiştirme. Her değişikliğin belirli bir gerekçesi olsun:

- anlam açıklığı,
- cümle veya paragraf akışı,
- klişe ya da dolgu,
- mekanik ritim,
- ton ve amaç uyumu,
- gönderge açıklığı,
- kaynak veya kesinlik sadakati.

Gerekçesi olmayan değişikliği geri al.

## Kaynak sadakati

Metindeki önermeleri sessizce ayır:

- doğrulanabilir olgu veya ölçüm,
- amaç, plan veya vaat,
- görüş ya da değerlendirme,
- duygu veya kişisel tavır,
- belirsizlik ve çekince,
- tekrar, dolgu veya işlevsiz süs.

İlk beş sınıfın anlamını ve kesinlik düzeyini koru. Son sınıfı başka sözcüklerle yeniden üretme.

- Bir hedefi gerçekleşmiş sonuç gibi yazma.
- Bir değerlendirmeyi ölçülmüş olguya dönüştürme.
- Kronolojik yakınlığı nedensellik gibi sunma.
- Kaynak yalnızca ilişki bildiriyorsa etki veya neden iddiası ekleme.
- Karşılaştırma zemini yoksa `daha`, üstünlük ölçütü yoksa `en` ekleme.
- Olumsuzluğu, istisnaları, koşulları ve nicelik sınırlarını koru.
- `Bazı` ifadesini `tüm`, `en az` ifadesini kesin sayı, `yalnızca` ifadesini genel kapsam hâline getirme.
- Bir hükmün veya sonucun hangi kişi, dönem, grup, koşul ya da bağlamla sınırlı olduğunu silme.
- `Henüz`, `artık`, `genellikle`, `kural olarak` ve benzeri kapsam belirleyicileri işlevsiz dolgu gibi çıkarma.
- Soyut övgünün dayandığı somut bilgi kaynakta varsa onu öne çıkar. Yoksa yeni dayanak üretme.

## Belirsizlik ve yorum seçimi

Kaynak metindeki bir ifade birden fazla makul yoruma açıksa anlamı kendin seçme.

- Belirsizlik korunarak doğal bir düzenleme yapılabiliyorsa ifadeyi koru.
- Düzenleme mutlaka bir yorum seçmeyi gerektiriyorsa kullanıcıdan açıklama iste.
- Kullanıcı inceleme veya karşılaştırma istediyse belirsizliği kısa bir notla belirt.
- Kullanıcı yalnızca son metni istediyse açıklama eklemek yerine kaynak anlamını en az değiştiren yapıyı koru.

## Değerlendirme ile olguyu ayır

Soyut ifade her zaman gereksiz değildir. Yazarın duygusunu, değerlendirmesini veya ikna amacını taşıyabilir.

- Bilgi verme amacı taşıyan bölümde olgu gibi sunulan kanıtsız fayda ve üstünlük iddiasını daralt, kaynağı varsa ona bağla veya çıkar.
- "Bu proje bizim için önemli bir dönüm noktasıdır" gibi açık yazar değerlendirmesini, değerlendirme olduğu anlaşılacak biçimde koru.
- Tanıtım metninde ikna amacını koru; hazır reklam kalıplarını daha özgül ve ölçülü bir söyleyişle değiştir.
- Kullanıcı özellikle "pazarlama dilini kaldır" veya "nötrleştir" dediyse soyut fayda ve üstünlük iddialarını daha sıkı temizle.
- Reklam cümlesini yalnızca daha sakin eş anlamlılarla yeniden kurma. Cümlenin işlevini ve metindeki dayanağını değerlendir.

## Yüksek riskli kalıplar

Bu yapıları otomatik olarak silme. İçerik taşımadan vurgu, geçiş, otorite veya heyecan üretmek için kullanıldıklarında düzenle:

- "günümüzün hızla değişen dünyasında", "her geçen gün", "bu bağlamda"
- "yalnızca ... değil, aynı zamanda ...", "mesele ... değil ..."
- "bir araçtan fazlası", "geleceğe açılan kapı", "dönüşümün anahtarı"
- "benzersiz", "çığır açan", "kritik", "dönüştürücü", "kusursuz"
- "öne çıkıyor", "fark yaratıyor", "bir üst seviyeye taşıyor"
- "ve sonra her şey değişti", "asıl mesele şu", "daha da çarpıcısı"
- art arda retorik sorular, üçlü sloganlar ve tek cümlelik dramatik paragraflar
- "Elbette!", "Harika soru", "Umarım faydalı olur", "Dilerseniz..."
- kaynaksız "uzmanlara göre", "araştırmalar gösteriyor", "genel kanı"

Hukuki, akademik, teknik veya edebî bağlamda işlev taşıyan ifadeyi koru. Örüntüleri tek sözcükte değil, kümeler ve tekrarlar halinde ara.

## Türkçeye özgü düzenleme

- Peş peşe gelen `-maktadır/-mektedir` yüklemlerini metnin türüne uygun doğal kiplerle sadeleştir. Sırf çeşitlilik sağlamak için farklı kipler kullanma.
- `gerçekleştirilmesi`, `sağlanması`, `yürütülmesi` gibi isim-fiil zincirlerini, anlam bozulmuyorsa eyleme döndür.
- Aktör kaynakta belliyse gereksiz edilgenliği azalt; belli değilse aktör uydurma.
- İngilizceden taşınmış kelime sırasını ve kalıp ifadeleri Türkçeleştir.
- Cümle başlangıçları, yüklem biçimleri veya uzunluklar mekanik biçimde tekrarlanıyorsa düşüncenin akışına göre yeniden kur; rastgele çeşitlilik üretme.
- Belirsiz `bu`, `böyle`, `ilgili` ve `söz konusu` göndergelerini açıklaştır.
- Aynı doğru terimi sırf tekrar olmasın diye rastgele eş anlamlılarla değiştirme.
- Metni aşırı sıkıştırıp telgraf diline dönüştürme.

## Yazarın sesini eşle

Kullanıcı bir yazı örneği verdiyse şu özellikleri çıkar:

- ortalama cümle uzunluğu ve uzunluk değişimi,
- sık kullandığı doğal bağlaçlar,
- birinci veya üçüncü kişi tercihi,
- teknik terim yoğunluğu,
- parantez, iki nokta ve noktalı virgül kullanımı,
- resmiyet ve doğrudanlık düzeyi,
- kısa vurgu cümlelerini kullanıp kullanmadığı,
- mizah, çekince ve kişisel yorum biçimi.

Örnekteki yazım yanlışlarını, dil bilgisi hatalarını ve tesadüfi tekrarları üslup özelliği olarak taklit etme.

## Terim ve gösterim tutarlılığı

Uzun veya teknik metinde sessizce bir terim ve gösterim listesi oluştur:

- tanımlanmış teknik terimler,
- kısaltmalar ve ilk açılımları,
- değişken, sembol ve denklem adları,
- başlık ve bölüm numaraları,
- ürün, yöntem ve model adları,
- büyük-küçük harf tercihleri.

Aynı kavramı sırf tekrar olmasın diye farklı terimlerle adlandırma. Kaynakta ayrı anlam taşıyan iki terimi tek terimde birleştirme. Sembol, indis, birim ve işaretleri dil düzenlemesinin parçası olarak değiştirme.

## Rapor bütünlüğünü koru

Metin bir rapor, inceleme notu, değerlendirme belgesi veya yönetici özetiyse yalnızca cümleleri değil, kanıt zincirini de koru.

- Her bölümün ve paragrafın işlevini sessizce belirle: bağlam, amaç, kapsam, yöntem, bulgu, yorum, sınırlılık, öneri veya karar.
- Bulguyla yorumu, yorumla öneriyi, öneriyle verilmiş kararı tek statüde birleştirme. Kaynakta aralarındaki sınır bulanıksa düzenleme sırasında kesinleştirme.
- İddia ile onu destekleyen sayı, alıntı, tablo, kaynak işareti ve sınırlılığı birbirinden uzaklaştırma.
- Bir verinin neyi gösterdiğini açıklaştırabilirsin; kaynakta bulunmayan neden, önem, risk veya sonuç ekleme.
- Öneriyi gerçekleşmiş uygulama, hedefi sonuç, beklentiyi taahhüt gibi yazma.
- Yönetici özetinde yalnızca rapor gövdesinde bulunan ana bulgu, sınır ve önerileri kullan. Kullanıcı istemedikçe yeni yönetici özeti üretme.
- Başlık hiyerarşisini, tablo ve şekil adlarını, bölüm numaralarını ve çapraz göndermeleri koru. Başlıkları yalnızca kullanıcı isterse veya başlık içerikle açıkça çelişiyorsa değiştir.
- Paragrafları tek biçimli bir şablona zorlama. İddia, dayanak ve sınır mevcutsa ilişkilerini görünür kıl; eksik parçayı sen üretme.
- Profesyonel tonu bürokratik dolguya dönüştürme. Aktör biliniyorsa açık özne ve somut fiil kullan; bilinmiyorsa aktör uydurma.
- Daha akıcı olsun diye önemli tekrarları silme. Bir terim, kapsam veya sınırlılık okurun yanlış anlamasını önlüyorsa tekrar işlevseldir.

Rapor düzenlemesinden sonra bulgu–yorum–öneri sınırlarını, bölüm içi dayanakları ve bölümler arası sayı, tarih, terim ve kesinlik tutarlılığını ayrıca denetle.

## Çalışma yöntemi

### 1. Envanter çıkar

Metnin türünü, amacını, müdahale düzeyini ve korunacak unsurları belirle. Sayı, tarih, özel ad, alıntı, kaynak işareti, kapsam belirleyicisi, terim, sembol ve temel iddiaları zihinsel bir kontrol listesine al.

### 2. Sorun kümelerini bul

En baskın sorunları belirle: ritim, söz dizimi, dolgu, reklam cilası, tiyatral vurgu, belirsiz atıf, çeviri kokusu, akış veya ses uyumsuzluğu. Tek bir işaretten "AI metni" sonucu çıkarma.

### 3. Düzenle

Seçilen müdahale düzeyinde düzenle. Komşu cümleleri birlikte değerlendir; bir cümledeki değişiklik sonraki cümlenin öznesini, zamanını veya mantıksal bağını bozmasın. Raporlarda bölümün işlevini ve bulgu–yorum–öneri sınırını koru.

### 4. Kaynak karşılaştırması yap

Son metindeki her sayı, tarih, özellik, sonuç, nedensellik, karşılaştırma, olumsuzluk, koşul, istisna, nicelik sınırı, terim, gösterim ve kişisel ayrıntının kaynakta karşılığını bul. Raporlarda yorumların dayanağını, önerilerin statüsünü ve çapraz göndermeleri de karşılaştır. Karşılığı yoksa çıkar veya kaynak metnin izin verdiği kesinlik düzeyine döndür.

### 5. Ses ve akış denetimi yap

Metni bir kez anlam, bir kez doğal duraklar için oku. Şunları kontrol et:

- Her cümlenin öncekiyle ilişkisi açık mı?
- Cümleler aynı kalıpla mı ilerliyor?
- Yazarın tavrı veya iletişim amacı kaybolmuş mu?
- Gereksiz bağlaçlar çıkarılmış mı?
- Özgün fakat doğal ifadeler yanlışlıkla düzleştirilmiş mi?
- Kullanıcının istediğinden fazla değişiklik yapılmış mı?
- Raporda bulgu, yorum, sınırlılık, öneri veya karar yanlışlıkla birbirine dönüşmüş mü?

## Referans yönlendirmesi

- Klişe, yapay ritim, gereksiz resmiyet, reklam dili veya çeviri kokusu baskınsa [Türkçe örüntüler](references/turkce-oruntuler.md) dosyasını oku.
- Cümleler doğru olduğu hâlde paragraf kopuksa, göndergeler belirsizse veya okuma akışı takılıyorsa [Akıcı Türkçe](references/akicilik.md) dosyasını oku.
- Metin rapor, inceleme notu, değerlendirme belgesi veya yönetici özeti ise [Rapor yazımı](references/rapor-yazimi.md) dosyasını oku.
- Kullanıcı açıkça temel bir kavram veya yönteme bütünlüklü giriş yazılmasını istiyorsa [Kavramsal girişler](references/kavramsal-girisler.md) dosyasını oku.
- Uzun veya karmaşık metinde birden fazla sorun varsa ilgili referans dosyalarını birlikte oku.

## Çıktı biçimi

Belirsizliği korumak mümkün değilse ve düzenleme bir yorum seçmeyi gerektiriyorsa önce kullanıcıdan açıklama iste.

Kullanıcı başka bir biçim istemediyse yalnızca son metni ver. Sohbet botu girişi veya kapanış teklifi ekleme.

Kullanıcı inceleme ya da karşılaştırma istediyse şu sırayı kullan:

1. Kısa teşhis
2. Düzeltilmiş metin
3. En önemli değişiklikler

## Kısa örnek

**Önce**

> Günümüzün hızla değişen iş dünyasında yenilikçi platformumuz, siparişleri tek ekranda topluyor ve tekrar eden onayları otomatikleştiriyor. Bu güçlü çözüm yalnızca süreçleri kolaylaştırmakla kalmıyor, sipariş başına gereken adım sayısını beşten üçe indirerek verimliliği de bir üst seviyeye taşıyor.

**Sonra**

> Platform, siparişleri tek ekranda topluyor ve tekrar eden onayları otomatikleştiriyor. Bu değişiklik, sipariş başına gereken adım sayısını beşten üçe indiriyor.

İkinci metin yeni özellik üretmez; kaynakta bulunan işlev ve ölçümü koruyup reklam kalıplarını çıkarır.
