import java.util.*;

class CoinChange {
    public static void main(String[] args) {
        // n coins of given denominations
        int[] S = { 1, 3, 5, 7 };

        // Total Change required
        int N = 8;

        // create a map to store solutions of subproblems
        Map<String, Integer> lookup = new HashMap<>();

        System.out.print("Total number of ways to get desired change is " + count(S, S.length - 1, N, lookup));
    }

    public static int count(int[] denoms, int i, int n, Map<String, Integer> dp) {
        if (i < 0 || n < 0) {
            return 0;
        } else if (n == 0) {
            return 1;
        }
        String key = i + "|" + n;
        if (!dp.containsKey(key)) {
            int with = count(denoms, i, n - denoms[i], dp);
            int skip = count(denoms, i - 1, n, dp);
            dp.put(key, with + skip);
        }
        return dp.get(key);
    }
}
