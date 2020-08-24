import java.util.*;
import java.io.*;
import java.lang.*;

public class Codeforces {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    void dfs(HashMap<Integer,List<Integer>> graph, int u, boolean[] visited) {
        visited[u] = true;
        for (int v : graph.get(u)) {
            if (!visited[v])
                dfs(graph, v, visited);
        }
    }

    void solve1() throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        int i = 0, j = 0, k = 0;
        while (st.hasMoreTokens()) {
            arr[i++] = Integer.parseInt(st.nextToken());
        }
        if (arr[0] + arr[1] <= arr[n-1]) {
            System.out.println(1 + " " + 2 + " " + n);
            return;
        }
        System.out.println(-1);
    }
	
    public static void main (String[] args) throws IOException {
        Codeforces cf = new Codeforces();
        st = new StringTokenizer(br.readLine());
        long t = Long.parseLong(st.nextToken());
        while (t-- > 0) {
            cf.solve1();
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
