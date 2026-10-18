# Sızıntı sanılan içerik korunur

## Kaynak

## 2.3 sürümündeki değişiklikler

Önceki sürümde istek zaman aşımı 30 saniyeydi; bu sürümde 60 saniyeye çıkarıldı. Eski davranışa `--legacy-timeout` bayrağıyla dönebilirsiniz. Kullanıcının isteği üzerine silinen hesapların kişisel verileri artık 30 gün içinde yok ediliyor. Özetleme modeli, istemde belirtilen JSON biçimine 200 denemenin 11'inde uymadı; bu nedenle çıktı artık biçim doğrulamasından geçiyor.

## Talep

Bu sürüm notunu okura hazırla.

## Korunması gerekenler

- Metin zaten okura doğrudan yazılmış olduğundan olduğu gibi kalmalı.
- `Önceki sürümde` karşılaştırması korunmalı: sürüm notunun okuru önceki sürümü kullanmıştır, karşılaştırma içeriktir.
- `Kullanıcının isteği üzerine` korunmalı: buradaki kullanıcı ürünün kullanıcısıdır, metni isteyen kişi değil.
- `istemde belirtilen` korunmalı: istem bu sürüm notunda modelin girdisidir, ajanın talimatı değil.
- Okura yapılan `dönebilirsiniz` yönlendirmesi ve `--legacy-timeout` bayrağı korunmalı.
- 30 ve 60 saniye, 30 gün, 200 denemenin 11'i ve `artık` korunmalı.

## Kaçınılması gerekenler

- `Önceki sürümde`, `Kullanıcının isteği üzerine` ya da `istemde` ifadesini konuşma sızıntısı sanıp silmek
- Okura yapılan yönlendirmeyi kullanıcıya teklif sanıp silmek
- `artık` sözcüğünü önceki duruma gönderme yaptığı için çıkarmak
- Sürüm notunu genel ürün tanımına çevirmek ya da zaman kiplerini değiştirmek
- Kaynakta olmayan sürüm numarası, tarih ya da neden eklemek

## Yapısal beklenti

- sert işaret: 0
- başlık: 1
- cümle: 4
