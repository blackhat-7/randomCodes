import sys

class Graph:
    V = None
    mat = []
    def __init__(self, v):
        self.V = v
        self.mat = [[0 for i in range(v)] for i in range(v)]

    def addEdge(self, s, e, w):
        if self.mat[s][e] == 0 or w < self.mat[s][e]: 
            self.mat[s][e] = w
            self.mat[e][s] = w
    
    def print(self):
        print(self.mat)

    def minDistance(self, dist, sptSet):
        min_index = sptSet.index(False)
        min = 10**12
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    def dijkstra(self, src): 
  
        dist = [10**12] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            u = self.minDistance(dist, sptSet) 
  
            sptSet[u] = True

            for v in range(self.V): 
                if self.mat[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.mat[u][v]: 
                        dist[v] = dist[u] + self.mat[u][v] 
  
        return dist[self.V-1]



n, m = map(int, input().split())
g = Graph(n)
for i in range(m):
    u, v, d = map(int, input().split())
    g.addEdge(u-1, v-1, d)

dist = g.dijkstra(0)

if dist != 10**12:
    print(dist)
else:
    print(-1)


