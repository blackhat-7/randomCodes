def partition(arr, low, high):
    p_index = high
    for i in range(low, high+1):
        if (i < p_index and arr[i] > arr[p_index]) or (i > p_index and arr[i] < arr[p_index]):
            arr[i], arr[p_index] = arr[p_index], arr[i]
    return p_index


def lomuto(arr, low, high):
    p_index = low
    pivot = arr[high]
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1
    arr[p_index], arr[high] = arr[high], arr[p_index]
    return p_index


def quickSort(arr, low, high):
    if low >= high:
        return
    pivot = lomuto(arr, low, high)
    quickSort(arr, low, pivot-1)
    quickSort(arr, pivot+1, high)


arr = [4, 7, 1, 3, 6, 3]
quickSort(arr, 0, len(arr)-1)
print(arr)

4, 7, 1, 3, 6, 3
1, 7, 4, 3, 6, 3
1, 3, 4, 7, 6, 3
1, 3, 3, 7, 6, 4
