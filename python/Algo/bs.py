def binary_search(items, item):
    low = 0
    high = len(items)-1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == item:
            return mid
        elif items[mid] < item:
            low = mid+1
        else:
            high = mid-1
    return -1


items = [1, 4, 6, 8, 9, 32, 57, 86]
print(binary_search(items, -1))
