#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = [1] + nums + [1]
        lookup = [[0]*len(nums) for _ in range(len(nums))]
        def helper(i, j):
            if lookup[i][j] or j-i == 1:
                return lookup[i][j]
            count = 0
            for k in range(i+1, j):
                count = max(count, nums[i]*nums[k]*nums[j] + helper(i, k) + helper(k, j))
            lookup[i][j] = count
            return count

        return helper(0, len(nums)-1)
'''

2 4
'''
# @lc code=end

