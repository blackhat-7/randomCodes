
def optimalCostBst(freq, lookup, i, j, level=1):
    if j < i:
        return 0
    if i == j:
        return freq[i] * level

    key = (i, j)
    if key not in lookup:
        minCost = float('inf')
        for k in range(i, j+1):
            cost = optimalCostBst(freq, lookup, i, k-1, level + 1) + optimalCostBst(freq, lookup, k+1, j, level + 1) + freq[k] * level
            if cost < minCost:
                minCost = cost
        lookup[key] = minCost
    
    return lookup[key]









freq = (25, 10, 20)
lookup = dict()
print(optimalCostBst(freq, lookup, 0, len(freq) - 1))