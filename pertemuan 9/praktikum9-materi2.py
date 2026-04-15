#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 2: membuat binary tree sederhana
#=============================================================

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None
        self.right = None

#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

#menampilkan isi node
print("Data pada root: ", root.data)
print("Child kiri root: ", root.left.data)
print("Child kanan root: ", root.right.data)
print("Child kiri dari B: ", root.left.left.data)
print("Child kanan dari B: ", root.left.right.data)
print("Child kiri dari C: ", root.right.left.data)
print("Child kanan dari C: ", root.right.right.data)

#PEMBAHASAN
#Kode tersebut digunakan untuk membuat binary tree sederhana dengan beberapa
#level. Pertama dibuat class Node yang menyimpan data serta memiliki child kiri dan
#kanan. Kemudian dibuat root dengan nilai "A", lalu ditambahkan hild level 1 yaitu
#"B" di kiri dan "C" di kanan. Setelah itu ditambahkan lagi child level 2, yaitu "D"
#dan "E" sebagai anak dari "B", serta "F" dan "G" sebagai anak dari "C".
#Terakhir, program menampilkan seluruh isi nose untuk memastikan bahwa struktur
#tree sudah terbentuk dengan benar sesuai hubungan parent dan child-nya.