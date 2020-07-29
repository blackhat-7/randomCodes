
def helper(arr, n, k, lookup):
    if k == 1:
        return sum(arr[:n])
    if n == 1:
        return arr[0]

    minSum = float('inf')
    for i in range(1, n):
        minSum = min(minSum, max(helper(arr, i, k-1, lookup), sum(arr[i:n])))
    return minSum

def paintersPartition(arr, n, k):
    lookup = [[-1]*n for i in range(n)]
    return helper(arr, n, k, lookup)


def possible(arr, n, k, threshold):
    painters = 1
    curr_sum = 0
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum > threshold:
            painters += 1
            curr_sum = arr[i]
    return painters <= k

def optimal(arr, n, k):
    low = max(arr)
    high = sum(arr)

    while low < high:
        mid = (low + high)//2
        if possible(arr, n, k, mid):
            high = mid
        else:
            low = mid + 1
    return low



arr = list(map(int, input().split()))
k = int(input())
n = len(arr)

print(paintersPartition(arr, n, k))
print(optimal(arr, n, k))