import java.util.Arrays;

public class SubsetSum {
    public static void main(String[] args) {
        // Input: set of items and a sum
        int[] A = { 7, 3, 2, 5, 8 };
        int sum = 18;

        if (subsetSum(A, sum))
            System.out.println("Yes");
        else
            System.out.println("No");
    }

    public static boolean subsetSum(int[] arr, int sum) {
        int[][] dp = new int[arr.length + 1][sum + 1];
        for (int i = 0; i < arr.length + 1; i++) {
            for (int j = 0; j < sum + 1; j++) {
                if (j == 0)
                    dp[i][j] = 1;
                else if (i == 0)
                    dp[i][j] = 0;
                else {
                    dp[i][j] = dp[i - 1][j];
                    if (j >= arr[i])
                        dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - arr[i]]);
                }
            }
            if (dp[i][sum] == 1) {
                return true;
            }
        }
        return false;
    }
}
