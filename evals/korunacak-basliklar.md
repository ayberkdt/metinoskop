# Korunması gereken başlıklar

## Kaynak

# Kurulum kılavuzu

Bu kılavuz dört bölümden oluşur: gereksinimler, kurulum, yapılandırma ve sorun giderme. Mevcut bir kurulumu güncelliyorsanız doğrudan üçüncü bölüme geçebilirsiniz.

## 1. Gereksinimler

Sunucuda en az 8 GB bellek ve 20 GB boş disk alanı bulunmalıdır. Python 3.12 veya üstü gerekir.

Ağ tarafında 8080 ve 8443 portları açık olmalıdır. Vekil sunucu kullanılıyorsa `HTTPS_PROXY` değişkeni tanımlanmalıdır.

## 2. Kurulum

Paketi `pip install metin-sunucu` komutuyla kurun. Kurulum yaklaşık iki dakika sürer.

Kurulum sonrasında `metin-sunucu --version` komutu sürüm numarasını yazdırmalıdır; yazdırmıyorsa PATH ayarını kontrol edin.

## 3. Yapılandırma

Yapılandırma dosyası `config/settings.yaml` yolundadır. `timeout` alanı saniye cinsinden bekleme süresidir; varsayılan 30'dur.

`retries` alanı deneme sayısıdır; varsayılan 3'tür. `timeout` değeri 0 yapılırsa istek süresiz bekler; bu ayar üretim ortamında önerilmez.

## 4. Sorun giderme

Sunucu başlamıyorsa önce `logs/server.log` dosyasına bakın. En sık hata, 8080 portunun başka bir süreç tarafından kullanılmasıdır.

Günlükte `PermissionDenied` görünüyorsa hizmet hesabının `config/` dizinine okuma yetkisi olduğunu doğrulayın.

## Talep

Derin düzeyde düzenle.

## Korunması gerekenler

- `# Kurulum kılavuzu` ve dört `##` başlığı aynı düzey, numara ve sırayla korunmalı; her biri gezinme işlevi taşıyor.
- Girişteki yönlendirme cümlesi (dört bölüm, güncelleme yapanların üçüncü bölüme geçebileceği) korunmalı; okurun nereden başlayacağını değiştiriyor.
- `En az` 8 GB, 20 GB, Python 3.12, 8080 ve 8443 portları, `HTTPS_PROXY`, bütün komutlar ve dosya yolları kod biçimiyle korunmalı.
- `timeout` 30, `retries` 3, 0 değerinde süresiz bekleme ve üretimde önerilmediği korunmalı.
- Bölüm içinde paragraflar hafifçe birleştirilebilir; bölümler birleştirilemez.

## Kaçınılması gerekenler

- Bölümleri birleştirmek veya yeniden numaralandırmak
- Yönlendirme cümlesini yol haritası dolgusu sanıp silmek
- Yeni alt başlık veya `###` düzeyi eklemek
- Sorun giderme adımlarını yapılandırma bölümüne taşımak
- "Önerilmez" ifadesini silmek veya yasağa çevirmek
- Komut, yol veya değer değiştirmek
