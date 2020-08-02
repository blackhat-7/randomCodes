#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    flag = 1
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z: return False
        if x == z or y == z or x + y == z: return True
        while y:
            x, y = y, x%y
        return z%x == 0
'''
3 5 4
x y
3 0
0 3
3 3
1 5
1 0
0 1
3 1
0 4


i j
max(0,j+i-y)  min(y, j+i)


1 2 3
x y


'''

# @lc code=end

