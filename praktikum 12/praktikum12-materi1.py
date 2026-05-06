#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Materi 1: Implementasi Algoritma Djikstra
#=============================================================

import heapq
graph = {
'A': {'B': 4, 'C': 2},
'B': {'D': 5},
'C': {'D': 1},
'D': {}
}
def dijkstra(graph, start):
    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}
    # Jarak node awal = 0
    distances[start] = 0
    # Priority queue
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

hasil = dijkstra(graph, 'A')
print(hasil)

#=============================================================
# PENJELASAN ALGORITMA DIJKSTRA
#=============================================================
# Algoritma Dijkstra digunakan untuk mencari jarak terpendek dari satu node ke node lain
# pada graph berbobot positif dengan prinsip greedy, yaitu selalu memilih node dengan
# jarak sementara paling kecil. Proses dimulai dari node awal dengan jarak 0, lalu
# memperbarui jarak ke setiap tetangganya jika ditemukan jalur yang lebih pendek.
# Proses ini dibantu dengan priority queue agar pemilihan node paling efisien.
# Pada contoh ini, jalur terpendek dari A ke D adalah melalui C (A -> C -> D = 3).
# Algoritma ini cepat dan efisien, namun tidak dapat digunakan jika terdapat bobot negatif.