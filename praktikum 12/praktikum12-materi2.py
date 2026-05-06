#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Materi 2: Implementasi Algoritma Bellman-Ford
#=============================================================

import heapq
graph = {
'A': {'B': 4, 'C': 2},
'B': {'D': 5},
'C': {'D': 1},
'D': {}
}

def bellman_ford(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relaksasi berulang
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances

hasil = bellman_ford(graph, 'A')
print(hasil)

#=============================================================
# PENJELASAN ALGORITMA BELLMAN-FORD
#=============================================================
# Algoritma Bellman-Ford digunakan untuk mencari jarak terpendek dari satu node ke node lain
# pada graph berbobot, termasuk yang memiliki bobot negatif. Algoritma ini bekerja dengan
# melakukan relaksasi semua edge secara berulang sebanyak (jumlah node - 1) untuk memastikan
# setiap node mendapatkan jarak minimum. Jika ditemukan jarak yang lebih kecil, maka nilai
# akan diperbarui. Berbeda dengan Dijkstra, Bellman-Ford lebih fleksibel karena dapat
# menangani bobot negatif, namun prosesnya lebih lambat. Algoritma ini juga dapat digunakan
# untuk mendeteksi adanya siklus negatif dalam graph.