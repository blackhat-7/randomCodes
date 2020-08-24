def recursive(dims, i, j, lookup):
    if j <= i+1:
        return 0
    
    if not lookup[i][j]:
        minCost = float('inf')
        for k in range(i+1, j):
            cost = recursive(dims, i, k, lookup) + recursive(dims, k, j, lookup)
            cost += dims[i] * dims[k] * dims[j]
            if cost < minCost:
                minCost = cost
        lookup[i][j] = minCost
    
    return lookup[i][j]


dims = list(map(int, input().split()))
length = len(dims)
lookup = [[0]*length for i in range(length)]
print(recursive(dims, 0, length-1, lookup))