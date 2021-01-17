class DisjoinSet:
    parent = {}
    rank = {}

    def makeSet(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[x] > self.rank[y]:
            self.parent[yset] = xset
        else:
            self.parent[xset] = yset
            self.rank[yset] += 1


ds = DisjoinSet()
for i in range(6):
    ds.makeSet(i)
ds.union(0, 5)
ds.union(1, 4)
print(ds.parent)
print(ds.find(5))
ds.union(1, 5)
print(ds.find(1))
