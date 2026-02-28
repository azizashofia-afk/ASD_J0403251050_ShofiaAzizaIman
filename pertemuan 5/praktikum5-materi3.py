#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Materi Rekursif: Menjumlahkan Elemen List
#=============================================================

def jumlah_list(data, index=0):
    #base case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    
    #recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index+1)

print("=====Program Jumlah Data List=====")
print(jumlah_list([2,4,5]))