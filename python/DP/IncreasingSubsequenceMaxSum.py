nums = list(map(int, input().split()))
length = len(nums)
lookup = [0] * length

for i in range(length):
    for j in range(i):
        if nums[i] > nums[j] and lookup[i] < lookup[j]:
            lookup[i] = lookup[j]
    lookup[i] += nums[i]

maxSum = max(lookup)

MSIS = []
currSum = maxSum
for i in reversed(range(length)):
    if currSum == lookup[i]:
        MSIS.append(nums[i])
        currSum -= nums[i]
    if currSum == 0:
        break
MSIS.reverse()

print(MSIS)