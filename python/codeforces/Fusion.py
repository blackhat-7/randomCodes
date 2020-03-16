n = int(input())

lst = list(map(int, input().split()))
sumLst = [0 for i in range(n-1)]

max = 0
maxIndex = 0

for i in range(n-1):
        sumLst[i] = lst[i] + lst[i+1]
        if sumLst[i] > max:
            max = sumLst[i]
            maxIndex = i
print(max)
print(maxIndex)
starShip = max
print(lst)
print(sumLst)
print()

for i in range(n-2):
    sum1 = 0
    sum2 = 0
    if maxIndex<len(lst)-1:
        sum1 = lst[maxIndex] + lst[maxIndex+1]
    if maxIndex > 0:
        sum2 = lst[maxIndex] + lst[maxIndex-1]
    
    if sum1 > sum2:
        lst.pop(maxIndex)
        lst[maxIndex] = max
        sumLst.pop(maxIndex)
        sumLst[maxIndex] = sum1
        starShip += sum1
    else:
        lst.pop(maxIndex-1)
        lst[maxIndex-1] = max
        sumLst.pop(maxIndex-1)
        sumLst[maxIndex-1] = sum2
        starShip += sum2
    print(lst)
    print(sumLst)
    print()


print(starShip)