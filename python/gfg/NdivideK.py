def helper(n, k, prev, lookup):
    if k == 0:
        if n == 0:
            return 1
        return 0
    elif n <= 0:
        return 0
    key = (n, k, prev)
    if key not in lookup:
        count = 0
        for i in range(prev):
            count += helper(n-i, k-1, i+1, lookup)
        lookup[key] = count
    return lookup[key]





n, k = map(int, input().split())
lookup = dict()
print(helper(n, k, n+1, lookup))