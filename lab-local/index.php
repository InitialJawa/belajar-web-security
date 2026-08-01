<?php
// ============================================================
// HALAMAN DEPAN "BADAN PUBLIK" (lab belajar web security)
// ============================================================
// Ini simulasi situs instansi yang "lupa maintenance":
// - Ada form upload "foto profil" yang cuma ngecek ekstensi
// - Tidak ada validasi isi file (celah utama)
// - Terlihat resmi dari depan, tapi ada pintu belakang terbuka
// ============================================================
$sukses = isset($_GET['sukses']) ? htmlspecialchars($_GET['sukses']) : '';
$gagal  = isset($_GET['gagal'])  ? htmlspecialchars($_GET['gagal'])  : '';
?>
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Badan Publik - Sistem Kepegawaian</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f4f8; color: #1a202c; }
  .header { background: #1a365d; color: #fff; padding: 18px 40px; display: flex; justify-content: space-between; align-items: center; }
  .header h1 { font-size: 20px; font-weight: 600; }
  .header small { opacity: .75; }
  .container { max-width: 960px; margin: 30px auto; padding: 0 20px; }
  .card { background: #fff; border-radius: 10px; padding: 28px; box-shadow: 0 2px 8px rgba(0,0,0,.08); margin-bottom: 20px; }
  .card h2 { font-size: 18px; margin-bottom: 14px; color: #1a365d; }
  .banner-lab { background: #fff7ed; border: 1px solid #fdba74; color: #9a3412; padding: 12px 16px; border-radius: 8px; font-size: 13px; margin-bottom: 20px; }
  .field { margin-bottom: 16px; }
  .field label { display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; }
  input[type="text"], input[type="file"] { width: 100%; padding: 10px 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 14px; }
  .btn { background: #1a365d; color: #fff; border: 0; padding: 11px 22px; border-radius: 6px; font-size: 14px; font-weight: 600; cursor: pointer; }
  .btn:hover { background: #2c5282; }
  .notif { padding: 10px 14px; border-radius: 6px; font-size: 13px; margin-bottom: 16px; }
  .notif.ok { background: #f0fff4; border: 1px solid #68d391; color: #22543d; }
  .notif.err { background: #fff5f5; border: 1px solid #fc8181; color: #742a2a; }
  .list { list-style: none; }
  .list li { padding: 10px 0; border-bottom: 1px solid #edf2f7; font-size: 14px; }
  .list li a { color: #2b6cb0; text-decoration: none; }
  .footer { text-align: center; padding: 24px; color: #718096; font-size: 12px; }
</style>
</head>
<body>
  <div class="header">
    <div>
      <h1>Badan Publik — Sistem Kepegawaian</h1>
      <small>Layanan Informasi Pegawai &amp; Profil Instansi</small>
    </div>
  </div>

  <div class="container">
    <div class="banner-lab">
      <strong>LAB BELAJAR (lokal):</strong> Situs ini <em>sengaja</em> dibuat rentan untuk latihan.
      Cuma jalan di <code>localhost</code>, bukan situs sungguhan.
    </div>

    <?php if ($sukses): ?>
      <div class="notif ok">Berhasil mengunggah file: <strong><?= $sukses ?></strong></div>
    <?php elseif ($gagal): ?>
      <div class="notif err">Upload gagal: <?= $gagal ?></div>
    <?php endif; ?>

    <div class="card">
      <h2>Unggah Foto Profil Pegawai</h2>
      <form method="POST" action="upload.php" enctype="multipart/form-data">
        <div class="field">
          <label for="nama">Nama Lengkap</label>
          <input type="text" id="nama" name="nama" placeholder="mis. Budi Santoso" required>
        </div>
        <div class="field">
          <label for="foto">File Foto (JPG/PNG)</label>
          <input type="file" id="foto" name="foto" required>
        </div>
        <button type="submit" class="btn">Unggah Foto</button>
      </form>
      <p style="font-size:12px;color:#718096;margin-top:12px;">
        Catatan sistem: hanya mengecek nama file berakhiran .jpg / .png. Isi file tidak diperiksa.
      </p>
    </div>

    <div class="card">
      <h2>Daftar Dokumen Publik</h2>
      <ul class="list">
        <li><a href="#">Profil Instansi (PDF)</a></li>
        <li><a href="#">SK Kepala Instansi Nomor 12/2024</a></li>
        <li><a href="#">Laporan Tahunan 2025</a></li>
      </ul>
    </div>
  </div>

  <div class="footer">Simulasi edukasi — dibuat untuk modul belajar web security, berjalan lokal.</div>
</body>
</html>
