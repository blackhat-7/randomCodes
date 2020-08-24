arr = list(map(int, input().split(', ')))

lookup = [1]*len(arr)
for i in range(1, len(arr)):
    for j in range(i):
        diff = abs(arr[i]-arr[j])
        if diff == 0 or diff == 1:
            lookup[i] = max(lookup[i], lookup[j]+1)
print(max(lookup))








'''

{2, 5, 6, 3, 7, 6, 5, 8}


'''