t = int(input())

for q in range(t):
    s = input()
    n = len(s)
    count = 0
    i = 1
    while(i < n):
        if s[i] != s[i-1]:
            count += 1
            i += 1
        i += 1
    print(count)