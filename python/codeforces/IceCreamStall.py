from collections import defaultdict, deque
import copy


def floyd(g, N):
    N += 1
    dist = copy.deepcopy(g)
    for i in range(N):
        dist[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist


n, m = map(int, input().split())
q = [0]*n
g = defaultdict(lambda: defaultdict(1))
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c
    g[b][a] = c

dist = floyd(g, n)

flag = 1
for u in g:
    for v in g[u]:
        if g[u][v] != dist[u][v]:
            print("No")
            flag = 0
            break
if flag:
    print("Yes")
