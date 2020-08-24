import java.util.LinkedList;
import java.util.Queue;

public class Semaphores {
    
}

class BinarySemaphore {
    int status;
    Queue<Integer> waitingQueue;
    public BinarySemaphore() {
        this.status = 1;
        this.waitingQueue = new LinkedList<>();
    }

    public synchronized void P(int task) throws InterruptedException {
        if (this.status == 1) {
            status = 0;
        } else {
            waitingQueue.add(task);
            wait();
        }
    }

    public synchronized void V(int task) {
        if (waitingQueue.isEmpty()) {
            this.status = 1;
        } else {
            waitingQueue.poll();
            notify();
        }
    }
}