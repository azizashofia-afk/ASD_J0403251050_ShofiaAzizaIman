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