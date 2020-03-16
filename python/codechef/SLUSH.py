t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    d = [0]*n
    f = [0]*n
    b = [0]*n

    extra = c.copy()
    for j in range(n):
        d[j], f[j], b[j] = map(int, input().split())
        if extra[d[j]-1]>0:
            extra[d[j]-1] -= 1
    
    sum = 0
    arr = [0]*n
    y = 0
    for j in range(n):
        if c[d[j]-1] > 0:
            sum += f[j]
            arr[j] = d[j]
            c[d[j]-1] -= 1
        
        else :
            for k in range(y, m):
                if extra[k] > 0:
                    sum += b[j]
                    arr[j] = k+1
                    extra[k] -= 1
                    c[k] -= 1
                    y = k
                    break
    print(sum)
    for j in range(n):
        print(arr[j], end=" ")
    print()

