#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Latihan 2: Studi Kasus DSF
#=============================================================

graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': [],
'E': [],
'F': []
}

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited)

'''
Pertanyaan Analisis
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
    DFS masuk ke node terdalam terlebih dahulu karena menggunakan pendekatan rekursif (atau stack) yang bekerja dengan prinsip "masuk
    sejauh mungkin sebelum kembali". Artinya, ketika sebuah node memiliki tetangga, algoritma akan langsung mengikuti satu jalur hingga
    mencapai node paling dalam (leaf) sebelum kembali ke node sebelumnya untuk mengeksplorasi jalur lain.
2. Apa yang terjadi jika urutan neighbor diubah?
    Jika urutan neighbor diubah, maka urutan asil DFS juga akan berubah. Hal ini karena DFS mengikuti urutan tetangga secara langsung saat 
    rekursi. Node yang muncul lebih dulu dalam daftar neighbor akan dieksplorasi lebih dalam terlebih dahulu, sehingga perubahan urutan 
    neighbor akan memengaruhi jalur yang diambil dan urutan kunjungan node.
3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
    Jika dibandingkan dengan BFS pada graph yang sama, DFS dan BFS menghasilkan urutan kunjungan yang berbeda. DFS menelusuri satu jalur hingga
    dalam sebelum berpindah ke jalur lain (misalnya: A -> B -> D -> E -> C -> F), sedangkan BFS menjelajah secara melebar per level (misalnya: A ->
    B -> C -> D -> E -> F). BFS lebih cocok untuk mencari jalur terdekat, sementara DFS lebih cocok untuk eksplorasi mendalam atau pencarian semua
    kemungkinan jalur.
'''