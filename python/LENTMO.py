def sum2d(x, n):
    sum=0
    for i in range(n):
        sum+=x[i][1]
    return sum

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    x = int(input())

    while(True):
        arr2 = [0]*n
        arr3 = arr
        diff = [0]*n
        for j in range(n):
            y = arr[j]^x
            arr2[j] = y
            diff[j] = [j, y-arr[j]]
        
        diff = sorted(diff,key=lambda l:l[1], reverse=True)

        for j in range(n):
            diff[j] = [diff[j][0], arr2[diff[j][0]]]

        for j in range(k):
            arr3[diff[j][0]] = diff[j][1]
        print(arr3)
        if (sum(arr3)>sum(arr)):
            arr = arr3
        else:
            break
    print(sum(arr))
        

    

    
        
