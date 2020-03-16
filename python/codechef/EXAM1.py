t = int(input())

for i in range(t):
    n = int(input())
    key = input()
    chef = input()
    score = n
    j=0
    while(j<n):
        if chef[j] == 'N':
            score -= 1
        elif chef[j] != key[j]:
            score -=1
            if j!=n-1:
                score -= 1
                j += 1
        j+=1

    print(score)