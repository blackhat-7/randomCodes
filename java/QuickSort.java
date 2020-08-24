import java.util.*;

public class QuickSort {
    
    public static void main(String[] args) {
        int[] arr = {8,7,3,4,6,5,9,2,8,4,7,5,2,3,8,9,4,0,2};
        System.out.println(Arrays.toString(arr));
        System.out.println(quickSelect(arr, 0, arr.length, 5));
    }

    public static int partition(int[] arr, int low, int high) {
        Random random = new Random();
        int pivotIndex = random.nextInt(high-low) + low;
        int t = arr[low];
        arr[low] = arr[pivotIndex];
        arr[pivotIndex] = t;
        int pivot = arr[low];
        int i = low;
        int j = high;

        while(i < j) {
            do {
                i++;
            } while (i < high && arr[i] < pivot);
            do {
                j--;
            } while (j >= low && arr[j] > pivot);
            if (i < j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = pivot;
        arr[low] = arr[j];
        arr[j] = temp;
        return j;
    }

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int mid = partition(arr, low, high);
            quickSort(arr, low, mid);
            quickSort(arr, mid+1, high);
        }
    }

    public static int quickSelect(int[] arr, int low, int high, int rank) {
        if (low == high) return arr[low];
        int pivotIndex = partition(arr, low, high);
        if (rank == pivotIndex) {
            return arr[rank];
        } else if (rank < pivotIndex) {
            return quickSelect(arr, low, pivotIndex, rank);
        } else {
            return quickSelect(arr, pivotIndex+1, high, rank);
        }
    }
}