/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {

    public static long merge(int[] arr, int low, int mid, int high) {
        long count = 0;
        int i = low, j = mid+1, k = 0;
        int[] merged = new int[high-low+1];

        while (j <= high) {
            while (i <= mid && arr[i] <= arr[j]) {
                merged[k++] = arr[i++];
            }
            count += mid-i+1;
            merged[k++] = arr[j++];
        }
        while (i <= mid) {
            merged[k++] = arr[i++];
        }
        
        for(i=0, j = low; i<high-low+1; ++i, ++j) {
            arr[j] = merged[i];
        }
    
        return count;
    }

    public static long divide(int[] arr, int low, int high) {
        if (low >= high) {
            return 0;
        }
        int mid = low + (high - low)/2;
        long left = divide(arr, low, mid);
        long right = divide(arr, mid+1, high);
        long m = merge(arr, low, mid, high);
        return left + right + m;

    }
	public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String[] s = br.readLine().split(" ");
            int[] arr = new int[n];
            for (int i=0; i<n; ++i) {
                arr[i] = Integer.parseInt(s[i]);
            }

            System.out.println(divide(arr, 0, n-1));
        }
	}
}