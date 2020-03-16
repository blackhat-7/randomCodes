from math import gcd
from functools import reduce

n, x = map(int, input().split())
lst = list(map(int, input().split()))

dist = []

for i in range(n):
    dist.append(abs(x-lst[i]))

def find_gcd(list):
    x = reduce(gcd, list)
    return x

print(find_gcd(dist))