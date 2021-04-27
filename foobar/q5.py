from collections import defaultdict, deque
import heapq


def gcd(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# ------------------------------------------------------------- #


def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    prime[0] = False
    prime[1] = False
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime


def helper(prime):
    count = 0
    good = [0]*(10**5+1)
    for i in range(0, 10**5+1):
        if i % 2 != 0 and prime[i] and prime[(i+1)//2]:
            count += 1
        good[i] = count
    return good


def solve(good):
    l, r = map(int, input().split())
    print(good[r] - good[l-1])


def main():
    good = helper(SieveOfEratosthenes(10**5))
    t = int(input())
    for _ in range(t):
        solve(good)


# ------------------------------------------------------------- #
if __name__ == '__main__':
    main()
