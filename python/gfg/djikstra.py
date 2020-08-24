import heapq
from collections import defaultdict

def djikstra(edges: List[List[int]], n: int, k: int):
    graph = defaultdict(dict)
    for u, v, w in edges:
        graph[u][v] = w

    heap = [(0, k)]
    dist = {}

    while heap:
        w, u = heapq.heappop(heap)
        if w not in dist:
            dist[u] = w
            for v in graph[u]:
                heapq.heappush(heap, (dist[u]+graph[u][v], v))
    return dist
