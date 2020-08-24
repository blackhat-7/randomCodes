#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#

# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        def helper(i, target):
            if i < 0:
                return [""] if target == 0 else []
            res = []
            digit = int(num[i])

            addPrefix = helper(i-1, target-digit)
            for prefix in addPrefix:
                res += [prefix + "+" + str(digit)] if prefix != "" else [str(digit)]

            subPrefix = helper(i-1, target+digit)
            for prefix in subPrefix:
                res += [prefix + "-" + str(digit)] if prefix != "" else [str(digit)]

            proPrefix = helper(i-1, target/(digit))
            print(proPrefix)
            for prefix in proPrefix:
                res += [prefix + "*" + str(digit)] if prefix != "" else [str(digit)]
            return res

        return helper(len(num)-1, target)

# @lc code=end

