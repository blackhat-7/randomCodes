arr = list(map(int, input().split()))
# low = 1
# seq = []
# for i in range(1, len(arr)):
#     if ((low and arr[i] > arr[i-1]) or (not low and arr[i] < arr[i-1])):
#             seq.append(arr[i-1])
#             low = not low
# if (low and arr[len(arr)-1]<seq[len(seq)-1]) or (not low and arr[len(arr)-1]>seq[len(seq)-1]):
#     seq.append(arr[len(arr)-1])
# print(seq)

dp = [1]*len(arr)
for i in range(len(arr)):
    for j in range(i):
        if (dp[j]%2==1 and arr[i] > arr[j]) or (dp[j]%2==0 and arr[i] < arr[j]):
            dp[i] = max(dp[i], dp[j]+1)
        print(dp)
# print(dp)