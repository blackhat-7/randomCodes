from bisect import bisect_left

array1 = [1, 2, 3, 4, 7, 9]
array2 = [0, 1, 2, 1, 1, 4]
counts = [0]*len(array1)

array1.sort()
array2.sort()

start = 0
for i in range(len(array2)):
    x = bisect_left(array2, array1[i]+1, start, len(array2))
    counts[i] = x
    start = x

print(counts)