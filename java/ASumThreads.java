import java.util.*;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;

public class ASumThreads implements java.lang.Runnable {
    
    private int[] array;
    private int sum, low, high;
    
    public ASumThreads(int[] a, int l, int h) {
        array = a; sum = 0; low = l; high = h;
    }
    public static void main(String[] args ) throws InterruptedException {
        int[] array = {1, 2, 3, 4, 5};
        ExecutorService exec = Executor.newFixedThreadPool(2);
        ASumThreads left = new ASumThreads(array, 0, array.length/2);
        ASumThreads right = new ASumThreads(array, array.length/2, array.length);
        exec.execute(left); exec.execute(right);

        if(!exec.isTerminated()) {
            exec.shutdown();
            exec.awaitShutdown(5L, TimeUnit.SECONDS);
        }
        
        System.out.println(left.getSum()+right.getSum());
    }

    @Override
    public void run() {
        for(int i=low; i<high; i++) {
            sum +=array[i];
        }
    }

    public int getSum() {
        return sum;
    }
}