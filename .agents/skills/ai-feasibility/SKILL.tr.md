---
name: ai-feasibility
description: >-
  Bir ürün veya iş akışında yapay zekâya gerçekten ihtiyaç olup olmadığını; teknik uygulanabilirlik, doğruluk, maliyet, mahremiyet ve insan onayı açısından değerlendirmek için kullanılır.
---

# Yapay Zekâ Uygulanabilirliği

## Karar sorusu
Bu işi yapay zekâ ile yapmak gerçekten doğru mu? Kurallı bir otomasyon, veritabanı sorgusu veya insan kontrolü daha güvenilir ve ekonomikse onu öner. Sırf güncel teknoloji olduğu için model kullanma.

## Değerlendirme
1. Kullanıcıyı, çözülmesi gereken işi, girdileri, istenen çıktıyı ve yanlış sonucun etkisini tanımla. Sınıflandırma, veri çıkarma, özetleme, arama veya gerçek eylem türünü ayır.
2. Önce model gerektirmeyen bir başlangıç çözümü belirle: iş kuralı, şablon, mevcut arama, geleneksel otomasyon veya manuel inceleme.
3. Yapay zekânın katkısı varsa en fazla iki yaklaşımı kıyasla. Örneğin yapılandırılmış veri çıkarma ile kaynak destekli yanıt üretimi. Gereken veri, bağlam, izin ve gerçek entegrasyonları açıkla.
4. Kişisel ve ticari verinin korunması, gizlilik, dış sağlayıcıya aktarım, kötü niyetli girdi ve yanıt sızması risklerini değerlendir. Etkisi yüksek veya geri dönüşsüz işlerde insan onayı öner.
5. Hata toleransı, gecikme, kullanım hacmi, maliyet varsayımları, gözlemlenebilirlik ve güvenli geri dönüş yolunu incele. Maliyet rakamının kaynağını veya yalnızca örnek olduğunu belirt.
6. Yetkili ve temsilî örneklerle küçük bir çevrimdışı değerlendirme öner: model dışı başlangıç, başarı ölçütleri, hata türleri ve üst maliyet sınırı. Gerçekte yapılmamış denemeyi yapılmış gibi gösterme.
7. Açık karar ver: yapay zekâ, klasik otomasyon, hibrit çözüm veya yetersiz kanıt. Kararı değiştirebilecek veriyi yaz.

## Çıktı
Karar özeti, alternatif karşılaştırması, veri ve güvenlik gereksinimleri, maliyet varsayımları, küçük değerlendirme planı ve devam/etmeme kriterleri.

## Sınırlar
İzin olmadan gerçek müşterinin özel verisini modele gönderme, ücretli API çağrısı başlatma veya otomatik yayın/işlem yetkisi varsayma. Doğruluk yüzdesi, uyum sertifikası veya sağlayıcı özelliği uydurma. Kabul edilen çözümü ayrıntılı otomasyona dönüştürmek için `workflow-architect` kullan.
