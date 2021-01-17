n, q = map(int, input().split())

arr = list(map(int, input().split()))
oddIndices = [0]*(n+1)
oddIndices[0] = 0
for i in range(1, len(arr)+1):
    oddIndices[i] = oddIndices[i-1] + 1 if arr[i-1] & 1 == 1 else oddIndices[i-1]

for i in range(q):
    l, r = map(int, input().split())
    if oddIndices[r] - oddIndices[l-1] > 0:
        print(0)
    else:
        print(1)
