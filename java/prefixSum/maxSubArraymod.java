package prefixSum;

import java.util.*;
// import java.io.*;

public class maxSubArraymod {

    public static void main(String[] args) {
        int[] arr = {324,234,2,34,234,2,34,1,23,647,4,556,234,1,23,122,5,34,7,75};
        int m = 23423;

        System.out.println(maxSubArray(arr, m));

        // int[] arr2 = 
        // Set<Integer> s = new HashSet<>();
        // for (int i : arr2) {
        //     s.add(i);
        // }
        // for(int i : s) {
        //     System.out.print(i + " ");
        // }
        // System.out.println();
    }

    public static int maxSubArray(int[] arr, int m) {
        int prefix = 0, res = 0;
        Set<Integer> set = new HashSet<>();

        for (int num : arr) {
            prefix = (prefix + num) % m;

            res = Math.max(prefix, res);

            int it = 0;
            for (int i : set) {
                if (i >= prefix + 1 && (i < it)) {
                    it = i;
                }
            }

            if (it != 0) {
                res = Math.max(res, prefix - it + m);
            }
            set.add(prefix);
            System.out.println(set.toString());
        }

        return res;
    }
    
}