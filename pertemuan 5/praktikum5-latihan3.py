#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 3: Mencari Nilai Maksimum
#=============================================================

def cari_maks(data, index=0):

    # Base case
    if index == len(data) -1:
        return data[index]
    
    # Recursive call
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa:
        return data [index]
    else:
        return maks_sisa
    
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# TUJUAN PROGRAM
# Fungsi cari_maks() digunakan untuk mencari nilai maksimum dalam list menggunakan rekursi

# ALUR PROGRAM
# 1. Pemanggilan awal: cari_maks([3,7,2,9,5], 0)
# artinya mulai dari index 0
# 2. Fase turun (Recursive call / Descending)
# fungsi terus memanggil dirinya dengan index + 1: cari_maks(data, 0)
                                                # -> cari_maks(data, 1)
                                                # -> cari_maks(data, 2)
                                                # -> cari_maks(data, 3)
                                                # -> cari_maks(data, 4)
# saat sampai di index terakhir (4): if index == len(data) - 1:
                                    # return data [indeex]
# karena: len(data) -1 = 4
# maka: return 5
# 3. Base case
# base case terjadi saat: - Sudah sampai elemen terakhir list
                        # - Tidak bisa membandingkan lagi ke depan
# kenapa harus ada base case? kalau tidak: - Rekursi akan terus berjalan
                                         # - Terjadi error (stack overflow)
# 4. Fase naik (Unwiding / Backtracking)
# sekarang mulai dibandingkan satu per satu dari belakang
# dari index 3: maks_sisa = 5
              # data[3] = 9
              # 9 > 5 -> return 9
# dari index 2: maks_sisa = 9 
              # data[2] = 2
              # 2 < 9 -> return 9
# dari index 1: maks_sisa = 9 
              # data[1] = 7
              # 7 < 9 -> return 9
# dari index 0: maks_sisa = 9 
              # data[0] = 3
              # 3 < 9 -> return 9 
# akhirnya: return 9