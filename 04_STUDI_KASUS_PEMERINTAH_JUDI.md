# 04 — STUDI KASUS: SITUS PEMERINTAH DISUSUPI JUDI ONLINE

> **Ringkasan:** Kasus nyata Indonesia — situs `.go.id` disisipi halaman judi online.
> Domainnya TIDAK dibajak; yang disusupi adalah folder/file di dalam server lewat
> celah CMS, password lemah, atau subdomain terlantar. Google dipercaya sama `.go.id`,
> makanya iklan judi "nebeng" biar naik ranking. Folder `praktik/` memvisualkan ini.

---

## 1. Bukti Nyata (Saya Cek Langsung, 1 Agustus 2026)

- **Situs resmi** `https://rotendao.bawaslu.go.id/` → **HTTP 200**, normal.
- **Link yang pernah berisi judi** `https://rotendao.bawaslu.go.id/slot-gacor-terbaru/`
  → sekarang **HTTP 404** (sudah dibersihkan BSSN). Saat aktif: halaman "slot gacor,
  deposit minimal Rp25 ribu".
- Contoh lain dari berita CNN 2023: `sipandu.dephub.go.id/assets/slot-gacor/`.
- **Petunjuk dari header** `rotendao.bawaslu.go.id`:
  ```
  Server: nginx/1.20.1
  X-Powered-By: PHP/8.3.31
  X-Generator: Drupal 10
  ```
  → situs ini pakai **CMS Drupal 10** di **nginx + PHP**. Ini satu-satunya petunjuk
  yang bisa dilihat dari luar.

## 2. Skala Masalah (Data Resmi)

- **BSSN 2024**: 3.908 laman pemerintah disusupi konten judi online, 678 instansi
  terdampak (laporan Lanskap Keamanan Siber 2024).
- **Tirto.id (Jul 2026)**: menemukan **191 domain** disalahgunakan (97 `.go.id` +
  94 `.ac.id`) lewat teknik *web defacement* dan *injeksi URL*.
- **Kasus PeduliLindungi.id** (Mei 2025): di-takedown karena disusupi konten judi.

## 3. Kenapa Domain Tidak Dibajak?

Domain `.go.id` terdaftar atas nama instansi (registrar PANDI). Membajak domain = ambil
alih akun registrar/Cloudflare admin → butuh social engineering/credential bocor,
sangat sulit dan jarang.

Analogi rumah: penyerang **tidak mencuri sertifikat tanah** (domain), tapi **masuk
lewat pintu belakang yang tidak dikunci** (celah server) lalu **menempel poster judi
di dinding dalam rumah** (membuat folder/file).

## 4. Yang Terlihat vs Yang Tidak Terlihat

**Terlihat dari luar (browser):**
- Situs resmi tetap normal (HTTP 200).
- Folder aneh seperti `/slot-gacor-terbaru/` yang isinya halaman judi.
- Header server (nginx/PHP/Drupal) sebagai petunjuk teknologi.

**TIDAK terlihat dari luar (di dalam server):**
- Password & akun admin CMS.
- File "pintu belakang" (web shell) yang disembunyikan penyerang.
- Log server (siapa login, kapan, dari IP mana).
- BSSN baru tahu metode persisnya setelah akses server + forensik.

> **Inilah jawaban kenapa "kamu nggak bisa lihat cara masuknya"** — memang tidak ada
> cara melihat dari luar. Pengunjung cuma melihat *hasilnya*.

## 5. Lima Metode Masuk yang Umum (Hasil Investigasi)

1. **CMS tidak di-update / plugin lawas** → ada bug yang bisa dieksploitasi
   (contoh bug Drupal/WordPress versi lama → bisa upload file tanpa izin → upload web shell).
2. **Password admin lemah** → ditebak/bruteforce → login sebagai admin → upload file.
3. **Fitur upload file tanpa validasi** → upload `.php` padahal seharusnya hanya gambar.
4. **Subdomain terlantar / dangling DNS** → instansi buat subdomain untuk proyek cloud,
   lupa menghapus catatan DNS saat proyek selesai → penyerang "klaim" subdomain itu
   (*subdomain takeover*).
5. **Situs tidak aktif / jarang diperbarui** → tidak ada yang memonitor → target favorit.

## 6. Kenapa Mereka Repot-repot "Nebeng"?

Ini **SEO black-hat**:
- Google menganggap domain `.go.id` / `.ac.id` terpercaya (otoritas tinggi).
- Link judi yang numpang di halaman pemerintah otomatis dianggap penting oleh Google.
- Efeknya: situs judi **naik ranking** pencarian tanpa perlu bangun domain baru
  (domain judi biasanya cepat diblokir/blacklist).
- Polri menyebut jaringan ini **hibrida**: "pelaksana teknis" lokal (spesialis SEO)
  + jaringan kriminal transnasional penyedia infrastruktur.

## 7. Pelajaran untuk Puncak C

- **Attack surface**: tiap website punya lapisan; yang "gampang ditembus" bukan domain,
  tapi aplikasi/server/subdomain di belakangnya.
- Cara investigasi (yang dipakai Tirto): **Google Dorking** — misal
  `site:go.id slot gacor` untuk menemukan halaman judi tersembunyi di domain resmi.
- Di bug bounty, kamu mencari celah **dengan izin** — persis tipe kelemahan di atas,
  tapi kamu yang menemukannya duluan dan dilaporkan.

---
**Praktik**: buka folder `praktik/` → `bawaslu/` → lihat `index.html` (situs normal),
`slot-gacor-terbaru/index.html` (yang disisipkan), dan `uploads/webshell.php`
("pintu belakang"). Semua penjelasan ada di `ANATOMI.md`.
