import sys

class Graph:
    V = None
    mat = []
    def __init__(self, v):
        self.V = v
        self.mat = [[0 for i in range(v)] for j in range(v)]
    
    def addEdge(self, s, e):
        self.mat[s][e] = 1
        self.mat[e][s] = 1
    
    def print(self):
        print(self.mat)
    
    def minDistance(self, dist, sptSet): 
  
        min = sys.maxsize
        min_index = 0

        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index

    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
            for v in range(self.V): 
                if self.mat[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.mat[u][v]: 
                    dist[v] = dist[u] + self.mat[u][v] 
        return dist

def main():

    n, m, a, b = map(int, input().split())
    g = Graph(n+1)
    for i in range(m):
        s, e = map(int, input().split())
        g.addEdge(s, e)

    A = g.dijkstra(a)
    B = g.dijkstra(b)

    i = 1
    count = 0

    while(i<n+1):
        if A[i]!=-1 and A[i]!=sys.maxsize and A[i]==B[i]:
            count += 1
        i += 1

    print(count)    



if __name__ == "__main__":
    main()
