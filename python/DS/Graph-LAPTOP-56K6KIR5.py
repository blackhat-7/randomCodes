from collections import deque
class Graph:
    
    V = None
    adjList = None

    def __init__(self, v):
        self.V = v
        self.adjList = {}
        for i in range(v):
            self.adjList[i] = deque()
    
    def addEdge(self, s, e, w=1):
        if s in self.adjList:
            self.adjList[s].append((e, w))
        #Unidirected
        # if e in self.adjList:
        #     self.adjList[e].append((s, w))
    
    def printGraph(self):
        print(self.adjList)

    def bfs(self, s):
        visited = [False] * self.V
        queue = deque()
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.popleft()
            print(s, end = " ")
            for v in self.adjList[s]:
                if not visited[v[0]]:
                    queue.append(v[0])
                    visited[v[0]] = True
        print()
    
    def dfs(self, s):
        visited = [False] * self.V
        stack = deque()
        stack.append(s)
        while stack:
            s = stack.pop()
            if not visited[s]:
                print(str(s) + " ", end="")
                visited[s] = True
            
            for v in self.adjList[s]:
                if not visited[v[0]]:
                    stack.append(v[0])
        print()



def main():
    g = Graph(4)
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
    g.printGraph()
    g.bfs(2)
    g.dfs(2)

main()
