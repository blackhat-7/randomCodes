#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack, prev_sign, curr_num, power, n = [], '+', 0, 0, len(s)

        for op in s:
            if op != ' ':
                if op.isdigit():
                    curr_num += int(op) * 10**power
                    power += 1
                else:
                    if prev_sign == '+':
                        stack.append(curr_num)
                    elif prev_sign == '-':
                        stack.append(-curr_num)
                    elif prev_sign == '*':
                        stack[-1] = stack[-1] * curr_num
                    else:
                        stack[-1] = int(stack[-1] / curr_num)
                    prev_sign = op
                    power = 0
                    curr_num = 0
        if prev_sign == '+':
            stack.append(curr_num)
        elif prev_sign == '-':
            stack.append(-curr_num)
        elif prev_sign == '*':
            stack[-1] = stack[-1] * curr_num
        else:
            stack[-1] = int(stack[-1] / curr_num)
        return sum(stack)

        
# @lc code=end

