# Otomasyon fırsatından iş akışı tasarımına

[**English**](automation-opportunity-to-design.md) · [Ana sayfa](../README.tr.md)

**Hedef:** Tekrarlanan bir işi anlamak, otomasyona ve gerekiyorsa yapay zekâya uygunluğunu değerlendirmek, onaylanmış süreci güvenli bir teknik tasarıma dönüştürmek.

Bu bir **manuel devir rehberidir**. Kendi kendine çalışan bir ajan, entegrasyon ya da müşteri sistemlerine erişim değildir. Önceki aşamanın çıktısı sonrakine aktarılır.

## 1. Otomasyon fırsatını seç

**Beceri:** [automation-discovery](../.agents/skills/automation-discovery/SKILL.tr.md)

```text
Müşteriden belge toplama işimizin mevcut adımlarını, sıklığını,
hatalarını ve insan onayı gereken noktalarını incele.
En fazla üç fırsatı sırala. Henüz gerçek işlem yapma.
```

**Devir:** Süreç haritası, fırsat öncelikleri, veri boşlukları ve ilk küçük kapsam.

**Karar:** İş sahibi yalnızca uygun bulduğu kapsamı seçer.

## 2. Yapay zekâ gerekip gerekmediğini belirle

**Beceri:** [ai-feasibility](../.agents/skills/ai-feasibility/SKILL.tr.md)

```text
Seçilen belgenin sınıflandırılması için kurallar ile yapay zekâyı
karşılaştır. Veri mahremiyeti, hata maliyeti, ölçüm yöntemi
ve model dışı geri dönüşü belirt. Ücretli çağrı yapma.
```

**Devir:** Yapay zekâ/klasik otomasyon/hibrit kararı ve doğrulama planı.

**Karar:** Model kullanımı yalnızca gerekli izin ve maliyet sınırlarıyla kabul edilir.

## 3. İş akışını tasarla

**Beceri:** [workflow-architect](../.agents/skills/workflow-architect/SKILL.tr.md)

```text
Onaylanan bölüm için en basit güvenli otomasyon tasarımını çıkar.
Tetikleyici, adımlar, durumlar, çift çalışma riski, hata kurtarma,
erişim izinleri ve insan onayını belirt. API uydurma, yayın yapma.
```

**Devir:** Akış, doğrulanan ve varsayılan entegrasyonlar, kabul kriterleri ve geliştirme işleri.

## 4. Geliştirme ve yayına hazırlık

Geliştirme görevleri için [software-planner](../.agents/skills/software-planner/SKILL.tr.md), yetkili ekip kodu hazırladıktan sonra **gerçek PR/diff ve test kanıtlarıyla** [code-reviewer](../.agents/skills/code-reviewer/SKILL.tr.md) ve [release-readiness](../.agents/skills/release-readiness/SKILL.tr.md) kullanılır.

**Karar:** Kod değişikliği, birleştirme ve canlıya alma için ayrı yetki gerekir.

## Devir özeti

```text
İş hedefi:
Mevcut süreç ve kanıtlar:
Seçilen otomasyon / elenen alternatifler:
Yapay zekâ kararı ve gerekçesi:
Entegrasyonlar ve erişim sahibi:
Veri riskleri / insan onayı:
Durumlar, tekrar deneme ve kurtarma:
Kabul kriterleri:
Gerçek test kanıtı:
Sıradaki karar:
```

Müşteri verilerini, kimlik bilgilerini ve özel sistem ayarlarını bu açık depoya eklemeyin.
