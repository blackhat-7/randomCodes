from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(lambda: [])
    
    def addEdge(self, s, d, w):
        self.graph[s].append([d, w])
        self.graph[d].append([s, w])
    
    def bfs(self, u):
        visited = [False for i in range(self.V)]
        q = deque()
        q.append(u)
        visited[u] = True
        while q:
            u = q.popleft()
            print(u, end=" ")
            for edge in self.graph[u]:
                if not visited[edge[0]]:
                    q.append(edge[0])
                    visited[edge[0]] = True
        print()

    def dfs(self, u):
        visited = set()
        def dfsUtil(u):
            visited.add(u)
            print(u, end=" ")
            for edge in self.graph[u]:
                if edge[0] not in visited:
                    dfsUtil(edge[0])
        dfsUtil(u)
        


def main():
    g = Graph(3)
    g.addEdge(0, 1, 2)
    g.addEdge(0, 2, 1)
    g.addEdge(2, 0, 1)
    g.bfs(0)
    g.dfs(2)

if __name__ == "__main__":
    main()
