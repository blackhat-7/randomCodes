t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    loss = 0
    for i in range(n):
        if arr[i] > k:
            loss += arr[i] - k
    print(loss)