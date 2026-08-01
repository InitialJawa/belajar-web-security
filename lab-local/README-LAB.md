# Lab Lokal — Simulasi "Situs Pemerintah yang Disusupi"

> **PERINGATAN:** Lab ini **hanya untuk latihan di PC sendiri** (localhost).
> Jangan pernah mencoba hal yang sama ke situs orang lain tanpa izin tertulis.
> Baca `07_ETIKA_DAN_HUKUM.md` dulu sebelum mulai.

## Apa ini?

Server web mini (PHP + Apache, di dalam Docker) yang sengaja dibuat rentan,
persis seperti **arsitektur banyak situs `.go.id`**: PHP + folder `uploads/` +
form upload yang hanya mengecek ekstensi file.

**Dua celah yang sengaja dibuat (dua-duanya nyata di lapangan):**
1. `upload.php` cuma mengecek **ekstensi** (.jpg/.png) — isi file tidak diperiksa.
2. Apache **salah setting** (khas shared hosting murah): file `.jpg/.jpeg/.png`
   dieksekusi sebagai kode PHP (lihat `AddType` di Dockerfile).

Keduanya ketemu → file "gambar" yang isinya PHP akan **jalan** begitu dibuka.

Di sinilah kamu akan **menyerang** — bukan menulis file sendiri — dan merasakan
persis rantai serangan yang membuat 3.908 laman pemerintah disusupi judi.

## Rantai Serangan (yang akan kamu lakukan)

1. **Recon** — buka situs, cari bagian yang menerima file (form upload).
2. **Upload webshell** — buat file PHP "yang menyamar jadi gambar", upload lewat form.
3. **Aktifkan** — buka file itu di browser, cek apakah kode PHP-nya jalan (RCE).
4. **Buat folder** — lewat webshell, buat folder `slot-gacor-terbaru/` + `index.html`
   **tanpa akses normal** (persis cara penyerang bikin folder judi).
5. **Lihat hasil** — buka `http://localhost:8081/slot-gacor-terbaru/` dan rasakan:
   folder itu muncul tanpa sepengetahuan pemilik.

## Jalankan

```powershell
cd "D:\ALL IN ONE\CODE\belajar-web-security\lab-local"
docker build -t lab-badan-publik .
docker run -d --name lab-badan-publik -p 8081:80 lab-badan-publik
```

Buka: http://localhost:8081/

> Catatan: pakai port 8081 karena 8080 di PC ini sudah dipakai proses lain.
> Kalau port 8081 ikut tabrakan, ganti angka di bagian `-p <port>:80`.

## Stop / Bersihkan

```powershell
docker stop lab-badan-publik
docker rm lab-badan-publik
docker rmi lab-badan-publik
```

## File

| File | Peran |
|---|---|
| `index.php` | Halaman depan "Badan Publik" dengan form upload foto |
| `upload.php` | "Pintu masuk" yang rapuh — cek ekstensi doang, isi file tidak diperiksa |
| `shell.php` | Web shell (pintu belakang) — dipakai setelah berhasil di-upload |
| `senjata-webshell.png` | Contoh "senjata": isi PHP berlabel `.png` — persis yang di-upload ke server |
| `uploads/` | Tempat file ter-upload (folder inilah yang "disusupi") |
| `Dockerfile` | Setup PHP 8.3 + Apache, termasuk "salah setting" AddType |
