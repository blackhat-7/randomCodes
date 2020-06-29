arr = list(map(int, input().split()))
n = len(arr)
# j = n-1
# i = 0
# while(i < j):
#     if arr[i] > n or arr[i] < 0:
#         while(j >= 0 and i < j and (arr[j] > n or arr[j] < 0)):
#             j -= 1
#         arr[i], arr[j] = arr[j], arr[i]
#     i += 1
# print(n)
# print(j)
# print(arr)

# for i in range(j+1):
#     arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
# print(arr)
# for i in range(n):
#     if arr[i] != i+1:
#         print(i+1)
#         break
i = 0; j = 0
while(j < n and i < n):
    while(j < n and arr[i] != i+1):
        x = arr[i]-1
        arr[i], arr[x] = arr[x], arr[i]
        print(arr)
        j += 1
    i += 1

print(arr)

ans = -1
for i in range(n):
    if arr[i] != i+1:
        ans = i + 1
        break
if ans != -1:
    print(ans)
else:
    print(-1)