#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 1: Rekursi Pangkat
#=============================================================

def pangkat(a, n):

    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    return a * pangkat(a, n-1)

print(pangkat(2, 4))

# TUJUAN PROGRAM
# Fungsi pangkat(a, n) digunakan untuk menghitung nilai a^n (a pangkat n) menggunakan rekursi
# contoh: pangkat(2, 4) berarti menghitung 2^4 = 16

# ALUR PROGRAM
# Ketika dipanggil: pangkat(2, 4)
# maka yang terjadi adalah: pangkat(2, 4)
                        # = 2 * pangkat(2, 3)
                        # = 2 * (2 *pangkat(2, 2))
                        # = 2 * (2 * (2 * pangkat(2, 1)))
                        # = 2 * (2 * ( 2 * ( 2 * pangkat(2, 0))))
# saat sampai di: pangkat(2, 0)
# karena n == 0, maka: return 1
# lalu proses mundur (backtracking):  = 2 * 1 = 2
                                    # = 2 * 2 = 4
                                    # = 2 * 4 = 8
                                    # = 2 * 8 = 16
# hasil akhirnya: 16

# BASE CASE
# Base case adalah kondisi berhenti rekursi
# Kenapa harus return 1? karena dalam matematika: a^0 =1  
# Kalau tidak ada base case: - Fungsi akan memanggil dirinya terus
                           # - Terjadi infinite recursion
                           # - Program eror (stack overflow)

# RECURSIVE CALL
# Bagian ini membuat fungsi memanggil dirinya sendiri dengan: - Nilai n dikurangi 1 setiap kalinya
                                                            # - Sampai akhirnya mencapai n == 0
# Secara konsep: a^n = a x a^n-1          