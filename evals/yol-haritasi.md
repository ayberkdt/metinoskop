# Yol haritası ve okur yönlendirmesi

## Kaynak

## Yapılandırma

Bu bölümde yapılandırma dosyasının nasıl düzenleneceği ele alınacaktır. Öncelikle dosyanın nerede bulunduğunu anlamak gerekir. Yapılandırma dosyası `config/settings.yaml` yolunda bulunur. Aşağıda dosyadaki alanlar sırayla incelenecektir.

`timeout` alanı saniye cinsinden bekleme süresini belirler; varsayılan değer 30'dur. Şimdi `retries` alanına bakalım. `retries` alanı başarısız istek için deneme sayısını belirler; varsayılan değer 3'tür. Bu noktaya ileride yeniden döneceğiz.

Peki bu ayarlar ne anlama geliyor? `timeout` değeri 0 olarak ayarlanırsa istek süresiz bekler. Bir sonraki bölümde göreceğimiz üzere bu davranış üretim ortamında önerilmez.

## Talep

Teknik belge. Standart düzeyde düzenle; bilgi taşımayan yönlendirme cümlelerini çıkar, alan açıklamalarını ve başlığı koru.

## Korunması gerekenler

- `## Yapılandırma` başlığı aynı düzeyde kalmalı.
- `config/settings.yaml` yolu satır içi kod olarak korunmalı.
- `timeout` alanının saniye cinsinden bekleme süresi olduğu ve varsayılanın 30 olduğu korunmalı.
- `retries` alanının deneme sayısı olduğu ve varsayılanın 3 olduğu korunmalı.
- `timeout` değeri 0 olduğunda isteğin süresiz beklediği korunmalı.
- Süresiz beklemenin üretim ortamında önerilmediği bilgisi ana metinde doğrudan verilmeli.
- Alan adları kod biçiminde kalmalı.

## Kaçınılması gerekenler

- "Bu bölümde ... ele alınacaktır", "Öncelikle ... anlamak gerekir", "Aşağıda ... incelenecektir", "Şimdi ... bakalım", "Bu noktaya ileride yeniden döneceğiz", "Peki bu ayarlar ne anlama geliyor?" cümlelerini korumak
- Duyuruyu "Aşağıda alanlar açıklanmaktadır" gibi başka bir duyuruyla değiştirmek
- "Bir sonraki bölümde göreceğimiz üzere" göndermesini korumak veya sonraki bölümün içeriğini uydurmak
- Kaynakta bulunmayan yeni alan, varsayılan değer veya davranış eklemek
- "Önerilmez" ifadesini yasağa çevirmek ya da silmek
