# Geçerli nedensel bağlaç korunur

## Kaynak

Havuz 50 bağlantı sınırına ulaştı; bu nedenle yeni istekler 30 saniye bekleyip zaman aşımına düştü. Etkilenen istek sayısı 2.140'tı.

## Talep

Olay inceleme notu. Standart düzeyde düzenle.

## Korunması gerekenler

- "Bu nedenle" bağlacı kaynağın kurduğu gerçek nedeni taşıdığı için korunabilmeli.
- 50 bağlantı, 30 saniye ve 2.140 istek korunmalı.
- Metin zaten doğalsa olduğu gibi bırakılabilmeli.

## Kaçınılması gerekenler

- Nedensel bağlacı zorlama geçiş sanıp silmek ve ilişkiyi belirsizleştirmek
- Sınır dolmasını ve zaman aşımını kronolojiye indirmek
- Kaynakta bulunmayan neden (rapor işi) eklemek
- Sayıları değiştirmek

## Yapısal beklenti

- sert işaret: 0
- cümle: 2
