---
name: web-audit
description: >-
  Web sitelerini ve açılış sayfalarını kullanıcı deneyimi, içerik, güven,
  erişilebilirlik ve dönüşüm akışı açısından kanıta dayalı incele.
  Kullanıcı bir site değerlendirmesi veya öncelikli iyileştirme planı istediğinde kullan.
---

# Web Audit

## Amaç ve sınır

Bir web sitesinin ziyaretçi açısından nasıl çalıştığını değerlendir ve en değerli iyileştirmeleri öner. Bu beceri bir tasarım incelemesidir; erişim testi, güvenlik taraması, performans ölçümü veya canlı sistem düzenlemesi değildir.

## Uygulama

1. **Hedefi belirle.** Site adresini, hedef kitleyi ve istenen ziyaretçi eylemini mevcut konuşmadan çıkar. Bilgi eksikse makul kapsam belirle; uzun anket yapma.
2. **Erişimi doğrula.** Mevcut araçlarla ana sayfayı ve kritik ziyaretçi yolculuğuna ait en çok üç ilgili sayfayı incele. Kaynak adresini ve inceleme tarihini kaydet. Erişim yoksa bunu açıkça söyle.
3. **Gördüğünle tahmin ettiğini ayır.** Metin/HTML incelemesi, ekran görüntüsü, tarayıcı üzerinden mobil emülasyon, fiziksel mobil cihaz ve kullanıcı davranışı birbirine eşdeğer değildir. Görsel inceleme yapıldıysa kullanılan görünüm türünü ve mümkünse ekran/viewport genişliği ile yüksekliğini kaydet. Mobil emülasyonu gerçek cihaz testi olarak sunma. Ekran görüntüsü olmadan renk, boşluk ve mobil yerleşim hakkında kesin hüküm kurma.
4. **Yolculuğu kontrol et.** İlk ekranda sunulan değer, gezinme, hedef kitleye hitap, harekete geçirici çağrılar, form/iletişim adımları, güven unsurları, içerik açıklığı ve olası erişilebilirlik engellerini değerlendir.
5. **Bulguları seç.** En fazla beş güçlü bulgu sun. Her biri için sayfa, gözlenen kanıt, ziyaretçi üzerindeki olası etki, uygulanabilir öneri ve öncelik ver.
6. **Doğrulama sınırını koru.** Ölçüm aracı çalışmadıysa hız puanı, SEO sıralaması, dönüşüm artışı veya kullanıcı davranışı uydurma. Görsel kanıt yoksa görsel değerlendirme yapıldığını iddia etme. Sayfadaki örnek arayüz, reklam tasarımı, hata mesajı veya örnek rakamları sitenin gerçek teknik durumu ya da ölçülmüş performansı sanma; "görselde yer alan örnek" olarak ayır ve belirsizlik varsa belirt.
7. **Güvenli kal.** Form gönderme, ödeme yapma, hesaba giriş yapma, site dosyalarını değiştirme veya otomatik tarama yükü oluşturma. Bu işlemler ayrıca açıkça yetkilendirilmelidir.

## Çıktı

- **İnceleme kapsamı:** URL'ler, tarih, kanıt türü (metin/HTML / masaüstü görsel / mobil emülasyon / fiziksel mobil cihaz). Görsel inceleme yapıldıysa kullanılan viewport veya ekran boyutlarını mümkün olduğunca belirt; görüntü alınamadıysa açıkça yaz.
- **Ana sonuç:** En önemli iyileştirme alanını 1-2 cümleyle açıkla.
- **Öncelikli bulgular:** En fazla beş madde; kanıt türü, sayfa/bölüm, olası etki, öneri, öncelik ve yaklaşık efor. Varsa her görsel bulguya ilgili ekran görüntüsünün gerçek referansını iliştir; referans mevcut değilse uydurma bağlantı veya görüntü numarası verme.
- **Uygulama sırası:** Önce yapılacak 2-3 küçük adım.
- **İncelenemeyenler:** Mobil görünüm, form davranışı, analitik veya performans gibi doğrulanamayan alanlar.

Raporu kullanıcı istemedikçe dosyaya yazma. Kullanıcı dosya isterse raporu `work/web-audit/` altında tut; özel raporları Git'e ekleme.
