class Graph:
    V = None
    mat = []
    def __init__(self, v):
        self.V = v
        self.mat = [[] for i in range(v)]
    
    def addEdge(self, s, e):
        self.mat[s].append(e)
        self.mat[e].append(s)
    
    def print(self):
        print(self.mat)

    def isReachable(self, s, d): 
        visited =[False]*(self.V) 
        queue=[] 
        queue.append(s) 
        visited[s] = True
        while queue: 
            n = queue.pop(0) 
            if n == d: 
                return True
            for i in self.mat[n]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
        return False



n = int(input())
t = int(input())
g = Graph(n+1)

for i in range(t):
    q, u, v = map(int, input().split())
    if q==1:
        g.addEdge(u, v)
    else:
        if g.isReachable(u, v):
            print("YES")
        else:
            print("NO")

