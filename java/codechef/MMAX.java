import java.util.*;
import java.lang.Math;

class MMAX {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int t = sc.nextInt();
        for(int i=0; i<t; i++) {
            long n = sc.nextLong();
            long k = sc.nextLong();
            long num1 = 0;
            long num2 = 0;
            if (n>2) {
                if (n>=k) {
                    num1 = k;
                    num2 = n-num1;
                }
                else {
                    num1 = k%n;
                    num2 = n-num1;
                }
                
                long sum2 = 2 * Math.min(num1, num2);
                System.out.println(sum2);
            }
            else {
                System.out.println(k%2);
            }
        }
    }
}