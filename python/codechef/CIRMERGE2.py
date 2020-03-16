
def findPenalty(lst, sumLst, penalties, penalty, n):
    if n==1:
        penalties.append(penalty)
        return penalties

    else :
        
        for i in range(n):
            templst = lst.copy()
            tempsumLst = sumLst.copy()
            sum = tempsumLst[i]
            tempsumLst.pop(i)

            if i==0:
                templst[0] = sum
                templst[n] = sum
                templst.pop(1)
                tempsumLst[0] = sum+templst[1]
                tempsumLst[-1] = templst[-2] + sum

            elif i==n-1:
                templst[0] = sum
                templst[n] = sum
                templst.pop(i)
                tempsumLst[0] = templst[0] + templst[1]
                tempsumLst[i-1] = templst[i-1] + sum

            else:
                templst[i] = sum
                templst.remove(templst[i+1])
                tempsumLst[i-1] = templst[i-1]+sum
                tempsumLst[i] = sum + templst[i+1]
            print(templst, tempsumLst)
            findPenalty(templst, tempsumLst, penalties, penalty+sum, n-1)
    return penalties

t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.append(lst[0])
    sumLst = []
    for j in range(n):
        sumLst.append(lst[j]+lst[j+1])
    
    penalties = findPenalty(lst, sumLst, [], 0, n)
    print(penalties)
    print(len(penalties))
    print(min(penalties))
    