
def longestZeroSum(arr, n):
    my_map = dict()
    curr_sum = 0
    my_map[0] = -1
    longest = 0
    for i, num in enumerate(arr):
        curr_sum += num
        if curr_sum in my_map:
            if i - my_map[curr_sum] > longest:
                longest = i - my_map[curr_sum]
        else:
            my_map[curr_sum] = i

    return longest


t = int(input())
for q in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(longestZeroSum(arr, n))


'''
2
5
4 2 -3 1 6
5
4 2 0 1 6
'''
