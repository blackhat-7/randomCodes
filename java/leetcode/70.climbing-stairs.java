/*
 * @lc app=leetcode id=70 lang=java
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int[] lookup = new int[n+1];
        lookup[1] = 1;
        lookup[2] = 2;

        for (int i=3; i<=n; ++i) {
            lookup[i] = lookup[i-1] + lookup[i-2];
        }

        return lookup[n];
    }
}
// @lc code=end

