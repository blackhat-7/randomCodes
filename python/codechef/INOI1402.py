n, m = map(int, input().split())

mat = [[float('inf')]*i+[0]+[float('inf')]*(n-i-1) for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    mat[a-1][b-1] = c
    mat[b-1][a-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i!=j:
                mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

fair = -1
for i in range(n):
    for j in range(n):
        if mat[i][j] != float('inf') and mat[i][j] > fair:
            fair = mat[i][j]
print(fair)