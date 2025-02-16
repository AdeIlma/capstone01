from tabulate import tabulate #import tabulate agar untuk menampilkan tabel
import regex as re #untuk memvalidasi email pada kode ini
import random  #untuk menampilkan ID secara random agar uniqe
from datetime import datetime #untuk mengambil tanggal dan waktu

#membuat data dummy
user = [
    {'Nama':'Jisoo', 'email': 'jisoo@gmail.com', 'password': 'jisoo123', 'saldo':20000000, 'transaksi':[]},
    {'Nama':'Jennie', 'email': 'jennie@gmail.com', 'password': 'jennie123', 'saldo':25000000, 'transaksi':[]},
    {'Nama':'Rose', 'email': 'rose@gmail.com', 'password': 'rose123', 'saldo':150000000, 'transaksi':[]},
    {'Nama':'Lisa', 'email': 'lisa@gmail.com', 'password': 'lisa123', 'saldo':20000000, 'transaksi':[]}
]

admin = [
    {'Nama':'admin', 'email': 'admin@gmail.com', 'password': 'admin123'}
]

barang = [
    {'ID': 567, 'Nama Barang': 'Huawei Pura 70 Ultra 16/512GB', 'Tipe': 'Smartphone', 'Merek': 'Huawei', 'Stock':30, 'Harga': 17999000},
    {'ID': 789, 'Nama Barang': 'Infinix GT20 Pro 8/256GB', 'Tipe': 'Smartphone', 'Merek': 'Infinix', 'Stock':40, 'Harga': 3999000},
    {'ID': 999, 'Nama Barang': 'Apple MacBook Pro M4 14 inci (2024)', 'Tipe': 'Laptop', 'Merek': 'Apple', 'Stock':10, 'Harga': 27999000},
    {'ID': 767, 'Nama Barang': 'Samsung Galaxy Tab S8+ 5G 8/256GB', 'Tipe': 'Tablet', 'Merek': 'Samsung', 'Stock':20, 'Harga': 16999000},
    {'ID': 666, 'Nama Barang': 'OPPO Find N3 Fold 16/512GB', 'Tipe': 'Smartphone', 'Merek': 'Oppo', 'Stock':15, 'Harga': 19999000},
    {'ID': 675, 'Nama Barang': 'Huawei Matepad Air 11.5 8/128GB', 'Tipe': 'Tablet', 'Merek': 'Huawei', 'Stock':25, 'Harga': 5999000},
    {'ID': 111, 'Nama Barang': 'Huawei MateBook D14 i5 12G 2024 ', 'Tipe': 'Laptop', 'Merek': 'Huawei', 'Stock':30, 'Harga': 7999000}
]

data_hapus = [] #untuk menyimpan data yang telah dihapus agar dapat dikembalikan lagi
existing_ids = {567, 789, 767, 666, 675, 111}  #Untuk menyimpan ID yang sudah digunakan

def random_id():
    """Fungsi untuk menghasilkan ID acak yang unik"""
    while True:  #Loop terus menerus sampai menemukan ID yang unik
        random.seed(42)
        new_id = random.randint(100, 999)  # Buat ID acak antara 100-999
        if new_id not in existing_ids:  # Cek apakah ID sudah ada di existing_ids
            return new_id  #Jika unik, kembalikan ID dan keluar dari loop

# Fungsi untuk validasi variabel2 yang menggunakan huruf
# function validasi input alfabet 
def validasi_input_alfabet(prompt):
    while True:
        inputan = input(prompt)
        if inputan.replace(" ","").isalpha(): #replace untuk mengubah dan isalpha untuk memvalidasi huruf agar tidak ada angka
            return inputan
        else:
            print('inputan harus huruf')

# function validasi input huruf
def validasi_input_angka(prompt):
    while True:
        inputan = input(prompt).strip() #fungsi strip agar menghilangkan strip 
        if inputan == '0':
            return None  # Mengembalikan None untuk menandakan pembatalan
        if inputan.isdigit():
            return int(inputan)
        print("Input harus berupa angka positif!")

def validasi_input_tipe(prompt):
  while True:
    inputan = input(prompt)
    if inputan == 'smartphone' or inputan == 'tablet' or inputan == 'laptop':
      return inputan
    else:
      print('inputan harus smartphone/tablet/laptop')

def input_data(prompt):
    while True:
        inputan = input(prompt).strip().lower()
        if inputan in ['ya', 'tidak']:
            return inputan  # Langsung return tanpa mencetak "Update selesai!"
        print('Inputan harus "ya" atau "tidak". Silakan coba lagi.')

