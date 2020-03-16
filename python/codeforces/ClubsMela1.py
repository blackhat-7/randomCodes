
n, q = map(int, input().split())
maxi = [-2] *(n+1)

for i in range(n):
    a, b = map(int, input().split())
    maxi[b] = max(b, maxi[a])

for i in range(q):
    x = int(input())
    print(maxi[x])
