# 05 — ISTILAH (KAMUS)

> **Ringkasan:** Referensi cepat. Kalau ketemu kata asing di materi lain, cek di sini.
> Ditulis sederhana + analogi.

---

## Dasar Web

- **HTTP** — bahasa komunikasi browser ↔ server (request & response).
- **Request** — permintaan browser ke server ("minta halaman").
- **Response** — jawaban server (berisi status code + isi halaman/data).
- **GET** — minta data (parameter nempel di URL).
- **POST** — kirim data (isi form; parameter di body).
- **Status code** — hasil permintaan: `200` ok, `302` redirect, `404` tidak ketemu,
  `500` error server.
- **Endpoint** — alamat khusus tempat data diproses, misal `/inc/query.php`.
- **Parameter** — data yang dikirim ke server (`?q=sayur&cat=11`).
- **Header** — identitas/kartu request (browser, bahasa, cookie).
- **Cookie** — "tanda pengenal" kecil di browser untuk sesi login/pelacakan.
- **CMS** — software pengelola website (WordPress, Drupal). "Pintu" utama sebuah website.
- **Web shell / backdoor** — file yang di-upload penyerang biar bisa pegang remote
  server. Ini "pintu belakang"-nya.

## Reverse Engineering & Otomasi

- **DevTools** — panel bawaan browser (F12) untuk inspeksi elemen & request.
- **Network tab** — daftar semua request yang lewat. Jendela dunia.
- **Preserve log** — pengaturan biar request lama nggak hilang saat refresh.
- **Pretty-print** — tombol di DevTools untuk merapikan JS yang minified.
- **Minified JS** — kode JS yang dipadatkan jadi satu baris (susah dibaca).
- **Honeypot** — field/form tersembunyi yang menarik bot. Bot mengisinya, manusia tidak.
  Kalau terisi → ketahuan bot.
- **Captcha** — tes "saya bukan robot".
- **Rate limit** — pembatasan jumlah request (contoh: antrian "number 10 in the queue").
- **JS-heavy** — website yang isinya cuma shell JS (butuh browser asli; curl tidak cukup).
- **Scraping** — mengambil data dari website secara otomatis.

## Keamanan / Serangan

- **Reverse engineering** — membongkar cara kerja sesuatu (website) dari jejaknya.
- **Attack surface** — semua titik yang bisa diserang (form, endpoint, file upload, subdomain).
- **Brute force** — menebak password berulang-ulang sampai benar.
- **SQL injection** — mengirim query aneh lewat input supaya database bocor.
- **XSS** — menyuntik script lewat input supaya jalan di browser korban.
- **File upload tanpa validasi** — upload file berbahaya (misal `.php`) padahal
  seharusnya hanya gambar → jalan masuk web shell.
- **Defacement** — mengubah tampilan website secara ilegal.
- **URL injection** — menyisipkan URL/halaman ilegal di dalam website resmi.
- **Dangling DNS** — catatan DNS yang menunjuk ke layanan yang sudah tidak dipakai.
- **Subdomain takeover** — mengklaim subdomain yang DNS-nya "menggantung" (dangling).
- **Google Dorking** — mencari di Google pakai operator khusus (contoh `site:go.id slot`).
- **Black-hat SEO** — trik kotor supaya naik ranking Google (contoh: nebeng link judi
  di situs pemerintah).
- **Bug bounty** — program di mana perusahaan/pemerintah membayar orang yang menemukan
  celah, **dengan izin dan aturan jelas**.
- **Scope** — batas yang boleh diuji di program bug bounty (halaman/subdomain apa saja).
- **Pentest / ethical hacking** — menguji keamanan secara sah dengan izin pemilik.
- **OSCP** — sertifikasi ethical hacking (goal jangka panjang Puncak C).

## Checker Username (Studi Kasus)

- **Taken / Free** — username terpakai / kosong.
- **Halaman profil** — `instagram.com/username`, `tiktok.com/@username`, dll.
- **API internal** — endpoint khusus platform yang lebih akurat dari halaman biasa
  (contoh IG: `i.instagram.com/api/v1/users/web_profile_info/?username=...`).
