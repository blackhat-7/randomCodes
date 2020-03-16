import math

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

n = int(input())
x = list(map(int, input().split()))
primes = []

for i in range(n):
    y = math.sqrt(x[i])
    if y == int(y) and (primes.count(y) or isPrime(y)):
        print("YES")
        primes.append(y)
    else:
        print("NO")
