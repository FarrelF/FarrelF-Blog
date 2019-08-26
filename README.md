# Farrel Franqois Blog
[![Netlify Status](https://api.netlify.com/api/v1/badges/edc59a5f-e63a-426c-ae65-cffe9153fa04/deploy-status)](https://app.netlify.com/sites/zen-edison-77bc37/deploys)
*Repository* GitHub ini merupakan Kode Sumber dari Blog saya. Blog ini saya buat menggunakan Pelican, yang berbasis Python.

## Cara Kerja
Kode Sumber ini hanya berguna untuk menghasilkan berkas HTML statis saja, dan ini tidak bisa di eksekusi secara langsung, seperti hal nya Blog yang di buat dengan WordPress. (Karena sesuai dengan peruntukan nya, yakni: *Static Site Generator*)

Untuk menghasilkan konten yang kemudian di sebar melalui Internet, saya men-*deploy* kode sumber ini ke Netlify, lalu mereka lah yang menghasilkan berkas HTML statis di dalam nya, yang kemudian di sebar ke Internet.

## Cara Install
Untuk meng-installnya, buatlah sebuah 'Lingkungan Virtual' (atau bahasa Inggris nya adalah: *Virtual Environment*) dengan `virtualenv`, lalu aktifkan "Lingkungan" tersebut.

Saya sarankan Anda gunakan Python 3.6, Python 3.7 atau yang lebih baru sebelum/saat membuat sebuah Lingkungan Virtual.

Setelah di aktifkan, Install semua ketergantungan yang ada di dalam berkas `requirements.txt` dengan `pip`.

Lalu, kamu bisa coba untuk menghasilkan sebuah berkas HTML Statis ini dengan Pelican, yang kemudian bisa kamu akses dengan Web Browser kamu.

Di dalam GNU/Linux, kamu dapat eksekusi perintah berikut agar Pelican dapat menghasilkan Berkas HTML Statis dan juga mengaktifkan fitur Web Server pada Python:

**Catatan**: Tapi sebelum itu, pastikan kalau kamu sudah berada di dalam Folder Kode Sumber nya, yah :-)

```bash
$ pelican --autoreload --listen
```

Sedangkan di Windows, ada tiga (yang sebenarnya 'empat') langkah yang harus kamu turuti, yaitu:
1. Hasilkan Berkas HTML terlebih dahulu dengan Pelican, menggunakan Perintah berikut:
```powershell
> pelican --autoreload
```
2. Kemudian, kamu buka lagi CMD/PowerShell di Jendela yang baru atau buka Tab Baru jika kamu menggunakan [Windows Terminal](https://github.com/microsoft/terminal), lalu aktifkan "Lingkungan Virtual" nya.

3. Setelah itu, Aktifkan fitur Web Server pada Python dengan perintah berikut:
```powershell
> pelican --listen
```

Setelah semua nya selesai dan dinyatakan berhasil, bisa kamu coba buka Alamat URL `http://localhost:8000` di dalam Web Browser kamu, dan kamu akan melihat hasilnya :-)

## Lisensi
Kode Sumber ini saya Lisensikan dengan GNU Affero General Public License v3 (GNU AGPLv3) yang merupakan Lisensi *Copyleft* dan bisa Anda lihat/baca di dalam berkas [COPYING](https://github.com/FarrelF/FarrelF-Blog/blob/master/COPYING).

Sedangkan konten yang ada di dalam blog ini, beserta terjemahan nya (kecuali jika di nyatakan [sebaliknya](https://farrel.franqois.id/catatan-hukum)) di lisensi kan dengan [Creative Commons Attribution-ShareAlike Internasional 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (Atau, disingkat: CC BY-SA 4.0).

Untuk lebih lengkap nya, silahkan kunjungi Laman [Lisensi](https://farrel.franqois.id/lisensi) di dalam Blog Saya :-)
