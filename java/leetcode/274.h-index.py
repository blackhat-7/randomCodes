#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hindex = 0
        for i in range(1, len(citations)+1):
            if citations[i-1] >= i and (i == len(citations) or citations[i] <= i):
                hindex = i
        return hindex
'''
0 1 3 5 6
6 5 3 1 0

0 0 0 0 0

5 5 5 5 5
'''
# @lc code=end

