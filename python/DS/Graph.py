class Graph:
    V = None
    adj = []
    def __init__(self, v):
        self.V = v
        self.adj = [[] for i in range(v)]

    def addEdge(self, s, e):
        self.adj[s].append(e)

    def print(self):
        print(self.adj)

    def DFS(self, start):
        visited = [False for i in range(self.V)]
        self.DFSUtil(start, visited)
        print()

    def DFSUtil(self, start, visited):
        visited[start] = True
        print(start, end=" ")
        for i in self.adj[start]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def BFS(self, start):
        visited = [False for i in range(self.V)]
        queue = [start]
        while(queue):
            start = queue.pop(0)
            visited[start] = True
            print(start, end = " ")
            for i in self.adj[start]:
                if not visited[i]:
                    queue.append(i)
        print()


def main():
    if __name__ == "__main__":
        main()
        
