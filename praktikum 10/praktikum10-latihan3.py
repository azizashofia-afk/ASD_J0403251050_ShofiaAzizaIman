#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 5: Rotasi Kiri pada BST yang tidak seimbang
#=============================================================

# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Fungi preorder untuk melihat isi tree
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

# Fungsi rotasi kiri
def rotate_left(x):
    # x adalah root lama
    y = x.right  # y adalah child kanan x
    T2 = y.left  # subtree kiri milik y disimpan sementara

    # proses rotasi
    y.left = x   # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2

    # y menjadi root baru
    return y

#--------------------------
# Program Utama
#--------------------------

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)

"""
Tree awal berbentuk miring ke kanan akibat data yang dimasukkan berurutan naik,
yaitu 10, 20, dan 30. Kondisi ini menyebabkan performa BST menurun karena
menyerupai linked list. Untuk memperbaikinya, digunakan fungsi rotate_left
yang bekerja dengan menjadikan child kanan sebagai root baru, kemudian root lama
menjadi child kiri dari node tersebut, serta subtree kiri dari child kanan
dipindahkan sebagai child kanan dari root lama. Setelah rotasi dilakukan,
struktur tree menjadi lebih seimbang dengan 20 sebagai root, 10 sebagai anak kiri,
dan 30 sebagai anak kanan. Program juga menampilkan hasil preorder dan struktur
tree sebelum dan sesudah rotasi untuk memperlihatkan perubahan yang terjadi.
"""