#==========================================================
# Nama  : Shofia Aziza Iman
# NIM   : J0403251050
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
#==========================================================

#==========================================================
# Latihan 3: Implementasi Bellman-Ford
#==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Relaksasi sebanyak (jumlah node - 1)
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


#==========================================================
# JAWABAN ANALISIS
#==========================================================
# 1. Berapa bobot langsung dari A ke B?
# Bobot langsung dari A ke B adalah 5
# 2. Berapa total bobot jalur A -> C -> B?
# melalui jalur A -> C -> B totalnya 4 + (-2) = 2
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# jalur melalui C lebih kecil dan dipilih sebagai jalur terpendek.
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# Bellman-Ford dapat digunakan pada bobot negatif karena melakukan relaksasi berulang pada semua edge,
# sehingga dapat menemukan jarak minimum yang benar.
# 5. Apa yang dimaksud dengan proses relaksasi edge?
# Relaksasi adalah proses memperbarui jarak jika ditemukan jalur yang lebih pendek.
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# Perbedaan utama dengan Dijkstra adalah Bellman-Ford bisa menangani bobot negatif tetapi lebih lambat, 
# sedangkan Dijkstra lebih cepat namun tidak bisa digunakan pada graph dengan bobot negatif.
