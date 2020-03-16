t = int(input())
for i in range(t):
    n = int(input())
    base = 2
    exp = n-1
    mod = 10**9+7

    result = 1
    base = base % mod
    while (exp>0):
        if (exp%2==1):
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod

    ans = (10%mod * result)%mod
    print(ans)