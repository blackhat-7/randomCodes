t = int(input())

for i in range(t):
    r, c = map(int, input().split())
    stable = True
    for j in range(r):
        arr = list(map(int, input().split()))
        if j==0 or j==r-1:
            for k in range(c):
                if (k==0 or k==c-1) and arr[k]>=2:
                    stable = False
                    break
                elif ((k>0 or k<c-1) and arr[k]>=3):
                    stable = False
                    break
        else:
            for k in range(c):
                if (k==0 or k==c-1) and arr[k]>=3:
                    stable = False
                    break
                elif ((k>0 or k<c-1) and arr[k]>=4):
                    stable = False
                    break
    print("Stable" if stable else "Unstable")

