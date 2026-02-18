#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
#=============================================================
# Praktikum 4 : Implementasi Dasar: Queue berbasis Linked List
#=============================================================

class Node:
    def __init__(self,data): #tandanya dia adalah konstruktor
        self.data = data #menyimpan nilai data
        self.next = None #pointer ke note berikutnya

# Queue dengan 2 pointer : head dan tail
class QueueLL:
    def __init__(self):
        self.head = None #node paling depan
        self.tail = None #node paling belakang
    
    def is_empty(self):
        return self.head is None


    def enqueue(self, data):
        #menambah data di belakang (tail)
        nodeBaru = Node(data)

        #Jika queue kosong, head dan tail menunjuk ke node yg sama
        if self.is_empty():
            self.head = nodeBaru
            self.tail = nodeBaru
            return
        
        #Jika queue tidak kosong:
        #Tail lama menunjuk ke node baru
        self.tail.next = nodeBaru
        #Tail pindah ke node baru
        self.tail = nodeBaru

    def dequeue(self):
        #menghapus data dari depan

        #1) lihat data yang paling depan
        data_terhapus = self.head.data

        #2) geser head ke node berikutnya
        self.head = self.head.next

        #3) jika setelah geser head menjadi none, maka queue kosong
        #tail juga harus jadi none
        if self.head is None:
            self.tail = None
        return data_terhapus

    def tampilkan(self):
        #menampilkan isi queue dari heaad
        current = self.head
        print("Head ->", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Tail di node terakhir")
    
#instantiasi objek class queueLL
q = QueueLL()
q.enqueue("S")
q.enqueue("H")
q.enqueue("O")
q.tampilkan()

q.dequeue()
q.tampilkan()