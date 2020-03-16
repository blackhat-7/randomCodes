t = int(input())

for i in range(t):
    s = input()
    t = input()
    flag = True

    if len(t)>=len(s):
        j = 0
        for k in range(len(t)):
            if s[j] != t[k]:
                if k==0 or s[j-1] != t[k]:
                    flag = False
                    break
                else:
                    j-=1
            if j+1<len(s):
                j += 1
        if s[len(s)-1] != t[len(t)-1]:
            flag = False
    else:
        flag = False
    if flag:
        print("YES")
    else:
        print("NO")
        