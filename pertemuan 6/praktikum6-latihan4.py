#=================================================
#Nama   : Shofia Aziza Iman
#NIM    : J0403251050
#Kelas  : B1
#=================================================
# Latihan 4 Memahami kode program (Merge Sort)
# ================================================

def merge_sort(data):
#fungsi merge sort untuk membagi data menjadi 2 
    if len(data) <= 1: #Error Handling
        return data

    mid = len(data) // 2 #Membagi data menjadi 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left) #data bagian sebelah kiri
    right_sorted = merge_sort(right) #data bagian sebelah kanan

    return merge(left_sorted, right_sorted)

def merge(left,right): #fungsi merge untuk menggabungkan 2 list yang sudah terurut menjadi tetap terurut

    result = []
    i = 0
    j = 0

    #Membandingkan elemen di kiri dan di kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+=1
    #Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 1. Apa yang dimaksud dengan base case?
# Base Case adalah kondisi dalam fungsi rekursif yang menandai titik pemberhentian perulangan,
# tanpa base case maka fungsi akan loop terus menerus.

# 2. Mengapa fungsi memanggil dirinya sendiri?
# Agar bisa memecahkan masalah kompleks menjadi sub-bagian masalah yang lebih kecil.

# 3. Apa tujuan fungsi merge()?
# Fungsi merge dipanggil untuk menggabungkan dua bagian atau list terpisah yang sebelumnya
# sudah diurutkan agar menjadi satu list yang tetap terurut.
# Namun, kode ini akan error karena dalam kode yang diberikan di soal, def merge atau
# fungsi merge tidak ada atau tidak dituliskan.