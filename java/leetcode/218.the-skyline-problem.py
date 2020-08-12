#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        stack = []
        res = []
        for b in buildings:
            if b[2] > stack[-1][1]:
                res += [b[0], b[1]]
            if b[1] < stack[-1][0]:
                stack += [b[1], b[2]]

# @lc code=end

