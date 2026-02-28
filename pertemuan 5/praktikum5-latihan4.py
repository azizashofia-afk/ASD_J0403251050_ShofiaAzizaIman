#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 4: Kombinasi Huruf
#=============================================================

def kombinasi(n, hasil=""):

    if len(hasil) == n:
        print(hasil)
        return
    
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi (2)

# BAGAIMANA JUMLAH KOMBINASI DIHASILKAN?
# Fungsi ini menghasilkan semua kombinasi huruf "A" dan "B" sepanjang n menggunakan rekursi
# setiap posisi punya 2 pilihan: - Tambah "A"
                               # - Tambah "B"
# jadi setiap level rekursi bercabang 2
# struktur pohon rekursi (n = 2)
# level 0: ""
# level 1: "A"
         # "B"
# level 2: "AA"
         # "AB"
         # "BA"
         # "BB"
# terlihat bahwa: - level 1 -> 2 kemungkinan
                # - level 2 -> 4 kemungkinan
# karena setiap posisi punya 2 pilihan dan ada n posisi
# maka total kombinasi adalah 2^n
# jadi untuk kombinasi(2)
# jumlah kombinasi yang dihasilkan: 2^2 =4

# KENAPA BISA 2^n?
# karena setiap pemanggilan rekursi: - Membuat 2 cabang
                                   # - Kedalaman rekursi = n
# secara struktur: - Pohon biner penuh
                 # - Jumlah daun = 2^n
                 # - Setiap daun = 1 kombinasi valid       
