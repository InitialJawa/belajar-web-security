# 03 — STUDI KASUS: instausername.com

> **Ringkasan:** Situs "generator username Instagram". Klaimnya pakai AI — ternyata
> cuma kombinasi kata dari list statis. Cekernya cuma ngecek halaman profil Instagram.
> Uangnya dari iklan Ezoic. Ini contoh nyata cara kerja tool SEO yang dibongkar.

---

## 1. Apa Situs Ini?

- **Generator username** ("Instagram Username Generator", tagline: *"generate a username
  using artificial intelligence"*).
- **Checker ketersediaan** username di `/availability`.
- **Halaman koleksi username** (`/ideas/funny`, `/ideas/boys`, dll) — landing page SEO.
- **Font generator** + checker username platform lain (TikTok, Twitch, Minecraft, YouTube).

## 2. Klaim "AI" — Ternyata Bukan AI

Deskripsi aslinya sendiri mengaku:
> *"usernames made up of words picked from lists of categories"*

Jadi yang disebut AI itu cuma **kombinasi acak**: kata user + prefix/suffix dari word-list
per kategori. Bukti nyata (saya tes POST `sayur` kategori Food):
- `sweetsayur`, `sayur_yummy`, `5_sayur`, `sayur.flavors`, `BYO_sayur`, dst.

**Endpoint generator**: `GET /inc/query.php?catid=11&n=sayur&num=5&business=`
→ balik JSON berisi ~100 username. (Kategori = daftar kata tematik.)

**Pelajaran**: iklan "AI" di website ≠ AI beneran. Selalu cek endpoint/logikanya.

## 3. Cara Kerja Checker Username

Form `/availability` mengirim POST:
- `q` = username yang dicek
- `ishuman` = checkbox "I'm not a robot"
- `fishondreo` = **hidden honeypot** (harus terisi lewat JS `oninput`/`onchange`)

Lalu ada **rate limit / antrian**: "You're number 10 in the queue" → halaman refresh
tiap 3 detik sampai hasil siap (karena Instagram membatasi cek massal).

**Logika cek** (dari `main_1.js`):
```js
$.ajax('https://instagram.com/' + n + '/')
  .success → "Username is taken"
  .error   → "Username is free"
```
Versi servernya sama idenya: PHP fetch halaman profil Instagram → 200 = taken,
error/404 = free.

## 4. Kelemahan Metode Cek "Fetch Halaman Profil"

- Nggak bisa bedain: **akun deactivate sementara** (username masih dicadangkan),
  **akun dihapus** (biasanya lepas), atau **akun dibanned** (username ditahan).
- Instagram bisa kasih captcha/login wall kalau request kebanyakan.
- Cek lewat halaman publik, bukan API resmi → hasil kadang salah.

**Kesimpulan praktis**: "Profile isn't available" / redirect `/404` itu indikator kuat
username kosong, TAPI satu-satunya cara pasti = coba claim/signup langsung.

## 5. Platform Lain: Sama Tapi Beda Jebakan

| Platform | Cara cek | Jebakan |
|---|---|---|
| **Instagram** | halaman profil → error/"Profile isn't available" | deactivate & banned juga tampil kosong |
| **YouTube** | `youtube.com/@handle` → "This page isn't available" | handle ≠ custom URL lama; handle dihapus lama dilepas |
| **TikTok** | redirect ke `tiktok.com/404?fromUrl=...` | banned juga bisa 404; butuh JS/signature buat otomatis |
| **Facebook** | paling nggak reliable | username TIDAK pernah dilepas, login wall, region |

## 6. Cara Situs Ini Mencari Uang

- **Iklan Ezoic** (banyak placeholder iklan, sticky/floating ad, video ad).
- **SEO multi-halaman**: ratusan halaman `/ideas/...` dalam 8 bahasa → trafik Google.
- **Jaringan tool**: font generator & checker platform lain saling me-link.

## 7. Stack Teknis

- jQuery 1.12.4 + ClipboardJS + PHP (`query.php`), di belakang **Cloudflare + Ezoic CDN**.
- `main_1.js` mengatur: AJAX generator, availability, dan favorit (localStorage `instaname`).

---
**Kaitan dengan modul**: ini contoh praktik dari `02` langkah 1–7. Kamu bisa ulangi
sendiri: buka situsnya → F12 → Network → isi form → lihat requestnya.
