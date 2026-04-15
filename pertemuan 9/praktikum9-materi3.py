#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 3 = Membuat traversal preorder
#=============================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

print("Hasil traversal preorder: ")
preorder(root)

#PEMBAHASAN
#Kode tersebut digunakan untuk melakukan traversal preorder pada binary tree. 
#Pertama dibuat class `Node` untuk menyimpan data serta child kiri dan kanan. 
#Lalu dibuat fungsi `preorder(node)` yang bekerja dengan cara mengunjungi node 
#saat ini terlebih dahulu (print data), kemudian ke subtree kiri, lalu ke subtree 
#kanan. Setelah itu dibuat tree dengan root `"A"`, child `"B"` dan `"C"`,
#serta `"D"` dan `"E"` sebagai anak dari `"B"`. Saat fungsi `preorder(root)` 
#dijalankan, data akan ditampilkan dengan urutan **root → kiri → kanan**, 
#yaitu: **A B D E C**.
