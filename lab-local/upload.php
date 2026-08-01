<?php
// ============================================================
// upload.php — "PINTU MASUK" yang rapuh (vulnerable upload)
// ============================================================
// CELAH #1: hanya mengecek EKSTENSI file (.jpg/.png), bukan ISI file
// CELAH #2: tidak membatasi ukuran / tidak memakai whitelist tipe MIME
// CELAH #3: file disimpan dengan NAMA dan EKSTENSI asli dari user
// ============================================================
$target_dir = __DIR__ . "/uploads/";
$nama        = isset($_POST['nama']) ? $_POST['nama'] : 'pegawai';

if (!isset($_FILES['foto']) || $_FILES['foto']['error'] !== UPLOAD_ERR_OK) {
    header("Location: index.php?gagal=file+tidak+terunggah");
    exit;
}

// ============================================================
// CELAH INTI: cek ekstensi doang, tanpa periksa isi file.
// Penyerang tinggal kasih nama file "foto.jpg" yang isinya PHP.
// ============================================================
$ekstensi = strtolower(pathinfo($_FILES['foto']['name'], PATHINFO_EXTENSION));
$boleh    = array('jpg', 'jpeg', 'png');

if (!in_array($ekstensi, $boleh)) {
    header("Location: index.php?gagal=ekstensi+harus+.jpg+atau+.png");
    exit;
}

$nama_file = date('Ymd_His') . "_" . $nama . "." . $ekstensi;
$nama_file = preg_replace('/[^a-zA-Z0-9_\.\-]/', '_', $nama_file); // bersihkan karakter aneh
$tujuan    = $target_dir . $nama_file;

if (move_uploaded_file($_FILES['foto']['tmp_name'], $tujuan)) {
    header("Location: index.php?sukses=" . urlencode($nama_file));
} else {
    header("Location: index.php?gagal=server+gagal+menyimpan+file");
}
exit;
