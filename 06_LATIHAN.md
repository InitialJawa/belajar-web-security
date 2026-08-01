# 06 — LATIHAN (BERTINGKAT)

> **Ringkasan:** Latihan dari mudah ke sulit. Semua latihan di level 1–2 aman & legal
> (website yang kamu pakai/buka sendiri). Level 3 butuh izin (PC sendiri/lab).

---

## Level 1 — Pemanasan (aman, legal)

**1. Alur request-response.**
Buka website favoritmu (contoh `google.com`). Tekan F12 → tab Network → refresh.
Cari request pertama (biasanya bernama `www.google.com`). Jawab:
- Metode apa? (GET/POST)
- Status code berapa?
- Cari response yang berisi "OK" / 200.

**2. Temukan request yang menghasilkan.**
Buka `https://instausername.com/` → F12 → Network → centang Preserve log →
ketik kata apa pun → klik Generate. Cari request baru yang muncul. Jawab:
- URL-nya apa?
- Parameter apa yang dikirim?
- Response-nya (tab Response) berisi apa?

**3. Baca JS.**
Di halaman yang sama, Ctrl+U → cari `<script src="...">` → buka `main_1.js`.
Temukan kata `query.php`. Jawab: apa yang dikirim ke endpoint itu?

## Level 2 — Menengah (curl)

**4. Replikasi generator pakai curl.**
Di terminal (PowerShell):
```powershell
curl.exe -s "https://instausername.com/inc/query.php?catid=11&n=sayur&num=5"
```
Jawab: response-nya JSON apa? Berapa username yang keluar?

**5. Cek status website dengan curl.**
```powershell
# 200 = normal, 404 = kosong/terhapus, 302 = redirect
curl.exe -s -o NUL -w "%{http_code}`n" "https://www.youtube.com/@bbc"
curl.exe -s -o NUL -w "%{http_code}`n" "https://www.youtube.com/@bbc"
```
Coba beberapa handle YouTube dan catat perbedaan kode statusnya.

**6. Baca header server.**
```powershell
curl.exe -s -o NUL -D - "https://rotendao.bawaslu.go.id/"
```
Cari baris `Server:`, `X-Powered-By:`, `X-Generator:`. Apa kesimpulanmu soal
teknologi situs itu? (Bandingkan dengan `04`.)

## Level 3 — Lanjutan (butuh izin; PC/lab sendiri)

**7. Bongkar praktik/ simulasi.**
Buka `praktik/bawaslu/` dan jawab pertanyaan berikut secara tertulis:
- Dari luar, apa yang terlihat dan tidak terlihat? (lihat `04`)
- Kalau kamu admin situs itu, apa yang pertama kamu periksa setelah menemukan
  folder `slot-gacor-terbaru/`?
- `webshell.php` itu berbahaya kenapa? Jelaskan dengan kata-katamu sendiri.

**8. [SELESAI 1 Agu 2026] Serang lab sendiri (Docker).**
Ikuti `lab-local/README-LAB.md` dan lakukan rantai ini **dengan tangan kamu sendiri**:
- Jalankan server lab di Docker (`localhost:8081`).
- **Recon**: temukan pintu masuk (form upload).
- **Upload webshell**: selundupkan kode PHP berlabel `.jpg/.png` (label tipuan,
  isi senjata). Server yang salah setting akan mengeksekusinya.
- **Aktifkan (RCE)**: buka file-nya + `?cmd=ls` → server menjalankan perintahmu.
- **Buat folder judi**: `mkdir` + tulis `index.html` lewat webshell, BUKAN edit file.
- **Lihat hasil**: buka `localhost:8081/uploads/slot-gacor-terbaru/` → halaman muncul
  tanpa sepengetahuan pemilik.

> **Pelajaran yang didapat sesi ini:**
> - 403 Forbidden muncul saat folder kosong (tidak ada `index.html`) → Apache menolak.
> - `<` dan `>` di shell itu redirection, BUKAN tag HTML → perintah gagal diam-diam.
>   Solusinya: bungkus isi HTML dengan tanda kutip `'...'`, atau pakai base64.
> - Penyerang tidak mengetik perintah manual di URL — mereka pakai tool. Coba
>   `lab-local/kontroler-webshell.py` (perintah `write` & `upload` memakai base64).
> - Rantai ini 100% mekanisme serangan asli (BSSN 2024), dijalankan legal di PC sendiri.

## Cara Mengecek Jawaban Sendiri

- Tidak ada kunci mutlak — yang penting kamu bisa **menjelaskan** alur request-response
  dan menunjukkan request mana yang menghasilkan hasil.
- Kalau ragu, buka `05_ISTILAH.md` lalu jawab lagi.
- Untuk latihan 4–6: jalankan command-nya, cocokkan dengan materi di `02` & `03`.

## Checklist Kelulusan Level 1–3

- [x] Bisa menemukan request yang menghasilkan di sebuah website.
- [x] Bisa membaca metode, URL, dan parameter dari request itu.
- [x] Bisa pakai curl untuk memanggil endpoint.
- [x] Bisa baca status code (200/302/404/500) dan menyimpulkan artinya.
- [x] Bisa menjelaskan perbedaan honeypot, captcha, dan rate limit.
- [x] **Bisa menjelaskan rantai upload webshell → RCE → buat folder (lab sendiri).**

---
Kalau checklist sudah semua tercentang → update `00_ROADMAP.md` langkah 4 & 6 jadi selesai.
