# Lab Belajar Web Security - "Badan Publik" rentan ala situs pemerintah
# Image: PHP 8.3 + Apache (mirip stack banyak situs .go.id: nginx/Apache + PHP)
FROM php:8.3-apache

# Aktifkan modul Apache mod_rewrite (standar, agar URL bersih)
RUN a2enmod rewrite

# ============================================================
# CELAH #2 (sengaja): "salah setting" khas shared hosting murah.
# Baris ini membuat Apache MENGEKSEKUSI file .jpg/.jpeg/.png
# sebagai kode PHP. Akibatnya: file berlabel gambar yang isinya
# PHP akan JALAN. (Lihat: AddType application/x-httpd-php)
# ============================================================
RUN printf 'AddType application/x-httpd-php .jpg .jpeg .png\n' > /etc/apache2/conf-available/salah-setting.conf \
 && a2enconf salah-setting

# Copy seluruh aplikasi lab ke document root
COPY index.php upload.php /var/www/html/
COPY uploads/ /var/www/html/uploads/

# Hak akses: folder uploads boleh ditulis web server (ini salah satu celahnya)
RUN chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html/uploads

EXPOSE 80
