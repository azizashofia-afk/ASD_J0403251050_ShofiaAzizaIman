#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 2: Tracing Rekursi
#=============================================================

def countdown(n):

    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)

# KENAPA OUTPUT 'KELUAR' MUNCUL TERBALIK?
# Karena rekursi bekerja seperti tumpukan (stack / LIFO - Last In First Out)
# Artinya yang terakhir masuk akan keluar pertama

# ALUR EKSEKUSI
# 1. Pemanggilan awal : countdown(3)
# Program berjalan kebawah (turun rekursi): Masuk: 2
                                            # Masuk: 3
                                                # Masuk: 1
                                                    # Selesai
# disini fungsi terus memanggil dirinya sampai n == 0
# 2. Saat base case tercapai: n == 0: Selesai
# fungsi tidak memanggil lagi dan mulai kembali ke atas
# 3. Proses kembali (Unwiding Stack): setelah countdown(0) selesai, program kembali ke: countdown(1)
# baris setelah pemanggilan rekursi dijalankan: print("Keluar:", 1)
# lalu kembali ke: countdown(2) -> print("Keluar:", 2)
# lalu: countdown(3) -> print("Keluar:", 3)

# KENAPA TERBALIK?
# karena: - 'Masuk' dicetak sebelum rekursi
        # - 'Keluar' dicetak setelah rekursi selesai
# rekursi itu masuk seperti lorong: - Masuk terus ke dalam (3 -> 2 -> 1 -> 0)
                                  # - Lalu keluar satu per satu dari yang paling dalam
# jadi urutan keluarnya: 1 -> 2 -> 3
# bukan: 3 -> 2 -> 1