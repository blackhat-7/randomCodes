from collections import defaultdict
import heapq


def get_path(parent, src, dest):
    if parent[dest] == -1:
        return [src]
    return get_path(parent, src, parent[dest]) + [dest]


def djikstra(edges, n, src, dest):
    graph = defaultdict(dict)
    for u, v, w in edges:
        graph[u][v] = w
    parent = [-1] * n
    dist = {}
    q = [(src, 0, -1)]

    while q:
        u, d, p = heapq.heappop(q)
        if u not in dist:
            dist[u] = d
            parent[u] = p
            for v in graph[u]:
                heapq.heappush(q, (v, dist[u] + graph[u][v], u))
    print(dist)
    return get_path(parent, src, dest), dist[dest]


edges = [[0, 1, -1], [0, 2, 4], [1, 2, 3],
         [1, 3, 2], [3, 1, 1], [1, 4, 2], [4, 3, -3]]
n = 5
src = 0
dest = 4
path, length = djikstra(edges, n, src, dest)
print('All shortest paths from', src, ':', path)
print('Path length:', length)
