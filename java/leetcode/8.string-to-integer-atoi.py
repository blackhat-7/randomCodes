#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
import math
class Solution:
    def myAtoi(self, str: str) -> int:
        int_max = 2147483648
        if type(str) == int:
            if str > int_max:
                return int_max
            elif str < -int_max:
                return -int_max
            return str
        str.lstrip()
        if str[0].isdigit() or str[0] == '+' or str[0] == '-':
            pos = True
            i = 0
            num = 0

            if str[0] == '-':
                pos = False
                i += 1
            elif str[0] == '+':
                i += 1
            
            j = i
            lenOfNum = 0
            while j < len(str) and str[j].isdigit():
                j += 1
                lenOfNum += 1
            
            if lenOfNum > 10:
                return 2147483648 if pos else -2147483648

            j = 0
            while j < lenOfNum:
                num += int(str[j]) * 10**(lenOfNum-j-1)
                j += 1

            if num > int_max:
                return int_max if pos else -int_max
            return num if pos else -num

        else:
            return 0
# @lc code=end

