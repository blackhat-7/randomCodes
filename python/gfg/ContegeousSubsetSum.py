t = int(input())
for q in range(t):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    
    sumArr = [arr[0]]
    for i in range(1, n):
        sumArr.append(sumArr[i-1] + arr[i])
    
    sumArr.append(0)
    i = 0; j = 0; found = 0
    while(i < n and j < n):
        if sumArr[j] - sumArr[i-1] == s:
            found = 1
            break
        if sumArr[j] - sumArr[i-1] > s:
            i += 1
        else:
            j += 1
    if found:
        print(i+1, j+1)
    else:
        print(-1)