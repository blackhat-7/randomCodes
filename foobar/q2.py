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


def helper(nums, i, x, notes, dp):
    if x < 0:
        return 0
    if x == 0:
        return 1
    key = (i, x)
    if key not in dp:
        using_i = 0
        skipping_i = 0
        if nums[i] > 0:
            using_i = helper(nums, i, x-notes[i], notes, dp)
        if i < 2:
            skipping_i = helper(nums, i+1, x, notes, dp)
        dp[key] = using_i + skipping_i
    return dp[key]


def solve():
    a, b, c, x = map(int, input().split())
    count = 0
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if i*500 + j*100 + k*50 == x:
                    count += 1

    print(count)


def main():
    t = 1
    for _ in range(t):
        solve()


# ------------------------------------------------------------- #
if __name__ == '__main__':
    main()
