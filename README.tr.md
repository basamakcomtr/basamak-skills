# Basamak Skills

**Basamak Bilişim tarafından geliştirilen, Codex ve uyumlu ajanlar için açık kaynak yapay zekâ becerileri.**

[**English**](README.md) · [Kurulum](docs/kurulum.md) · [Sürüm geçmişi](CHANGELOG.md) · [MIT Lisansı](LICENSE)

Her beceride işin amacı, kapsamı, kanıt kuralları ve güvenlik sınırları tanımlanır.

## Beceriler

| Beceri | Amacı |
| --- | --- |
| [web-audit](.agents/skills/web-audit/SKILL.tr.md) | Web sitesi deneyimini, içeriğini ve dönüşümünü değerlendirmek |
| [technical-troubleshooter](.agents/skills/technical-troubleshooter/SKILL.tr.md) | Yazılım ve altyapı hatalarını güvenli biçimde teşhis etmek |
| [support-assistant](.agents/skills/support-assistant/SKILL.tr.md) | Müşteri destek talepleri, CRM görev ve yanıt taslakları |
| [code-reviewer](.agents/skills/code-reviewer/SKILL.tr.md) | PR ve kod değişikliklerini kanıta dayalı incelemek |
| [software-planner](.agents/skills/software-planner/SKILL.tr.md) | Özellik taleplerini geliştirme görevlerine ve kabul kriterlerine dönüştürmek |

**Dil seçimi:** Codex otomatik olarak İngilizce `SKILL.md` talimatlarını kullanır. Özgün Türkçe metinler `SKILL.tr.md` dosyalarında korunur. Türkçe yanıt isteyebilir veya ilgili Türkçe dosyayı doğrudan okutabilirsiniz. İngilizce kullanım kalitesi ayrıca uçtan uca doğrulanmamıştır.

## Hızlı kurulum

Git ve Bash gerekir. Codex'in çalıştığı bilgisayarda:

```bash
git clone https://github.com/basamakcomtr/basamak-skills.git
bash basamak-skills/scripts/install.sh --user
```

Beş beceri `~/.agents/skills/` altında sembolik bağlantılarla kaydedilir. Yalnızca tek proje için:

```bash
bash basamak-skills/scripts/install.sh --project /proje/yolu
```

**Mevcut becerilerin üzerine yazılmaz.** Klonlanan depoyu taşımayın veya silmeyin. Yeni Codex oturumu açın; otomatik keşif çalışmıyorsa ilgili `SKILL.md` dosyasını doğrudan okutun.

```text
~/.agents/skills/software-planner/SKILL.md dosyasını oku ve
bu özelliği uygulanabilir geliştirme görevlerine ayır.
```

Ayrıntılar: [Kurulum ve güncelleme](docs/kurulum.md).

## İş akışı

[Müşteri talebinden kod incelemesine](workflows/feature-request-to-review.tr.md):
`support-assistant` → `software-planner` → yetkili geliştirme ekibi → `code-reviewer`.

Bu bir rehberdir; CRM kaydı açmaz veya kendiliğinden kod değiştirmez.

## Güvenlik ve lisans

Beceri talimatları kimlik bilgisi, müşteri verisi veya Basamak Bilişim'in sistemlerine erişim sağlamaz. Kullanıcı yetkisi olmadan gerçek sistem işlemleri yapılmaz. Otomatik testler model davranışını garanti etmez.

**Sürüm:** [1.1.0](VERSION) · [Sürüm geçmişi](CHANGELOG.md). GitHub etiketi/yayını ayrıca oluşturulacak.

**Lisans:** [MIT](LICENSE), © 2026 Basamak Bilişim. OpenAI'nin resmî ürünü değildir.
