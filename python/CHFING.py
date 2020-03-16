t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    count = 0
    if k>1:
        count = k-1
    if k>n:
        m = (k-n-1)//(n-1) + 1
        count += m*(2*(k-n)-(m-1)*(n-1))//2
    print(count%(10**9+7))
