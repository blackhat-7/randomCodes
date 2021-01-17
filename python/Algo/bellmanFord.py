def get_path(parent, src, dest):
    if parent[dest] == -1:
        return [src]
    return get_path(parent, src, parent[dest]) + [dest]


def bellman_ford(edges, n, src):
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[src] = 0
    for i in range(n - 1):
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
    for i in range(n):
        print('Path from', src, 'to', i, ':', get_path(parent, src, i))

    return dist, parent


edges = [[0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, 2], [3, 1, 1], [1, 4, 2], [4, 3, -3]]
n = 5
source = 0
dist, parent = bellman_ford(edges, n, source)
print('All shortest paths from', source, ':', dist)
print('All parents :', parent)
