nums = list(map(int, input().split()))
length = len(nums)

inc = [1]*length
dec = [1]*length

for i in range(1, length):
    if nums[i] > nums[i-1]:
        inc[i] = inc[i-1] + 1

for i in reversed(range(length-1)):
    if nums[i] > nums[i+1]:
        dec[i] = dec[i+1] + 1

maxBitonicLength = 0
for i in range(length):
    maxBitonicLength = max(maxBitonicLength, inc[i] + dec[i] - 1) 

print(maxBitonicLength)