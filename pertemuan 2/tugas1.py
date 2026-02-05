nama_file = "pertemuan 2/stok_barang.txt"

#fungsi membaca data
def baca_stok_barang(nama_file):
    stok_dict = {}
    with open("pertemuan 2/stok_barang.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            parts = baris.split(",")
            if len(parts) !=3:
                continue
            kode, barang, stok_str = parts
            stok_int = int(stok_str)
            stok_dict[kode] = {"barang": barang, "stok": stok_int}
    return stok_dict

#memanggil fungsi baca_stok_barang
buka_stok = baca_stok_barang(nama_file)

#fungsi menu ke 1 (tampilkan stok) pake tabel
def tampilkan_stok(stok_dict):
    if len(stok_dict) == 0:
        print("Data Kosong")
        return
    print("\n===== Stok Barang Fotokopi Shofia =====")
    print(f"{'Kode Barang' : <10} | {'Nama Barang' : <12} | {'Stok Barang' : >5}")
    print("-" * 32)
    
    for kode in sorted(stok_dict):
        barang=stok_dict[kode]["barang"]
        stok=stok_dict[kode]["stok"]
        print(f"{kode : <10} | {barang: <12} | {stok: >5}")

#fungsi  menu 2 (mencari barang berdasarkan kode)
def cari_barang(stok_dict):
    kode_cari = input("Masukkan kode barang yang ingin dicari: ").strip()

    if kode_cari in stok_dict:
        barang= stok_dict [kode_cari]["barang"]
        stok= stok_dict [kode_cari]["stok"]
        print("\n===== Barang ditemukan =====")
        print(f"Kode Barang     : {kode_cari}")
        print(f"Nama Barang     : {barang}")
        print(f"Stok Barang     : {stok}")
    else:
        print("\nBarang tidak ditemukan")

#fungsi menu 3 (tambah barang baru)
def tambah_barang(stok_dict, nama_file):
    print("\n===== Tambah Barang Baru =====")
    kode = input("Masukkan kode barang: ").strip()
    
    #cek kode sudah ada atau belum
    if kode in stok_dict:
        print("Kode barang sudah digunakan!")
        return
    
    nama = input("Masukkan nama barang: ").strip()

    try:
        stok = int(input("Masukkan jumlah stok: "))
    except ValueError:
        print("Stok harus berupa angka! Penambahan barang dibatalkan")
        return
    
    if stok < 0:
        print("Stok tidak boleh negatif. Penambahan barang dibatalkan.")
        return
    
    #tambah ke dictionary
    stok_dict[kode] = {
        "barang": nama,
        "stok": stok
    }
    #simpan ke file
    with open(nama_file, "a", encoding="utf-8") as file:
        file.write(f"\n{kode},{nama},{stok}")
    print("Barang berhasil ditambahkan!")

#fungsi menu 4 (update stok barang)
def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang akan diupdate stoknya: ").strip()
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan. Update dibatalkan.")
        return
    stok_lama = stok_dict[kode]["stok"]
    print(f"Stok saat ini: {stok_lama}")

    print("\nPilih jenis update: ")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihanupdate = input("Masukkan pilihan: ").strip()
    
    if pilihanupdate not in ["1", "2"]:
        print("Pilihan tidak valid. Update dibatalkan.")
        return
    try:
        jumlah = int(input("Masukkan jumlah stok: ").strip())
    except ValueError:
        print("Jumlah harus berupa angka.")
        return
    if jumlah <= 0:
        print("Angka tidak boleh negatif atau nol. Update dibatalkan.")
        return

    #tambah stok
    if pilihanupdate == "1":
        stok_baru = stok_lama + jumlah

    #kurangi stok
    else:
        if jumlah > stok_lama:
            print("Stok tidak mencukupi. Update dibatalkan.")
            return
        stok_baru = stok_lama - jumlah
    
    # stok_lama = stok_dict[kode]["stok"]
    #memasukkan nilai baru ke dictionary
    stok_dict[kode]["stok"] = stok_baru
    print(f"Update berhasil. Stok barang dengan kode {kode} berubah dari {stok_lama} menjadi {stok_baru}.")

#fungsi menu 5 (menyimpan perubahan ke file)
def simpan_data(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):
            barang = stok_dict [kode]["barang"]
            stok = stok_dict [kode] ["stok"]
            file.write(f"{kode}, {barang}, {stok}\n")

#fungsi main (menu utama)
def main():
    buka_stok = baca_stok_barang(nama_file)

while True:
    print("\n===== MENU DATA BARANG FOTOKOPI SHOFIA =====")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan kode")
    print("3. Tambah barang baru")
    print("4. Update stok barang")
    print("5. Simpan data ke file")
    print("0. Keluar")

    pilihan = input("Pilihan menu: ").strip()

    if pilihan == "1":
        tampilkan_stok(buka_stok)

    elif pilihan == "2":
        cari_barang(buka_stok)

    elif pilihan == "3":
        tambah_barang(buka_stok, nama_file)

    elif pilihan == "4":
        update_stok(buka_stok)

    elif pilihan == "5":
        simpan_data(nama_file, buka_stok)
        print("Data berhasil disimpan!")

    elif pilihan == "0":
        print("Program selesai. Terimakasih!")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()