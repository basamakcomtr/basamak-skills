# Basamak Skills

**Basamak Bilişim tarafından geliştirilen; dijital ürün geliştirme, büyüme ve operasyon yönetimi için açık kaynak yapay zekâ ajanı becerileri.**

[**English**](README.md) · [Kurulum](docs/kurulum.md) · [İş akışları](workflows/) · [Sürüm geçmişi](CHANGELOG.md) · [MIT lisansı](LICENSE)

Basamak Skills, **13 bağımsız uzmanlık talimatından** oluşur. Her biri kullanım koşullarını, kanıta dayalı yaklaşımı, beklenen çıktıyı ve güvenlik sınırlarını açıklar. Bunlar bir web servisi veya hesaplarınıza erişen hazır entegrasyonlar değildir.

## Beceriler

### Web ve büyüme

| Beceri | Amacı |
| --- | --- |
| [web-audit](.agents/skills/web-audit/SKILL.tr.md) | Web sitesi deneyimi ve ziyaretçi yolculuğunu değerlendirmek |
| [conversion-optimizer](.agents/skills/conversion-optimizer/SKILL.tr.md) | Dönüşüm kaybı olasılıklarını ve küçük iyileştirmeleri belirlemek |
| [saas-positioning](.agents/skills/saas-positioning/SKILL.tr.md) | SaaS hedef kitlesi, değer önerisi ve farklılaşmayı netleştirmek |
| [pricing-review](.agents/skills/pricing-review/SKILL.tr.md) | Fiyatlandırma, paketleme ve müşteri geçişlerini değerlendirmek |

### Yazılım geliştirme

| Beceri | Amacı |
| --- | --- |
| [technical-troubleshooter](.agents/skills/technical-troubleshooter/SKILL.tr.md) | Uygulama ve altyapı sorunlarını güvenle teşhis etmek |
| [software-planner](.agents/skills/software-planner/SKILL.tr.md) | İstekleri geliştirme görevleri ve kabul kriterlerine dönüştürmek |
| [code-reviewer](.agents/skills/code-reviewer/SKILL.tr.md) | Gerçek kod değişikliklerini kanıt üzerinden incelemek |
| [release-readiness](.agents/skills/release-readiness/SKILL.tr.md) | Canlıya çıkış öncesi risk ve test kanıtlarını değerlendirmek |

### Otomasyon ve yapay zekâ

| Beceri | Amacı |
| --- | --- |
| [automation-discovery](.agents/skills/automation-discovery/SKILL.tr.md) | Değerli iş otomasyonu fırsatlarını seçmek |
| [workflow-architect](.agents/skills/workflow-architect/SKILL.tr.md) | Hata ve istisnaları da kapsayan iş akışları tasarlamak |
| [ai-feasibility](.agents/skills/ai-feasibility/SKILL.tr.md) | Yapay zekânın gerekli ve uygulanabilir olup olmadığını değerlendirmek |

### Müşteri operasyonları

| Beceri | Amacı |
| --- | --- |
| [support-assistant](.agents/skills/support-assistant/SKILL.tr.md) | Müşteri destek talebini, görev ve yanıt taslaklarını hazırlamak |
| [subscription-lifecycle](.agents/skills/subscription-lifecycle/SKILL.tr.md) | Yenileme, bildirim, sona erme ve yeniden açma süreçlerini tasarlamak |

**Dil:** Otomatik keşif için ana dosya İngilizce `SKILL.md` dosyasıdır. Her becerinin `SKILL.tr.md` adlı Türkçe karşılığı bulunur. Yapay zekâdan Türkçe yanıt isteyebilirsiniz. Paket testleri modelin gerçek yanıt kalitesini garanti etmez.

## Codex için hızlı kurulum

Git ve Bash gerekir:

```bash
git clone https://github.com/basamakcomtr/basamak-skills.git
bash basamak-skills/scripts/install.sh --user
```

Yalnızca tek bir proje için:

```bash
bash basamak-skills/scripts/install.sh --project /proje/yolu
```

Betik **13 becerinin tamamını** sembolik bağlantıyla kaydeder, mevcut becerilerin üzerine yazmaz. Depoyu yerinden kaldırmayın; ajan için yeni oturum açın.

Örnek kullanım:

```text
automation-discovery becerisini kullan.
Faturaların manuel toplanma sürecinde otomasyon fırsatlarını belirle.
Yapay zekâyı zorunlu varsayma.
```

```text
conversion-optimizer becerisini kullan.
Web sitemizde kayıt dönüşümünü engelleyen üç öncelikli sorunu bul.
Gözlemleri varsayımlardan ayır.
```

Otomatik keşif çalışmıyorsa ilgili `SKILL.md` dosyasını okutun. Kurulum yöntemi Codex'in kullandığı `.agents/skills/` dizinine yöneliktir. Diğer ajanların dosya yerleşimi farklı olabilir; **Claude Code, Cursor ve diğer ortamlar için uçtan uca uyumluluk doğrulanmış değildir.** Ayrıntılar: [kurulum kılavuzu](docs/kurulum.md).

## Birlikte kullanım

- [Müşteri talebinden kod incelemesine](workflows/feature-request-to-review.tr.md)
- [Otomasyon fikrinden iş akışı tasarımına](workflows/automation-opportunity-to-design.tr.md)

Bu rehberler adımlar arası **manuel devir** sağlar; otomatik CRM kaydı veya canlı sistem erişimi vermez.

## Ortak ilkeler

- Önce hedefi anla ve en küçük yararlı çözümü seç.
- Gözlem, kanıt, varsayım ve bilinmeyeni ayrı tut.
- Ölçüm, rakip bilgisi, test sonucu veya entegrasyon yeteneği uydurma.
- Daha basit ve güvenilir ise yapay zekâ yerine kural kullan.
- Açık yetki olmadan canlı veriyi değiştirme, müşteri mesajı gönderme, ücretli API çağırma, yayın, ödeme, hizmet kapatma veya silme yapma.

Kontroller:

```bash
python3 -m unittest discover -s tests -v
```

**Sürüm:** [1.2.0](VERSION) · [Değişiklikler](CHANGELOG.md). Dosyadaki sürüm numarası ayrıca GitHub etiketi veya yayını oluşturulduğu anlamına gelmez.

**Lisans:** [MIT](LICENSE), © 2026 Basamak Bilişim. OpenAI veya başka bir ajan üreticisinin resmî ürünü değildir.
