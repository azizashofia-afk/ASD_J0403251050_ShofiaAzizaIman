#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 4: membuat traversal inorder
#=============================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat fungsi inorder: left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

print("Hasil traversal inorder: ")

#PEMBAHASAN
#Kode tersebut digunakan untuk melakukan **traversal inorder** pada binary tree. 
# Pertama dibuat class `Node` untuk menyimpan data serta child kiri dan kanan.
#  Kemudian dibuat fungsi `inorder(node)` yang bekerja dengan urutan **kiri → root → kanan**, 
# artinya program akan mengunjungi subtree kiri terlebih dahulu, lalu node saat ini, 
# dan terakhir subtree kanan. Setelah itu dibuat tree dengan root `"A"`, child `"B"` 
# dan `"C"`, serta `"D"` dan `"E"` sebagai anak dari `"B"`. Saat fungsi `inorder(root)` 
# dijalankan, data akan ditampilkan dengan urutan **D B E A C**.
