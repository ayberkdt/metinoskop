# Teknik terim ve gösterim tutarlılığı

## Kaynak

GRGM1200 yerçekimi modeli, 1200 derece ve 1190 mertebeye kadar kullanıldı. Denklem (3), Δv değerini km/s cinsinden verir. RK4 çözücüsünde tolerans 10⁻⁶ olarak ayarlandı; sonuç 2,40 ± 0,03 km/s bulundu.

## Talep

Metni doğal ve akıcı teknik Türkçeyle düzenle. Terimleri, sembolleri ve sayısal gösterimleri koru.

## Korunması gerekenler

- `GRGM1200` model adı ve `RK4` yöntem adı aynı yazılmalı.
- 1200 derece ile 1190 mertebe arasındaki kavramsal ayrım korunmalı.
- Denklem numarası `(3)` değişmemeli.
- `Δv`, `km/s`, `10⁻⁶` ve `±` işaretleri korunmalı.
- `2,40 ± 0,03 km/s` değeri ve ondalık virgüller değişmemeli.

## Kaçınılması gerekenler

- Derece ve mertebe terimlerini eş anlamlı gibi değiştirmek veya birleştirmek
- `Δv` sembolünü başka bir değişkenle değiştirmek
- `10⁻⁶` değerini yuvarlamak ya da düz metinde farklı bir büyüklüğe çevirmek
- Denklem numarasını bölüm numarası gibi yorumlamak
- Ondalık virgülleri noktaya çevirmek
- `±` işaretini kaldırmak veya belirsizliği kesin değere dönüştürmek
