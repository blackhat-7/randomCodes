
def merge(arr, low, mid, high):
    tempArr = [0] * (high-low+1)
    i, j, k = low, mid+1, 0
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            tempArr[k] = arr[i]
            i += 1
        else:
            tempArr[k] = j
            j += 1
        k += 1
    while i <= mid:
        tempArr[k] = arr[i]
        i += 1
        k += 1
    while j <= high:
        tempArr[k] = arr[j]
        j += 1
        k += 1
    for i in range(low, high+1):
        arr[i] = tempArr[i-low]


def mergeSort(arr, low, high):
    if high == low:
        return
    mid = low + ((high - low) >> 1)
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)
    print(arr)


arr = [8, 3, 7, 8, 3, 4, 79, 2, 4, 73, 6, 3, 78, 34]
mergeSort(arr, 0, len(arr)-1)
print(arr)
