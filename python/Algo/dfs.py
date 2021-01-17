from collections import defaultdict, deque


def create_graph(lst):
    graph = defaultdict(dict)
    for edge in lst:
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1
    return graph


def dfs_traverse(graph, src, visited):
    visited.add(src)
    # Do any processing
    print(src, end=" ")
    for dest in graph[src]:
        if dest not in visited:
            dfs_traverse(graph, dest, visited)


graph = create_graph([[1, 3], [1, 2], [2, 4], [3, 4]])
print(graph)
dfs_traverse(graph, 1, set())
