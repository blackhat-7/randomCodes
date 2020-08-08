import java.util.*;
import java.lang.*;
import java.io.*;

final class NthRoot {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int x = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());
            
            if (x == 0) { System.out.println(0); continue; }

            double epsilon = 0.0001, low = 1, high = x, mid = low + (high-low)/2;
            double err = Math.pow(mid, n) - x;

            while (Math.abs(err) >= epsilon) {
                if (err > epsilon) {
                    high = mid;
                } else {
                    low = mid;
                }
                mid = low + (high-low)/2;
                err = Math.pow(mid, n) - x;
            }

            System.out.println(mid);

        }
    }
}