nums = list(map(int, input().split()))
length = len(nums)
lookup = [1] * length

maxLength = 1

for i in range(1, length):
    for j in range(i):
        if nums[j] < nums[i]:
            lookup[i] = max(lookup[i], lookup[j] + 1)
    maxLength = max(maxLength, lookup[i])

print(maxLength)

