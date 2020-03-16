s = input()
q = int(input())
n = len(s)

dynamic = [0]*n

for i in range(1, n):
    dynamic[i] = dynamic[i-1]
    if s[i] != s[i-1]:
        dynamic[i] += 1

for i in range(q):
    l, r = map(int, input().split())
    print(dynamic[r-1]-dynamic[l-1])