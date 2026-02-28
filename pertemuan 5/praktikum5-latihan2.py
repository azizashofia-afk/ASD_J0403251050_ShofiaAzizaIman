#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 1: Tracing Rekursi
#=============================================================

def countdown(n):

    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)