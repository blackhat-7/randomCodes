def sumOfDigits(x):
    sum = 0
    for i in str(x):
        sum+=int(i)
    return sum

t = int(input())
for i in range(t):
    n = int(input())
    ans = 10*n + (10-(sumOfDigits(n)%10))%10
    print(ans)