t = int(input())
for q in range(t):
    n = int(input())
    if n%2==0:
        flag = 1
        for i in range(1, n**2+1, n):
            if flag:
                for j in range(i, i+n):
                    print(j, end=" ")
                flag = not flag
            else:
                for j in range(i+n-1, i-1, -1):
                    print(j, end=" ")
                flag = not flag
            print()
    else:
        for i in range(1, n**2+1, n):
            for j in range(i, i+n):
                print(j, end=" ")
            print()
