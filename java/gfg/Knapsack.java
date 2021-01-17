public class Knapsack {
    public static void main(String[] args) {
        // Input: set of items each with a weight and a value
        int[] v = { 20, 5, 10, 40, 15, 25 };
        int[] w = { 1, 2, 3, 8, 7, 4 };

        // Knapsack capacity
        int W = 10;

        System.out.println("Knapsack value is " + knapSack(v, w, W));
    }

    public static int knapSack(int[] values, int[] weights, int cap) {
        int[][] dp = new int[values.length + 1][cap + 1];
        for (int i = 1; i < values.length + 1; i++) {
            for (int j = 1; j < cap + 1; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j >= weights[i - 1]) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - weights[i - 1]] + values[i - 1]);
                }
            }
        }
        return dp[values.length][cap];
    }
}
