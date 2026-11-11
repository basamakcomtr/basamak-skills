# Müşteri talebinden kod incelemesine

**Amaç:** Gelen bir özellik isteğini doğru sınıflandırıp uygulanabilir geliştirme
planına ve gerçek bir PR üzerinde güvenli kod incelemesine aktarmak.

Bu, otomatik çalışan bir orkestrasyon değildir. Her aşama ayrı bir Codex
görevi olabilir. **Önceki aşamanın çıktısını sonraki göreve kullanıcı taşır.**
Bu repo bir iş akışı rehberi sunar; müşteri CRM'sine veya ürün koduna bağlanmaz.

## Başlamadan önce

Buradaki SKILL.md yolları varsayılan kullanıcı kurulumuna (`~/.agents/skills/`) göredir.
Proje kapsamlı kurulumda projenin `.agents/skills/` yolunu kullanın.


- İlgili ürün, müşteri talebi ve (varsa) destek kaydını belirle.
- Müşteriye ait kişisel verileri, erişim anahtarlarını ve gizli logları
  görev metninden çıkar; GitHub'a kopyalama.
- Kod veya PR incelemesi gerekiyorsa gerçek **ürün deposuna** erişim
  gerekir. Bu beceri deposu, ürün uygulamasının kodunu içermez.
- Codex otomatik beceri keşfine güvenme: her görevde ilgili SKILL.md
  dosyasını doğrudan okut.

## Aşama 1 — Talebi değerlendir

**Beceri:** `support-assistant`

**Talimat dosyası:** `.agents/skills/support-assistant/SKILL.md`

**Codex görevi:**

```text
~/.agents/skills/support-assistant/SKILL.md
dosyasını oku ve talimatları uygula.

Aşağıdaki destek talebini değerlendir: [TALEP METNİ]
Bilinen ürün ve müşteri bağlamı: [VARSA BAĞLAM]

Tür ve öncelik için kısa gerekçe; doğrulanmış bilgiler ve belirsizlikler;
iç kullanım için CRM görev taslağı; müşteriye kısa yanıt hazırla.
Özelliğin mevcut olduğunu varsayma. Önceden verilen bilgiyi tekrar isteme.
Görev açma, mesaj gönderme veya sistemde değişiklik yapma.
```

**Devredilecek çıktı:** Talebin özeti, beklenen kullanıcı sonucu,
bilinenler/bilinmeyenler, varsa önerilen geliştirme ihtiyacı ve
yapılmamış işlemlerin durumu.

**Karar noktası:** Talep bir kullanım sorusuysa önce özelliğin
mevcudiyetini yetkili ekip doğrulasın. Özellik veya değişiklik
ihtiyacı netleşmediyse geliştirme kararı verilmiş gibi ilerleme.

## Aşama 2 — Geliştirme planını oluştur

**Beceri:** `software-planner`

**Talimat dosyası:** `.agents/skills/software-planner/SKILL.md`

**Codex görevi:**

```text
~/.agents/skills/software-planner/SKILL.md
dosyasını oku ve talimatları uygula.

Önceki aşamanın özeti: [AŞAMA 1 ÇIKTISI]
İstenen geliştirme kararı: [ONAYLANMIŞ KAPSAM]
İlgili ürün deposu veya teknik kanıt: [VARSA]

Önce mevcut durumla varsayımları ayır. En küçük uygulanabilir kapsamı,
kapsam dışını, sıralı geliştirme görevlerini ve her görev için bitti ölçütünü
hazırla. Normal kullanım ve önemli hata/izin durumu için kabul kriterleri
yaz. Kod erişimi yoksa tablo, API veya bileşen adı uydurma.
Dosya değiştirme, commit, push veya deploy yapma.
```

**Devredilecek çıktı:** Onaylanan kapsam ve kapsam dışı işler, teknik
kararlar/varsayımlar, iş paketleri, kabul kriterleri, bağımlılıklar,
asgarî doğrulama ve varsa veri/dağıtım riskleri.

**Karar noktası:** Bir geliştirici veya yetkili kişi kapsamı ve kabul
kriterlerini onaylamadan uygulamaya geçme. Kritik teknik belirsizlik varsa
önce kısa keşif görevi tamamlanmalı.

## Aşama 3 — Uygulama (beceri dışında)

Planı gerçek ürün deposunda çalışan yetkili geliştirme ekibine aktar.
Uygulama, bu dağıtım deposunda değil ilgili uygulama deposunda
yapılır. Değişiklik için ayrı yetki, uygun dal/PR ve ilgili kontroller gerekir.

**Devredilecek çıktı:** Gerçek PR bağlantısı veya erişilebilir diff,
değişen davranış, ilgili kabul kriterleri, yapılan testler ve bilinen
sınırlamalar. **Henüz PR/diff yoksa kod incelemesi tamamlandı deneme.**

## Aşama 4 — PR incelemesi

**Beceri:** `code-reviewer`

**Talimat dosyası:** `.agents/skills/code-reviewer/SKILL.md`

**Codex görevi:**

```text
~/.agents/skills/code-reviewer/SKILL.md
dosyasını oku ve talimatları uygula.

Gerçek PR veya diff: [PR URL / DIFF]
Onaylanan kapsam ve kabul kriterleri: [AŞAMA 2 ÇIKTISI]
Geliştiricinin test özeti: [VARSA]

Değişiklikleri planlanan davranış ve kabul kriterlerine göre incele.
Yalnızca kanıtlanabilir işlevsel, güvenlik veya regresyon risklerini dosya
ve satır referanslarıyla belirt. Kanıtlanmış sorun yoksa açıkça söyle.
Çalıştırmadığın testleri çalıştırılmış gösterme.
Kod değiştirme, PR onaylama, merge veya deploy yapma.
```

**Devredilecek çıktı:** Önceliklendirilmiş gerçek bulgular (varsa),
testlerin gerçekten doğruladığı alanlar, kalan belirsizlikler ve
merge öncesi alınması gereken karar.

**Karar noktası:** İnceleme sonucu tek başına merge veya canlıya dağıtım
yetkisi sağlamaz. Son kararı yetkili kişi verir.

## Tek kayıtlık devir özeti

Her aşamanın sonunda yalnızca gerekli alanları aktar:

```text
Talep / hedef:
Doğrulanmış mevcut durum:
Belirsizlikler:
Onaylanan kapsam:
Kabul kriterleri:
Çalışılan repo / PR:
Gerçekten yapılan işlemler ve testler:
Bir sonraki karar / sorumlu:
```

Yalnızca ilgili alanları doldur; boş alanları varsayımla tamamlayıp
doğrulanmış gibi gösterme. Müşteri mesajları, erişim bilgileri ve
özel dokümanları bu kütüphanenin GitHub commit'lerine koyma.

## Diğer beceriler ne zaman devreye girer?

- `technical-troubleshooter`: Yeni özellik talebi yerine üretimde
  yaşanan bir hata varsa, belirtileri teşhis etmek için önce kullan.
- `web-audit`: Geliştirme ihtiyacı web sitesi kullanıcı deneyimi
  veya dönüşüm sorunu ise, ölçülmüş/gözlenmiş bulgularla planı besle.

Bu iki beceri her işte zorunlu değildir; yalnızca ihtiyaç varsa kullan.
