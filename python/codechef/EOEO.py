t = int(input())
for q in range(t):
    ts = int(input())
    x = ts
    count = 0
    while(x%2 == 0):
        count += 1
        x //= 2
    ans = ts//(2**(count+1))
    print(ans)