t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    n = len(arr)

    single = False
    double = False
    for j in range(n):
        if k % arr[j] != 0:
            single = True
            ans = str(k//arr[j]+1)
            print("YES", end=" ")
            for l in range(n):
                if l == j:
                    print(ans, end=" ")
                else:
                    print("0", end=" ")
            print()
            break
    
    if not single:
        for j in range(n-1):
            if not double:
                for l in range(j+1, n):
                    if arr[j]%arr[l] != 0 and arr[l]%arr[j] != 0:
                        double = True
                        if (j>l):
                            j, l = l, j
                        x = (k-arr[l])//arr[j]+1
                        print("YES ", end="")
                        for m in range(n):
                            if m == j:
                                print(x, end=" ")
                            elif m == l:
                                print("1", end=" ")
                            else:
                                print("0", end=" ")
                        print()
                        break
            else:
                break
                
    if not single and not double:
        print("NO")
    
    




                
    