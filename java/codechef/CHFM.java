import java.util.*;

class CHFM {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int t = sc.nextInt();
        for(int j=0; j<t; j++) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            double total = 0;
            for(int i=0; i<n; i++) {
                arr[i] = sc.nextInt();
                total += arr[i];
            }
            double avg = total/n;
            double coin = total - avg*(n-1);
            boolean possible = false;
            for(int i=0; i<n; i++) {
                if ((double) arr[i] == coin) {
                    possible = true;
                    System.out.println(i+1);
                    break;
                }
            }
            if (!possible) {
                System.out.println("Impossible");
            }
        }
    }
}