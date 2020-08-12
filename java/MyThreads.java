import java.lang.Runnable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class MyThreads {
    
    public static void main(String[] args) {
    
        // // 10 Threads 10 Tasks
        //     for (int i=0; i<10; ++i) {
        //         new Thread(new Task(i)).start();
        //     }

        // // 10 Threads 100 Tasks
        
        // ExecutorService exec = Executors.newFixedThreadPool(10);
        // for (int i=0; i<100; ++i) {
        //     exec.execute(new Task(i));
        // }

        // num of cores Threads 10 tasks
        int numOfCores = Runtime.getRuntime().availableProcessors();
        ExecutorService exec = Executors.newFixedThreadPool(numOfCores);
        for (int i=0; i<10; ++i) {
            exec.execute(new Task(i));
        }
        exec.shutdown();
        try {
            if (exec.awaitTermination(100, TimeUnit.MILLISECONDS)) {
                exec.shutdownNow();
            }
        } catch(InterruptedException e) {
            exec.shutdownNow();
        }
    }
}

class Task implements Runnable {
    private int taskNum;
    public Task(int num) {
        this.taskNum = num;
    }
    @Override
    public void run() {
        try {
            System.out.println("Performaing task : " + taskNum);
            Thread.sleep(5000);
        } catch (InterruptedException e) { }
        System.out.println("Task " + taskNum + " is complete.");
    }
}