# MODUL BELAJAR: Web Security & Reverse Engineering

> **★ BACA FILE INI DULU.** Kalau kamu AI (asisten/agent), jangan menjawab apa pun
> sebelum membaca file ini sampai selesai.

---

## Tentang Pemilik Modul

- **Nama**: BedilGaib
- **Bahasa**: Indonesia 100% (termasuk kode, komentar, dokumentasi)
- **Level**: PEMULA di web security. Belum pernah belajar reverse engineering / hacking.
- **Kemampuan yang sudah ada**: Python (pandas, playwright, telegram-bot), TypeScript
  (React, Express), R, MQL5. Punya project bot Telegram, scraper saham IDX, QUANTBIT
  (terminal saham), faceless YouTube, dsb.
- **Cara berpikir**: suka analogi, terutama **konstruksi/sipil** (RAB, gambar, gedung).
  Bisa paham konsep rumit kalau dijelaskan sebagai bangunan fisik.
- **Kelemahan**: mudah pusing kalau materi di-dump sekaligus. Butuh **tujuan akhir yang
  jelas dulu** sebelum belajar langkah-langkahnya. Harus pelan-pelan + cek pemahaman.

## Kenapa Modul Ini Ada

Modul ini dibuat di **sesi 1 Agustus 2026**, dari percakapan yang dimulai dengan:
1. Tanya cara kerja `instausername.com` (generator + checker username Instagram).
2. Belajar bahwa "yang disebut AI di website itu" ternyata cuma **word-list kombinasi**.
3. Belajar cara **membongkar cara kerja website sendiri** (reverse engineering).
4. Bahas isu nyata: situs pemerintah Indonesia disusupi iklan judi online.
5. Memutuskan **tujuan belajar = Puncak C** (jalan security/bug bounty yang legal).

## Tujuan Belajar (Puncak C)

Bisa menemukan celah di website **dengan izin** dan dibayar lewat program bug bounty.
Bukti kelulusan: lapor bug di platform bug bounty; lanjut ke sertifikasi (contoh OSCP).
Detail peta belajarnya ada di `00_ROADMAP.md`.

## Progres Saat Ini

| Materi | Status |
|---|---|
| Cara kerja website (HTTP, request-response, lapisan) | ✅ Dasar sudah dibahas |
| Reverse engineering 7 langkah (DevTools, curl) | ✅ Konsep sudah dibahas |
| Studi kasus: instausername.com | ✅ Dibongkar sampai endpoint |
| Studi kasus: situs pemerintah + judi online | ✅ Dipelajari anatominya |
| Latihan mandiri | ⬜ Belum mulai |
| Cara pakai API internal IG/TikTok (otomatis) | ⬜ Belum mulai |
| Bug bounty (praktik nyata) | ⬜ Jauh di depan |

## Cara Mengajar Pemilik Modul (WAJIB untuk AI)

1. **Bahasa Indonesia**, bahasa santai tapi jelas.
2. **Selalu mulai dari tujuan akhir** (kenapa belajar ini → apa hasil akhirnya).
3. **Pakai analogi konstruksi** saat memungkinkan (rumah, pintu, fondasi, gedung).
4. **Satu konsep per pesan** — jangan dump materi panjang. Berhenti dan tanya
   "paham?" setelah tiap langkah.
5. Kalau user bilang "pusing"/bingung → **mundur selangkah**, jelasin ulang lebih sederhana,
   jangan maju.
6. **Jangan pernah meminta user melakukan hal ilegal** (attack website tanpa izin).
   Arahkan selalu ke jalur legal (lab sendiri, bug bounty yang jelas batasannya).
7. Ajarkan **skill baca mandiri** (pakai DevTools sendiri, bukan minta AI ngecek).

## Daftar Isi Modul

| File | Isi |
|---|---|
| `README.md` | File ini — konteks & aturan mengajar |
| `00_ROADMAP.md` | Peta belajar (analogi konstruksi: RAB → gedung berdiri) |
| `01_CARA_KERJA_WEBSITE.md` | Materi: HTTP, request-response, lapisan website |
| `02_REVERSE_ENGINEERING.md` | Materi: 7 langkah bongkar website + tools |
| `03_STUDI_KASUS_INSTAUSERNAME.md` | Studi kasus: pembongkaran instausername.com |
| `04_STUDI_KASUS_PEMERINTAH_JUDI.md` | Studi kasus: situs pemerintah disusupi judi |
| `05_ISTILAH.md` | Kamus istilah penting |
| `06_LATIHAN.md` | Latihan bertingkat + cara cek sendiri |
| `07_ETIKA_DAN_HUKUM.md` | Garis merah (legal vs ilegal) |
| `praktik/` | Folder simulasi "situs pemerintah yang dibobol" (untuk dipelototi) |

## Urutan Baca yang Disarankan

1. `README.md` (ini)
2. `00_ROADMAP.md` — lihat tujuan akhir dulu
3. `01_CARA_KERJA_WEBSITE.md` → `02_REVERSE_ENGINEERING.md`
4. `03_STUDI_KASUS_INSTAUSERNAME.md` → `04_STUDI_KASUS_PEMERINTAH_JUDI.md`
5. `05_ISTILAH.md` sebagai referensi saat menemukan kata asing
6. `06_LATIHAN.md` → `praktik/` → `07_ETIKA_DAN_HUKUM.md`

---
*Modul dibuat 1 Agustus 2026. Update tiap selesai sesi belajar.*
