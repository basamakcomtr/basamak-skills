---
name: workflow-architect
description: >-
  İş otomasyonlarında tetikleyici, veri akışı, entegrasyon, hata kurtarma, yinelenen olay ve insan onayı tasarlamak için kullanılır. Canlıya alma veya gerçek sistemlerde işlem yapma yetkisi vermez.
---

# Otomasyon İş Akışı Mimarisi

## Amaç
Doğrulanmış bir iş sonucuna ulaşan, mümkün olduğunca sade ve güvenilir bir otomasyon tasarlamak. Hangi sürecin otomasyona alınacağı henüz kararlaştırılmadıysa önce `automation-discovery` kullanılmalı.

## Tasarım adımları
1. İş sahibini, tetikleyiciyi, beklenen çıktıyı, asıl veri kaynağını, işlem hacmini ve hata durumunda ne olması gerektiğini tanımla. Mevcut sistem yeteneklerini önerilen yeteneklerden ayır.
2. Süreci durumlarla göster: alındı, doğrulandı, işlendi, tamamlandı, hata, insan incelemesi. Aynı olayın iki kez gelmesi veya yarıda kesilmesi gibi durumları unutma.
3. Her adımı mevcut sisteme veya önerilen bileşene bağla. Dış entegrasyon için veri yönünü, gerekli alanları, erişim sahibini, doğrulanmış sınırları ve devre dışı kalırsa izlenecek yolu yaz.
4. Önce kesin kuralları değerlendir. Yapay zekâ gerekiyorsa girdiyi, çıktı şemasını, belirsizlik eşiğini, insan denetimini ve güvenli geri dönüş yolunu belirle.
5. Gerçek işlem üreten adımlarda tekrar çalıştırma güvenliğini değerlendir: tekillik anahtarı, sınırlı yeniden deneme, zaman aşımı, kayıt, yanlışlıkla ikinci mesaj veya ödeme üretmeme. Basit işte gereksiz kuyruk veya mikroservis dayatma.
6. Onay noktalarını, erişim yetkilerini, kişisel veri risklerini ve hata görüldüğünde operatörün nasıl müdahale edeceğini açıkla.
7. Üç ila altı geliştirme işi ve başarı, tekrar eden olay, servis hatası, manuel müdahale için doğrulanabilir kabul senaryoları yaz.

## Çıktı
Hedef, metinsel iş akışı diyagramı, adım/girdi/çıktı/hata tablosu, açık varsayımlar, ihtiyaç duyulan entegrasyonlar, kısa iş planı ve kurtarma senaryoları.

## Güvenlik
Doğrulamadan API, veritabanı tablosu veya erişim bilgisi varmış gibi davranma. Yetki olmadan canlı iş akışı çalıştırma, zamanlama, dosya silme, bildirim gönderme veya müşteri verisi değiştirme. Yapay zekâ riskinde `ai-feasibility`, kod geliştirme planında `software-planner` ile birlikte çalış.
