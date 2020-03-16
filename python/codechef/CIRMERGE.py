t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.append(lst[0])
    sumLst = []
    for j in range(n):
        sumLst.append(lst[j]+lst[j+1])
    
    penalty = 0
    
    while(n>1):
        print(lst, sumLst)
        minSum = sumLst[0]
        minIndex = 0

        for j in range(1, n):
            if sumLst[j] < minSum:
                minSum = sumLst[j]
                minIndex = j

        penalty += minSum
        sumLst.pop(minIndex)

        if minIndex==0:
            lst[0] = minSum
            lst[n] = minSum
            lst.pop(1)
            sumLst[0] = minSum+lst[1]
            sumLst[-1] = lst[-2] + minSum 

        elif minIndex==n-1:
            lst[0] = minSum
            lst[n] = minSum
            lst.pop(minIndex)
            sumLst[0] = lst[0] + lst[1]
            sumLst[minIndex-1] = lst[minIndex-1] + minSum

        else:
            lst[minIndex] = minSum
            lst.remove(lst[minIndex+1])
            sumLst[minIndex-1] = lst[minIndex-1]+minSum
            sumLst[minIndex] = minSum + lst[minIndex+1]
        n -= 1
        print(penalty)

    print(lst, sumLst)
    print(penalty)