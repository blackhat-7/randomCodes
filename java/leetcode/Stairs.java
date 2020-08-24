import java.util.*;

class Stairs{
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int n = sc.nextInt();
        int c;
        if (n==0) c = 0;
        else c = countWays(n);
        System.out.println(c);
    }

    public static int countWays(int n) {
        if (n==0) {
            return 1;
        }
        if (n<0) {
            return 0;
        }
        return countWays(n-1) + countWays(n-2) + countWays(n-3);
    }

}
