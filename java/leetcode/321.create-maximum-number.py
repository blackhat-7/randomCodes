#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#

# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        def memo(m, n, length):
            if m == -1 and n == -1:
                return None
            elif length == 1:
                return [ max(0 if m==-1 else max(nums1[:m+1]), 0 if n==-1 else max(nums2[:n+1])) ]
            
            digit = 0
            prefix = []
            for k in range(m+1):
                pre = memo(k-1, n, length-1)
                if pre and nums1[k] >= digit:
                    digit = nums1[k]
                    prefix = pre
            for k in range(n+1):
                pre = memo(m, k-1, length-1)
                if pre and nums2[k] >= digit:
                    digit = nums2[k]
                    prefix = pre

            return prefix + [digit] if prefix != [] else None

        return memo(m-1, n-1, k)

# @lc code=end

