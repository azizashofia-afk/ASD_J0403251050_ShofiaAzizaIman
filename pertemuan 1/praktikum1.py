#====================================================
#praktikum 1 : konsep ADT dan file handling
#latihan dasar 1A : membaca seluruh isi file
#====================================================

#membuka file dengan mode read ("r")
with open("pertemuan 1/data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() #membaca keseluruhan isi file dalam satu string
print(isi_file)

print("=== Hasil read ===")
print("tipe data:", type(isi_file))
print("jumlah karakter: ", len(isi_file))
print("jumlah baris: ", isi_file.count("\n")+1)

#membuka file per baris
print("=== Membaca file per baris ===")
jumlah_baris = 0
with open("pertemuan 1/data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("baris ke-", jumlah_baris)
        print("isinya: ", baris)

#====================================================
#praktikum 1 : konsep ADT dan file handling
#latihan dasar 2A : parsing baris menjadi kolom data
#====================================================

with open("pertemuan 1/data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan
        print("NIM: ", nim, "| Nama: ", nama, "| Nilai: ", int(nilai))

#====================================================
#praktikum 1 : konsep ADT dan file handling
#latihan dasar 3A : membaca file dan menyimpan ke list
#====================================================

data_list = [] #inisialisasi list untuk menampung data mahasiswa

with open("pertemuan 1/data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan
        #simpan sebagai list "[nim,nama,nilai]"
        data_list.append([nim,nama,int(nilai)])

print("=== Data mahasiswa dalam list ===")
print(data_list)

print("=== Jumlah record dalam list ===")
print("jumlah record",len(data_list))

#====================================================
#praktikum 1 : konsep ADT dan file handling
#latihan dasar 4A : membaca file dan menyimpan ke dictionary
#====================================================

data_dict = {} #buat variabel untuk dictionary
with open("pertemuan 1/data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #simpan data mahasiswa ke dictionary
        data_dict[nim] = {             #key
            "nama": nama,              #values
            "nilai": int(nilai)        #values
        }
print("=== Data mahasiswa dalam dictionary ===")
print(data_dict)
