#=============================================================
# Nama: Shofia Aziza Iman
# NIM: J0403251050
# Kelas: B1
#=============================================================
# Materi 3: Implementasi DFS
#=============================================================

#Implementasi Graph
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

def dfs(graph,node,visited):
#fungsi untuk melakukan penelusuran graph menggunakan DFS
#graph: dictionary yang menyimpan graph
#node: menyimpan noode yang sedang dikunjungi
#visited: menyimpan node yang sudah dikunjungi

    #tandai node aat ii sebagai node yg suda dikunjungi
    visited.add(node)

    #tampilkan node yg sedang dikunjungi
    print(node, end=" ")

    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:

        #jika tetagga belum ernah dikunjungi
        if neighbor not in visited:
            #lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

#set visited
visited = set()

#menjalankan dfs dari A
dfs(graph, "A", visited)