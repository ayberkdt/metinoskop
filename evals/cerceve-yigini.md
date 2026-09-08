# Çerçeve yığını

## Kaynak

Bu bağlamda, performans açısından, önerilen yöntem kapsamında değerlendirilmesi gereken temel husus, bellek kullanımı noktasında ortaya çıkan %35'lik artıştır. Güvenlik perspektifinden bakıldığında ise yöntem, mevcut erişim denetimi çerçevesinde herhangi bir değişiklik gerektirmemektedir. Uygulanabilirlik bakımından yöntem, 8 GB belleğe sahip cihazlar üzerinden sınanmıştır; daha düşük bellekli cihazlar noktasında henüz veri bulunmamaktadır.

## Talep

Teknik değerlendirme raporu. Standart düzeyde düzenle; çerçeve adlarını hâl eki, iyelik veya fiille kur.

## Korunması gerekenler

- %35 bellek artışı ve 8 GB değeri korunmalı.
- Yöntemin erişim denetiminde değişiklik gerektirmediği korunmalı.
- Daha düşük bellekli cihazlar için `henüz` veri bulunmadığı sınırı korunmalı.
- Performans, güvenlik ve uygulanabilirlik olmak üzere üç değerlendirme eksenini ayıran yapı korunabilmeli; eksen adları gerekiyorsa kalabilir.

## Kaçınılması gerekenler

- Aynı cümlede `bağlamda`, `açısından`, `kapsamında`, `noktasında` yığınını bırakmak
- Çerçeve adlarını "yönünden", "itibarıyla", "ekseninde" gibi başka çerçevelerle değiştirmek
- "Değerlendirilmesi gereken temel husus" çerçevesini korumak
- Bellek artışını kaynakta olmayan bir nedene bağlamak
- `Henüz` sınırını silmek veya düşük bellekli cihazlarda çalışmadığını iddia etmek
- Teknik tonu gündelikleştirmek

## Yapısal beklenti

- çerçeve yığını: 0
- sert işaret: 0
