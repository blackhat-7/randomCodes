/*
 * @lc app=leetcode id=258 lang=java
 *
 * [258] Add Digits
 */

// @lc code=start
class Solution {
    public int addDigits(int num) {
        int sum;
        while (num >= 10) {
            sum = 0;
            while (num!=0) {
                sum += num%10;
                num /= 10;
            }
            num = sum;
        }
        return num;
    }
}
// @lc code=end

