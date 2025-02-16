# 📦 Sistem Manajemen Barang
Sistem Manajemen Barang adalah aplikasi berbasis CLI (Command Line Interface) yang memungkinkan pengguna untuk mengelola barang, melakukan transaksi, serta login sebagai admin atau user.
## ✨ Fitur-Fitur
#### 1. Login & Role Management
- Sistem login untuk admin dan user
- Peran admin dapat mengelola barang
- Peran user hanya bisa membeli barang
#### 2. Manajemen Barang (Admin)
- Menampilkan daftar barang dalam tabel
- Menambahkan barang baru
- Menghapus barang (soft delete)
- Mengembalikan barang yang dihapus
- Mengubah informasi barang
#### 3. Transaksi (User)
- Pembelian barang oleh user
- Saldo user otomatis berkurang saat pembelian
#### 4. Data Storage Sementara
- Data barang disimpan dalam list berbasis dictionary

## 🛠️ Cara Menjalankan
#### 1. Persiapan
- Pastikan Python 3.6 ke atas telah terinstal
- Instal dependensi yang diperlukan dengan perintah berikut:
- 
  `!pip install tabulate`
  `!pip install regex` 
#### 2. Jalankan Program
- Jalankan skrip Python:
  
  `python main.py`
#### 3. Login sebagai Admin atau User
- Masukkan username & password yang tersedia di dalam kode

## 📂 Struktur Data
Barang disimpan dalam bentuk list berisi dictionary seperti contoh berikut:

`barang = [
    {'ID': 567, 'Nama Barang': 'Huawei Pura 70 Ultra 16/512GB', 'Tipe': 'Smartphone', 'Merek': 'Huawei', 'Stock':30, 'Harga': 17999000},
    {'ID': 789, 'Nama Barang': 'Infinix GT20 Pro 8/256GB', 'Tipe': 'Smartphone', 'Merek': 'Infinix', 'Stock':40, 'Harga': 3999000}
]`
user dan admin juga disimpan dalam bentuk list seperti contoh atas. 

## 🔑 Catatan Tambahan
- Validasi Input: Sistem memastikan inputan yang dimasukkan sesuai dengan tipe data yang diharapkan.
- Soft Delete: Barang yang dihapus tidak benar-benar dihapus, tetapi bisa dikembalikan.
- Format Tampilan: Menggunakan tabulate agar tampilan lebih rapi.
