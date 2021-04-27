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

def digitSum(x):
    res = 0
    while x != 0:
        res += x % 10
        x //= 10
    return res


def solve():
    n, a, b = map(int, input().split())
    res = 0
    for i in range(1, n+1):
        x = digitSum(i)
        if x >= a and x <= b:
            res += i
    print(res)


def main():
    t = 1
    for _ in range(t):
        solve()


# ------------------------------------------------------------- #
if __name__ == '__main__':
    main()
