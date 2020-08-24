import java.util.*;


public class SieveOfEratosthenese {
    public static void main(String[] args) {
        int n = 50;

        boolean[] primes = new boolean[n];
        Arrays.fill(primes, true);
        int p = 2;

        while (p*p < n) {
            if (primes[p]) {
                for (int i=p*p; i<n; i += p) {
                    primes[i] = false;
                }
            }
            ++p;
        }

        for (int i=2; i<n; ++i) {
            if (primes[i]) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }
}