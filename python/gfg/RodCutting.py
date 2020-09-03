from functools import lru_cache


def helper(arr, n, dp):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    if dp[n] == -1:
        for i in range(3):
            dp[n] = max(dp[n], helper(arr, n-arr[i], dp) + 1)
    return dp[n]

    


t = int(input())

for q in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(helper(arr, n, [-1 for i in range(n+1)]))
