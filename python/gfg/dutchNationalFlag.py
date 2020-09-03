
def dutch(arr, n):
    i = 0
    j = n-1
    mid = 0
    while mid <= j:
        if arr[mid] == 0:
            arr[mid], arr[i] = arr[i], arr[mid]
            i += 1; mid += 1 
        elif arr[mid] == 2:
            arr[mid], arr[j] = arr[j], arr[mid]
            j -= 1
        else:
            mid += 1


t = int(input())#code#code

for q in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dutch(arr, n)
    print(*arr)

# 0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0
