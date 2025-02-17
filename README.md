## 📌 Ganteng Ganteng Seluler - Manajemen Data Barang dan Transaksi  

### 📖 Deskripsi  
Proyek ini merupakan sistem manajemen data barang dan transaksi sederhana menggunakan Python. Program ini memungkinkan pengguna untuk login sebagai **user** atau **admin**, melakukan pembelian, serta mengelola data barang (CRUD).    

## **Fitur Utama**
- **Login Pengguna dan Admin**:  
  - Pengguna dapat masuk dengan akun mereka untuk melakukan transaksi.  
  - Admin memiliki akses untuk mengelola data barang.  

- **Manajemen Barang (CRUD - Create, Read, Update, Delete)**:  
  - Menampilkan daftar barang yang tersedia dalam bentuk tabel.  
  - Menambahkan barang baru ke dalam daftar.  
  - Menghapus barang dari daftar.  
  - Memperbarui informasi barang.  
  - Mengembalikan barang yang sebelumnya telah dihapus.  

- **Transaksi Pembelian**:  
  - Pengguna dapat memilih produk berdasarkan kategori (laptop, smartphone, tablet).  
  - Sistem akan memverifikasi saldo pengguna sebelum transaksi berhasil.  
  - Riwayat transaksi akan disimpan di akun pengguna.  

## **Teknologi yang Digunakan**
- Python 3
- Library:
  - `tabulate` → Untuk menampilkan data dalam bentuk tabel  
  - `random` → Untuk menghasilkan ID unik secara acak  
  - `datetime` → Untuk mencatat tanggal dan waktu transaksi  

## **Struktur Data**
- **`user`**: Menyimpan informasi pengguna, termasuk nama, email, password, saldo, dan riwayat transaksi.  
- **`admin`**: Menyimpan akun admin yang dapat melakukan manajemen barang.  
- **`barang`**: Menyimpan daftar barang elektronik yang tersedia, termasuk ID, nama, tipe, merek, stok, dan harga.  
- **`data_hapus`**: Menyimpan data barang yang telah dihapus untuk dapat dikembalikan jika diperlukan.  
- **`akun_login`**: Menyimpan data pengguna yang sedang login agar dapat digunakan di fitur lain.  

## **Validasi Input**
Program ini memiliki berbagai fungsi validasi input untuk memastikan bahwa pengguna memasukkan data yang sesuai:
- **`validasi_input_alfabet()`** → Hanya menerima input berupa huruf.  
- **`validasi_input_angka()`** → Memastikan input hanya berupa angka.  
- **`validasi_input_tipe()`** → Memastikan tipe barang hanya dapat berupa `smartphone`, `tablet`, atau `laptop`.  

## 📦 Instalasi  
Pastikan Anda telah menginstal **Python 3.x** di komputer Anda. Kemudian, instal dependensi yang diperlukan dengan menjalankan:  
```bash
pip install tabulate
```

---

## 🚀 Cara Menjalankan Program  
1. Jalankan script Python:  
   ```bash
   python nama_script.py
   ```
2. Masukkan email dan password sesuai dengan akun user atau admin yang tersedia.  
3. Ikuti petunjuk yang muncul di terminal.  

---

## 🛠 Library yang Digunakan  
| Library   | Fungsi |
|-----------|--------|
| `tabulate` | Menampilkan data dalam bentuk tabel |
| `random`   | Menghasilkan ID unik untuk barang |
| `datetime` | Mengambil tanggal dan waktu transaksi |

---

## 👥 Akun Default  
**User**  
- 📧 `jisoo@gmail.com` | 🔑 `jisoo123` | 💰 `Rp20.000.000`  
- 📧 `jennie@gmail.com` | 🔑 `jennie123` | 💰 `Rp25.000.000`  
- 📧 `rose@gmail.com` | 🔑 `rose123` | 💰 `Rp150.000.000`  
- 📧 `lisa@gmail.com` | 🔑 `lisa123` | 💰 `Rp20.000.000`  

**Admin**  
- 📧 `admin@gmail.com` | 🔑 `admin123`  

---

## 📜 Lisensi  
Proyek ini bebas digunakan untuk keperluan pembelajaran dan pengembangan lebih lanjut. 🚀
