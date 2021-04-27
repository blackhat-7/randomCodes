from collections import defaultdict, deque


def bfs(g, visited, soldiers):
    q = deque()
    for i, s in enumerate(soldiers):
        q.append(s+[i])
        visited[s[0]] = i
    while q:
        new_q = deque()
        while q:
            sol = q.popleft()
            if sol[1] > 0:
                for c in g[sol[0]]:
                    if c in visited:
                        if visited[c] != sol[2]:
                            return True
                    else:
                        new_q.append([c, sol[1]-1, sol[2]])
                        visited[c] = sol[2]
        q = new_q
    return False


t = int(input())
for q in range(t):
    n, r, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(r):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    soldiers = []
    for _ in range(m):
        u, v = map(int, input().split())
        soldiers.append([u, v])
    visited = {}
    if bfs(g, visited, soldiers) or len(visited) != n:
        print("No")
    else:
        print("Yes")
