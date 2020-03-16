import time
import random

n = 10000
arr = [ random.randint(0,n-1) for i in range(n-1,-1,-1)]
def maxRange(arr, n):
    maxDiff = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]<arr[j] and j-i>maxDiff:
                maxDiff = j-i
    return maxDiff

def maxRangeSmart(arr, n):
    maxDiff = 0
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if (arr[i]<arr[j] or j-i<maxDiff) :
                if (j-i>maxDiff) :
                    maxDiff = j-i
                break
    return maxDiff

start = time.time()
print(maxRange(arr, n))
print(time.time()-start)

start = time.time()
print(maxRangeSmart(arr, n))
print(time.time()-start)