t = int(input())
for i in range(t):
    n = int(input())
    c = list(map(int ,input().split()))
    h = list(map(int, input().split()))
    x = [0]*n
    for j in range(n):
        l = j-c[j] if j-c[j]>=0 else 0
        r = j+c[j] if j+c[j]<=n-1 else n-1
        for k in range(l, r+1):
            x[k] += 1
    
    print(x)
    x.sort()
    h.sort()
    if x == h:
        print("YES")
    else:
        print("NO")

