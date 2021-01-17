from collections import defaultdict
import heapq


class Graph:

    def __init__(self, n):
        self.N = n
        self.g = defaultdict(dict)
        self.edges = []

    def addEdge(self, u, v, w):
        self.g[u][v] = w
        self.g[v][u] = w
        heapq.heappush(self.edges, (w, u, v))

    def removeEdge(self, u, v, w):
        del self.g[u][v]
        del self.g[v][u]
        self.edges.remove((w, u, v))

    def doesCycleExist(self):
        def helper(u, visited, restack, prev):
            visited.add(u)
            restack.add(u)
            for v in self.g[u]:
                if v not in visited:
                    if helper(v, visited, restack, u):
                        return True
                elif v != prev and v in restack:
                    return True
            restack.remove(u)
            return False

        visited = set()
        for i in range(self.N):
            if i not in visited and helper(i, visited, set(), -1):
                return True
        return False

    def kruskalMST(self):
        mst = Graph(self.N)
        edges = self.edges[:]
        while edges and len(mst.edges) != self.N-1:
            w, u, v = heapq.heappop(edges)
            mst.addEdge(u, v, w)
            if mst.doesCycleExist():
                mst.removeEdge(u, v, w)
        print(mst.edges)


graph = Graph(7)
edges = [
    (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
    (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
]

for edge in edges:
    graph.addEdge(*edge)

graph.kruskalMST()
