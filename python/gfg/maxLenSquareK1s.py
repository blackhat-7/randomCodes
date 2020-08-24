
m, n = map(int, input().split())

mat = []
for i in range(m):
    mat.append(list(map(int, input().split(', '))))

lookup = mat.copy()
for i in range(1, m):
    lookup[i][0] += lookup[i-1][0]
for i in range(1, n):
    lookup[0][i] += lookup[0][i-1]
for i in range(1, m):
    for j in range(1, n):
        lookup[i][j] += lookup[i-1][j] + lookup[i][j-1] - lookup[i-1][j-1]

q = int(input())

for _ in range(q):
    row, col, k  = map(int, input().split())

    low = 0
    high = min(row, col, m-row-1, n-col-1)
    maxLen = 0
    while low <= high:
        mid = (low + high)//2
        count = lookup[row+mid][col+mid] - (lookup[row+mid][col-mid-1] if col>mid else 0) - (lookup[row-mid-1][col+mid] if row > mid else 0) + (lookup[row-mid-1][col-mid-1] if row > mid and col > mid else 0)
        if count > k:
            high = mid-1
        elif count <= k:
            maxLen = 2*mid + 1
            low = mid+1
    print(maxLen)

'''
1, 0, 1, 0, 0
1, 0, 1, 1, 1
1, 1, 1, 1, 1
1, 0, 0, 1, 0


O(m*n + q*(log(max_dist)))

'''