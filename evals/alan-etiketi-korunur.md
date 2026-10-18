# Belgenin alan etiketi korunur

## Kaynak

### Komut

`csvtara rapor.csv`

Girdi: UTF-8 kodlamalı CSV dosyası.

Çıktı: Bozuk satırların numarası ve hata türü.

Uyarı: Araç dosyayı yerinde düzeltmez; düzeltilmiş kopya için `--duzelt` seçeneği gerekir.

### Terimler

Bozuk satır: sütun sayısı başlık satırınınkiyle eşleşmeyen satır.

Kaçış hatası: tırnak içinde kapanmamış alan.

## Talep

Bu README bölümünü geliştir.

## Korunması gerekenler

- Metin olduğu gibi kalmalı: `Girdi:`, `Çıktı:`, `Uyarı:` belgenin alan etiketidir; `Bozuk satır:` ve `Kaçış hatası:` sözlük maddesidir. Etiket içeriğin türünü duyurmuyor, alanın adını veriyor.
- Komut, `--duzelt` seçeneği ve uyarının olumsuzluğu (`yerinde düzeltmez`) korunmalı.

## Kaçınılması gerekenler

- Alan etiketlerini ya da sözlük maddelerini `Etiket ve anons yok` kuralı sanıp düzyazıya çevirmek
- Uyarıyı yumuşatmak ya da seçeneği uydurulmuş bir örnekle açıklamak
- Kaynakta olmayan kurulum adımı ya da hata türü eklemek

## Yapısal beklenti

- etiketli cümle: 0
- sert işaret: 0
