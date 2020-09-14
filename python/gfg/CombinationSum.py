def solve(n):
    res = set()
    res.add(frozenset([n]))
    if n == 0 or n == 1:
        return res
    for i in range(1, n//2+1):
        x = solve(i)
        y = solve(n-i)
        for a in x:
            for b in y:
                a = set(a)
                a.update(set(b))
                res.add(frozenset(a))
    return res

n = int(input())
print(solve(n))