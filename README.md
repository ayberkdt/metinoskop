# Metinoskop

[![Validate package](https://github.com/ayberkdt/metinoskop/actions/workflows/validate.yml/badge.svg)](https://github.com/ayberkdt/metinoskop/actions/workflows/validate.yml)
![License: MIT](https://img.shields.io/badge/license-MIT-2e7d32)
![Agent Skill](https://img.shields.io/badge/agent-skill-2563eb)
![Language: Türkçe](https://img.shields.io/badge/language-T%C3%BCrk%C3%A7e-c62828)

Türkçe metinlerdeki mekanik yapay zekâ ritmini, basmakalıp ifadeleri ve kurumsal dolguyu ayıklayan taşınabilir agent skill'i ve editoryal rehber seti.

Metinoskop, metni sırf farklı görünsün diye yeniden yazmaz. Anlamı, olguları, kesinlik düzeyini, yazarın tavrını ve uygun resmiyet düzeyini koruyarak yalnızca gerekli editoryal müdahaleyi yapar.

## Ne yapar?

- Mekanik cümle ritmini ve tekrarlanan kalıpları düzeltir.
- Gereksiz `-maktadır/-mektedir` zincirlerini ve isim-fiil yığılmalarını sadeleştirir.
- Kurumsal dolgu, reklam dili ve tiyatral vurguyu azaltır.
- Belirsiz göndergeleri ve kopuk paragraf geçişlerini açıklaştırır.
- İngilizceden taşınmış söz dizimini doğal Türkçeye yaklaştırır.
- Kullanıcının sağladığı yazı örneğine göre ses ve ton eşleştirmesi yapar.
- Temel kavramlara kaynakta bulunan bağlam, problem, soru ve çözüm ilişkisiyle bütünlüklü girişler kurar.
- Kaynakta bulunmayan olgu, tarih, sayı, alıntı veya kişisel ayrıntı eklemez.

## Temel ilkeler

1. Kullanıcının açık talebi ve belirttiği kapsam önceliklidir.
2. Kaynak metindeki olgular, belirsizlikler ve yazar tavrı korunur.
3. Doğal ve işlevini yerine getiren cümleler sırf değişiklik üretmek için bozulmaz.
4. Kronolojik yakınlık nedensellik gibi sunulmaz.
5. Metnin bir AI dedektöründen geçeceği vaat edilmez.

## Kurulum

### Skills CLI

Metinoskop'u desteklenen agent ortamlarına genel olarak kurmak için:

```bash
npx skills add ayberkdt/metinoskop --global
```

Mevcut kurulumu güncellemek için:

```bash
npx skills update metinoskop --global
```

Yalnızca geçerli projeye kurmak isterseniz `--global` seçeneğini kaldırın. Kurulumdan sonra agent oturumunu yenileyin veya skill listesini yeniden yükleyin.

### Elle kurulum

Depoyu kullandığınız agent ortamının skill dizinine klonlayın:

```bash
git clone https://github.com/ayberkdt/metinoskop.git /path/to/skills/metinoskop
```

Çalışma zamanında gereken ana dosya `SKILL.md` dosyasıdır. `references/` klasörü ayrıntılı Türkçe örüntü, akıcılık ve kavramsal giriş rehberlerini; `agents/openai.yaml` ise destekleyen istemciler için arayüz metadata'sını içerir.

## Kullanım

Skill'i doğrudan adıyla çağırabilirsiniz:

```text
$metinoskop

Aşağıdaki metni doğal Türkçeyle yeniden yaz. Anlamı ve olguları koru:

[metin]
```

Doğal dilde bir talep de yeterlidir:

```text
Bu metni insanileştir; robotik ifadeleri ve pazarlama dilini temizle.
```

Belirli bir müdahale düzeyi isteyebilirsiniz:

```text
Bu e-postaya hafif bir Metinoskop düzenlemesi uygula. Cümle yapısını mümkün olduğunca koru.
```

```text
Bu raporu derin düzeyde düzenle. Paragraf akışını yeniden kur fakat hiçbir sayı, tarih veya iddiayı değiştirme.
```

### Yazarın sesini eşleştirme

Kendi yazınızdan kısa bir örnek vererek metnin o sese yaklaşmasını sağlayabilirsiniz:

```text
$metinoskop

Önce aşağıdaki iki paragraftan üslubumu çıkar:
[yazı örneği]

Şimdi bu metni aynı resmiyet, ritim ve doğrudanlık düzeyiyle düzenle:
[düzenlenecek metin]
```

Yazım yanlışları ve tesadüfi tekrarlar üslup özelliği olarak taklit edilmez.

### Kavramsal giriş

Temel bir kavramı kuru bir tanımla açmak yerine, kaynakta bulunan bilgiler arasında bütünlüklü bir giriş kurabilirsiniz:

```text
$metinoskop

Önbellek kavramını tanıtan kısa bir giriş yaz. Kaynakta bulunan bağlam, problem, soru ve çözüm arasında doğal bir akış kur; yeni risk veya fayda ekleme.

[kaynak bilgiler]
```

Problem kaynakta yoksa Metinoskop problem uydurmaz; bağlamdan doğrudan soruya veya kavrama geçer. Soru işareti ve retorik merak zorunlu değildir.

## Kısa örnek

**Önce**

> Günümüzün hızla değişen iş dünyasında yenilikçi platformumuz, siparişleri tek ekranda topluyor ve tekrar eden onayları otomatikleştiriyor. Bu güçlü çözüm yalnızca süreçleri kolaylaştırmakla kalmıyor, sipariş başına gereken adım sayısını beşten üçe indirerek verimliliği de bir üst seviyeye taşıyor.

**Sonra**

> Platform, siparişleri tek ekranda topluyor ve tekrar eden onayları otomatikleştiriyor. Bu değişiklik, sipariş başına gereken adım sayısını beşten üçe indiriyor.

Düzenlenmiş sürüm yeni özellik üretmez; kaynakta bulunan işlev ve ölçümü koruyup reklam kalıplarını çıkarır.

## Kapsam ve sınırlar

Metinoskop bir dil ve paragraf akışı editörüdür.

- Olgu doğrulaması yapmaz.
- Kaynakta olmayan bilgi üretmez.
- Kullanıcı istemedikçe olay sırasını, sahne yapısını, bakış açısını veya anlatı sonucunu değiştirmez.
- Hukuki, akademik veya teknik metindeki gerekli terminolojiyi otomatik olarak gündelikleştirmez.
- Her düzgün cümleyi değiştirmeye çalışmaz; metin zaten doğal ve uygunsa olduğu gibi bırakabilir.

Kavramsal giriş kurmak bu kapsam içindedir; olay örgüsünün, sahne yapısının veya bakış açısının yeniden kurulması değildir.

## Nasıl çalışır?

Metinoskop düzenleme sırasında altı aşamalı bir denetim uygular:

1. Metnin türünü, amacını, muhatabını ve korunacak unsurları belirler.
2. Ritim, dolgu, reklam cilası, belirsiz atıf, çeviri kokusu ve akış sorunlarını kümeler hâlinde inceler.
3. Kavramsal giriş istenmişse kaynakta bulunan bağlam, problem, soru ve çözüm ilişkisini çıkarır.
4. Kullanıcının istediği müdahale düzeyinde düzenler.
5. Son metindeki sayı, tarih, iddia, nedensellik ve karşılaştırmaları kaynakla karşılaştırır.
6. Ses, ton, gönderge açıklığı ve paragraf akışını son kez denetler.

Ayrıntılı örüntüler yalnızca gerektiğinde `references/` altından yüklenir; böylece ana skill yönergesi kısa ve taşınabilir kalır.

## Depo yapısı

```text
metinoskop/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── akicilik.md
│   ├── kavramsal-girisler.md
│   └── turkce-oruntuler.md
├── evals/
│   ├── akademik.md
│   ├── hukuki.md
│   ├── kurumsal.md
│   ├── kisisel.md
│   ├── kaynak-sadakati.md
│   └── kavramsal-giris.md
├── scripts/
│   └── validate-package.py
├── .github/
│   └── workflows/
│       └── validate.yml
├── AGENTS.md
├── LICENSE
└── README.md
```

## Geliştirme ve doğrulama

Bağımlılık gerektirmeyen yerel paket kontrolü:

```bash
python scripts/validate-package.py
```

Agent Skills keşfini denetlemek için:

```bash
npx --yes skills@1.5.20 add . --list
```

GitHub Actions, `main` dalına gönderilen her değişiklikte ve pull request'lerde bu kontrolleri çalıştırır.

`evals/` klasörü tek bir beklenen çıktı dayatmaz. Her vaka; korunması gereken olguları, kesinlik düzeyini ve biçimi, ayrıca kaçınılması gereken davranışları tanımlar. Böylece farklı ama geçerli düzenlemeler aynı editoryal ölçütlerle değerlendirilebilir.

## Katkı

Hata örneklerini ve geliştirme önerilerini [GitHub Issues](https://github.com/ayberkdt/metinoskop/issues) üzerinden paylaşabilirsiniz. Davranış değişikliği yapan pull request'lerde `SKILL.md`, README ve ilgili eval vakalarının birbiriyle uyumlu kalması gerekir.

## Lisans

Bu proje MIT Lisansı altında yayımlanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.
