/*
 * @lc app=leetcode id=871 lang=java
 *
 * [871] Minimum Number of Refueling Stops
 */

// @lc code=start
class Solution {
    public int minRefuelStops(int t, int sf, int[][] s) {
        long[] dp = new long[s.length + 1];
        dp[0] = sf;

        for (int i=0; i<=s.length; i++) {
            for (int j=i; j >= 0 && s[i][0] <= dp[j] ; j--) {
                dp[j+1] = Math.max(dp[j+1], dp[j] + s[i][1]);
            }
        }
        System.out.println(dp.toString());
        return 0;
        
    }

    /*
    
    
    */

}
// @lc code=end

