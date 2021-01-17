from collections import defaultdict, deque


def create_graph(lst):
    graph = defaultdict(dict)
    for edge in lst:
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1
    return graph


def bfs_traverse(graph, src):
    q = deque()
    visited = set()
    q.append(src)
    visited.add(src)
    while q:
        e = q.popleft()
        # Do processing stuff
        print(e, end=" ")
        for dest in graph[e]:
            if dest not in visited:
                q.append(dest)
                visited.add(dest)


graph = create_graph([[1, 3], [1, 2], [2, 4], [3, 4]])
print(graph)
bfs_traverse(graph, 1)
