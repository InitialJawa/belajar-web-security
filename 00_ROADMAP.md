# 00 — PETA BELAJAR (ROADMAP)

> **Ringkasan:** Belajar security itu seperti proyek bangunan — ada gambar/RAB dulu,
> lalu fondasi, struktur, finishing, sampai gedung berdiri. Di modul ini, "gedung
> berdiri" artinya kamu bisa menemukan celah website dengan izin dan dibayar (bug bounty).

---

## Analogi: Bikin Rumah vs Bikin Skill Security

| Fase bangunan | Fase belajar web security | Bukti selesai (kamu bisa...) |
|---|---|---|
| **Gambar + RAB** | Paham bahan baku web: **HTTP** (request → response) | Jelaskan alur request-response pakai bahasamu sendiri |
| **Material & pondasi** | Baca HTML, CSS, JS + tahu fungsi DevTools | Buka View Source & tahu form itu ngirim apa |
| **Kolom & balok** | Lihat semua request lewat **DevTools Network** | Tahu request mana yang "menghasilkan hasil" |
| **Finishing** | **Replikasi** request dengan curl/Postman | Response sama persis tanpa browser |
| **Serah terima** | Bisa bongkar website apa pun + tahu batas legalnya | Bikin sendiri tool / lapor bug di program bug bounty |

## Ada 3 "Puncak" — Kamu Pilih Puncak C

- **Puncak A — Pembuat Tool Otomatis**: bikin scraper/bot/checker. (Nggak dipilih.)
- **Puncak B — Web Developer**: bangun website. (Nggak dipilih.)
- **Puncak C — Security / Bug Bounty** ✅ **DIPILIH**: cari celah website *dengan izin*,
  dibayar via program bug bounty, lanjut sertifikasi (OSCP).

Kenapa Puncak C yang dipilih: ketertarikan pada "bagaimana website bisa dibobol" +
mau pakai skill bongkar-bongkar secara legal dan bermanfaat.

## Langkah Belajar Puncak C (urutan)

1. **[SELESAI] Paham cara kerja website** → `01` — HTTP, lapisan website.
2. **[SELESAI konsep] Reverse engineering** → `02` — 7 langkah, DevTools, curl.
3. **[SELESAI] Studi kasus** → `03` + `04` — bongkar tool nyata & serangan nyata.
4. **[BELUM] Latihan mandiri** → `06` — praktik DevTools/curl di website yang kamu izinkan.
5. **[BELUM] API internal & otomasi** — cara cek username batch (IG/TikTok/YT) via endpoint.
6. **[BELUM] Setup lab sendiri** — bikin website "korban" di lokal (PC sendiri) untuk
   latihan menyerang secara legal.
7. **[BELUM] Bug bounty pemula** — platform seperti HackerOne/Bugcrowd, baca scope,
   lapor bug pertama.

## Aturan Emas Sepanjang Jalan

- **Hanya serang yang kamu punya izin** (PC/lab sendiri, atau program bug bounty).
- Paham konsep ≠ boleh melakukannya di dunia nyata. Izin adalah segalanya.
- Kalau pusing di langkah mana pun: mundur, ulang, baru maju.

---
*Lanjutan: kalau langkah 4 selesai, update README progres + tandai di sini.*
