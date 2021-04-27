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

def helper(lst, i, j, dp):
    if i < 0 or j < 0 or i >= len(lst) or j >= len(lst[0]):
        return 0
    if dp[i][j] == -1:
        right = helper(lst, i, j+1, dp)
        down = helper(lst, i+1, j, dp)
        dp[i][j] = max(right, down) + lst[i][j]
    return dp[i][j]


def solve():
    n = int(input())
    lst = [[], []]
    lst[0] = list(map(int, input().split()))
    lst[1] = list(map(int, input().split()))
    dp = [[-1]*n for _ in range(2)]
    print(helper(lst, 0, 0, dp))


def main():
    t = 1
    for _ in range(t):
        solve()


# ------------------------------------------------------------- #
if __name__ == '__main__':
    main()
