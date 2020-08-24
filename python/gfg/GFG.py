def helper(arr, n, m, dp):
    if n<0:
        return 0
    key = (n,m)
    if key not in dp:
        a = helper(arr, n-2, m, dp)
        b = helper(arr, n-3, m, dp)
        dp[key] = max(a,b) + (arr[n] if n<m else 0)
    return dp[key]

t = int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    
    print(helper(arr, n+1, n, {}))






'''
Input:
2
6
5 5 10 100 10 5
3
1 2 3
Output:
110
4
'''