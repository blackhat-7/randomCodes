arr = [2,3,5,6,1,4]

def conquer(low, mid, high, arr, count):
    j = mid
    for i in range(high, mid-1, -1):
        while(j>=0):
            if arr[i] < arr[j]:
                j -= 1
        arr.insert(j, arr[i])


def divide(low, high, arr, count):
    if high-low == 1:
        if arr[high]>arr[low]:
            low, high = high, low
            count += 1
        mid = (high-low)//2 + low
        count = divide(low, mid, arr, count)
        count = divide(mid+1, high, arr, count)

        return conquer(low, mid, high, arr, count)

def countInversions(arr):
    count = divide(0, len(arr)-1, arr, 0)
    return count
