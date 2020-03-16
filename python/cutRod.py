import sys
import time

n = 1700
price = [i for i in range(n)]

def cutRod(price, n):
    if n<=0:
        return 0
    else:
        maxVal = -32767
        for i in range(n):
            maxVal = max(maxVal, price[i]+cutRod(price, n-i-1))
    return maxVal

def cutRodSmart(price, n):
    min_int = -32767
    val = [0 for i in range(n+1)]
    
    for i in range(1, n+1):
        maxVal = min_int
        for j in range(i):
            maxVal = max(maxVal, price[j]+val[i-j-1])
        val[i] = maxVal
    
    return val[n]

# start = time.time()
# print(cutRod(price, n))
# print(time.time()-start)
start = time.time()
print(cutRodSmart(price, n))
print(time.time()-start)