#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 6: Rotasi Kanan pada BST yang tidak seimbang
#=============================================================

# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Fungsi rotasi kanan
def rotate_right(x):
    # x adalah root lama
    y = x.left   # y adalah child kiri x
    T2 = y.right # subtree kanan milik y disimpan sementara

    # proses rotasi
    y.right = x  # x jadi child kanan dari y
    x.left = T2  # child kiri x diganti dengan T2

    # y jadi root baru
    return y

#--------------------------
# Program Utama
#--------------------------

# Membuat tree tidak seimbang:
# 30 -> 20 -> 10
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# lakukan rotasi kanan
root = rotate_right(root)

print("\nPreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)

"""
Tree awal terbentuk miring ke kiri akibat data yang dimasukkan berurutan turun,
yaitu 30, 20, dan 10, sehingga struktur menyerupai linked list dan menyebabkan
penurunan efisiensi operasi. Untuk mengatasinya, digunakan fungsi rotate_right
yang bekerja dengan menjadikan child kiri sebagai root baru, kemudian root lama
menjadi child kanan dari node tersebut, serta subtree kanan dari child kiri
dipindahkan menjadi child kiri dari root lama. Setelah proses rotasi dilakukan,
struktur tree menjadi lebih seimbang dengan 20 sebagai root, 10 sebagai anak kiri,
dan 30 sebagai anak kanan. Program juga menampilkan traversal preorder dan struktur
tree sebelum dan sesudah rotasi untuk memperlihatkan perubahan yang terjadi.
"""