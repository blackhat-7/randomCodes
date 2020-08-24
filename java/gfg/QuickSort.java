import java.util.*;

public class QuickSort {

    static class Pair {
        int x, y;
        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void swap(int[] arr, int low, int high) {
        int temp = arr[high];
        arr[high] = arr[low];
        arr[low] = temp;
    }
    
    public static int hoare(int[] arr, int low, int high) {
        int pivot = arr[low];
        int i = low-1, j = high+1;

        while(true) {
            do {
                i++;
            } while(arr[i] < pivot);
            do {
                j--;
            } while(arr[j] > pivot);
            if (i >= j) {
                return j;
            }
            swap(arr, i, j);
        }
    }

    public static int lomuto(int[] arr, int low, int high) {
        int pivot = arr[high];
        int pivotIndex = low;

        for (int i=low; i<high; ++i) {
            if (arr[i] <= pivot) {
                swap(arr, i, pivotIndex++);
            }
        }
        swap(arr, pivotIndex, high);
        return pivotIndex;
    }

    public static void sort(int[] arr, int low, int high) {
        Stack<Pair> stack = new Stack<>();
        stack.push(new Pair(low, high));

        while (!stack.empty()) {
            Pair p = stack.pop();
            if (p.x < p.y) {
                int pivot = hoare(arr, p.x, p.y);
                stack.push(new Pair(p.x, pivot));
                stack.push(new Pair(pivot+1, p.y));
            }
        }
    }

    public static void main(String[] args) {
        int n = 10;
        int[] arr = new int[n];
        Random rand = new Random();
        for (int i=0; i<n; ++i) {
            arr[i] = rand.nextInt(100);
        }
        
        sort(arr, 0, arr.length-1);
        System.out.println(Arrays.toString(arr));

    }
}
