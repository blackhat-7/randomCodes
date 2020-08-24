def collectMaxPoints(matrix, i, j, m, n, lookup):
    if i < 0 or j < 0 or i > m or j > n or matrix[i][j] == -1:
        return 0
    
    key = (i, j)
    if key not in lookup:
        right = 0; left = 0
        if i & 1:
            left = collectMaxPoints(matrix, i, j - 1, m, n, lookup)
        else:
            right = collectMaxPoints(matrix, i, j + 1, m, n, lookup)
        down = collectMaxPoints(matrix, i + 1, j, m, n, lookup)
        lookup[key] = max(left, right, down) + matrix[i][j]
    
    return lookup[key]


mat = [
		[1, 1, -1, 1, 1],
		[1, 0, 0, -1, 1],
		[1, 1, 1, 1, -1],
		[-1, -1, 1, 1, 1],
		[1, 1, -1, -1, 1]
	]

lookup = dict()
print("Maximum value collected is", collectMaxPoints(mat, 0, 0, len(mat)-1, len(mat[0])-1, lookup))