
def solve(mat, m, n):
    row = 0
    col = 0

    while 1:
        for j in range(col, n):
            print(mat[row][j], end=" ")
        row += 1
        if row >= m:
            break
        for i in range(row, m):
            print(mat[i][n-1], end=" ")
        n -= 1
        if col >= n:
            break
        for j in reversed(range(col, n)):
            print(mat[m-1][j], end=" ")
        m -= 1
        if row >= m:
            break
        for i in reversed(range(row, m)):
            print(mat[i][col], end=" ")
        col += 1
        if col >= n:
            break
    print()


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    mat = [[0]*n for i in range(m)]
    row, col = 0, 0
    for i in range(m*n):
        mat[row][col] = arr[i]
        col += 1
        if col == n:
            col = 0
            row += 1
    solve(mat, m, n)
    
