
def longestAlternatingSubsequence(nums, start, end, lookup, inc=False, prev=float('inf')):
    if start == end + 1:
        return 0

    key = (start, prev)
    if key not in lookup:
        include = 0
        if (inc and nums[start] > prev) or (not inc and nums[start] < prev):
            include = longestAlternatingSubsequence(nums, start + 1, end, lookup, not inc, nums[start]) + 1
        exclude = longestAlternatingSubsequence(nums, start + 1, end, lookup, inc, prev)
        lookup[key] = max(include, exclude)
    return lookup[key]



nums = 8, 9, 6, 4, 5, 7, 3, 2, 4
lookup = dict()
print(longestAlternatingSubsequence(nums, 0, len(nums) - 1, lookup))