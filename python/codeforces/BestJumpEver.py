n = int(input())
a = list(map(int, input().split()))

max = a[0]
c = 1

for i in range(1, n):
    if a[i]>max:
        max = a[i]
        c += 1
print(c)