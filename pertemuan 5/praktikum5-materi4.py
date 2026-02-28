#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Contoh Backtracking: Kombinasi Biner (n)
#=============================================================

# Fungsi rekursif untuk menghasilkan kombinasi biner sepanjang n
def biner(n, hasil=""):

    # Base case: jika panjang string 'hasil' sudah sama dengan n
    # artinya kombinasi sudah lengkap dan siap dicetak
    if len(hasil) == n:
        print(hasil)    # Cetak kombinasi biner
        return          # Hentikan rekursi pada cabang ini
    
    # Recursive case (Choose + Explore)
    # Tambahkan karakter '0' ke string hasil
    # lalu panggil kembali fungsi biner
    biner(n, hasil + "0")

    # Tambahkan karakter '1' ke string hasil
    # lalu panggil kembali fungsi biner
    biner(n, hasil + "1")

print("=====Program Kombinasi Biner=====")
print(biner(3))
