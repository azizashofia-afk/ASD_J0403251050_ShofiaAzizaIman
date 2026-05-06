#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 1: Studi Kasus BFS
#=============================================================

graph = {
'Rumah': ['Sekolah', 'Toko'],
'Sekolah': ['Perpustakaan'],
'Toko': ['Pasar'],
'Perpustakaan': [],
'Pasar': []
}

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')

'''
Pertanyaan Analisis
1. Node mana yang dikunjungi pertama?
    Node yang dikunjungi pertama dalam proses BFS adalah "Rumah", karena algoritma selalu memulai
    traversal dari node awal yang diberikan. Pada kode tersebut, "Rumah" langsung dimasukkan ke 
    dalam queue dan diproses pertama kali sebelum node lainnya.
2. Mengapa BFS cocok untuk mencari jalur terdekat?
    BFS cocok digunakan untuk mencari jalur terdekat karena cara kerjanya yang menjelajah graph 
    secara melebar (level by level). Artinya, semua node yang memiliki jarak satu langkah dari titik
    awal akan dikunjungi terlebih dahulu, kemudian dilanjutkan ke node dengan jarak dua langkah, dan
    seterusnya. Dengan cara ini, node yang pertama kali ditemukan dijamin merupakan jalur paling 
    pendek dalam graph tanpa bobot
3. Apa perbedaan urutan BFS jika struktur graph diubah
    Urutan kunjungan BFS dapat berubah jika struktur graph diubah, terutama pada urutan tetangga dalam
    setiap node. Karena BFS menggunakan antrian (queue), node yang dimasukkan lebih dulu akan diproses
    lebih dulu. Oleh karena itu, perubahan urutan pada daftar tetangga akan memengaruhi urutan kunjungan 
    BFS, meskipun titik awalya tetap sama.
'''