---
name: conversion-optimizer
description: >-
  Web sitesi ve açılış sayfalarında teklif, kayıt veya satış dönüşümünü düşüren sürtünmeleri kanıta göre belirlemek, öncelikli iyileştirmeleri ve küçük deneyleri tasarlamak için kullanılır. Genel site denetimi veya doğrulanmamış başarı iddiaları için kullanılmaz.
---

# Dönüşüm İyileştirme

## Amaç
Belirli bir dönüşüm hedefini etkileyen en önemli sorunları bulmak. Baştan tasarım önermek yerine kanıtlanabilir, küçük ve geri alınabilir iyileştirmelere odaklan. Genel UX denetimi gerekiyorsa `web-audit` kullan.

## Çalışma adımları
1. Dönüşüm eylemini (teklif gönderme, deneme başlatma, satın alma), hedef kitleyi, sayfaları ve mevcut ölçüm bilgisini belirle. Zaten verilen bilgileri tekrar sorma.
2. İncelenen URL ve tarihle birlikte veri kaynağını yaz: sayfa metni, gerçek ekran görüntüsü, analitik olay, kullanıcı görüşmesi veya başka bir doğrulanmış kaynak. **Gözlem, hipotez ve bilinmeyeni ayır.** Yalnızca HTML görmüşken mobil tasarımı gördüğünü iddia etme.
3. Ziyaretçi yolculuğunu baştan sona incele: giriş vaadi, ürünün anlaşılması, güven, harekete geçirici çağrı, form/ödeme ve tamamlanma durumu.
4. En fazla üç bulguyu etki olasılığı, kanıt güveni ve uygulama eforuna göre sırala. Ölçüm verisi yoksa güven düzeyini düşük tut.
5. İlk bulgu için somut metin veya etkileşim değişikliği, etkilenen bölüm, başarı ölçütü ve en küçük kabul kontrolünü yaz.
6. A/B testi öneriyorsan hipotezi, birincil metriği ve risk ölçütlerini tanımla. Trafik hacmi bilinmiyorsa anlamlı istatistiksel sonuç vaat etme.

## Çıktı
Hedef ve kanıt kaynakları; üçe kadar öncelikli sorun ve öneri; ilk uygulanacak küçük değişiklik; nasıl doğrulanacağı; doğrulanmamış alanlar.

## Güvenlik ve sınırlar
Gerçek veri olmadan dönüşüm oranı, gelir artışı, ısı haritası sonucu veya müşteri yorumu uydurma. Kullanıcı yetkilendirmedikçe canlı sayfayı değiştirme, forma veri gönderme ve analitik hesabına müdahale etme. Kişisel verileri rapora taşıma. Teknik geliştirme için `software-planner`, fiyatlandırma için `pricing-review` ile ilişkilendir.
