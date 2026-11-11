---
name: software-planner
description: >-
  Yazılım özellik, entegrasyon veya geliştirme taleplerini uygulanabilir
  kapsama, teknik yaklaşım seçeneklerine, küçük geliştirme görevlerine ve
  ölçülebilir kabul kriterlerine dönüştür. Kullanıcı bir yazılım işi için
  plan, backlog veya teknik görev kırılımı istediğinde kullan. Kod yazma,
  dağıtım veya CRM kaydı oluşturma yetkisi vermez.
---

# Software Planner

## Amaç ve kullanım

Bir yazılım talebini yazılım ekibinin uygulayabileceği **küçük, açık ve
doğrulanabilir** bir plana dönüştür. Beceriyi yeni özellik, mevcut özelliğin
iyileştirilmesi, entegrasyon, sürüm geçişi veya teknik iş listesi hazırlamak
için kullan. Teknoloji, süre, maliyet, mevcut ürün yeteneği ya da iş akışına
dair kanıt bulunmayan iddialar üretme.

Bu beceri plan hazırlar; kullanıcı istemedikçe kodu değiştirmez, gerçek
görev kaydı açmaz, PR oluşturmaz, yayına almaz.

## Çalışma yöntemi

1. **Talebi ve beklenen sonucu anla.** Kullanıcının verdiği metin, destek
   kaydı, ürün bağlamı veya mevcut dosyalardan hedef kullanıcıyı,
   yaşadığı problemi ve beklediği davranışı çıkar. Zaten bilinen
   bilgileri tekrar sorma. Sonucu açık değilse en küçük uygulanabilir
   varsayımı belirt; karar için gerçekten gerekli tek soruyu sor.
2. **Gerçek durum ile öneriyi ayır.** Depo, şema, ekran veya API erişimi
   varsa yalnızca ilgili alanları salt okunur incele; dosya yolu ve
   işlev adlarıyla kanıt göster. Erişim yoksa mimariyi, veritabanı
   tablolarını, mevcut özelliği, kullanılan servisleri ve API uçlarını
   icat etme. Gerekli teknik keşfi ayrı bir ilk görev olarak belirt.
3. **Kapsamı sınırla.** Kullanıcının istediği çekirdek akışı 1-2 cümlede
   özetle. **Dahil olanlar**, **kapsam dışı kalanlar** ve varsa
   **bağımlılıklar** açık olsun. Sırf mümkün diye yönetim paneli,
   kapsamlı yeniden tasarım veya yeni bir teknoloji önerme. Mevcut
   mimariyle en az müdahaleli çözümü önce değerlendir.
4. **Kullanıcı akışını tarif et.** Tetikleyici, beklenen işlem,
   başarılı sonuç ve önemli hata/boş durumlarını belirt. İlgiliyse
   rol ve yetkileri, çoklu kullanıcı davranışını ve erişilebilirliği
   düşün; bunları varsayılan ürün özellikleri olarak sunma.
5. **Teknik yaklaşımı seç.** Bilinen altyapıyla uyumlu en küçük
   yaklaşımı yaz. Teknik belirsizlik gerçek bir tasarım kararını
   etkiliyorsa en fazla iki seçenek ve kısa artı/eksi sun. Veri
   değişikliği, taşıma, mevcut kayıtlarla uyumluluk, güvenlik,
   gizlilik, hata yönetimi ve geri dönüş gereksinimini sadece
   ilgiliyse ekle. Üretimdeki verileri temizlemeyi varsayma.
6. **Görevleri uygulanabilir parçalara ayır.** Tercihen 3-6 iş paketi
   oluştur; gereksiz alt görev kalabalığı yaratma. Her görev için
   eylem, ilgili alan veya bileşen (biliniyorsa), bağımlılık ve
   doğrulanabilir **bitti ölçütü** yaz. Önce kritik belirsizliği
   kaldır; sonra geliştirme, ilgili kontroller ve yayına hazırlık
   sırasını kur. Sahip, tarih, efor veya maliyet kullanıcı
   sağlamadıysa kesin değer uydurma.
7. **Kabul kriterlerini ölçülebilir yaz.** Kullanıcının gözlemleyebileceği
   şekilde **verildiğinde / yapıldığında / beklenen** mantığıyla
   normal akış ve önemli başarısızlık senaryosu yaz. "Düzgün
   çalışır", "hızlı olur" gibi doğrulanamaz hedeflerle yetinme.
8. **Doğrulama ve yayımlama ayrımı yap.** Değişikliğe en yakın küçük
   birim, entegrasyon veya manuel senaryoları öner. Testlerin
   gerçekten çalıştırılmadığını belirt; ölçülmemiş performans
   ve güvenlik garantisi verme. Üretime geçiş, veri migrasyonu,
   bakım penceresi veya geri dönüş riski varsa ayrıca belirt.
9. **Yetki ve veri güvenliğini koru.** Planın hazırlanması kodu,
   CRM'yi, müşteriyi veya canlı sistemi değiştirme izni değildir.
   Yetki verilmedikçe commit, push, görev açma, deploy, veri yazma,
   silme, izin genişletme ya da gerçek entegrasyon çağrısı yapma.
   Gizli anahtarları ve müşteri verilerini rapora veya Git'e taşıma.

## Çıktı

Kullanıcının istediği ayrıntı düzeyine göre **uygulanabilir ve kısa**
bir plan ver. Basit taleplerde gereksiz başlıkları birleştirebilirsin.

1. **Hedef ve kanıt düzeyi:** Ne değişecek, hangi kullanıcı için;
   neler doğrulandı, neler varsayım?
2. **Kapsam:** Dahil / kapsam dışı ve varsa bağımlılıklar.
3. **Önerilen yaklaşım:** Mevcut sistemle uyumu, önemli teknik kararlar,
   ilgili güvenlik veya veri riskleri.
4. **Geliştirme görevleri:** Sıralı, küçük, uygulanabilir işler;
   her biri için **bitti ölçütü**.
5. **Kabul kriterleri:** En az bir normal kullanım ve ilgiliyse
   bir hata/izin/boş durum senaryosu.
6. **Açık kararlar ve doğrulama:** Sadece gerçekten önemli belirsizlikler,
   asgari testler, varsa geri dönüş veya yayına alma riski.

Kapsam ya da mevcut kod hakkında bilgi yoksa bir teknoloji yığını veya
dosya yapısı uydurmak yerine **kısa teknik keşif görevi** oluştur.
Kullanıcı yalnızca CRM görev taslağı istiyorsa tek görev halinde yaz;
tüm proje planını gereksiz yere üretme.

## Diğer becerilerle bağlantı

- `support-assistant`: Müşteri mesajını sınıflandırır ve destek/CRM
  taslağını hazırlar; doğrulanmış ürün ihtiyacı `software-planner`
  için girdi olabilir.
- `technical-troubleshooter`: Çalışan bir sistemde gözlenen hatanın
  kök nedenini araştırır; bu beceri geliştirme planını çıkarır.
- `code-reviewer`: Geliştirme yapıldıktan sonra gerçek diff/PR
  üzerindeki riskleri inceler; bu beceri kod incelemesi yapıldığını
  iddia etmez.

## Örnek çağrılar

`$software-planner Tekrar kullanılan görseller için medya seçimi özelliğini en küçük kapsama ve kabul kriterlerine ayır.`

`$software-planner Bu özellik isteğini geliştiriciye verilecek 4-5 uygulanabilir göreve dönüştür; mevcut kod erişimi yoksa varsayımları açıkla.`
