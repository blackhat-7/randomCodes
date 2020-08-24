
def minSumPartition(nums, lookup, i, sum1 = 0, sum2 = 0):
    if i < 0:
        return abs(sum1 - sum2)
    
    key = (i, sum1, sum2)
    if key not in lookup:
        include = minSumPartition(nums, lookup, i-1, sum1 + nums[i], sum2)
        exclude = minSumPartition(nums, lookup, i-1, sum1, sum2 + nums[i])
        lookup[key] = min(include, exclude)
    return lookup[key]

nums = list(map(int, input().split()))

lookup = dict()
print(minSumPartition(nums, lookup, len(nums) - 1))









'''
10 20 15 5 25

10 20 15 5

'''
