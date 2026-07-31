# Davranışsal değerlendirmeler

Bu klasördeki vakalar tek bir beklenen metni dayatmaz. Amaç, farklı geçerli düzenlemelerin aynı kaynak sadakati ve editoryal sınırlar içinde kalıp kalmadığını değerlendirmektir.

Her vaka için:

1. `Kaynak` ve `Talep` bölümlerini `$metinoskop` ile çalıştırın.
2. Çıktıyı `Korunması gerekenler` maddeleriyle karşılaştırın.
3. `Kaçınılması gerekenler` bölümündeki ihlallerden herhangi biri varsa vakayı başarısız sayın.
4. Tek bir cümle yapısını veya sözcük seçimini zorunlu tutmayın.

Yeni bir davranış kuralı eklenirken en az bir mevcut vaka güncellenmeli veya yeni bir vaka eklenmelidir.

## Deterministik ön denetim

Bir model çıktısını kaynakta açıkça korunan değişmezler bakımından denetlemek için:

```bash
python scripts/eval-runner.py evals/teknik.md outputs/teknik.txt
```

Çalıştırıcı sayı, tarih, URL, kod, dipnot, kapsam belirleyicisi, teknik ad, sembol, denklem numarası ve ölçüm kayıplarını yakalar. Birebir çıktı karşılaştırması yapmaz. Akıcılık, ton, gönderge yorumu ve genel anlam uyumu elle veya model hakemiyle değerlendirilmelidir.

Rapor vakalarında ayrıca bulgu, yorum, sınırlılık, öneri ve karar statülerinin korunup korunmadığını; tablo, başlık ve çapraz göndermelerin doğru içeriğe bağlı kalıp kalmadığını inceleyin. Bu ilişkiler yalnızca sözcük varlığıyla güvenilir biçimde ölçülemediği için değerlendirme insan veya model hakemi gerektirir.
