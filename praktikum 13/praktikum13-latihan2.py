#==========================================================
# Nama  : Shofia Aziza Iman
# NIM   : J0403251050
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
#==========================================================

#==========================================================
# Latihan 2 : Implementasi Algoritma Kruskal
#==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# Menyimpan hasil MST
mst = []

# Menyimpan total bobot MST
total_weight = 0

# Set untuk menyimpan node yang sudah terhubung
connected = set()

# Memproses setiap edge
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight

        # Menandai node sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total_weight)


#==========================================================
# PERTANYAAN DAN JAWABAN ANALISIS
#==========================================================

# 1. Edge mana yang dipilih pertama kali?
#    Edge C - D dengan bobot 1 dipilih pertama kali karena
#    memiliki bobot paling kecil.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena algoritma Kruskal bertujuan membentuk MST dengan
#    total bobot minimum.

# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST adalah 6.

# 4. Mengapa edge tertentu tidak dipilih?
#    Karena edge tersebut dapat membentuk cycle atau tidak
#    diperlukan lagi setelah semua node terhubung.