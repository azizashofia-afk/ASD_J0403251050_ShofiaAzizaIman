#==========================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: TPL B1
#==========================================
# Latihan 3 Tracing insertion sort
#==========================================

# Buat program dengan menggunakan algoritma insertion sort
# Tracing dengan data = [5, 2, 4, 6, 1, 3]


def insertion_sort(data):
    for i in range(1, len(data)):
        
        #menyimpan elemen yg akan disisipkan
        key = data[i]

        # j menunjuk ke elemen sebelum i
        j = i - 1 
        
        #selama belum melewati awal list dan elemen di kiri lebih besar dari key
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        
        data[j+1] = key
    return data

data = [5, 2, 4, 6, 1, 3]
print("Data awal: ",data)
print("Hasil sorting: ",insertion_sort(data))


# 1. Tuliskan isi list setelah iterasi i = 1
# [2, 5, 4, 6, 1, 3]

# 2. Tuliskan isi list setelah iterasi i = 3
# [2, 4, 5, 6, 1, 3]

# 3. Berapa kali pergeseran terjadi pada iterasi i = 4
# Terjadi 4 kali pergeseran ke kiri, ketika j = -1 pergeseran akan berhenti


