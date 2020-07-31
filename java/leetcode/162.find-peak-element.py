#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        if high == 0:
            return high
        elif high == 1:
            return high if nums[high] > nums[low] else low

        while low <= high:
            mid = low + (high-low)//2
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
                return mid
            elif nums[mid] < nums[mid+1]:
                low = mid+1
            else:
                high = mid-1
        return low

        
# @lc code=end

'''
1 4 3 4 5 6 7

'''