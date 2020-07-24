from collections import deque

start = list(map(int, input().split()))
end = list(map(int, input().split()))

arr = list(zip(start, end))
arr.sort()
res = deque()
res.append(arr[0])
for i in range(1, len(start)):
    if res[-1][1] > arr[i][0] and res[-1][1] > arr[i][1]:
        res.pop()
        res.append(arr[i])
    else:
        res.append(arr[i])

print(res)
    