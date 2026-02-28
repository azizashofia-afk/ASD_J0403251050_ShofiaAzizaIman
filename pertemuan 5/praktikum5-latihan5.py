#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Studi kasus: Generator PIN
#=============================================================

def buat_pin(panjang, hasil=""):

    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    for angka in ["0",  "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)

# BAGAIMANA CARA MENCEGAH ANGKA YANG SAMA MUNCUL BERULANG?
# saat ini program boleh mengulang angka, misalnya: - 000
                                                  # - 111
                                                  # - 202
# kalau ingin tanpa pengulangan angka, maka kita harus: - Tidak memilih angka yang sudah ada di hasil
                                                      # - Menggunakan konsep permutasi
# cara 1 - Cek Manual
# tambahkan pengecekan sebelum rekursi: if angka not in hasil:
# sekarang hasilnya hanya: 012
                         # 021
                         # 102
                         # 120
                         # 201
                         # 210
# jumlahnya: 3! = 6
# kenapa sekarang jadi 3!?
# karena: - Kita memilih tanpa pengulangan
        # - Ini jadi permutasi
# rumusnya: n!
# untuk 3 angka unik: 3 x 2 x 1 = 6 
# cara 2 - Gunakan List dan Hapus Elemen
# versi lebih rapih secara algoritma backtracking
# tambahkan: for i in range(len(angka_tersedia)):
              # angka = angka_tersedia[i]
              # sisa = angka_tersedia[:i] + angka_tersedia[i+1:]
              # buat_pin(sisa, hasil + angka)   
# ini konsep klasik permutation backtracking