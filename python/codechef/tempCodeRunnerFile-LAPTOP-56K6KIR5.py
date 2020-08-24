t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    num5 = 0
    num10 = 0
    flag = 1
    for i in range(n):
        if arr[i] == 5:
            num5 += 1
        elif arr[i] == 10 and num5 > 0:
            num5 -= 1
        elif arr[i] == 15:
            if num10 > 0:
                num10 -= 1
            elif num5 > 1:
                num5 -= 2
        else:
            flag = 0
            break
    if flag:
        print("YES")
    else:
        print("NO")
