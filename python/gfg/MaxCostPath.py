from collections import defaultdict, deque

class Edge:
    def __init__(self, s, d, w):
        self.s, self.d, self.w = s, d, w

edges = [
		Edge(0, 6, 11), Edge(0, 1, 5), Edge(1, 6, 3), Edge(1, 5, 5),
		Edge(1, 2, 7), Edge(2, 3, -8), Edge(3, 4, 10), Edge(5, 2, -1),
		Edge(5, 3, 9), Edge(5, 4, 1), Edge(6, 5, 2), Edge(7, 6, 9),
		Edge(7, 1, 6)
	]
src = 0
cost = 50
graph = defaultdict(dict)

for e in edges:
    graph[e.s][e.d] = e.w
    graph[e.d][e.s] = e.w

# BFS
q = deque()
q.append((50, 0, set([0])))
max_cost = float('inf')
while q:
    c, u, path = q.popleft()
    if c > cost:
        max_cost = min(max_cost, c)
    for v in graph[u]:
        if v not in path:
            new_path = set(path)
            new_path.add(v)
            q.append((c + graph[u][v], v, new_path))
print(max_cost)