#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Contoh Backtracking: Kombinasi Biner dengan batas '1' (Pruning)
#=============================================================

# Fungsi rekursif untuk menghasilkan kombinasi biner sepanjang n
# dengan batas maksimal jumlah angka '1'
def biner_batas(n, batas, hasil="", jumlah_1=0):

    # Pruning (pemotongan cabang)
    # Jika jumlah angka '1' sudah melebihi batas, maka hentikan proses pada cabang ini
    if jumlah_1 > batas:
        return
    
    # Base case: jika panjang string sudah sama dengan n artinya kombinasi sudah lengkap
    if len(hasil) == n:
        print(hasil)    # Cetak kombinasi yang valid
        return
    
    # Recursive case

    # Pilihan 1: Tambah '0'
    # jumlah_1 tidak berubah karena tidak menambah angka 1
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilihan 2: Tambah '1'
    # jumlah_1 bertambah 1 karena menambahkan angka 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

print("====Kombinasi biner dengan batas 1=====")
print(biner_batas(4, 2))