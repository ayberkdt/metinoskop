# Türkçe bağlayıcılarla zaten iyi bağlanmış metin korunur

## Kaynak

Basınç 2 bar'ın altına düştüğünde vana kapanır; sistem ancak basınç yeniden 2,5 bar'a çıkınca açılır. Vana kapalıyken pompa çalışmaya devam ederse hat ısınır, bu yüzden pompa da aynı sinyalle durdurulur. Bakım sırasında sinyal elle verilebilir, ama bu durumda vananın kapandığı göstergeden doğrulanmalıdır.

## Talep

Bu teknik açıklamayı doğallaştır.

## Korunması gerekenler

- Metin zaten doğal; ilişkiler ek ve bağlaç kaynaklarıyla (`-diğinde`, `ancak ... -ınca`, `-ken`, `-se`, `bu yüzden`, `ama`) doğru kurulmuş. Olduğu gibi bırakılabilmeli.
- 2 bar, 2,5 bar eşikleri ve aralarındaki fark korunmalı.
- Koşul (`devam ederse`), neden (`bu yüzden`) ve zorunluluk (`doğrulanmalıdır`) korunmalı.
- Genel sistem davranışını anlatan geniş zaman korunmalı.

## Kaçınılması gerekenler

- `ancak ... çıkınca` sınırlamasını silmek ya da `ancak` bağlacını karşıtlık sanıp değiştirmek
- Ekleri cümle başı bağlaçlara açmak (`Basınç 2 bar'ın altına düşer. Bu durumda vana kapanır.`)
- `bu yüzden` bağlacını sırf çeşitlilik için `dolayısıyla`, `bu nedenle` ile değiştirmek
- Geniş zamanı geçmişe çevirmek ya da zorunluluğu tavsiyeye indirmek

## Yapısal beklenti

- sert işaret: 0
- yakın tekrar: 0
- cümle: 3
- düzyazı paragrafı: 1
