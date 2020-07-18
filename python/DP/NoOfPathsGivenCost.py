
def recursive(matrix, cost, i, j, lookup):
    if cost < 0 or i < 0 or j < 0:
        return 0
    if cost == matrix[i][j] and i == 0 and j == 0:
        return 1
    key = (i, j, cost)
    if key not in lookup:
        lookup[key] = recursive(matrix, cost - matrix[i][j], i-1, j, lookup) + recursive(matrix, cost - matrix[i][j], i, j-1, lookup)
    return lookup[key]



m, n = map(int, input().split())
matrix = []
for i in range(m):
    matrix.append(list(map(int, input().split())))
cost = int(input())

lookup = dict()
print(recursive(matrix, cost, m - 1, n - 1, lookup))