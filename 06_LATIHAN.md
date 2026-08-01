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

**8. Bikin "korban" sendiri (lab).**
Buat website sederhana di PC kamu (misal pakai Node/Express atau file HTML statis),
lalu coba diri sendiri:
- Temukan endpoint/form di website itu.
- Replikasi request-nya dengan curl.
- Catat apa yang terjadi kalau kamu kirim input aneh (misal teks super panjang).
Tujuannya: paham alur request-response tanpa melanggar apa pun.

## Cara Mengecek Jawaban Sendiri

- Tidak ada kunci mutlak — yang penting kamu bisa **menjelaskan** alur request-response
  dan menunjukkan request mana yang menghasilkan hasil.
- Kalau ragu, buka `05_ISTILAH.md` lalu jawab lagi.
- Untuk latihan 4–6: jalankan command-nya, cocokkan dengan materi di `02` & `03`.

## Checklist Kelulusan Level 1–2

- [ ] Bisa menemukan request yang menghasilkan di sebuah website.
- [ ] Bisa membaca metode, URL, dan parameter dari request itu.
- [ ] Bisa pakai curl untuk memanggil endpoint.
- [ ] Bisa baca status code (200/302/404/500) dan menyimpulkan artinya.
- [ ] Bisa menjelaskan perbedaan honeypot, captcha, dan rate limit.

---
Kalau checklist sudah semua tercentang → update `00_ROADMAP.md` langkah 4 jadi selesai.
