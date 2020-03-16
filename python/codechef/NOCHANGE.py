t = int(input())

for i in range(t):
    n, p = map(int, input().split())
    d = list(map(int, input().split()))
    for j in range(n-1, -1, -1):
        if p > 0 and p % d[j] != 0:
            p -= (p//d[j])*d[j]
            print(p, d[j])
    print(p)
