#==========================================================
# Nama  : Shofia Aziza Iman
# NIM   : J0403251050
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
#==========================================================

#==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
#==========================================================

import heapq

# Representasi graph berbobot antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


start_node = 'Bogor'
hasil = dijkstra(graph, start_node)

print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(start_node, "->", kota, "=", jarak)


#==========================================================
# ANALISIS
#==========================================================
# 1. Node awal yang digunakan apa?
# Node awal yang digunakan adalah Bogor.

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Depok dengan jarak 2 adalah yang paling dekat dari Bogor.

# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Bandung dengan jarak 8 adalah yang paling jauh dari Bogor.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Algoritma dimulai dari Bogor dengan jarak 0, lalu menghitung jarak ke tetangga
# terdekat yaitu Depok (2) dan Jakarta (5). Dari Depok, ditemukan jalur lebih pendek ke Jakarta
# (2 + 2 = 4) dibanding langsung (5), kemudian dilanjutkan ke Bandung melalui Depok atau Jakarta.
# Jalur terbaik ke Bandung adalah Bogor -> Depok -> Bandung (2 + 6 = 8). Proses ini terus
# memilih jarak terkecil menggunakan priority queue hingga semua node diperbarui.