#================================================
# NAMA : SHOFIA AZIZA IMAN
# NIM : J0403251050
# Kelas : TPL B / P1
#================================================
#================================================ 
# Tugas Hands-On: Sistem Antrian Bengkel Motor 
#================================================

#======================
# Class Node
#======================
class Node:
    def __init__(self, no, nama, servis):
        #menyimpan data pelanggan
        self.no = no            #nomor antrian
        self.nama = nama        #nama pelanggan
        self. servis = servis   #jenis servis

        #pointer ke node berikutnya
        self.next = None

#======================
# Class Queue (Linked List)
#======================
class QueueBengkel:
    def __init__(self):
        #pointer depan (pelanggan pertama)
        self.front = None

        #pointer belakang (pelanggann terakhir)
        self.rear = None

    def is_empty(self):
        return self.front is None
    #=======================
    # Enqueue (Tambah Pelanggan)
    #=======================
    def enqueue(self, no, nama, servis):
        #membuat node baru
        node_baru = Node(no, nama, servis)

        #jika antrian kosong
        if self.is_empty():
            self.front = node_baru
            self.rear = node_baru
            return
            
            #node terakhir menunjuk ke node baru
        self.rear.next = node_baru

            #rear berpindah ke node baru
        self.rear = node_baru

    #========================
    # cek apakah nomor antrian sudah ada
    # =======================
    def ceknoantrian(self, no):
        current = self.front

        #traversal seluruh antrian
        while current is not None:
            if current.no == no:
                return True
            current = current.next

        return False    
        
    #=========================
    # Dequeue (Layani Pelanggan)
    #=========================
    def dequeue(self):
        #jika antrian kosong
        if self.is_empty():
            print("Antrian kosong. Tidak ada pelanggan.")
            return None

        #simpan pelanggan terdepan
        pelanggan = self.front

        #front pindah ke node berikutnya
        self.front = self.front.next

        #jika setelah dihapus antrian menjadi kosong
        if self.front is None:
            self.rear = None
        return pelanggan

        print("Melayani pelanggan:")
        print(f"    No Antrian  : {pelanggan.no}")
        print(f"    Nama        : {pelanggan.nama}")
        print(f"    Servis      : {pelanggan.servis}") 

    #===========================
    # Tampilkan Antrian
    #===========================
    def tampilkan(self):
        #jika antrian kosong
        if self.is_empty():
            print("Antrian masih kosong.")
            return
            
        print("===== Data Antrian Bengkel =====")

        #mulai dari node paling depan
        current = self.front

        #traversal sampai akhir
        while current is not None:
            print(f"No Antrian  : {current.no}")
            print(f"Nama        : {current.nama}")
            print(f"Servis      : {current.servis}")
            print("------------------------------")

            #pindah ke node berikutnya
            current = current.next

#===========================
# Program Utama
#===========================
def main():
    q = QueueBengkel()

    while True:
        print("\n========== Sistem Antrian Bengkel ==========")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih Menu: ").strip()

        if pilih == "1":
            no = input("Masukkan No Antrian : ").strip()
            if not no:
                print("No antrian tidak boleh kosong!")
                continue
            if not no.isdigit():
                print("No antrian harus berupa angka!")
                continue
            if q.ceknoantrian(no):
                print("No antrian sudah dipakai!")
                continue
            nama = input("Masukkan Nama : ").strip()
            if not nama:
                print("Nama tidak boleh kosong!")
                continue
            if not nama.isalpha():
                print("Nama hanya boleh huruf!")
                continue
            servis = input("Servis : ").strip()
            if not servis:
                print("Servis tidak boleh kosong!")
                continue
            q.enqueue(no, nama, servis)
            print("Pelanggan berhasil ditambahkan ke dalam antrian!")
        elif pilih == "2":
            pelanggan = q.dequeue()
            if pelanggan is not None:
                print(f"Pelanggan dilayani : {pelanggan.no} - {pelanggan.nama} - {pelanggan.servis}")
        elif pilih == "3":
            q.tampilkan()
        elif pilih == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

#menjalankan program
if __name__ == "__main__":
    main()