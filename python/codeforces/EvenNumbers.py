n, t = map(int, input().split())

arr = [0]*n
even = [i for i in range(1, n+1)]

print(arr, even)
for i in range(t):
    q, l, r = map(int, input().split())

    if q=='a':
        arr[l] = r

    else:

