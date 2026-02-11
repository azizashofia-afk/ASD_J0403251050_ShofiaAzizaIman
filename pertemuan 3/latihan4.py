#====================================================
#TUGAS PRAKTIKUM LINKED LIST

#Nama: Shofia Aziza Iman
#NIM: J0403251050
#Kelas: B1
#====================================================

#====================================================
#Latihan no 4
#====================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def display(self):
        if not self.head:
            print("kosong")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def merge(self, list2):
        if not self.head:
            return list2
        
        if not list2.head:
            return self 
        
        self.tail.next = list2.head
        self.tail = list2.tail
        return self

list1 = LinkedList()
list2 = LinkedList()

input1 = input("Masukkan elemen untuk Linked list 1 (pisahkan koma): ")
if input1.strip() != "":
    elements1 = list(map(int, input1.split(",")))
    for el in elements1:
        list1.insert_at_end(el)
input2 = input("Masukkan elemen untuk Linked List 2 (pisahkan koma): ")
if input2.strip() != "":
    elements2 = list(map(int, input2.split(",")))
    for el in elements2:
        list2.insert_at_end(el)

print("\nLinked List 1:", end=" ")
list1.display()

print("Linked List 2:", end=" ")
list2.display()

merged = list1.merge(list2)
print("Linked List setelah digabungkan:", end=" ")
merged.display()