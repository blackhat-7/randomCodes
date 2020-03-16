a, b, c, d = map(int, input().split())

arr = [a,b,c]
arr.sort()
time = 0

if arr[1]-arr[0] < d:
    time += d - (arr[1] - arr[0])
if arr[2]-arr[1] < d:
    time += d - (arr[2] - arr[1])

print(time)