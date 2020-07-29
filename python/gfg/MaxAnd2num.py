
def checkBit(pattern, arr, n):
    count = 0
    for i in range(n):
        if (arr[i] & pattern) == pattern:
            count += 1
            if count > 1:
                break
    return count


def maxAnd(arr):
    n = len(arr)
    max_and_res = 0
    for i in range(31, -1, -1):
        pattern = max_and_res | (1 << i)
        count = checkBit(pattern, arr, n)
        if count > 1:
            max_and_res = max_and_res | (1 << i)
    print(max_and_res)
        





arr = [4, 8, 6, 2] 

maxAnd(arr)