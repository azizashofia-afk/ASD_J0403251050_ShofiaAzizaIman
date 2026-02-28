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