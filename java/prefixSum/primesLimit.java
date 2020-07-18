package prefixSum;

import java.util.*;
import java.io.*;

public class primesLimit {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        String[] s = bf.readLine().split(" ");
        int[] arr = new int[n];

        for (int i = 0; i < n; ++i) {
            arr[i] = Integer.parseInt(s[i]);
        }

        List<Integer> primes = new ArrayList<Integer>();
        sieve(primes);
        
        List<Integer> primes_sum = new ArrayList<>();
        primes_sum.add(0);
        for (int i = 1; i < primes.size(); ++i) {
            primes_sum.add(primes_sum.get(i - 1) + primes.get(i - 1));
        }

        for (int i = 0; i < n; ++i) {
            System.out.print(helper(arr[i], primes, primes_sum) + " ");
        }
        System.out.println();
    }

    public static void sieve(List<Integer> primes) {
        int n = 1000000;
        boolean[] pr = new boolean[n];
        Arrays.fill(pr, true);
        int p = 2;
        
        while (p * p < n) {
            if (pr[p]) {
                for (int i = p * p; i < n; i += p) {
                    pr[i] = false;
                }
            }
            p += 1;
        }

        for (int i = 2; i < n; ++i) {
            if (pr[i]) {
                primes.add(i);
            }
        }
        
    }

    public static int helper(int limit, List<Integer> primes, List<Integer> primes_sum) {
        int max_prime = -1;
        int max_length = -1;
        for (int i = 0; primes.get(i) <= limit; ++i) {
            for (int j = 0; j < i; ++j) {
                int currSum = primes_sum.get(i) - primes_sum.get(j);

                if (currSum > limit) {
                    break;
                }
                if (Collections.binarySearch(primes, currSum) >= 0) {
                    if (i - j  + 1 > max_length) {
                        max_length = i - j + 1;
                        max_prime = currSum;
                    }
                }
            }
        }
        return max_prime;
    }

}