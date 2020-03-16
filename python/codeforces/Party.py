class Graph:
    V = None
    mat = []
    def __init__(self, v):
        self.V = v
        self.mat = [[] for i in range(v)]
    
    def add(self, s, e):
        self.mat[s].append(e)
        #self.mat[e].append(s)
    
    def print(self):
        print(self.mat)

    def DFS(self, start):
        visited = [False for i in range(self.V)]
        maxCount = self.DFSUtil(start, visited, 0, 0)
        return maxCount
    
    def DFSUtil(self, start, visited, maxCount, count):
        visited[start] = True
        if count>maxCount:
            maxCount = count
        for i in self.mat[start]:
            if not visited[i]:
                maxCount = self.DFSUtil(i, visited, maxCount, count+1)
        return maxCount
            

def main():
    n=int(input())
    lst = []
    g = Graph(n+1)
    for i in range(n):
        lst.append(int(input()))
    check = []
    for i in range(n):
        if lst[i] != -1:
            g.add(lst[i], i+1)
        else:
            check.append(i+1)
    max = 0
    for i in check:
        x = g.DFS(i)
        if x>max:
            max = x
    print(max+1)

        

if __name__ == "__main__":
    main()
