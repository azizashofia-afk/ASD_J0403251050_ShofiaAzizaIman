#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 1 = Membuat Node
#=============================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat root
root = Node("A")

#menampilkan isi node
print("Data pada root", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

#PEMBAHASAN#
#Kode tersebut digunakan untuk membuat satu node dasar pada 
#struktur binary tree. Di dalam class Node, terdapat atribut data 
#untuk menyimpan nilai, serta left dan right yang digunakan untuk
#menunjuk ke anak kiri dan kanan (yang awalnya bernilai None karena belum diisi)
#Kemudian dibuat satu node sebagai root dengan nilai "A", sehingga saat
#ditampilkan, data pada root berisi "A", sedangkan child kiri dan kanan
#masih kosong karena belum ditambahkan node lain.