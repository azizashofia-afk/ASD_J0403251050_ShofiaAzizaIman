#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Materi 1: Implementasi Algoritma Kruskal
#=============================================================

# Daftar edgde: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]
# Mengurutkan edge berdasarkan bobot
edges.sort()

mst = []
total_weight = 0

# Set sederhana untuk node yang sudah dipilih
connected = set()

for weight, u, v in edges:

    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

#=============================================================
# PENJELASAN ALGORITMA KRUSKAL
#=============================================================
# Algoritma Kruskal digunakan untuk membentuk Minimum Spanning Tree (MST)
# dengan cara memilih edge yang memiliki bobot paling kecil terlebih dahulu.
# Setiap edge akan ditambahkan ke MST jika tidak membentuk cycle, sehingga
# seluruh node dapat terhubung dengan total bobot minimum. Pada program ini,
# edge diurutkan dari bobot terkecil menggunakan sort(), lalu dipilih satu
# per satu untuk membentuk MST dan menghitung total bobot akhirnya.