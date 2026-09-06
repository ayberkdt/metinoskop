# Kısa kalması gereken paragraf

## Kaynak

Yedekleme betiği her gece 02.00'de çalışır ve tam yedeği `backup/` dizinine yazar. Yedekler 30 gün saklanır; daha eski dosyalar betik tarafından silinir. Betik, disk doluluğu %90'ı aşarsa yedek almayı atlar ve günlüğe uyarı yazar.

`--purge` seçeneği bütün yedekleri geri alınamaz biçimde siler.

Betiği elle çalıştırmak için `python backup.py --now` komutunu kullanın. Elle çalıştırma gecelik zamanlamayı değiştirmez.

## Talep

Teknik belge. Standart düzeyde düzenle.

## Korunması gerekenler

- Tek cümlelik `--purge` uyarısı ayrı paragraf olarak korunmalı; yalıtılmışlığı uyarının görülmesini sağlıyor.
- 02.00, 30 gün, %90 ve komutlar kod biçimiyle korunmalı.
- "Geri alınamaz" ifadesi korunmalı.
- Elle çalıştırmanın zamanlamayı değiştirmediği korunmalı.
- Metin zaten doğal olduğundan olduğu gibi bırakılabilmeli.

## Kaçınılması gerekenler

- Uyarı cümlesini komşu paragrafla birleştirmek
- "Geri alınamaz" ifadesini yumuşatmak veya "Dikkat!", "Önemli:" gibi tiyatral vurgu eklemek
- Paragraf sırasını değiştirmek
- İlk paragrafı üç ayrı paragrafa bölmek
- Kaynakta bulunmayan seçenek, süre veya davranış eklemek
