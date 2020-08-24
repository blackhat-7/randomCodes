t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    sum = 0
    for i in range(n):
        sum += min(a[i], b[i])
    print(sum)