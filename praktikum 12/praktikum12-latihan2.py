#==========================================================
# Nama  : Shofia Aziza Iman
# NIM   : J0403251050
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
#==========================================================

#==========================================================
# Latihan 2: Implementasi Dijkstra
#==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak lebih besar dari yang sudah ada, skip
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update jika lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


#==========================================================
# JAWABAN ANALISIS
#==========================================================
# 1. Berapa jarak terpendek dari A ke B?
# Jarak terpendek dari A ke B adalah 4 melalui jalur A -> C -> D. 
# 2. Berapa jarak terpendek dari A ke C?
# Jarak terpendek dari A ke C adalah 2 melalui jalur A -> C -> D.
# 3. Berapa jarak terpendek dari A ke D?
# Jarak terpendek dari A ke D adalah 3 melalui jalur A -> C -> D.
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Jarak ke D lebih kecil melalui C karena 2 + 1 = 3 lebih kecil dibanding melalui B yaitu 4 + 5 = 9.
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# Priority queue berfungsi untuk memilih node dengan jarak terkecil secara efisien.
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Algoritma Dijkstra tidak cocok untuk bobot negatif karena menggunakan pendekatan greedy
# yang mengasumsikan jarak terpendek yang sudah dipilih tidak akan berubah.