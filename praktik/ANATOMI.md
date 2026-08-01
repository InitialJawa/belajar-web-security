# Anatomi: Situs Pemerintah Disusupi Judi Online

## Yang TERLIHAT dari luar (oleh siapa pun yang buka browser)
- `rotendao.bawaslu.go.id/`            -> HTTP 200 (situs normal)
- `rotendao.bawaslu.go.id/slot-gacor-terbaru/` -> HTTP 200 (halaman judi, SEKARANG sudah 404 karena dibersihkan)
- Header server: `Server: nginx/1.20.1`, `X-Powered-By: PHP/8.3.31`, `X-Generator: Drupal 10`
  -> Inilah PETUNJUK satu-satunya: situs ini pakai CMS **Drupal 10** di server **nginx + PHP**.

## Yang TIDAK terlihat dari luar (kenapa kamu "nggak bisa lihat")
- Nama pengguna & password admin CMS.
- File `uploads/webshell.php` yang disembunyikan penyerang.
- Log server (siapa login, kapan, dari IP mana).
- Semua ini ada DI DALAM server — kamu tidak bisa melihatnya lewat browser.

## Cara masuk yang umum (dari investigasi tirto.id + BSSN, 2024-2026)
1. **CMS tidak di-update / plugin lawas** -> ada bug yang bisa dieksploitasi
   (contoh: bug di Drupal/WordPress versi lama -> bisa upload file tanpa izin -> upload webshell.php).
2. **Password admin lemah** -> ditebak/bruteforce, lalu login sebagai admin -> upload file.
3. **Fitur upload file tanpa validasi** -> upload file `.php` padahal seharusnya cuma boleh gambar.
4. **Subdomain terlantar / dangling DNS** -> instansi buat subdomain buat proyek, lupa hapus,
   penyerang "klaim" subdomain itu (subdomain takeover).
5. **Situs tidak aktif / jarang diperbarui** -> tidak ada yang monitor -> target favorit.

## Kenapa mereka repot-repot?
Google menganggap domain .go.id "terpercaya". Link judi yang numpang di halaman
bawaslu.go.id otomatis dianggap penting oleh Google -> situs judinya naik ranking.