def login(): #fungsi login admin dan user
  while True: #perulangan untuk input email dan password agar jika salah akan balik lagi ke input
     email = input('Masukkan Email: ')
     password = input('Masukkan Password: ')
     if not re.fullmatch(r'\b\w+@\w+.\S*\b', email): #memvalidasi email agar ketika salah bisa kembali ke input, menggunakan regex
      print('Email tidak valid')
      continue #melewati kondisi ini, karena kondisinya jika bukan dari validasi email
     for cari_akun in user: #perulangan untuk mencari akun pada data dummy user, disini membuat variabel yang mendefinisikan data user
       if cari_akun['email'] == email and cari_akun['password'] == password: #jika pada data user sudah benar email dan passwordnya maka akan berhasil login
          print(f"\nLogin Berhasil! Selamat datang, {cari_akun['Nama']}")
          print(f"Saldo Anda: Rp{cari_akun['saldo']:,}")
          return cari_akun # Mengembalikan informasi user yang login agar dapat disimpan pada akun_login
     for cari_admin in admin:
       if cari_admin['email'] == email and cari_admin['password'] == password:
          print(f"\nLogin Berhasil! Selamat datang, {cari_admin['Nama']}")
          return cari_admin # Mengembalikan informasi user yang login agar dapat disimpan pada akun_login

     print('Email atau Password salah')

akun_login = None
# akun_login akan menyimpan data akun agar bisa digunakan di fitur lain

#Menampilkan data barang
def tampilkan_barang(barang):
  teks = "\nData Barang Ganteng Ganteng Seluler:"
  lebar = 80  # Atur lebar
  print(f"\033[1m{teks.center(lebar)}\033[0m")
  print(tabulate(barang, headers = 'keys', tablefmt='simple_grid')) #menampilkan data barang menggunakan library tabulate

# Fungsi untuk menambah data baru
def menambahkan_data(barang):
        id = random_id() #menggunakan fungsi random_id agar id untuk fungsi menambahkan data
        nama_barang = input('Masukkan nama barang: ').title() #input data title digunakan agar huruf kapital didepan kata
        tipe = validasi_input_tipe('Masukkan tipe barang (smartphone/tablet/laptop): ').title()
        merek = validasi_input_alfabet('Masukkan merek barang: ').title()
        stock = validasi_input_angka('Masukkan stok: ')
        harga = validasi_input_angka('Masukkan harga: ')
        barang.append({'ID': id, 'Nama Barang': nama_barang, 'Tipe': tipe, 'Merek': merek, 'Stock': stock, 'Harga': harga})
        print(f"\nData berhasil ditambahkan!")
        return tampilkan_barang(barang)

def hapus_data(barang):
    global data_hapus
    while True:
        tampilkan_barang(barang)
        id_hapus = validasi_input_angka('Masukkan ID data yang ingin dihapus (0 untuk keluar): ')
        if id_hapus is None:  # Handle pembatalan
            return
        id_hapus = int(id_hapus)  # Konversi ke integer 
        
        for item in barang:
            if item['ID'] == id_hapus:
              konfirmasi = input_data("Apakah Anda yakin ingin menghapus data ini? (ya/tidak): ")
              if konfirmasi.lower() != "ya":
                  continue
              data_hapus.append(item)
              barang.remove(item)
              print("\nData Berhasil Dihapus!")
              break
        else:
            print("Data tidak ditemukan. Silakan coba lagi.")
            continue

        lanjut = input_data("Apakah ingin menghapus barang lain? (ya/tidak): ")
        if lanjut.lower() == "tidak":
            break

