# İnsan ve yapay metin: araştırma bulguları

LLM metnini insan metninden ayıran ölçülmüş farklar ve Metinoskop'taki karşılıkları. Bulgular İngilizce derlemlerdendir. AI ve insan Türkçesini üslup bakımından karşılaştıran hakemli bir çalışma bulunamadı (2026-10 taraması); Türkçe karşılıklar bu yüzden çıkarımdır ve depo vakalarıyla sınanmıştır.

Güven: **A** birden çok bağımsız çalışma aynı yönü buldu; **B** tek çalışma, büyük derlem; **C** modele ya da türe göre değişiyor.

## Bulgular ve kararlar

| # | Bulgu | Kaynak | Güven | Türkçe karşılığı | Karar |
|---|---|---|---|---|---|
| 1 | Talimatla ayarlanmış modeller şimdiki zaman ortaç yan cümlesini insanın 2–5 katı kullanır (GPT-4o 5,3 kat). | Reinhart 2025, giriş ve Şekil 3 | B | Cümle sonuna virgülle eklenen `-arak/-erek` kuyruğu (`…indirdi, kullanıcı deneyimini iyileştirerek.`) ve `, bu da … sağlamaktadır` eki | Kuyruk önerme taşıyorsa öznesiyle ayrı cümle; yalnızca önem söylüyorsa sil. Cümle içindeki doğal zarf-fiil (`ölçerek denetledi`) kalır. |
| 2 | LLM metni insan metnine göre 1,5–2 kat fazla adlaştırma içerir. | Reinhart 2025; Herbold 2023, Tablo 3–4 | A | `analizinin gerçekleştirilmesi`, `değerlendirme yapılması` | Yüklemi çekimli fiille kur; teknik işlem adı ve akademik terim kalır (kural 4). |
| 3 | LLM cümleleri 10–30 sözcük bandında toplanır; insan metninde uzun cümle daha sık, uzunluk dağılımı daha geniştir. | Muñoz-Ortiz 2024, §4.1.1, Şekil 3 | B | Bütün cümleleri orta uzunluğa çeken düzenleme | Tek ilişki taşıyan uzun cümleyi bölme; ana bulgu kısa cümleyle verilebilir. Uzunluğu rastgeleleştirme: değişkenlik içerikten gelir. |
| 4 | 2024 biyomedikal özetlerindeki fazla sözcüklerin neredeyse tamamı biçem sözcüğüdür; 379 biçem sözcüğünün %66'sı fiil, %14'ü sıfat. Önceki kaymalar içerik adıydı. | Kobak 2025, §2.1; Liang 2024; Juzek 2025 | A | `altını çizmek`, `vurgulamak`, `gözler önüne sermek`, `derinlemesine incelemek`, `kritik`, `kayda değer`, `kapsamlı`, `çok yönlü`, `zengin`, `dinamik` | Biçem fiilinin yerine gösterilen şeyi yaz (`önemini vurguluyor` → hangi değer, hangi fark). Sözcük yasağı değildir; işlevine bakılır. |
| 5 | ChatGPT denemeleri insan denemelerinden daha az kiplik ve kanıt işareti, daha çok adlaştırma içerir. | Herbold 2023, özet ve Tartışma | B | Kesin konuşan, çekincesiz AI metni | Çekinceyi "AI izi" diye silme. Yazarken bilginin statüsünü kaynağın düzeyinde işaretle; kaynakta olmayan çekince de ekleme. Downtoner kullanımı model ailesine göre ters yönlü (Reinhart); "AI çok çekince kullanır" genellemesi desteklenmez. |
| 6 | LLM metni daha nötr ve daha olumlu; insan haberinde korku ve tiksinti daha çok. | Muñoz-Ortiz 2024, özet; Guo 2023 (HC3), Şekil 3 | A | `başarısız oldu` → `beklenen düzeye ulaşamadı`; `sorun` → `gelişime açık alan` | Olumsuz bulguyu ve eleştiriyi kaynağın sertliğiyle yaz. Yumuşatma, kesinliği değiştirmenin bir türüdür. |
| 7 | Model çıktılarının %92–100'ü söz dizimi şablonu (yinelenen POS 6-gramı) içerir; insan referanslarında %36–46. Model büyüklüğü ve örnekleme ayarı bunu azaltmaz. | Shaib 2024, Tablo 3 ve §7 | B | Her paragrafı aynı kalıpla açmak, her cümleyi aynı yüklem kalıbıyla bitirmek | Cümle kuruluşu bilgiye göre değişir; ardışık cümlelerde aynı iskeleti yinelemek yerine ilişkiyi Türkçenin kaynaklarıyla kur. |
| 8 | ChatGPT denemelerinin hepsi aynı kapanış kalıbıyla biter; HC3 gönüllüleri `Firstly … Finally` iskeletini ve düzenli, resmî yapıyı not eder. | Herbold 2023, Tartışma; Guo 2023, §3.2 | B | `Sonuç olarak`, `İlk olarak … Son olarak`, her bölümde aynı giriş-kapanış | İskeleti tür ve içerik belirler; yol haritası ve kalıp kapanış kuralları geçerlidir. |
| 9 | Talimatla ayarlanmış model yazarları birbirine benzetir (içerik homojenleşmesi); etki modelin eklediği metinden gelir. | Padmakumar 2024, §4–6 | B | Her konuya uyan genel cümle | Kaynağın kendine özgü ayrıntısını öne al; genel önem cümlesi kurma. |
| 10 | ChatGPT cevapları daha uzun (ortalama 198'e karşı 143 sözcük) ama sözcük dağarcığı daha dar. | Guo 2023 (HC3), Tablo 3 | B | Bilgi eklemeden uzayan cevap | Uzunluk bilgi miktarını izler. |
| 11 | Çok dilli LLM'lerin söz dizimi hedef dilden çok İngilizceye benzer (Çince ve Fransızca için ölçüldü). | Guo 2025, §4.3 | C (Türkçe ölçülmedi) | Çeviri kokusu | `turkce-ritim-ve-ceviri-kokusu.md` kuralları; Türkçe için çıkarımdır. |
| 12 | Sözcük çeşitliliği ölçüye, modele ve insan karşılaştırma grubuna göre ters yönlü çıkar. | Herbold 2023; Muñoz-Ortiz 2024; Guo 2023 | C | — | Eş anlamlı döndürerek çeşitlilik üretme; terim sabit kalır. |

## Yanılgılar

- **"İnsan metni daha değişkendir, öyleyse uzunluğu ve sözcüğü değiştir."** Değişkenlik içerikten gelir. Cümle uzunluğunu rastgeleleştirmek, eş anlamlı döndürmek ya da hata eklemek insanlaştırmaz; Metinoskop dedektör atlatmaz. Depo ölçümünde iyi yazılmış kısa Türkçe metinlerin uzunluk değişkenliği yapay örnekten düşük çıktı; değişkenlik eşiği bu yüzden denetime konmadı.
- **"AI çok çekince kullanır, çekinceyi sil."** Ölçülen yön çoğu zaman terstir (bulgu 5). Çekince kanıt düzeyidir.
- **"Edilgeni etkene çevir, daha insani olur."** GPT-4o failsiz edilgeni insanın yaklaşık yarısı oranında kullanır (Reinhart 2025). Edilgen kararı aktörün bilgi değerine bakar (kural 6).
- **"Belirli sözcükleri yasakla."** Fazla sözcükler bir işlev ailesidir (biçem fiili, değerlendirme sıfatı). Aynı sözcük doğru işlevde kalır.

## Kaynaklar

PDF'ler bu depoya konmaz; bağlantılar açık erişimlidir.

- Reinhart A. ve ark. (2025). Do LLMs write like humans? Variation in grammatical and rhetorical styles. *PNAS* 122, e2422455122. https://arxiv.org/abs/2410.16107
- Herbold S. ve ark. (2023). A large-scale comparison of human-written versus ChatGPT-generated essays. *Scientific Reports* 13. https://arxiv.org/abs/2304.14276
- Guo B. ve ark. (2023). How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection (HC3). https://arxiv.org/abs/2301.07597
- Muñoz-Ortiz A., Gómez-Rodríguez C., Vilares D. (2024). Contrasting Linguistic Patterns in Human and LLM-Generated News Text. *Artificial Intelligence Review* 57:265. https://arxiv.org/abs/2308.09067
- Shaib C. ve ark. (2024). Detection and Measurement of Syntactic Templates in Generated Text. EMNLP 2024. https://arxiv.org/abs/2407.00211
- Padmakumar V., He H. (2024). Does Writing with Language Models Reduce Content Diversity? ICLR 2024. https://arxiv.org/abs/2309.05196
- Kobak D. ve ark. (2025). Delving into LLM-assisted writing in biomedical publications through excess vocabulary. *Science Advances* 11(27). https://arxiv.org/abs/2406.07016
- Liang W. ve ark. (2024). Mapping the Increasing Use of LLMs in Scientific Papers. COLM 2024. https://arxiv.org/abs/2404.01268
- Juzek T., Ward Z. (2025). Why Does ChatGPT "Delve" So Much? COLING 2025. https://arxiv.org/abs/2412.11385
- Shaib C. ve ark. (2025). Measuring AI "Slop" in Text. https://arxiv.org/abs/2509.19163
- Mitchell E. ve ark. (2023). DetectGPT. ICML 2023. https://arxiv.org/abs/2301.11305
- Guo Y. ve ark. (2024). The Curious Decline of Linguistic Diversity. Findings of NAACL 2024. https://arxiv.org/abs/2311.09807
- Üyük C. ve ark. (2024). Crafting Tomorrow's Headlines: Neural News Generation and Detection in English, Turkish, Hungarian, and Persian. NLP4PI 2024. https://arxiv.org/abs/2408.10724
- Guo Y. ve ark. (2025). Do Large Language Models Have an English "Accent"? ACL 2025. https://arxiv.org/abs/2410.15956
