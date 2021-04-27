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


def solve():
    x, y = map(int, input().split())
    count = 0
    while x <= y:
        x *= 2
        count += 1
    print(count)


def main():
    t = 1
    for _ in range(t):
        solve()


# ------------------------------------------------------------- #
if __name__ == '__main__':
    main()