def mengubah_data(barang):
    while True:
        tampilkan_barang(barang)
        id_update = validasi_input_angka('Masukkan ID produk yang ingin diupdate (0 untuk keluar): ')
        if id_update is None:
            return

        # Cari barang berdasarkan ID
        produk_ditemukan = None
        for item in barang:
            if item['ID'] == int(id_update):
                produk_ditemukan = item
                break
        
        if produk_ditemukan is None:
            print("ID tidak ditemukan. Silakan coba lagi.")
            continue

        while True:
            print("\n=== Pilih Data yang Ingin Diperbarui ===")
            print("1. Nama Barang")
            print("2. Tipe")
            print("3. Merek")
            print("4. Stock")
            print("5. Harga")
            print("0. Selesai")

            pilihan = validasi_input_angka("Masukkan pilihan: ")
            if pilihan is None or pilihan == 0:
                break
            update_berhasil = True
            match int(pilihan): #match case ini cocok untuk kondisi yang tetap 
                case 1:
                    produk_ditemukan["Nama Barang"] = input('Masukkan Nama Barang baru: ').strip().title()
                case 2:
                    produk_ditemukan["Tipe"] = validasi_input_tipe('Masukkan Tipe baru (Smartphone/Tablet/Laptop): ').strip().title()
                case 3:
                    produk_ditemukan["Merek"] = validasi_input_alfabet('Masukkan Merek baru: ').strip().title()
                case 4:
                    stock_baru = validasi_input_angka('Masukkan Stock baru: ')
                    if stock_baru is not None:
                        produk_ditemukan["Stock"] = int(stock_baru)
                    else:
                        update_berhasil = False
                case 5:
                    harga_baru = validasi_input_angka('Masukkan Harga baru: ')
                    if harga_baru is not None:
                        produk_ditemukan["Harga"] = int(harga_baru)
                    else:
                        update_berhasil = False
                case _:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                    update_berhasil = False

            if update_berhasil:
                print("Data berhasil diperbarui!")

        if input_data("Apakah ingin mengubah produk lain? (ya/tidak): ").lower() != "ya":
            print("Keluar dari mode update data.")
            return

def kembali_data(barang):
    global data_hapus
    if not data_hapus:
        print("Tidak ada data yang dapat dikembalikan.")
        return

    while True:
        print("\nData yang dapat dikembalikan:")
        print(tabulate(data_hapus, headers='keys', tablefmt='simple_grid'))

        id_kembali = validasi_input_angka("Masukkan ID produk yang ingin dikembalikan (0 untuk keluar): ")
        if id_kembali is None:  # Handle pembatalan
            return
            
        id_kembali = int(id_kembali)  # Konversi ke integer untuk perbandingan

        for item in data_hapus:
            if item['ID'] == id_kembali:
              konfir = input_data("Apakah Anda yakin ingin mengembalikan data ini? (ya/tidak): ")
              if konfir.lower() == "ya":
                barang.append(item)
                data_hapus.remove(item)
                print(f"Data dengan ID {id_kembali} berhasil dikembalikan.")
                return
              else:
                print("Pengembalian dibatalkan.")
                return  # Kembali meminta input baru
        print("ID tidak ditemukan, silakan coba lagi.")

def pembelian(barang, akun_login):
    while True:  # Loop utama agar pengguna bisa memilih barang berulang kali
        print("\n=== PEMBELIAN PRODUK ===\n")

        # PILIH TIPE PRODUK
        while True:
            print("Pilih jenis produk:")
            tipe_produk = validasi_input_tipe("Masukkan jenis produk (laptop/smartphone/tablet): ").capitalize()
            tipe_tersedia = {item['Tipe'] for item in barang}

            if tipe_produk in tipe_tersedia:
                print(f"Jenis produk tersedia: {tipe_produk}")

                # Filter barang sesuai dengan tipe produk
                barang_filtered = [item for item in barang if item['Tipe'] == tipe_produk]

                # Tampilkan daftar barang dalam tabel
                print("\nDaftar Produk Tersedia:")
                print(tabulate(barang_filtered, headers="keys", tablefmt="simple_grid"))
                break  # Keluar dari loop jika tipe produk valid
            else:
                print("Jenis produk tidak tersedia. Silakan coba lagi.")

        # PILIH ID PRODUK
        while True:
            id_produk = validasi_input_angka("Masukkan ID produk yang ingin dibeli: ")

            # Cek apakah ID produk ada dalam daftar barang yang difilter
            produk_ditemukan = None  # Awalnya tidak ada produk yang ditemukan
            for item in barang_filtered:  # Loop melalui setiap item dalam daftar barang_filtered
              if item['ID'] == id_produk:  # Jika ID produk cocok dengan yang dicari
                  produk_ditemukan = item  # Simpan produk yang ditemukan
                  break  # Berhenti mencari setelah menemukan produk pertama yang cocok

            if produk_ditemukan: #kemudian jika produk_ditemukan maka akan print nama barang dan jumlah stokny
                print(f"Produk ditemukan: {produk_ditemukan['Nama Barang']} (Stok: {produk_ditemukan['Stock']})")
                break  # Keluar dari loop jika produk ditemukan
            else:
                print("ID produk tidak ditemukan. Silakan masukkan ID yang benar.")

        # INPUT JUMLAH PEMBELIAN
        while True:
            jumlah_beli = validasi_input_angka("Masukkan jumlah produk yang ingin dibeli: ")
            if jumlah_beli > produk_ditemukan['Stock']:
                print("Stok tidak mencukupi, silakan coba lagi.")
                continue
            break  # Keluar dari loop jika jumlah beli valid

        # HITUNG TOTAL HARGA
        total_harga = produk_ditemukan['Harga'] * jumlah_beli
        print(f"Total harga: Rp{total_harga:,}")

        # CEK SALDO
        if akun_login['saldo'] >= total_harga:
            akun_login['saldo'] -= total_harga  # Kurangi saldo user
            produk_ditemukan['Stock'] -= jumlah_beli  # Kurangi stok barang

            print(f"Pembelian berhasil! Sisa saldo Anda: Rp{akun_login['saldo']:,}")
            print(f"Stok tersisa: {produk_ditemukan['Stock']}")

            # Menyimpan transaksi
            akun_login['transaksi'].append({
                'Nama Barang': produk_ditemukan['Nama Barang'],
                'Jumlah': jumlah_beli,
                'Harga': produk_ditemukan['Harga'],
                'Total Harga': total_harga,
                'Tanggal': datetime.today().strftime("%Y-%m-%d %H:%M:%S")  # Tambahkan tanggal transaksi otomatis
            })

            print("Barang berhasil ditambahkan ke transaksi.")
        else:
            print(f"Saldo tidak mencukupi. Anda kekurangan Rp{total_harga - akun_login['saldo']:,}")

        print("\n")
        # Tanya apakah ingin menghapus lagi
        if input_data("Apakah Anda ingin menambah barang? (ya/tidak):  ") == "tidak":
            break  # Keluar dari loop utama jika pengguna memilih "tidak"

