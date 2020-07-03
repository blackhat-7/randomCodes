import java.util.*;

public class dsaLab3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i=0; i<n; ++i) {
            arr[i] = sc.nextInt();
        }

        int t = sc.nextInt();
        int index, val;
        for (int i=0; i<t; ++i) {
            val = sc.nextInt();
            index = binarySearch(arr, 0, n-1, val, n, -1);
            if (index!=-1) {
                int lowest = findLowest(arr, 0, index, val, index);
                int highest = findHighest(arr, index, n-1, val, index);
                System.out.println(highest-lowest+1);
            }
            else {
                System.out.println(-1);
            }
        }
        sc.close();
    }

    public static int binarySearch(int[] arr, int low, int high, int val, int lowest, int highest) {
        if (low>high) {
            return -1;
        }
        int mid = low + (high-low)/2;
        if (arr[mid] == val) {
            return mid;
        }
        if (val < arr[mid]) {
            return binarySearch(arr, low, mid-1, val, lowest, highest);
        }
        else {
            return binarySearch(arr, mid+1, high, val, lowest, highest);
        }
    }
    public static int findLowest(int[] arr, int low, int high, int val, int lowest) {
        if (high>=low) {
            int mid = low + (high-low)/2;
            if (arr[mid] == val) {
                lowest = (mid < lowest) ? mid : lowest;
                return findLowest(arr, low, mid-1, val, lowest);
            }
            if (val < arr[mid]) {
                return findLowest(arr, low, mid-1, val, lowest);
            }
            else {
                return findLowest(arr, mid+1, high, val, lowest);
            }
        }
        return lowest;
    }
    public static int findHighest(int[] arr, int low, int high, int val, int highest) {
        if (high>=low) {
            int mid = low + (high-low)/2;
            if (arr[mid] == val) {
                highest = (mid > highest) ? mid : highest;
                return findHighest(arr, mid+1, high, val, highest);
            }
            if (val < arr[mid]) {
                return findHighest(arr, low, mid-1, val, highest);
            }
            else {
                return findHighest(arr, mid+1, high, val, highest);
            }
        }
        return highest;
    }
}