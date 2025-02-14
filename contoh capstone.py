from tabulate import tabulate

# simpan data capstone
data = [{'nama': 'aldi', 'umur': 20, 'asal': 'kaltim'},
        {'nama': 'stef', 'umur': 30, 'asal': 'surabaya'},
        {'nama': 'stef', 'umur': 30, 'asal': 'surabaya'}]

# agar lebih mudah dalam menggunakan tabulate
def read_data(data):
    print( tabulate(data, headers='keys', tablefmt='fancy_grid'))

# function validasi input
def validasi_input_alfabet(prompt):
    while True:
        inputan = input(prompt)
        if inputan.isalpha():
            return inputan
        else:
            print('inputan harus huruf')

def validasi_input_angka(prompt):
    while True:
        inputan = input(prompt)
        if inputan.isdigit():
            return int(inputan)
        else:
            print('inputan harus angka')

# create
def create_data(data):
    nama = validasi_input_alfabet('masukan nama : ')
    umur = validasi_input_angka(input('masukan umur : '))
    asal = validasi_input_alfabet('masukan asal : ')
    data.append({'nama': nama, 'umur': umur, 'asal': asal})
    return read_data(data)


# function utama
def main():
    while True:
        print('1. create data')
        print('2. read data')
        print('3. exit')
        pilihan = validasi_input_angka('masukan pilihan : ')
        if pilihan == 1:
            create_data(data) # jalankan function create data
        elif pilihan == 2:
            read_data(data)
        elif pilihan == 3:
            break

main() # menjalankan function main
# dilanjutkan sampai update dan delete serta fitur tambahan