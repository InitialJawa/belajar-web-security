# 02 — REVERSE ENGINEERING (Membongkar Cara Kerja Website)

> **Ringkasan:** Website yang punya form pasti meninggalkan jejak: file JS, endpoint,
> request. Reverse engineering = baca jejak itu untuk paham logikanya. Ada 7 langkah.

---

## Mindset: 3 Lapisan yang Bisa Kamu Baca

| Lapisan | Yang kamu lihat | Cara membacanya |
|---|---|---|
| 1. Tampilan | Form, tombol, halaman | View Source / Inspect Element |
| 2. Logika | Apa yang terjadi saat submit | DevTools → tab **Network** |
| 3. Data | Endpoint & response | curl / Postman |

Tujuan: **temukan "request yang menghasilkan hasil"** — itulah jantung website.

## Tools (gratis, semua ada di Windows)

- **DevTools browser** (F12) — skill nomor 1.
- **curl** (bawaan Windows) — tiru request dari terminal.
- **Postman** (opsional) — repetisi request dengan nyaman.
- **VS Code / Notepad++** — baca JS yang di-minify.

## 7 Langkah Membongkar Website

**1. Amati di browser.** Pakai websitenya manual. Catat: isi form, tombol, perubahan URL
saat submit, pesan error.

**2. Buka DevTools → Network → centang "Preserve log".** Refresh, lalu setiap aksi
muncul sebagai baris request. Ini "jendela dunia".

**3. Cari request yang "menghasilkan".** Klik tombol/submit, lihat request mana yang
muncul. Lihat: metode (GET/POST), URL, parameter, header, cookie.

**4. Inspeksi response.** Klik request → tab Response. Kalau response berisi hasil
(misal daftar username / "is free") → **endpoint ketemu**.

**5. Baca JS-nya.** Ctrl+U (View Source) → cari `<script src="...">` → buka file itu.
Kalau minified (satu baris panjang), di DevTools → Sources ada tombol **Pretty-print `{}`**.
Cari kata kunci: URL endpoint, `$.ajax`, `fetch(`, `success/error`.

**6. Replikasi dengan curl.** Tiru request tadi di terminal. Kalau response sama tanpa
browser = kamu paham 90%.

**7. Identifikasi penghalang.** Inilah yang bikin tiap website beda tingkat kesulitannya:

| Penghalang | Apa itu | Contoh nyata |
|---|---|---|
| **Honeypot** | Field tersembunyi anti-bot | `fishondreo` di instausername |
| **Captcha** | "Saya bukan robot" | di halaman checker |
| **Rate limit** | Antrian cek biar nggak spam | "You're number 10 in the queue" |
| **JS-heavy** | Halaman cuma shell, butuh browser asli | Instagram, TikTok |
| **Signature/cookies** | Token wajib yang dibuat JS | TikTok |

## Contoh Cepat (sudah pernah kita lakukan)

Di `instausername.com`:
1. Inspect form → ketemu field tersembunyi `fishondreo` (honeypot) → langkah 1 & 5.
2. Baca `main_1.js` → ketemu logika `$.ajax(instagram.com/username)` →
   success = taken, error = free → langkah 5.
3. POST pakai curl → "You're number 10 in the queue" → ada rate limit → langkah 7.
4. Generator → `main_1.js` menunjuk `/inc/query.php` → curl ke sana → JSON username
   → endpoint ketemu → langkah 6.

## Tiga Pertanyaan Kunci (tanyakan setiap lihat request)

1. Request ini metode apa, ke URL mana, kirim parameter apa?
2. Response-nya berisi apa?
3. Kalau kupakai curl tanpa browser, hasilnya sama atau beda? Kenapa?

---
**Latihan**: buka `06_LATIHAN.md` → Level 1 no. 2 dan Level 2.
