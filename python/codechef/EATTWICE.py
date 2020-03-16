t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    max1 = 0
    d1 = 0
    max2 = 0
    d2 = 0

    for j in range(n):
        d, v = map(int, input().split())
        
        if v > max1:
            if d == d1:
                max1 = v
            else:
                max2 = max1
                d2 = d1
                max1 = v
                d1 = d
        elif v>max2:
            if d != d1:
                max2 = v
                d2 = d 
    print(max1 + max2)
