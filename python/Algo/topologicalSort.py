from collections import defaultdict, deque


def create_graph(lst):
    graph = defaultdict(dict)
    for edge in lst:
        graph[edge[0]][edge[1]] = 1
    return graph


def dfs(graph, src, visited):
    visited.add(src)
    arr = [src]
    for v in graph[src]:
        if v not in visited:
            arr += dfs(graph, v, visited)
    return arr


def topologicalSort(graph, n):
    visited = set()
    arr = []
    for i in range(n):
        if i not in visited:
            arr = dfs(graph, i, visited) + arr
    return arr


edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0),
         (3, 4), (5, 1), (7, 0), (7, 1)]
n = 8
graph = create_graph(edges)
arr = topologicalSort(graph, n)
print(arr)
