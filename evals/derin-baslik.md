# Aşırı başlık derinliği

## Kaynak

## 3. Yapılandırma

### 3.1 Bağlantı ayarları

#### 3.1.1 Zaman aşımı

`timeout` alanı saniye cinsinden bekleme süresidir; varsayılan değer 30'dur.

#### 3.1.2 Yeniden deneme

`retries` alanı başarısız istek için deneme sayısıdır; varsayılan değer 3'tür.

### 3.2 Günlük ayarları

#### 3.2.1 Düzey

`log_level` alanı `info` veya `debug` değerini alır; varsayılan `info`dur.

## Talep

Teknik belge. Derin düzeyde düzenle; hiyerarşiyi içeriğin gerektirdiği derinliğe indir, bütün alanları ve varsayılan değerleri koru. Belge başka yerden bölüm numarasına gönderme yapmıyor.

## Korunması gerekenler

- `## 3. Yapılandırma` başlığı aynı düzeyde kalmalı.
- `timeout`, `retries` ve `log_level` alanları satır içi kod olarak, açıklamaları ve varsayılanlarıyla (30, 3, `info`) korunmalı.
- `log_level` için `info` ve `debug` değerleri korunmalı.
- Dördüncü düzey başlıklar kaldırılmalı; bağlantı ve günlük ayarları ya iki `###` alt bölüm ya da tek bölüm içinde iki paragraf olarak sunulabilmeli.

## Kaçınılması gerekenler

- `####` düzeyini korumak
- Her alanı ayrı başlık altında tutmak
- Yeni alan, değer veya davranış eklemek
- Varsayılan değerleri değiştirmek veya alanları birbirine karıştırmak
- Kod biçimini kaldırmak
- Her cümleyi ayrı paragraf yapmak

## Yapısal beklenti

- en derin düzey: <= 3
- başlık: <= 3
- başlık: >= 1
