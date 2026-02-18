#========================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
#========================================================
# Praktikum 4 : Implementasi Dasar: Node pada Linked List
#========================================================

# Membuat clas  Node (merupakan unit dasar )

class Node:
    def __init__(self,data): #tandanya dia adalah konstruktor
        self.data = data #menyimpan nilai data
        self.next = None #pointer ke note berikutnya


# 1) Membuat node satu persatu
nodeA = Node("A") #memanggil konstruktor
nodeB = Node("B")
nodeC = Node("C")

# 2) menghubungkan node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) menentukan node pertama (head)
head = nodeA

# 4) traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

#====================================================
#Implementasi Dasar: Linked List + insert
#====================================================

class LinkedList: #class implementasi stack
    def __init__(self):
        self.head = None #awalnya kosong

    def insert_awal(self,data): #push dalam stack
        #1) buat node baru
        nodeBaru = Node(data) #panggil class node  

        #2) node baru menunjuk ke head lama
        nodeBaru.next = self.head

        #3) head pindah ke  node baru
        self.head = nodeBaru

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        #menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah: ", data_terhapus)

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("===List Baru===")
ll = LinkedList() #instantiasi objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()