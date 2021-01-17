from collections import defaultdict, deque


def colorMap(edges, n):
    graph = defaultdict(dict)
    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1
    colors = [-1]*n
    for u in range(n):
        is_color_available = [True]*n
        for v in graph[u]:
            if colors[v] != -1:
                is_color_available[colors[v]] = False
        for i, isAvailable in enumerate(is_color_available):
            if isAvailable:
                colors[u] = i
                break
    return colors


edges = [[0, 1], [0, 2], [1, 3]]
n = 4
colors = colorMap(edges, n)
print(colors)
