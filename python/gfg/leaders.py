import collections
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = collections.deque()
    curr_max = 0
    for i in reversed(range(n)):
        if arr[i] >= curr_max:
            curr_max = arr[i]
            res.appendleft(arr[i])
    print(*res)
