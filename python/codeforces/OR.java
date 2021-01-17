import java.util.*;

public class OR {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, q;
        int[] oddIndices;
        n = sc.nextInt();
        q = sc.nextInt();
        oddIndices = new int[n + 1];
        oddIndices[0] = 0;
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            oddIndices[i + 1] = (x % 2 == 0) ? oddIndices[i] : oddIndices[i] + 1;
        }

        for (int i = 0; i < q; i++) {
            int l = sc.nextInt();
            int r = sc.nextInt();
            if (oddIndices[r] != oddIndices[l])
                System.out.println(0);
            else
                System.out.println(1);
        }
        sc.close();
    }
}