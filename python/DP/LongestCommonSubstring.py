string1 = input()
string2 = input()

len1 = len(string1)
len2 = len(string2)

dp = [[0]*(len2+1) for i in range(len1+1)]
length_of_max_substring = 0
end_index = 0

# Fill DP
for i in range(len1+1):
    for j in range(len2+1):
        if i != 0 and j != 0:
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > length_of_max_substring:
                    length_of_max_substring = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

print("Length:", length_of_max_substring)
print("Substring:", string1[end_index - length_of_max_substring : end_index + 1])
