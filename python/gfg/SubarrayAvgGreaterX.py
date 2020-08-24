arr = list(map(int, input().split()))
k = int(input())
n = len(arr)
maxLen = -1


# BruteForce
for i in range(n):
    prevAvg = 0
    for j in range(i, n):
        avg = (prevAvg*(j-i)+arr[j])/(j-i+1)
        if avg >= k and j-i+1 > maxLen:
            maxLen = j-i+1
        prevAvg = avg

# print(maxLen)


#Optimal

newArr = [arr[i]-k for i in range(n)]
print(newArr)

prefixSum = [0]*n
for i in range(n):
    prefixSum[i] = newArr[i] + prefixSum[i-1] if i > 0 else newArr[i]











'''

avg = sum/len

prevAvg*prevLen+new / prevLen + 1

'''