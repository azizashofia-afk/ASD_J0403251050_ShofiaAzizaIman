#====================================================
#TUGAS PRAKTIKUM LINKED LIST

#Nama: Shofia Aziza Iman
#NIM: J0403251050
#Kelas: B1
#====================================================

#====================================================
#Latihan no 2
#====================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def search (self, key):
        if not self.head:
            return None

        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

cll = CircularSinglyLinkedList()
input_data = input("Masukkan elemen ke dalam Circular Linked List (pisahkan dengan koma): ")

if input_data.strip() != "":
    elements = list(map(int, input_data.split(",")))
    for el in elements:
        cll.insert_at_end(el)
else:
    elements = []

key = int(input("Masukkan elemen yang ingin dicari: "))

if not elements:
    print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
else:
    result = cll.search(key)
    if result:
        print(f"Elemen {key} ditemukan dalam Circular Linked List.")
    else:
        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")