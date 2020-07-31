#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countP, countS = [0]*256, [0]*256
        lenP, res = len(p), []
        length = start = end = 0

        for c in p:
            countP[ord(c)] += 1

        while end < len(s):
            countS[ord(s[end])] += 1
            if countS[ord(s[end])] <= countP[ord(s[end])]:
                length += 1
            if length == lenP:
                while countS[ord(s[start])] > countP[ord(s[start])] or countP[ord(s[start])] == 0:
                    if countP[ord(s[start])] != 0:
                        countS[ord(s[start])] -= 1
                    start += 1
                if end - start + 1 == lenP:
                    res.append(start)
            end += 1
        
        return res
# @lc code=end

