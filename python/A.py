t = int(input())

while(t):
    n = int(input())
    m = list(map(int, input().split()))
    count = 0
    ma = max(m)
    for i in m:
        if i + 100-ma >= 50:
            count+=1
        print(count)
        t-=1

