import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class MyGenericHeap<T extends Comparable<T>> {
    private List<T> heap;
    int size;
    public MyGenericHeap(int capacity) {
        this.heap = new ArrayList<>(capacity);
        this.size = 0;
    }

    public int left(int i) { return 2*i + 1; }
    public int right(int i) { return 2*i + 2; }
    public int parent(int i) { return (i-1)/2; }
    public T getMin() { return heap.get(0); }
    public void swap(int i, int j) {
        T temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }
    

    public void add(T key) {
        heap.add(key);
        int i = size++;
        while (heap.get(parent(i)).compareTo(heap.get(i)) > 0) {
            swap(i, parent(i));
            i = parent(i);
        }
    }

    public T extractMin() {
        if (size == 0) return null;
        if (size == 1) return heap.get(--size);
        T min = heap.get(0);
        size--;
        heap.set(0, heap.get(size));
        minHeapify(0);
        return min;
    }

    public void minHeapify(int i) {
        int min = i;
        int l = left(i);
        int r = right(i);
        if (l < size && heap.get(min).compareTo(heap.get(l)) > 1) {
            min = left(min);
        }
        if (r < size && heap.get(min).compareTo(heap.get(r)) > 1) {
            min = right(min);
        }
        if (min != i) {
            swap(min, i);
            minHeapify(min);
        }
    }
    
    @Override
    public String toString() {
        int i = 0, j = 0;
        StringBuilder heapStr = new StringBuilder();
        while (j < size) {
            heapStr.append(heap.get(j++) + " ");
            if (j == Math.pow(2, (i+1))-1) {
                heapStr.append("\n");
                i++;
            }
        }
        return heapStr.toString();
    }
    
    public static void main(String[] args) {
        MyGenericHeap<Integer> hp = new MyGenericHeap<>(32);
        Random r = new Random();
        for (int i=0; i<32; ++i) {
            hp.add(r.nextInt(100));
        }
        System.out.println(hp.toString());
        hp.extractMin();
        hp.extractMin();
        System.out.println(hp.toString());

    }

}





