t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    m = 0
    for j in range(n):
        a = 20*x[j]-10*y[j]
        a = 0 if a<0 else a
        
        if a>m:
            m = a
    print(m)