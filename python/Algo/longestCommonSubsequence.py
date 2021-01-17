def lcs(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


def lcs_recursive(text1, text2, m, n, dp):
    if m == 0 or n == 0:
        return 0

    if (m, n) not in dp:
        dp[(m, n)] = 0
        if text1[m] == text2[n]:
            dp[(m, n)] = 1 + lcs_recursive(text1, text2, m-1, n-1, dp)
        dp[(m, n)] = max(dp[(m, n)], lcs_recursive(text1, text2, m-1, n, dp),
                         lcs_recursive(text1, text2, m, n-1, dp))
    return dp[(m, n)]


text1 = 'abcda'
text2 = 'cbcaa'

length = lcs_recursive(text1, text2, len(text1)-1, len(text2)-1, {})
print(length)

'''
  0 a b c d a
0 0 0 0 0 0 0
c 0 0 0 1 1 1
b 0 0 1 1 1 1
c 0 0 1 2 2 2
a 0 1 1 2 2 3
a 0 1 1 2 2 3
'''
