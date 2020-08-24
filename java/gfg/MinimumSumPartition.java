import java.util.*;

class MinimumSumPartition {
    public static void main(String[] args) {
        int[] arr = {10, 20, 15, 5, 25};
        int sum = Arrays.stream(arr).sum();
        int n = arr.length;
        boolean[][] dp = new boolean[n+1][sum+1];

        for (int i=0; i<n+1; ++i) {
            dp[i][0] = true;
            for (int j=1; i>0 && j<sum+1; ++j) {
                dp[i][j] = dp[i-1][j];
                if (arr[i-1] <= j) {
                    dp[i][j] |= dp[i-1][j-arr[i-1]];
                }
            }
        }
        int i = sum/2;
        while (i >= 0 && !dp[n-1][i]) i--;
        System.out.println(sum - 2*i);
    }
}
