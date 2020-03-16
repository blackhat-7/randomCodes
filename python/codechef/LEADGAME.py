n = int(input())

max_lead1 = 0
max_lead2 = 0

for i in range(n):
    x, y = map(int, input().split())
    if x-y >= 0 and x-y > max_lead1:
        max_lead1 = x-y
    elif x-y < 0 and y-x > max_lead2:
        max_lead2 = y-x

if max_lead1 > max_lead2:
    print(1, max_lead1)
else:
    print(2, max_lead2)