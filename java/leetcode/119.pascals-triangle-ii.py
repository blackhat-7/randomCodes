#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [0]*(rowIndex+1)
        for i in range(rowIndex+1):
            res[i] = math.comb(rowIndex, i)
        return res
# @lc code=end

'''
1 1 2 3 5 8
'''