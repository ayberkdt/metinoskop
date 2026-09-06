# Yüzeyde yapay görünen gerekli ifade

## Kaynak

`retries` alanı yalnızca ağ hatalarında geçerlidir; sunucunun 4xx yanıtlarında yeniden deneme yapılmaz. Bu ayrım önemlidir: 429 yanıtı da bir 4xx yanıtı olduğundan hız sınırı aşıldığında istek otomatik olarak yinelenmez ve çağıran tarafın bekleyip yeniden göndermesi gerekir. Sonuç olarak `retries` değeri 0 yapıldığında ağ hataları için de tek deneme yapılır; `timeout` bundan etkilenmez. Bu noktada dikkat edilmesi gereken bir husus vardır: `timeout` süresi her deneme için ayrı ayrı uygulanır, toplam süre için değil.

## Talep

Teknik belge. Standart düzeyde düzenle; yapay görünen çerçeve ifadelerini temizle ama teknik ayrımları eksiksiz koru.

## Korunması gerekenler

- `retries` alanının yalnızca ağ hatalarında geçerli olduğu ve 4xx yanıtlarında yeniden deneme yapılmadığı korunmalı.
- 429 yanıtının 4xx sayıldığı, hız sınırı aşıldığında isteğin otomatik yinelenmediği ve çağıran tarafın bekleyip yeniden göndermesi gerektiği açıklaması eksiksiz kalmalı.
- `retries` değeri 0 olduğunda ağ hataları için tek deneme yapıldığı ve `timeout` değerinin bundan etkilenmediği korunmalı.
- `timeout` süresinin toplam süre için değil her deneme için ayrı uygulandığı ayrımı korunmalı.
- "Bu ayrım önemlidir" ve "dikkat edilmesi gereken bir husus vardır" çerçeveleri çıkarılabilir; ardından gelen içerik çıkarılamaz.
- "Sonuç olarak" bağlacı, gerçek bir çıkarımı başlattığı için korunabilir veya doğal bir bağlaçla değiştirilebilir; çıkarımın kendisi silinemez.
- Alan adları satır içi kod olarak kalmalı.

## Kaçınılması gerekenler

- 429 açıklamasını "açık olanın açıklaması" sayıp silmek
- Her deneme için ayrı `timeout` bilgisini silmek veya toplam süreye çevirmek
- Ağ hataları ile sunucu yanıtlarını tek bir hata sınıfında birleştirmek
- "Yapılmaz" ifadesini "önerilmez" gibi zayıflatmak
- "Sonuç olarak" ile başlayan cümleyi kalıp sonuç sanıp çıkarımıyla birlikte silmek
- Kaynakta bulunmayan başka HTTP kodu, bekleme süresi veya varsayılan değer eklemek
