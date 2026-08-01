# 01 — CARA KERJA WEBSITE

> **Ringkasan:** Semua website itu cuma satu hal: **browser mengirim request (permintaan),
> server mengirim response (jawaban)**. Kalau kamu paham alur ini, semua materi berikutnya
> jadi mudah.

---

## 1. Analogi: Makan di Warung

- Kamu = **browser** (yang minta).
- Warung = **server** (yang punya makanan = data).
- **Request** = "Bang, minta satu porsi nasi goreng" → ini pesananmu ke server.
- **Response** = warung menyajikan nasi goreng → ini jawaban server (berupa halaman website).

Setiap kali kamu buka website, browser "memesan" halaman ke server, dan server "menyajikan"
isi halamannya. Sesederhana itu.

## 2. Anatomi Request (Pesanan ke Server)

Sebuah request punya 3 bagian penting:

1. **Metode** — jenis permintaan. Dua yang paling sering:
   - `GET` → "tolong beri saya data" (minta halaman, minta hasil pencarian).
   - `POST` → "saya kirim data ke kamu" (isi form login, kirim username untuk dicek).
2. **URL** — alamat tujuannya, misal `https://instausername.com/availability`.
   - Bisa ada **parameter** di URL (request GET), contoh: `?q=sayur&cat=11` →
     "saya minta data dengan kata kunci sayur, kategori 11".
3. **Header + Cookies** — "kartu identitas" browser. Server pakai ini untuk tahu
   browser kamu, bahasa, siapa kamu (cookie login), dan memblokir bot.

## 3. Response (Jawaban Server)

Server menjawab dengan:
- **Status code** — kode hasil. Ini PENTING banget untuk reverse engineering:
  - `200` = OK, ketemu / berhasil.
  - `302` = redirect (pindah halaman lain).
  - `404` = tidak ketemu. (Di studi kasus checker username: "tidak ketemu" = username kosong!)
  - `500` = error di server.
- **Body** — isi sebenarnya (HTML halaman, atau data JSON).

## 4. Lapisan Website (Kenapa "Domain" Tidak Mudah Dibobol)

Website itu seperti rumah bertingkat. Dari luar ke dalam:

| Lapisan | Analogi rumah | Contoh | Kekuatan |
|---|---|---|---|
| **Domain / DNS** | Sertifikat tanah + papan nama | `bawaslu.go.id` | Paling kuat |
| **Server web** | Bangunan rumahnya | nginx, Apache | Sedang |
| **Aplikasi (CMS)** | Pintu & jendela rumah | WordPress, Drupal | Sering lemah |
| **Subdomain terlantar** | Jendela loteng yang lupa dikunci | `staging.bawaslu.go.id` | Paling lemah |

**Poin kuncinya**: penyerang jarang membobol "sertifikat tanah" (domain). Mereka masuk
lewat pintu/jendela yang lupa dikunci (CMS lama, password lemah, subdomain terlantar).
Ini yang membuat kasus "situs pemerintah disusupi judi" bisa terjadi (lihat `04`).

## 5. Kenapa Ini Fondasi Buat Puncak C

Semua skill security web bertumpu pada satu pertanyaan:
> "Kalau saya kirim request khusus ke server, jawabannya beda atau nggak?"

Bug bounty = menemukan request khusus yang bikin server salah bertindak. Jadi pahami
request-response dulu, sisanya menyusul.

---
**Latihan mini**: buka `06_LATIHAN.md` → Latihan Level 1 no. 1.
