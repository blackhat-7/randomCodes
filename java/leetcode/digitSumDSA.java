import java.util.*;

class digitSumDSA {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        long t = sc.nextInt();
        for(int i=0; i<t; ++i) {
            String s = sc.next();
            long len = s.length();
            long n = Long.parseLong(s);
            boolean ans = recursive(n, n, len, 0, len);
            if (ans) System.out.println("YES");
            else System.out.println("NO");
        }
    }

    public static boolean recursive(long original, long n, long len, long sum, long power) {
        if (len==1) {
            if (sum + Math.pow((n%10), power) == original) return true;
            else return false;
        }
        sum += Math.pow((n%10),power);
        if (sum == original) {
            return false;
        }
        return recursive(original, n/10, len-1, sum, power);
    }
}
