/*package whatever //do not write package name here */

import java.io.*;

class Gfg {
    static class Pair {
        long key, val;
        Pair(long key, long val) { this.key = key; this.val = val; }
    }

    int LAS(int[] arr, int n) {
        int countInc = 1;
        int lastInc = arr[0];
        int countDec = 1;
        int lastDec = arr[0];
        boolean inc_isInc = true;
        boolean dec_isInc = false;
        for (int i=5; i<n; i++) {
            if (arr[i] > lastInc && inc_isInc) {
                System.out.print(arr[i] + " ");
                lastInc = arr[i];
                inc_isInc = false;
                countInc++;
            } else if (arr[i] < lastInc && !inc_isInc) {
                System.out.print(arr[i] + " ");
                lastInc = arr[i];
                inc_isInc = true;
                countInc++;
            }

            if (arr[i] > lastDec && dec_isInc) {
                lastDec = arr[i];
                dec_isInc = false;
                countDec++;
            } else if (arr[i] < lastDec && !dec_isInc) {
                lastDec = arr[i];
                dec_isInc = true;
                countDec++;
            }
        }
        System.out.println();
        System.out.println(countInc + " " + countDec);
        return Math.max(countInc, countDec);
    }

	public static void main (String[] args) throws IOException {
        Gfg gfg = new Gfg();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long t = Long.parseLong(br.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String[] s1 = br.readLine().split(" ");
            int[] arr1 = new int[n];
            for (int i=0; i<n; i++) {
                arr1[i] = Integer.parseInt(s1[i]);
            }
            System.out.println(gfg.LAS(arr1, n));
            
        }
	}
}
/*
Input:
2
6
1 3 0 5 8 5
2 4 6 7 9 9
8
75250 50074 43659 8931 11273 27545 50879 77924
112960 114515 81825 93424 54316 35533 73383 160252

Output:
1 2 4 5
6 7 1
*/
