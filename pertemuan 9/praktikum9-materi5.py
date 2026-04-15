#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 5: membuat traversal postorder
#=============================================================

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None
        self.right = None

#membuat traversal postorder: left -> right -> root
def postorder(node):
    if node is None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

print("Hasil traversal postorder: ")
postorder(root)

#PEMBAHASAN
#Kode tersebut digunakan untuk melakukan **traversal postorder** pada binary tree. 
# Pertama dibuat class `Node` untuk menyimpan data serta child kiri dan kanan. 
# Kemudian dibuat fungsi `postorder(node)` yang seharusnya berjalan dengan urutan 
# **kiri → kanan → root**, yaitu mengunjungi subtree kiri terlebih dahulu, lalu 
# subtree kanan, dan terakhir node saat ini. Setelah itu dibuat tree dengan root `"A"`,
#  child `"B"` dan `"C"`, serta `"D"` dan `"E"` sebagai anak dari `"B"`. Namun 
# pada kode ini terdapat kesalahan logika, karena kondisi `if node is None` membuat
#  fungsi tidak berjalan dengan benar (harusnya `if node is not None`). Seharusnya 
# hasil traversal postorder yang benar adalah **D E B C A**.
