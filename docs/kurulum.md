# Kurulum, güncelleme ve kaldırma

[**English**](installation.md) · [Ana sayfa](../README.tr.md)

Git, Bash ve yerel SKILL.md dosyalarını okuyabilen Codex gerekir.

## Kullanıcıya kurulum

```bash
git clone https://github.com/basamakcomtr/basamak-skills.git
bash basamak-skills/scripts/install.sh --user
```

Beceriler `~/.agents/skills/` altında bağlantıyla kaydedilir. Asıl dosyalar klonlanan depoda kalır.

## Projeye özel kurulum

```bash
bash basamak-skills/scripts/install.sh --project /mutlak/proje/yolu
```

Beceriler projenin `.agents/skills/` dizinine bağlanır. Betik mevcut dosya, klasör veya farklı bağlantının **üzerine yazmaz**.

## Kullanma

Codex'i yeni oturumda açın. Otomatik keşif çalışmazsa doğrudan talimat verin:

```text
~/.agents/skills/support-assistant/SKILL.md dosyasını oku.
Bu destek talebine yanıt ve CRM görev taslağı hazırla. İşlem yapma.
```

Bağlantı oluşması otomatik keşfin doğrulandığı anlamına gelmez.

## Güncelleme

```bash
git -C basamak-skills status
git -C basamak-skills pull --ff-only
```

Değişiklikler için önce [sürüm geçmişini](../CHANGELOG.md) okuyun.

## Kaldırma

Yalnızca kendi kurulumunuzun oluşturduğu ve Basamak Skills deposuna işaret ettiği doğrulanan sembolik bağlantıları kaldırın; diğer becerilere dokunmayın. Ardından isterseniz depo klonunu silebilirsiniz.

Betik kimlik bilgisi istemez, gerçek sistemde değişiklik yapmaz. Ana `SKILL.md` talimatları İngilizce, aynı klasördeki `SKILL.tr.md` dosyaları özgün Türkçe talimatlardır. Türkçe referans gerekiyorsa `SKILL.tr.md` dosyasını doğrudan okutabilirsiniz.
