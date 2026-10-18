# Okura doğrudan metin

Metin, ajan ile kullanıcı arasındaki konuşmayı görmemiş son okura gider. Konuşma, talimat, önceki taslaklar, araç çıktıları ve ajanın çalışma sırası okurun dünyasında yoktur.

## Okuru belirle

- **Varsayılan:** okur konuşmayı görmedi.
- **Kullanıcı tanımlarsa** ("bana not olarak yaz", "Selin'e yanıt olarak düzenle") o tanım geçerlidir. Okur kullanıcının kendisiyse ortak bağlama gönderme sızıntı değildir.
- **Okurun tarafı olduğu yazışma:** e-postadaki `geçen ay konuştuğumuz gibi` ortak geçmişe gönderir; içeriktir (`iyi-metin`).
- **Test:** konuşmayı görmemiş okur `ben`, `biz`, `sen` kim, anlıyor mu; cümle ona bilgi veriyor mu? `Biz` ajan ile kullanıcıysa ya da `sen` kullanıcıysa ve okur bunlardan biri değilse sızıntı vardır.

## Sızıntı aileleri

| Aile | Örnek | Karar |
|---|---|---|
| Konuşmaya gönderme | `konuştuğumuz gibi`, `isteğin üzerine`, `talimatta belirtildiği gibi`, `verdiğin dosyaya göre`, `kullanıcının istediği üzere` | Gönderme gider; taşıdığı olgu ya da kaynak bilgisi kalır. |
| Kullanıcıya teklif | `istersen ... ekleyebilirim`, `bir sonraki adımda ... bakabilirim`, `şunu yapabiliriz`, `ister misiniz?` | Okura bilgi vermiyorsa gider; gerçek bir seçenek varsa statüsüyle okura çevrilir. |
| Çalışma süreci | `önce X'i inceledim, sonra testi çalıştırdım`, `analizi tamamladım` | Sıra ve ilk tekil şahıs gider; bulgunun dayanağı olan yöntem kalır (`kayıtlar incelendi`). |
| Düzenleme geçmişi | `daha net olsun diye yeniden yazıldı`, `önceki taslakta`, `(düzeltildi)`, `güncelleme:` | Gider; metin yalnızca son hâlini söyler. |
| Teslim ambalajı, ajan kimliği | `İşte düzenlenmiş rapor:`, `Umarım faydalı olur`, `bir yapay zekâ olarak` | Gider; taşıdığı belirsizlik varsa olgunun statüsü olarak yazılır. |
| Okurun erişemediği nesne | ajanın geçici dosyası, oturum ya da araç adı, `promptta` | Gönderme gider, bilgi kalır. Okurun erişebildiği depo dosyası, URL ya da ek kalır. |
| Metne konmuş not | `[?]`, `(kaynakta belirsiz)`, `TODO: kontrol et` | Metin dışı nota taşınır. Kaynaktaki yer tutucu (`[tarih eklenecek]`) yazarındır; doldurulmaz, silinmez. |

## Bilgiyi kurtar

Sızıntıyı temizlemek bir çekinceyi, varsayımı ya da kapsam sınırını silme gerekçesi değildir.

| Önce | Sonra |
|---|---|
| Konuştuğumuz gibi bütçe 2 milyon TL. | Bütçe 2 milyon TL. |
| Verdiğin 2024 satış dosyasına göre iade oranı %6,2. | 2024 satış verilerine göre iade oranı %6,2. |
| Burada sunucu saatlerinin senkron olduğunu varsaydım. | Bu hesap, sunucu saatlerinin senkron olduğu varsayımına dayanır. |
| Bunu doğrulayamadım. | Bu değer doğrulanmadı. |
| Emin değilim ama gecikme ağ kaynaklı olabilir. | Gecikme ağ kaynaklı olabilir. |
| Kullanıcının belirttiği üzere pilot iptal edildi. | Pilot iptal edildi. |
| Önce `cache.py` dosyasına baktım, sonra yük testini çalıştırdım. | `cache.py` incelendi ve yük testi çalıştırıldı. |

Süreç cümlesini yöntem cümlesine çevirirken yapılmış iş geçmişte kalır (`incelendi`) ve aktör uydurulmaz (`ekip inceledi` değil).

## Teklifi okura çevir

- **Statü:** `yapabiliriz` olasılıktır → `yapılabilir`. `yapılmalıdır` öneriye, `yapılacak` karara yükseltir. Kaynak açıkça öneriyorsa (`kaldırılmasını öneririm`) öneri kalır: `kaldırılması önerilir`.
- **Aktör:** `biz` okur için tanımsızdır; kaynakta adı geçen aktör yoksa edilgen ya da adlaştırılmış yapı kur.
- **Koşul düşmez:** `yük testi temiz geçerse sürümü çıkarabiliriz` → `Yük testi temiz geçerse sürüm çıkarılabilir`.

## Metin dışı not

Metin önce ve eksiksiz gelir; olduğu gibi okura gönderilebilmelidir. Not, metinden sonra `---` ile ayrılır ve yalnızca üç durumda yazılır: yorum seçimi zorunluysa (tek soru), kullanıcı kapsamı daralttığı için bir anlam hatası metinde kaldıysa, kullanıcı inceleme istediyse. Belirsiz yer metinde kaynaktaki hâliyle kalır.

## Sızıntı olmayanlar

- Kurumsal yanıtta `talebiniz doğrultusunda aboneliğiniz iptal edildi`: okur talebin sahibidir.
- Belge içi gönderme: `Tablo 2'de`, `3. bölümde`, `Ek A`.
- Sürüm notunda `Önceki sürümde zaman aşımı 30 saniyeydi`: okur önceki sürümü kullanmıştır.
- Gereksinim metninde `kullanıcının isteği üzerine`: ürünün kullanıcısıdır.
- Dil modeli metninde `istemde belirtilen biçim`: istem çalışmanın nesnesidir.
- Akademik `biz` (`... olduğunu çıkarabiliriz`): yazarın okurla kurduğu akıl yürütmedir.
- Okura yönelik yönlendirme (`--legacy-timeout ile dönebilirsiniz`).

Bekçi vakalar: `sizinti-sanilan-icerik-korunur`, `iyi-metin`.

## Aşırı uygulama belirtileri

- Varsayımı, `doğrulanmadı` bilgisini, çekinceyi ya da bulgunun dayanağı olan yöntemi silmek.
- `yapabiliriz`i öneriye ya da karara yükseltmek; `biz` yerine kaynakta olmayan aktör yazmak.
- Okurun tarafı olduğu yazışmadaki ortak geçmişi, kurumsal yanıtı ya da sürüm notundaki karşılaştırmayı silmek.
- Kaynaktaki yer tutucuyu silmek ya da doldurmak.
- Her düzenlemeye not eklemek.

## Stil denetimi

`style-lint.py` adayları `sizinti` ailesinde işaretler (konuşmaya gönderme, `-ebilirim`/`-ebiliriz`, `istersen`, ilk tekil şahıs süreç fiili, önceki taslak ya da sürüm, parantez içi düzenleme işareti, `İşte ...`, `prompt`). Aynı biçimler yazışmada ve sürüm notunda içerik olduğu için aile bağlamsaldır; ajan kimliği `sohbet` sert ailesindedir. Okurun konuşmayı görmediği biliniyorsa:

```bash
python scripts/style-lint.py rapor.md --son-okur
```

Bu kipte adaylar sert sayılır ve tek bir aday kalsa bile betik 1 ile çıkar. Okurun tarafı olduğu yazışmada kullanmayın. Tam örnek: `evals/konusma-sizintisi-rapor.md` ve gold çıktısı.
