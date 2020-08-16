import java.io.*;

class SearchRotatedArray {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String[] s = br.readLine().split(" ");
            int[] arr = new int[n];
            for (int i=0; i<n; ++i) {
                arr[i] = Integer.parseInt(s[i]);
            }
            int k = Integer.parseInt(br.readLine());

            int low = 0, high = n-1, mid;
            while (low < high) {
                mid = low + (high-low)/2;
                if (arr[mid] > arr[high]) {
                    low = mid+1;
                } else {
                    high = mid;
                }
            }
            int realLow, realHigh;
            if (k > arr[n-1]) {
                realLow = 0;
                realHigh = low-1;
            } else {
                realLow = low;
                realHigh = n-1;
            }
            while (realLow < realHigh) {
                mid = realLow + (realHigh-realLow)/2;
                if (k > arr[mid]) {
                    realLow = mid+1;
                } else {
                    realHigh = mid;
                }
            }
            if (arr[realLow] == k) System.out.println(realLow);
            else System.out.println(-1);
        }
    }
}