#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        n, total = len(A), sum(A)
        currSum = maxSum = sum(a*i for i, a in enumerate(A))
        for i in range(n-1):
            currSum = currSum - total + A[i]*(n)
            maxSum = max(maxSum, currSum)
        return maxSum
        

# @lc code=end

