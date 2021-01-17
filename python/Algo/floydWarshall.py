def get_path(path, src, dest):
    if path[src][dest] == src:
        return [src]
    return get_path(path, src, path[src][dest]) + [path[src][dest]]


def print_all_pair_shortest_paths(path, n):
    for src in range(n):
        for dest in range(n):
            if src != dest:
                print(
                    f'Path from {src} to {dest}: {get_path(path, src, dest)+[dest]}')


def floyd_warshall(edges, n):
    dist = [[float('inf')]*n for _ in range(n)]
    path = [[None]*n for _ in range(n)]
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = float('inf')
    for i in range(n):
        dist[i][i] = 0

    for i in range(n):
        for j in range(n):
            if dist[i][j] != float('inf'):
                path[i][j] = i
            else:
                path[i][j] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]
            if dist[i][i] < 0:
                print("Contains negative cycle")
                return None
    print_all_pair_shortest_paths(path, n)
    return dist


edges = [[1, 0, 4], [1, 2, 3], [3, 1, -1], [0, 2, -2], [2, 3, 2]]
n = 4

all_pairs_shortest_dist = floyd_warshall(edges, n)
print(all_pairs_shortest_dist)
