---
name: subscription-lifecycle
description: >-
  Abonelik ve yıllık hizmet yenilemelerinde bildirim, ödeme doğrulama, süre dolması, pasife alma ve yeniden etkinleştirme süreçlerini güvenli biçimde tasarlamak için kullanılır. Gerçek faturalama veya hesap işlemi yapmaz.
---

# Abonelik Yaşam Döngüsü

## Amaç
Yenilemeleri müşteri açısından öngörülebilir, işletme açısından kayıtlı ve hataya dayanıklı hale getirmek. Yıllık yazılım, barındırma ve sürekli hizmet sözleşmelerinde uygulanabilir.

## Çalışma yöntemi
1. Yetkili veri kaynaklarını belirle: abonelik başlangıcı ve bitişi, sözleşmedeki yenileme koşulu, ödeme durumu, hizmet durumu, iletişim tercihleri ve sorumlu kişi. Sözleşme şartı ile sistem alışkanlığını karıştırma.
2. Gerekli durumları modelle: aktif, yenileme yaklaşıyor, vadesi geldi, varsa ek süre, süresi doldu/pasif, yenilendi/yeniden aktif. Sözleşmede yoksa otomatik ek süre veya kapatma kuralı icat etme.
3. Yenileme tutarının hesaplanması, bildirim içeriğinin hazırlanması, mesajın **gerçekte gönderilmesi**, iletim sonucunun kaydı, ödemenin doğrulanması ve hizmetin pasife alınması işlemlerini birbirinden ayır. Hazırlanan bildirim gönderilmiş sayılmaz.
4. Her geçişte zaman, saat dilimi, sorumlu, yinelenen iş güvenliği, müşteri açıklaması ve kayıt gereksinimini belirle. Cron iki kez çalışınca çift bildirim veya çift ödeme çıkmamalı.
5. Vade gününde ödeme, manuel yenileme, sözleşme tarihi değişikliği, ulaşmayan bildirim, banka havalesi gecikmesi, itiraz, pasif hizmetin yeniden açılması ve veri saklama gibi istisnaları değerlendir.
6. En sınırlı otomasyonu öner. Bildirim takvimi var diye site kapatma yetkisi çıkarma. Pasife alma veya silme için açık iş kuralı, uygun bildirim, yetki, veri koruma ve geri dönüş mekanizması iste.
7. Yenileme yaklaşan kayıtlar, doğrulanmış gönderimler, ödeme eşleştirme hataları, yanlış kapatma ve yeniden açma süresi gibi ölçütler belirle.

## Çıktı
Durum-geçiş tablosu, doğrulanmış takvim, güvenlik kuralları, istisnalar, kabul senaryoları ve insan onayı gereken adımlar.

## Güvenlik
Sözleşme oranı, TÜFE hesabı, KDV tutarı, gönderim başarısı veya müşteri ödemesi uydurma. Açık yetki olmadan fatura oluşturma, mesaj gönderme, siteyi kapatma, kaydı değiştirme veya veriyi silme. Teknik tasarım için `workflow-architect`, fiyat kararı için `pricing-review` becerisine yönlendir.
