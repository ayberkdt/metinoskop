# Kavramsal giriş

## Kaynak

Sistem aynı veritabanı sorgularını tekrar tekrar çalıştırıyor. Bu tekrarlar ortalama yanıt süresini 800 milisaniyeye çıkarıyor. Önbellek, sık kullanılan sorguların sonuçlarını saklıyor. Önbellek etkinleştirildiğinde bu sistemde ortalama yanıt süresi 240 milisaniyeye indi.

## Talep

Önbellek kavramını tanıtan kısa bir giriş yaz. Bağlam, problem, soru ve çözüm arasında bütünlüklü bir akış kur.

## Korunması gerekenler

- Tekrarlanan veritabanı sorguları gerçek problem olarak görünmeli.
- 800 ve 240 milisaniye değerleri doğru bağlamda korunmalı.
- Önbelleğin sık kullanılan sorgu sonuçlarını sakladığı açıklanmalı.
- Sonucun yalnızca `bu sistemde` ölçüldüğü sınırı korunmalı.
- Kavram, girişteki gerçek soruya cevap vermeli.

## Kaçınılması gerekenler

- Siber güvenlik, maliyet veya ölçeklenebilirlik gibi kaynakta olmayan sorunlar eklemek
- Önbelleği her sistem için kesin çözüm gibi sunmak
- Tiyatral soru, yapay aciliyet veya pazarlama dili kullanmak
- Ölçülen sonucu genel performans garantisine dönüştürmek
