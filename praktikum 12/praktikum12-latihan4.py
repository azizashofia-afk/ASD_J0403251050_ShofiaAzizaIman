#==========================================================
# Nama  : Shofia Aziza Iman
# NIM   : J0403251050
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
#==========================================================

#==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
#==========================================================

import heapq

# Graph lokasi kampus (waktu tempuh dalam menit)
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
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


hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


#==========================================================
# JAWABAN ANALISIS 
#==========================================================
# 1. Lokasi mana yang paling dekat dari Gerbang?
# Kantin adalah yang paling dekat karena memiliki jarak 2 menit dari Gerbang.
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 7 menit melalui jalur Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1).
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# Tidak, karena jalur langsung belum tentu memiliki total bobot paling kecil.
# Contohnya, ke Aula bisa langsung dari Kantin (2 + 7 = 9), tetapi lebih cepat melalui Lab (7).
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Karena semua bobot bernilai positif (waktu tempuh), sehingga Dijkstra dapat
# bekerja optimal dan efisien untuk mencari jalur tercepat.