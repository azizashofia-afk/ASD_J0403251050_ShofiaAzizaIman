#==========================================================
# Nama  : Shofia Aziza Iman
# NIM   : J0403251050
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
#==========================================================

#==========================================================
# Latihan 5 : Tugas Mandiri MST
# Kasus 1 : Jaringan Jalan Antar Kota
# Algoritma: Kruskal
#==========================================================

# Daftar edge: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# Menyimpan hasil MST
mst = []

# Menyimpan total bobot MST
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses algoritma Kruskal
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

# Menampilkan total bobot minimum
print("Total bobot minimum =", total_weight)


#==========================================================
# PERTANYAAN DAN JAWABAN ANALISIS
#==========================================================

# 1. Kasus apa yang dipilih?
#    Kasus yang dipilih adalah jaringan jalan antar kota.

# 2. Algoritma apa yang digunakan?
#    Algoritma yang digunakan adalah Kruskal.

# 3. Edge mana saja yang dipilih dalam MST?
#    Edge yang dipilih adalah Bogor - Depok,
#    Depok - Jakarta, dan Depok - Bandung.

# 4. Berapa total bobot MST?
#    Total bobot MST adalah 9.

# 5. Mengapa edge tertentu tidak dipilih?
#    Karena edge tersebut dapat membentuk cycle atau
#    memiliki bobot lebih besar dibanding edge lainnya.