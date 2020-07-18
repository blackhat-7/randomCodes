nums = list(map(int, input().split()))
length = len(nums)

inc = [0]*length
dec = [0]*length

for i in range(length):
    for j in range(i):
        if nums[i] > nums[j] and inc[i] < inc[j]:
            inc[i] = inc[j]
    inc[i] += 1

for i in reversed(range(length)):
    for j in reversed(range(i+1, length)):
        if nums[i] > nums[j] and dec[i] < dec[j]:
            dec[i] = dec[j]
    dec[i] += 1

# print(inc, dec)
maxBitonicSubsequence = 0
for i in range(length):
    if inc[i] + dec[i] - 1 > maxBitonicSubsequence:
        maxBitonicSubsequence = inc[i] + dec[i] - 1

print(maxBitonicSubsequence)
