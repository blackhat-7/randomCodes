#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        lst, end = collections.deque(), 0
        for i, n in enumerate(nums):
            if i == 0 or nums[i-1] != n-1:
                if i != 0 and end != int(lst[-1]):
                    lst[-1] = lst[-1] + '->' + str(end)
                lst.append(str(n))
                end = n
            else:
                end += 1
                if i == len(nums)-1:
                    lst[-1] = lst[-1] + '->' + str(end)
        
        return lst
# @lc code=end

