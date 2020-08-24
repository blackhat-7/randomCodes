string = input()
length = len(string)+1

dp = [[0]*length for i in range(length)]

for i in range(length):
    for j in range(length):
        if i == 0 or j == 0:
            dp[i][j] = 0
        else:
            if string[i-1] == string[j-1] and i != j:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[length-1][length-1])