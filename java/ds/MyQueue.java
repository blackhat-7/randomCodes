// package ds;

import java.util.NoSuchElementException;
import java.util.Queue;

public class MyQueue<T> {

    private static class QueueNode<T> {
        private T data;
        private QueueNode<T> next;
        public QueueNode(T data) {
            this.data = data;
        }
    }

    private QueueNode<T> first;
    private QueueNode<T> last;

    public boolean isEmpty() { return first == null; }

    public T peek() {
        if (first == null)
            throw new NoSuchElementException();
        return first.data;
    }

    public void add(T data) {
        QueueNode<T> new_node = new QueueNode<T>(data);
        if (last != null)
            last.next = new_node;
        last = new_node;
        if (first == null) 
            first = new_node;
    }

    public T remove() {
        if (first == null) 
            throw new NoSuchElementException();
        T data = first.data;
        first = first.next;
        if (first == null)
            last = null;
        return data;
    }
    
    public static void main(String[] args) {
        MyQueue<Integer> q = new MyQueue<>();
        q.add(5);
        q.add(2);
        q.add(7);
        System.out.println(q.peek());
        q.remove();
        System.out.println(q.peek());
        q.remove();
        System.out.println(q.isEmpty());
        q.remove();
        System.out.println(q.isEmpty());
        // q.remove();
    }

}