
/*package whatever //do not write package name here */

import java.util.*;
import java.io.*;
import java.lang.*;

class Gfg {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    int dfs(int mat[][], int i, int j, int dp[][]) {
        if (i < 0 || j < 0 || j == mat.length) {
            return Integer.MAX_VALUE;
        }
        if (i == mat.length) {
            return 0;
        }
        if (dp[i][j] == -1) {
            int down = dfs(mat, i+1, j, dp);
            int left = dfs(mat, i+1, j-1, dp);
            int right = dfs(mat, i+1, j+1, dp);
            dp[i][j] = Math.min(down, Math.min(left, right)) + mat[i][j];
        }
        return dp[i][j];
    }

    String letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    List<String> helper(int arr[], int i, Map<Integer,List<String>> dp) {
        if (i == arr.length) {
            return new ArrayList<>(Arrays.asList(""));
        }
        if (arr[i]==0)
            return null;
        if (!dp.containsKey(i)) {
            List<String> res = new ArrayList<>();
            List<String> sing = helper(arr, i+1, dp);
            for (String s : sing) {
                res.add(letters.charAt(arr[i]-1) + s);
            }
            if (i+1<arr.length && 10*arr[i] + arr[i+1] >= 1 && 10*arr[i] + arr[i+1] <= 26) {
                List<String> doub = helper(arr, i+2, dp);
                char ch = letters.charAt(10*arr[i] + arr[i+1]-1);
                for (String s : doub) {
                    res.add(ch + s);
                }
            }
            dp.put(i, res);
        }
        return dp.get(i);
    }

    void solve() throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int arr[] = new int[n];
        int i = 0;
        while (st.hasMoreTokens()) {
            arr[i++] = Integer.parseInt(st.nextToken());
        }
        List<String> res = helper(arr, 0, new HashMap<Integer,List<String>>());
        for (String s : res)
            System.out.print(s + " ");
        System.out.println();
    }

	public static void main (String[] args) throws IOException {
        Gfg gfg = new Gfg();
        long t = Long.parseLong(br.readLine());
        while (t-- > 0) {
            gfg.solve();
        }
	}

    static class Tuple {
        int a, b, c;
        Tuple(int a, int b) { this.a = a; this.b = b;}
        Tuple(int a, int b, int c) { this.a = a; this.b = b; this.c = c; }
        
    }

    int gcd(int x, int y) {
        return (y == 0) ? x : gcd(y, x%y);
    }
}
