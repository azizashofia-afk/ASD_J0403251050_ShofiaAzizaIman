#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Materi Rekursif: Call Stack
# Tracing bilangan (masuk-keluar)
# input 3
# 3-2-1 | 1-2-3
# Keluar
#=============================================================

def hitung(n):

    #base case
    if n == 0:
        print("selesai")
        return

    print("Masuk:", n)     #fase stacking
    hitung(n-1)            #recursive case
    print("Keluar", n)     #fase unwiding

print("=====Program Tracing=====")
hitung(3)