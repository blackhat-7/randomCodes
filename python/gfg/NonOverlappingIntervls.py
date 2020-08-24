from collections import deque

start = list(map(int, input().split()))
end = list(map(int, input().split()))

arr = list(zip(start, end))
arr.sort()
res = deque()

for i in range(len(start)-1):
    if arr[i][1] < arr[i+1][0]:
        res.append((arr[i][1], arr[i+1][0]))
print(res)