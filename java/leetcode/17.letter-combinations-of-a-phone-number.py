#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from functools import lru_cache
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        if len(digits) == 0:
            return []

        @lru_cache(None)
        def helper(i):
            if i == len(digits):
                return [""]
            
            res = []
            suffix = helper(i+1)
            for char in nums[digits[i]]:
                for s in suffix:
                    res.append(char + s)
            return res

        return helper(0)

# @lc code=end

