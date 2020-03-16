import java.math.BigDecimal;
import java.util.*;

public class Tprime {
    
    public static boolean isPrime(long n) {
        if (n <= 1) { 
            return false;
        }
        if (n <= 3) { 
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
    
        long i = 5;
        while(i * i <= n) { 
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
            i += 6;
        }
    
        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigDecimal decimal;

        int n = sc.nextInt();
        long[] x = new long[n];
        for(int i=0; i<n; i++) {
            x[i] = sc.nextLong();
        }

        for(int i=0; i<n; i++) {
            decimal = new BigDecimal(Math.sqrt(x[i]));
            if(decimal.scale() <= 0 && isPrime(decimal.longValue()))
                System.out.println("YES");
            else
                System.out.println("NO");
        }
        sc.close();
    }
}