---
name: automation-discovery
description: >-
  Tekrarlanan iş süreçlerinde otomasyon fırsatlarını iş değeri, veri hazırlığı, entegrasyon eforu ve hata riski açısından değerlendirmek için kullanılır. Yapay zekânın her iş için zorunlu olduğunu varsaymaz.
---

# Otomasyon Fırsatlarını Keşfetme

## Amaç
Bir sürecin otomasyona uygun olup olmadığını ve en önce hangi bölümün ele alınacağını belirlemek. Bazen en iyi çözüm süreçteki gereksiz adımı kaldırmak veya basit bir kural kullanmaktır.

## İnceleme
1. İş sürecini tetikleyici, sorumlu kişi, girdi, adımlar, çıktı, tekrar sıklığı ve yaşanan hatalarla birlikte tanımla. Kararı etkilemeyen ayrıntılar için uzun soru listesi oluşturma.
2. Tekrarlanan ve kurala bağlanan adımları, insan onayı gerektiren kararları ve istisnaları ayır. Otomasyon yapmama seçeneğini de değerlendir.
3. Fırsatları bilinen zaman kaybı, işlem hacmi, hata sıklığı ve iş etkisine göre karşılaştır. Veri yoksa para tasarrufu veya yatırım getirisi rakamları uydurma; niteliksel puan kullan.
4. Veri kalitesini, izinleri, mevcut uygulamaları, entegrasyon imkânlarını, sorumlu kişiyi ve hata kayıtlarını değerlendir. Kişisel veri veya gizli bilgilerin işlendiği noktaları belirt.
5. En fazla üç fırsatı beklenen değer, uygulanabilirlik, geri alınabilirlik ve risk açısından sırala. Karmaşık bir sistem değişikliği yerine sınırlı kapsamlı ilk parçayı öner.
6. Seçilen fırsat için tetikleyici → girdi → karar → çıktı → hata → insan onayı zincirini taslak olarak kur. Ayrıntılı mimari gerekiyorsa `workflow-architect` becerisine devret.

## Sonuç
Kısa süreç haritası, kanıta göre sıralanmış fırsatlar, ilk uygulanacak kapsam, başarı ölçütü, gerekli erişimler ve açık riskler.

## Sınırlar
Doğrulamadan API veya entegrasyon varmış gibi davranma. Belirli kurallarla çözülen işlemlere gereksiz yapay zekâ önerme. Kullanıcı yetki vermedikçe gerçek veriyi değiştirme, mesaj gönderme, otomasyon çalıştırma veya erişim bilgisi isteme. Bu aşama keşif ve önceliklendirmedir; canlı kurulum değildir.
