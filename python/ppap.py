string = input()
sub = input()
n = len(string)
k = len(sub)
x = [[0]*k for i in range(n)]


for i in range(n):
    for j in range(k):
        if string[i] == sub[j]:
            x[i][j] = x[i][j-1] + 1 if j>= 1 else 1
        else:
            x[i][j] = x[i][j-1] if j>=1 else 0

print(x)
