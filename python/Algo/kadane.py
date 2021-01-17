
def kadanes(arr):
    if all(num < 0 for num in arr):
        return max(arr), [max(arr)]
    max_sum = float('-inf')
    curr_sum = 0
    start, end = 0, 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum < 0:
            curr_sum = 0
            start = i+1
        max_sum = max(max_sum, curr_sum)
        end = i if max_sum == curr_sum else end
    return max_sum, arr[start:end+1]


# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr = [-1, -2, -6]
max_contiguous_sum, max_contiguous_sum_arr = kadanes(arr)
print(max_contiguous_sum_arr)
print(max_contiguous_sum)
