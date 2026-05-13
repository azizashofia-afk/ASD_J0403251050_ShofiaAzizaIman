#==========================================================
# Nama  : Shofia Aziza Iman
# NIM   : J0403251050
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
#==========================================================

#==========================================================
# Latihan 4 : Studi Kasus Jaringan Kabel Antar Gedung
# Algoritma: Prim
#==========================================================

import heapq

# Representasi weighted graph antar gedung
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Priority queue untuk menyimpan edge
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total biaya minimum
    total_weight = 0

    # Memproses edge
    while edges:
        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru dari node tersebut
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# Menjalankan algoritma Prim dari GedungA
mst, total = prim(graph, 'GedungA')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total biaya minimum
print("Total biaya minimum =", total)


#==========================================================
# PERTANYAAN DAN JAWABAN ANALISIS
#==========================================================

# 1. Algoritma apa yang digunakan?
#    Algoritma yang digunakan adalah Prim.

# 2. Edge mana saja yang dipilih?
#    Edge yang dipilih adalah GedungA - GedungC,
#    GedungC - GedungD, dan GedungD - GedungB.

# 3. Berapa total biaya minimum?
#    Total biaya minimum adalah 6.

# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena MST dapat menghubungkan seluruh gedung dengan
#    biaya pemasangan kabel paling minimum tanpa membentuk cycle.