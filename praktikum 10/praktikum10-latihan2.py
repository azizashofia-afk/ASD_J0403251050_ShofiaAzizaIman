#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 4: Membuat BST yang tidak seimbang
#=============================================================

# Class node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data  # nilai pada node
        self.left = None  # child kiri
        self.right = None # child kanan
    
# Fungsi insert untuk BST
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)
    
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

# Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

#--------------------
# Program Utama
#--------------------
root = None

#Data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root)

"""
Ketidakseimbangan terjadi karena data dimasukkan secara berurutan naik,
yaitu 10, 20, dan 30. Dalam BST, jika data yang dimasukkan selalu lebih
besar dari node sebelumnya, maka node akan terus ditempatkan di sisi kanan,
sehingga membentuk struktur seperti linked list (miring ke kanan).
Program menggunakan class Node untuk merepresentasikan node dan fungsi insert
untuk memasukkan data sesuai aturan BST. Selain itu, digunakan fungsi preorder
untuk menampilkan isi tree dan fungsi tampil_struktur untuk melihat bentuk
struktur tree. Hasil akhirnya menunjukkan bahwa tree menjadi tidak seimbang
karena semua node berada di satu sisi, yang dapat mempengaruhi efisiensi operasi.
"""