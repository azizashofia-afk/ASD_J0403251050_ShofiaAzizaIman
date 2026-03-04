#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 1 Memahami Kode program (Insertion sort)
#=============================================================

def insertion_sort(data):
    for i in range(1, len(data)):

        #menyimpan nilai yang akan disisipkan
        key = data[i]

        # j menunjuk ke elemen sebelum i
        j = i - 1

        #selama belum melewati awal list dan elemen di kiri lebih besar dari key
        while j >= 0 and data[j] > key:

            #geser elemen yg lebih besar satu langkah ke kanan
            data[j +1] = data[j]

            #mundur ke indeks sebelumnya utk diperbandingkan
            j -= 1
        
        #masukkan key ke tempat yg sudah kosong
        data[j + 1] = key
    
    #mengembalikan list yg sudah terurut
    return data

# 1. Mengapa perulangan dimulai dari indeks 1?
# karena ketika key ada di indeks 0 dia tidak akan terjadi apa apa karena belum bisa dibandingkan elemennya karna baru 1 elemen

# 2. Apa fungsi variabel key?
# fungsi key yaitu menyimpan nilai yang sedang ingin dimasukkan ke posisi yang benar
# menyimpan nilai sementara yang sedang diproses supaya nilainya tidak hilang sat elemen lain digeser

# 3. Mengapa menggunakan while, bukan for?
# Karena kita akan membandingkan semua elemen dan kita tidak tahu pasti berapa kali pergeseran akan terjadi. Pada while j >= 0 and data[j] > key
# kode akan menggeser ke kanan selama masih ada elemen di kiri dan nilainya lebih besar dari key.

# 4. Operasi apa yang terjadi di dalam while?
# Operasi perbandingan, yaitu membandingkan elemen di kiri dengan key (data[j] > key).
# Operasi pergeseran, menggeser elemen yang lebih besar ke kanan (data[j+1] = data[j]).
# Operasi pengurangan indeks, pindah satu langkah ke kiri untuk cek elemen berikutnya


