# BookPals 📚

[![Deployment](https://github.com/D09-PBP2023/proyek-tengah/actions/workflows/pbp-deploy.yml/badge.svg)](https://github.com/D09-PBP2023/proyek-tengah/blob/main/.github/workflows/pbp-deploy.yml)
[![Styling](https://img.shields.io/badge/Styling-CDN_Tailwind-blue)](https://tailwindcss.com/)

"Rajin Membaca, Cerewet di BookPals"
> Sebuah karya dari kami, kelompok D09 untuk Indonesia.

> Proyek ini dibuat untuk memenuhi tugas Proyek Tengah Semester pada mata kuliah Pemograman Berbasis Platform (PBP) yang diselenggarakan oleh Fakultas Ilmu Komputer, Universitas Indonesia di Semester Gasal Tahun Ajaran 2023/2024.

# [Anggota Kelompok]
Proyek aplikasi ini dibuat oleh kelompok D09 yang beranggotakan:
- [Arvin](https://github.com/ArvinCS) (2206041562)
- [Gilang Fajar Pratama](https://github.com/gilangp03) (2206082631)
- [Marvel Martin Everthard](https://github.com/marvelm57) (2206081345)
- [Muhammad Radhitya Utomo](https://github.com/MRadhityaUtomo) (2206830744)
- [Taniella](https://github.com/eilalleinat) (2206082316)
- [Tengku Laras Malahayati](https://github.com/rxa15) (2206081641)

# [Latar Belakang BookPals]
Buku adalah jendela dunia. Ungkapan tersebut mengandung arti yang sangat luas sekaligus mengajak semua orang untuk membaca buku karena orang yang membaca buku akan memperoleh wawasan pengetahuan yang sangat bermanfaat. Beragam karya tulis semakin berkembang sejak manusia menemukan aksara. Dari kitab susastra kuno, kita dapat menggali kemampuan manusia dalam memahami beragam fenomena dalam kehidupan. Diseminasi pengetahuan ke berbagai belahan dunia semakin pesat sejak manusia menemukan mesin cetak. Penemuan teknologi komputer dan internet awalnya diharapkan akan semakin mendukung penyebaran informasi. Sayangnya, minat baca tidak berbanding lurus dengan penemuan teknologi tersebut. Secara singkat, dapat disimpulkan bahwa minat membaca di berbagai belahan dunia semakin menurun yang akhirnya juga mempengaruhi kemampuan literasi seseorang. 

Dalam sebuah riset yang dilakukan oleh UNESCO, Indonesia dinyatakan sebagai salah satu negara yang menduduki urutan bawah literasi dunia. Riset tersebut menunjukkan bahwa minat baca masyarakat Indonesia **HANYA 0.001%**. Akan tetapi, Indonesia menduduki peringkat kelima dunia dalam negara yang memiliki gadget terbanyak (Sumber: [KOMINFO](https://www.kominfo.go.id/content/detail/10862/teknologi-masyarakat-indonesia-malas-baca-tapi-cerewet-di-medsos/0/sorotan_media#:~:text=Fakta%20pertama%2C%20UNESCO%20menyebutkan%20Indonesia,1%20orang%20yang%20rajin%20membaca)). Dengan kondisi yang sedemikian rupa, kami ingin menumbuhkan kembali minat baca tanpa mengabaikan kemajuan teknologi. Dalam projek ini, kami akan merancang sebuah aplikasi berbasis web bernama **BookPals** yang dapat digunakan untuk menghubungkan para penikmat buku dan literasi. Perancangan aplikasi ini terinspirasi dari kegiatan [**BACA BARENG**](https://instagram.com/bacabareng.sbc?igshid=MzRlODBiNWFlZA==) yang diadakan oleh Silent Book Club Jakarta di Taman Literasi Martha Tiahahu. Setiap anggota komunitas tersebut biasanya memilih satu buku pilihan masing-masing yang kemudian akan diceritakan kembali di hadapan anggota lainnya. Dengan mengandaikan kegiatan anggota komunitas tersebut, kami membuat perancangan fitur yang mampu mengajak pengguna untuk saling bertukar buku dan memberikan ulasan setelah membacanya. Tidak hanya itu, kami juga mengundang pengguna kami untuk menjelajahi buku-buku baru melalui opsi pemilihan buku berdasarkan genre, kategori, serta rating yang diberikan oleh pengguna lain. 

Kami berharap kehadiran BookPals tidak hanya dapat mengembalikan minat literasi masyarakat Indonesia, tetapi juga memberikan wadah bagi para peminat buku untuk saling bertukar pandangan. Melalui aplikasi ini, kami berupaya menciptakan lingkungan bagi para pembaca untuk berinteraksi, berbagi ulasan, dan mendiskusikan berbagai buku yang mereka baca. Mari bersama-sama menjelajahi dunia literasi bersama BookPals. 
# [Daftar Modul yang Akan Diimplementasikan]
Berikut adalah daftar modul yang akan diimplementasikan dalam proyek ini beserta penjelasannya:
1. **Modul Kelompok**
   
| Modul | Penjelasan |
| -- | -- |
| **Authentication** | Pengguna BookPals dapat melakukan registrasi akun, *login*, dan *logout*|
| **About Us** | Pengguna BookPals dapat melihat deskripsi dan latar belakang pembuatan BookPals oleh Kelompok D09|

2. **Modul Buku**
   
| Modul | Penjelasan |
| ------ | -- |
| **Book Catalog** | Modul ini terdiri dari submodul **list book**, **book view**, **list owner**, dan **bookmark/add to favorites**, yang masing-masing berperan agar pengguna BookPals dapat **melihat list buku-buku yang tersedia**, **menampilkan judul dan informasi terkait suatu buku yang dipilih**, **menampilkan *username* pengguna-pengguna lain yang memiliki buku tersebut**, serta **menambahkan buku yand dipilih ke *bookmark***|
| **Book Sharing** | Modul ini terdiri dari submodul **Book Review** dan **Book Swap** yang berperan agar pengguna BookPals dapat mengisi dan menampilkan ulasannya terhadap suatu buku dan menginisiasi pertukaran buku dengan pengguna yang lain |
| **Book Entry & Review for Admin** | Admin BookPals akan mengecek apakah suatu buku yang akan ditambahkan ke list buku telah tersedia di database. Kemudian, admin akan menyetujui/menolak *request* menambah suatu buku dari pengguna BookPals | 
# [Sumber Dataset Katalog Buku]
Kami akan menggunakan *dataset* dari Kaggle: https://www.kaggle.com/datasets/drahulsingh/best-selling-books sebagai *database* dari list buku yang akan ditampilkan di BookPals.
# [*Role* Pengguna]
Berikut adalah jenis peran pengguna BookPals beserta penjelasannya:
## 1. User
### User yang Telah Terautentikasi
- Melakukan pencarian dan *filter* buku
- Melihat list buku
- Menambahkan buku ke *bookmark*
- Memberikan rating dan ulasan terkait buku yang telah dibaca
- Melakukan pertukaran buku dengan pengguna lain
- Membuat *request* penambahan buku ke *database*
### User yang Belum Terautentikasi (*Guest*)
- Melakukan pencarian dan *filter* buku
- Melihat list buku
## 2. Admin
- Mengecek apakah buku yang di-*request* oleh User telah tersedia di list buku atau tidak
- Menyetujui/Menolak permintaan menambah buku dari User

# [Setup the development]

1. Buat env dengan `python -m venv env`.
2. Setiap memulai development, aktifkan env dengan `activate` di folder `env/Scripts`.
3. Install semua package yang wajib dengan `pip install -r requirements.txt`.
4. Lakukan sinkronisasi migration files dengan `python manage.py migrate`.
5. Voila! Coba jalankan proyeknya dengan `python manage.py runserver`.
