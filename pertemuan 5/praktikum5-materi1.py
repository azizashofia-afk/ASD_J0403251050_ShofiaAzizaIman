#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Materi Rekursif: Faktorial
# recursive case => 3! = 3 x 2 x 1
# base case => 0 berhenti
#=============================================================

def faktorial(n):
    if n == 0:
        return 1
    #recursive case
    return n*faktorial(n-1)     #n-1*n-2*n-3.........n-?

print("=====Prrogram Faktorial=====")
print("Hasil Faktorial : ", faktorial(3))