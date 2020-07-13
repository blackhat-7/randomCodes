package OOP;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ArraySum implements Runnable {
    int[] arr;
    int sum, low, high;
    public ArraySum(int[] arr, int low, int high) {
        this.sum = 0;
        this.arr = arr;
        this.low = low;
        this.high = high;
    }
    public void serialSum() {
        for (int i=low; i<high; ++i) {
            sum += arr[i];
        }
    }
    public int getSum() { return sum;}
    public void run() {
        serialSum();
    }

    public static void main(String[] args) throws InterruptedException{
        int n = 10;
        int ans = 0;
        int[] arr = new int[n];
        for (int i=0; i< n; ++i) {
            arr[i] = i;
            ans += i;
        }
        ArraySum left = new ArraySum(arr, 0, n/2);
        ArraySum right = new ArraySum(arr, n/2, n);
        Thread t1 = new Thread(left);
        Thread t2 = new Thread(right);
        t1.start(); t2.start();
        t1.join(); t2.join();
        int result = left.getSum() + right.getSum();
        System.out.println(result + " " + ans);

        ExecutorService exec = Executors.newFixedThreadPool(2);
        exec.execute(left); exec.execute(right);
        if (!exec.isTerminated()) {
            exec.shutdown();
            exec.awaitTermination(5L, TimeUnit.SECONDS);
        }
        System.out.println(left.getSum() + right.getSum() + " " + ans);
    }
}