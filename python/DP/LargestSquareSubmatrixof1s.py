rowLen, colLen = map(int, input().split())
matrix = []
for i in range(rowLen):
    matrix.append(list(map(int, input().split())))

lookup = matrix.copy()
maxSubMatrixlen = 0

for i in range(rowLen):
    for j in range(colLen):
        if i and j and matrix[i][j] == 1:
            lookup[i][j] = min(lookup[i][j-1], lookup[i-1][j], lookup[i-1][j-1]) + 1
        if maxSubMatrixlen < lookup[i][j]:
            maxSubMatrixlen = lookup[i][j]

print(maxSubMatrixlen)


