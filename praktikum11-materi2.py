#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Materi 2: Implementasi BFS
#=============================================================

#struktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque

#representasi graph
graph = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['B','C']
}

def bfs(graph,start):
    #fungsi untuk melakukan penelusuran graph dengan BFS
    #graph : dictionary yang menyimpanstruktur dari graph
    #start : node awal penelusuran

    #queue digunakan untuk menyimpan node yang akan diproses / dibaca
    queue = deque()
    
    #variabel yang digunakan untuk menyimpan node yang sudah diproses/sudah dikunjungi
    visited = set()

    #masukkan node awal ke queue
    queue.append(start)

    #tandai node awal sebagai node yang sudah dikunnjungi
    visited.add(start)

    while queue:
        #mengambil node paling depan dari queue
        node = queue.popleft()

        #tampilkan node yang sedang dikunjungi
        print(node,end=" ")

        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi 
            if neighbor not in visited:
                #tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                #masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)

#menjalankkan BFS dari node A
bfs(graph,'A')