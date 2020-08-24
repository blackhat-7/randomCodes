t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    num5 = 0
    num10 = 0
    flag = True
    for i in range(n):
        if arr[i] == 5:
            num5 += 1
        elif arr[i] == 10 and num5 > 0:
            num5 -= 1
            num10 += 1
        elif arr[i] == 15 and num10 > 0:
            num10 -= 1
        elif arr[i] == 15 and num5 > 1:
            num5 -= 2
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
