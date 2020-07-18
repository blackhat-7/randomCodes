
def rodCuttingProduct(n, lookup):
    if n == 1:
        return 1
    
    key = n
    if n not in lookup:
        maxCost = n
        for i in range(1, n):
            cost = i * rodCuttingProduct(n - i, lookup)
            if maxCost < cost:
                maxCost = cost
        lookup[key] = maxCost
    return lookup[key]


# rod length
n = 15;
lookup = dict()
print(rodCuttingProduct(n, lookup))

