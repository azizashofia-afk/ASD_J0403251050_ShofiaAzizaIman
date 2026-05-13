#==========================================================
# Nama  : Shofia Aziza Iman
# NIM   : J0403251050
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
#==========================================================

#==========================================================
# Latihan 1 : Memahami Konsep Spanning Tree
#==========================================================

# Daftar edge pada graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
# Tidak memiliki cycle dan semua node terhubung
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan seluruh edge graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


#==========================================================
# PERTANYAAN DAN JAWABAN ANALISIS
#==========================================================

# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki lebih banyak edge dan dapat membentuk cycle,
#    sedangkan spanning tree hanya menggunakan edge yang diperlukan
#    untuk menghubungkan semua node tanpa cycle.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena cycle menyebabkan penggunaan edge berlebih dan membuat
#    koneksi menjadi tidak efisien.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree hanya membutuhkan jumlah edge sebanyak
#    jumlah node - 1 agar semua node tetap terhubung tanpa cycle.