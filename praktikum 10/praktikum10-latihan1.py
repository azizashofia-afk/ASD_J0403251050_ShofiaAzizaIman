#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 1: BST
#=============================================================

# Class Node untuk membuat node pada Binary Search Tree
class Node:
    def __init__(self, data):
        self.data = data   # menyimpan nilai data
        self.right = None  # pointer ke anak kanan
        self.left = None   # pointer ke anak kiri

# Fungsi untuk insert data ke dalam BST
def insert(root, data):
    if root is None:       # jika tree kosong
        return Node(data)  # buat node baru jadi root
    
    if data < root.data:   # jika data lebih kecil -> ke kiri
        root.left = insert(root.left, data)
    elif data > root.data: # jika data lebih besar -> ke kanan
        root.right = insert(root.right, data)
    # jika sama (duplikat), tidak dimasukkan (di-skip)

    return root            # kembalikan root

# Mengisi data BST
root = None
data_list = [50, 30, 70, 20, 40, 50, 80]

for data in data_list:
    root = insert(root, data) # insert satu per satu

print("BST berhasil dibuat")

"""
Binary Search Tree (BST), yaitu tree yang memiliki aturan setiap node di sebelah kiri 
lebih kecil dari root dan di sebelah kanan lebih besar dari root. Program dimulai 
dengan membuat class Node sebagai elemen dasar yang menyimpan data serta pointer ke anak
kiri dan kanan. Kemudian dibuat fungsi insert yang bekerja secara rekursif untuk menempatkan
data sesuai aturan BST. Jika root kosong maka dibuat node baru, jika data lebih kecil
maka dimasukkan ke kiri, dan jika lebih besar ke kanan. Data yang duplikat tidak
dimasukkan ke dalam tree. Setelah itu, beberapa data dimasukkan ke dalam BST
sehingga terbentuk struktur tree yang sesuai.
"""

#=============================================================
# Latihan 2: Traversal Inorder
#=============================================================

# Fungsi inorder (Left - Root - Right)
def inorder(root):
    if root is not None:
        inorder(root.left)          # kunjungi kiri
        print(root.data, end=" ")   # tampilkan root
        inorder(root.right)         # kunjungi kanan

print("hasil Inorder: ")
inorder(root)

"""
Traversal inorder adalah proses mengunjungi node dengan urutan kiri, root, kemudian 
kanan (Left-Root-Right). Karena menggunakan BST, hasil dari traversal inorder akan 
menghasilkan data yang sudah terurut dari nilai terkecil ke terbesar. Fungsi inorder 
dibuat secara rekursif dengan mengunjungi subtree kiri terlebih dahulu, kemudian 
mencetak nilai node, lalu dilanjutkan ke subtree kanan.
"""

#=============================================================
# Latihan 3: Search di BST
#=============================================================

# Fungsi mencari data dalam BST
def search(root, key):
    if root is None:        # jika node kosong -> tidak ditemukan
        return False
    
    if root.data == key:    # jika ketemu
        return True
    elif key < root.data:   # kalau lebih kecil -> cari ke kiri
        return search(root.left, key)
    else:                   # kalau lebih besar -> ke kanan
        return search(root.right, key)
    
# Uji pencarian
key = 140

if search(root, key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")

"""
Proses pencarian memanfaatkan sifat BST sehingga lebih efisien dibandingkan pencarian 
biasa. Jika nilai yang dicari sama dengan node saat ini maka data ditemukan. Jika
nilai lebih kecil maka pencarian dilanjutkan ke subtree kiri, dan jika lebih
besar ke subtree kanan. Jika node bernilai None, berarti data tidak ditemukan.
Pada bagian akhir dilakukan pengujian dengan mencari nilai tertentu untuk
mengetahui apakah data tersebut ada dalam BST atau tidak.
"""