from tabulate import tabulate

data = [
    {'Kode': 1, 'Nama': 'John', 'Usia': 25, 'Kota': 'Jakarta'},
    {'Kode': 2, 'Nama': 'Diana', 'Usia': 30, 'Kota': 'Surabaya'},
    {'Kode': 3, 'Nama': 'Bob', 'Usia': 22, 'Kota': 'Bandung'}
]

# Fungsi untuk validasi nama (hanya huruf)
def validasi_alfabet(alfabet):
    return alfabet.isalpha()

# Fungsi untuk validasi usia (harus angka)
def validasi_angka(angka):
    return angka.isdigit()

# Fungsi untuk menambah data baru
def create_data():
  while True:
        kode = input('Masukkan Kode: ')
        nama = input('Masukkan Nama: ')
        usia = input('Masukkan Usia: ')
        kota = input('Masukkan Asal: ')

        # Cek apakah input valid
        if validasi_angka(kode) and validasi_alfabet(nama) and validasi_angka(usia) and validasi_alfabet(kota):
            data.append({'Kode': int(kode), 'Nama': nama, 'Usia': int(usia), 'Kota': kota})  # Tambahkan ke list
            print(f"\nData Berhasil Ditambahkan!")
            print(f"Kode: {kode}, Nama: {nama}, Usia: {usia}, Kota: {kota}")
            break
        else:
            print("\nData Gagal Ditambahkan! Pastikan input benar (Nama & Kota hanya huruf, Usia hanya angka).")

# untuk menampilkan data
def read_data():
  print(tabulate(data, headers = 'keys', tablefmt='grid'))

# untuk melakukan update data 
def update_data():
    while True:
        try:
            # Meminta input kode yang ingin diupdate
            kode_update = input('Masukkan Kode data yang ingin di update (0 untuk keluar): ')
            validasi_angka(kode_update)
            kode_update = int(kode_update)

            if kode_update == 0:
                print("Update dibatalkan.")
                break  # Keluar dari loop utama jika user memilih keluar

            # Periksa apakah kode ada dalam data
            for item in data:
                if item['Kode'] == kode_update:
                    while True:  # Loop untuk update beberapa kali sebelum kembali ke input kode baru
                        update = input('Masukkan data yang ingin di update (Kode/Nama/Usia/Kota): ').strip().lower()
                        if update == 'nama':
                            item["Nama"] = input('Masukkan Nama baru: ').strip().title()
                            validasi_alfabet(item["Nama"])  
                        elif update == 'usia':
                            item["Usia"] = input('Masukkan Usia baru: ')
                            validasi_angka(item["Usia"])
                        elif update == 'kota':
                            item["Kota"] = input('Masukkan Kota baru: ').strip().title()
                            validasi_alfabet(item["Kota"])
                        else:
                            print("Pilihan tidak valid. Silakan coba lagi.")
                            continue  # Kembali ke input update jika salah
                        
                        # Tanya apakah ingin update lagi
                        update_lagi = input("Apakah ingin update data lain? (ya/tidak): ").strip().lower()
                        if update_lagi == 'ya':
                            break  # Kembali ke input kode_update
                        else:
                            print("\nData Berhasil Diupdate!")
                            return  # Keluar dari fungsi update_data

            else:
                print("Data tidak ditemukan. Silakan coba lagi.")
                continue  # Kembali ke input kode jika kode tidak ditemukan

        except ValueError:
            print("Kode harus berupa angka.")
            continue  # Kembali ke input kode jika input tidak valid

#untuk menghapus data yang diinginkan
def delete_data():
  while True:
    try:
      kode_delete = input('Masukkan Kode data yang ingin di delete (0 untuk keluar): ')
      validasi_angka(kode_delete)
      kode_delete = int(kode_delete)

      if kode_delete == 0:
        print("Delete dibatalkan.")
        break

      for item in data:
        if item['Kode'] == kode_delete:
          data.remove(item)
          print(f"\nData Berhasil Dihapus!")

          for i, item in enumerate(data, start=1):  #untuk data yang dihapus agar dimulai dari 1
            item["Kode"] = i
  
          return

      else:
        print("Data tidak ditemukan. Silakan coba lagi.")

    except ValueError:
      print("Kode harus berupa angka.")
      return

def main():
  while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Baca Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == '1':
      create_data()
    elif pilihan == '2':
      read_data()
    elif pilihan == '3':
      update_data()
    elif pilihan == '4':
      delete_data()
    elif pilihan == '5':
      print("Terima kasih! Program selesai.")
      break

main()