def cek_saldo(akun_login):
  print(f"Saldo Anda: Rp{akun_login['saldo']:,}") #menggunakan akun_login karena variabel akun_login ini menyimpan data aktivitas user

def tampilkan_transaksi(akun_login):
  # Tampilkan isi transaksi
  print("\nRiwayat Transaksi Anda:")
  print(tabulate(akun_login['transaksi'], headers="keys", tablefmt="simple_grid"))

def top_up(akun_login):
  while True:
    tambah_saldo = validasi_input_angka("Masukkan jumlah saldo yang ingin ditambahkan: ")
    if tambah_saldo > 0:
        akun_login['saldo'] += tambah_saldo
        print(f"Top up berhasil! Saldo sekarang: Rp{akun_login['saldo']:,}")
    else:
        print("Jumlah top up harus lebih dari 0!")
    return

def main():
  global akun_login
  while True:
    print("\nMenu:")
    print("1. Login")
    print("2. Keluar")
    pilihan = input("Pilih menu (1/2): ")
    match int(pilihan):

      case 1 :
        akun_login = login() #data tersimpan dalam variabel sementara
        #JIKA YANG LOGIN ADALAH ADMIN
        while True:
          if akun_login in admin:
            print("Selamat datang, admin!")
            print("\n=== MENU UTAMA ===")
            print("1. Tampilkan Barang")
            print("2. Tambah Barang")
            print("3. Ubah Barang")
            print("4. Hapus Barang")
            print("5. Kembalikan Barang yang Dihapus")
            print("6. Keluar")
            pilihan = input("Pilih menu (1/2/3/4/5/6): ")
            match int(pilihan): #match case ini cocok untuk kondisi yang tetap
              case 1 :
                tampilkan_barang(barang)
              case 2 :
                menambahkan_data(barang)
              case 3 :
                mengubah_data(barang)
              case 4 :
                hapus_data(barang)
              case 5 :
                kembali_data(barang)
              case 6 :
                print("Terima kasih! Program selesai.")
                return
        #JIKA YANG LOGIN ADALAH USER
          elif akun_login in user:
            while True:
              print(f"SELAMAT DATANG DI TOKO GANTENG GANTENG SELULER, {akun_login['Nama']}")
              print("\nMenu:")
              print("1. Beli Barang")
              print("2. Cek Saldo")
              print("3. Riwayat Transaksi")
              print("4. Tambah Saldo")
              print("5. Keluar")
              pilihan = input("Pilih menu (1/2/3/4/5): ")
              match int(pilihan): #match case ini cocok untuk kondisi yang tetap
                case 1 :
                  pembelian(barang, akun_login)
                case 2 :
                  cek_saldo(akun_login)
                case 3 :
                  tampilkan_transaksi(akun_login)
                case 4 :
                  top_up(akun_login)
                case 5 :
                  print("Keluar")
                  return
          else:
              print("Login gagal! Akun tidak ditemukan.")
      case 2 :
        print("Keluar")
        return

main()