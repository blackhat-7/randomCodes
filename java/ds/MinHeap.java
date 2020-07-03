import java.util.*;

public class MinHeap {
    private int[] harr;
    private int capacity;
    private int size;

    public MinHeap(int c) {
        this.harr = new int[c];
        this.capacity = c;
        this.size = 0;
    }
    // public MinHeap(int[] arr) {
    //     harr = arr;
    //     minHeapify(i)
    // }

    public static void main(String[] args) {
        MinHeap heap = new MinHeap(5);
        heap.add(5);
        heap.add(3);
        heap.add(1);
        heap.add(2);
        heap.add(3);
        heap.print();
        heap.decreaseKey(3, 0);
        heap.print();
        System.out.println(heap.extractMin());
        heap.print();
    }

    public int parent(int i) { return (i-1)/2; }
    public int left(int i) { return 2*i + 1; }
    public int right(int i) { return 2*i + 2; }

    public void swap(int i, int j) {
        int temp = harr[i];
        harr[i] = harr[j];
        harr[j] = temp;
    }

    public boolean add(int val) {
        if (size != capacity) {
            size++;
            int i = size - 1;
            harr[i] = val;
            while (harr[i] < harr[parent(i)]) {
                swap(i, parent(i));
                i = parent(i);
            }
            return true;
        }
        return false;
    }

    public boolean decreaseKey(int i, int val) {
        if (size != 0 || harr[i] < val) {
            harr[i] = val;
            while (harr[i] < harr[parent(i)]) {
                swap(i, parent(i));
                i = parent(i);
            }
            return true;
        }
        return false;
    }

    public int extractMin() {
        if (size != 0) {
            int min = harr[0];
            size--;
            harr[0] = harr[size];
            minHeapify(0);
            return min;
        }
        return Integer.MAX_VALUE;
    }

    public boolean minHeapify(int i) {
        if (i < size) {
            int smallest = i;
            int left = left(i);
            int right = right(i);
            if (left < size && harr[left] < harr[smallest]) {
                smallest = left;
            }
            if (right < size && harr[right] < harr[smallest]) {
                smallest = right;
            }
            if (smallest != i) {
                swap(i, smallest);
                minHeapify(smallest);
            }
            return true;
        }
        return false;
    }
    public void print() {
        for (int i=0; i<size; ++i) {
            System.out.print(harr[i] + " ");
        }
        System.out.println();
    }
}