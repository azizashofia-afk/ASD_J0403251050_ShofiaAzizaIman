#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 6: struktur organisasi perusahaan
#=============================================================

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None
        self.right = None

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#membuat tree struktur organisasi
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff1")
root.left.right = Node("Staff2")

root.right.right = Node("Staff3")

print("Struktur Organisasi (Preorder): ")
preorder(root)

#PEMBAHASAN
#Kode tersebut digunakan untuk membuat **struktur organisasi perusahaan menggunakan 
# binary tree**. Class `Node` dipakai untuk menyimpan data jabatan serta child kiri dan kanan. 
# Kemudian dibuat fungsi `preorder` yang menampilkan node dengan urutan **root → kiri → 
# kanan**. Setelah itu dibentuk tree dengan root `"Direktur"`, lalu level pertama berisi
#  `"Manajer A"` di kiri dan `"Manajer B"` di kanan. Pada level kedua, `"Manajer A"` 
# memiliki `"Staff1"` dan `"Staff2"`, sedangkan `"Manajer B"` memiliki `"Staff3"`. 
# Saat traversal preorder dijalankan, struktur organisasi akan ditampilkan mulai dari 
# atas (Direktur) lalu turun ke cabang kiri dan kanan secara berurutan.
