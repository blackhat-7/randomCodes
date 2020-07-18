arr = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

i = 0

while i < len(arr):
    if arr[i] <= 0:
        i += 1
    while i < len(arr) and arr[i] > 0:
        if arr[arr[i] - 1] > 0:
            temp = arr[i]
            arr[i] = arr[arr[i]- 1]
            arr[temp - 1] = -1
        else:
            arr[arr[i] - 1] -= 1
            arr[i] = 0

for i in range(len(arr)):
    arr[i] = -arr[i]

print(arr)