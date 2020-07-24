n = int(input())
arr = list(input().split())

vowels = {'a','e','i','o','u'}
count = [0]*n
count[0] = 1 if arr[0][0] in vowels and arr[0][-1] in vowels else 0
for i in range(1, n):
    count[i] = count[i-1]
    if arr[i][0] in vowels and arr[i][-1] in vowels:
        count[i] += 1

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(count[r] - count[l-1] if l != 0 else count[r])
    

'''
abce iasdo asdas asdasu rtyra osdi
1      1     0      1     0    1
0      1     2      3     4    5
'''