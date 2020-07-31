#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        maps = collections.defaultdict(lambda: 0)
        for c in s:
            maps[c] += 1
        lst = [(maps[c], c) for c in maps]
        lst.sort(reverse=True)
        res = ""
        for item in lst:
            res += item[1]*(item[0])
        return res 
# @lc code=end

