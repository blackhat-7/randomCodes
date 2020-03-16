import java.util.*;
import java.math.BigInteger;

class Compress {

    static void prime(BigInteger x) {
        BigInteger i = BigInteger.TWO;
        String ans = "";

        while(x.compareTo(BigInteger.ONE)==1) {
            if (x.mod(i)==BigInteger.ZERO) {
                ans += i.toString()+"*";
                x = x.divide(i);
            }
            else {
                if (i==BigInteger.TWO) {
                   i = i.add(BigInteger.ONE);
                }
                else {
                   i = i.add(BigInteger.TWO);
                }
            }
        }
        ans = ans.substring(0, ans.length()-1);
        System.out.println(ans);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        BigInteger n = BigInteger.valueOf(s.length());
        prime(n);
    }
}