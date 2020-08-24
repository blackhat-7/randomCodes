package prefixSum;

import java.io.*;

public class MaxSubarraySumLessK {
    public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int n = Integer.parseInt(s[0]), k = Integer.parseInt(s[1]);
		
		s = br.readLine().split(" ");
		int[] arr = new int[n];
		int[] prefixSum = new int[n];
		
		for (int i = 0; i < n; ++i) {
		    arr[i] = Integer.parseInt(s[i]);
		    if (i > 0)
		        prefixSum[i] = arr[i] + prefixSum[i-1];
		    else
		        prefixSum[i] = arr[i];
		}
		
		int min = 0, max = n, mid, ans = 0;
		
		while (min <= max) {
		    mid = min + (max - min) / 2;
		    
		    boolean flag = true;
		    for (int i = mid; i < n; ++i) {
		        if (prefixSum[i] - prefixSum[i - mid] > k) {
		            flag = false;
		            break;
		        }
		    }
		    
		    if (flag) {
		        min = mid + 1;
		        ans = mid;
		    } else {
		        max = mid - 1;
		    }
		}
		System.out.println(ans);
	}
}
