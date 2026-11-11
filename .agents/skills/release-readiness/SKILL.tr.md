---
name: release-readiness
description: >-
  Bir yazılım sürümünün canlıya alınmadan önce gerçek değişiklik, test sonucu, veri geçişi, operasyonel etki ve geri alma imkânıyla değerlendirilmesi için kullanılır. Yapılmayan testleri yapılmış saymaz.
---

# Canlıya Çıkış Hazırlığı

## Hedef
Belirli bir sürüm için kanıta dayalı **yayına hazır / koşullu hazır / hazır değil** kararı üretmek. Her sürümde uzun bir kontrol listesi çalıştırmak yerine gerçek riskleri belirle.

## İnceleme
1. Depoyu, dalı veya commit kimliğini, hedef ortamı, yapılacak değişikliği ve dağıtım yolunu kaydet. Gerçek sürüm bilinmiyorsa önce doğrulanması gerektiğini belirt.
2. Kod farkı veya doğrulanmış değişiklik özetine göre riskleri ayır: kimlik doğrulama, yetki, veritabanı, ödeme, arka plan işleri, entegrasyon, URL/SEO, önbellek ve bağımlılıklar.
3. Her ciddi riske uygun küçük bir doğrulama eşleştir. Var olan test sonuçları ile henüz çalıştırılması önerilen testleri kesin olarak ayır; test adı ve kapsamını yaz.
4. Gerektiğinde ortam ayarlarını, gizli anahtarların varlığını ifşa etmeden, zamanlanmış işleri, veritabanı yedeğini, izleme imkanını ve yayın sonrası geri dönüş yolunu değerlendir.
5. Geri alınabilir ve geri alınamaz adımları ayır. Özellikle veritabanı değişikliğinde kodun eski sürüme dönmesinin veriyi otomatik olarak geri getirmeyeceğini belirt.
6. Engelleyici sorunları ve yalnızca izlenmesi gereken riskleri ayır. En kısa güvenli yayın sırasını öner: ön kontrol, yayın, kritik ekran/süreç kontrolü, gözlem ve gerektiğinde geri alma.

## Çıktı
İncelenen sürüm, kanıt seviyesi, önemli riskler, gerçekten çalıştırılmış testler, eksik kontroller, yayın kararı ve kısa geri alma yaklaşımı.

## Kurallar
CI sonucunun yeşil olması tek başına kusursuzluk garantisi değildir. Ancak küçük bir metin değişikliği için kapsam dışı ağır test yükü de önermemelisin. İzin olmadan PR birleştirme, canlı yayın, migration, gizli anahtar değiştirme veya veri silme. Satır bazlı incelemede `code-reviewer`, canlı hatada `technical-troubleshooter` kullan.
