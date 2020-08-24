dest = [2, 3, 4, 5]
n = len(dest)
k = 2
dest.sort(reverse=True)

count = k
totalTime = 0
for i in range(0, n, k):
    totalTime += 2 * dest[i]

print(totalTime)