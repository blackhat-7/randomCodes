#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pointers = [0]*len(primes)
        res = [1]
        while n > 1:
            next, pr = float('inf'), [0]
            for i, p in enumerate(primes):
                if primes[i]*res[pointers[i]] <= next:
                    pr = pr + [i] if primes[i]*res[pointers[i]] == next else [i]
                    next = primes[i]*res[pointers[i]]
            for p in pr:
                pointers[p] += 1
            res.append(next)
            n -= 1
        return res[-1]

# @lc code=end

