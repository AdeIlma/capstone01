from tabulate import tabulate

data = [
    {'Kode': 1, 'Nama': 'John', 'Usia': 25, 'Kota': 'Jakarta'},
    {'Kode': 2, 'Nama': 'Diana', 'Usia': 30, 'Kota': 'Surabaya'},
    {'Kode': 3, 'Nama': 'Bob', 'Usia': 22, 'Kota': 'Bandung'}
]

# Fungsi untuk validasi nama (hanya huruf)
def validasi_alpabet(alpabet):
    return alpabet.isalpha()

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
        if validasi_angka(kode) and validasi_alpabet(nama) and validasi_angka(usia) and validasi_alpabet(kota):
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
            kode_update = input('Masukkan Kode data yang ingin di update (0 untuk keluar): ')
            validasi_angka(kode_update)
            kode_update = int(kode_update)

            if kode_update == 0:
                print("Update dibatalkan.")
                break

            # mencari data yang ingin di update
            for item in data:
              if item['Kode'] == kode_update:
                while True:
                    update = input('Masukkan data yang ingin di update (Kode/Nama/Usia/Kota): ').strip().lower()
                    if update == 'nama':
                        item["Nama"] = input('Masukkan Nama baru: ').strip().title()
                        validasi_alpabet(item["Nama"])
                    elif update == 'usia':
                        item["Usia"] = input('Masukkan Usia baru: ')
                        validasi_angka(item["Usia"])
                    elif update == 'kota':
                        item["Kota"] = input('Masukkan Kota baru: ').strip().title()
                        validasi_alpabet(item["Kota"])
                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")
                        continue

                    print(f"\nData Berhasil Diupdate!")
                    return

            # Jika kode tidak ditemukan
            else:
              print("Data tidak ditemukan. Silakan coba lagi.")

        except ValueError:
            print("Kode harus berupa angka.")
            return

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
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Baca Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Keluar")

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