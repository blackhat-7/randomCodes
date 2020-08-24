
def rodCutting(prices, n, lookup):
    if n == 0:
        return 0 
    
    key = n
    if n not in lookup:
        maxCost = float('-inf')
        for i in range(1, n+1):
            cost = prices[i-1] + rodCutting(prices, n - i, lookup)
            if maxCost < cost:
                maxCost = cost
        lookup[key] = maxCost
    return lookup[key]

# length = { 1, 2, 3, 4, 5, 6, 7, 8 };
prices = [1, 5, 8, 9, 10, 17, 17, 20]

# rod length
n = 4;
lookup = dict()
print(rodCutting(prices, n, lookup))


'''
                            4
            1 3                         2 2
    

'''