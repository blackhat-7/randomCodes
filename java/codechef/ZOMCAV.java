package codechef;

import java.util.*;

class ZOMCAV {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int t = sc.nextInt();
        for(int i=0; i<t; i++) {
            int n = sc.nextInt();
            int[] c = new int[n];
            int[] h = new int[n];
            int[] x = new int[n];
            
            for(int j=0; j<n; j++) {
                c[j] = sc.nextInt();
            }
            for(int j=0; j<n; j++) {
                h[j] = sc.nextInt();
            }
            System.out.println(Arrays.toString(c));
            for(int j=0; j<n; j++) {
                int l = (j-c[j]>=0) ? c[j] : 0;
                int r = (j+c[j]<=n-1) ? c[j] : n-1;
                System.out.println(r);
                for(int k=l; k<=r; k++) {
                    x[k]++;
                }
            }
            Arrays.sort(x);
            Arrays.sort(h);
            System.out.println(Arrays.toString(x));
            if(x==h) {
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }
            
        }
    }
}