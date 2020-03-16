import java.util.*;

class LinkedList {
    static LNode  head;
    static int size = 0;
    LinkedList(int v) {
        size++;
        LNode new_node = new LNode(v); 

        if (head == null) 
        { 
            head = new LNode(v); 
            return; 
        } 
        new_node.next = null; 

        LNode last = head;  
        while (last.next != null) 
            last = last.next; 
        last.next = new_node; 
        return;
    }

    LinkedList(LNode new_node) {
        size++;
        if (head == null) 
        { 
            head = new_node;
            return; 
        } 
        new_node.next = null; 

        LNode last = head;  
        while (last.next != null) 
            last = last.next; 
        last.next = new_node; 
        return;
    }
    

    static class LNode {
        int key;
        LNode next;
        LNode(int k) {
            key = k;
            next = null;
        }
    }

    void swap(LNode x) {
        int a = x.key;
        int b = x.next.key;
        x.key = b;
        x.next.key = a;
    }
    void sort() {
        LNode temp = head;
        for(int i=0; i<size; i++) {
            for(int j=1; j<size; j++) {
                if (temp.key>temp.next.key) {
                    swap(temp);
                }
                temp = temp.next;
            }
            temp = head;
        }
    }

    void display() {
        LNode temp = head;
        while(temp!=null) {
            System.out.print(temp.key + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    void find() {
        LNode temp = head;
        System.out.print(temp.key + " ");
        while(temp.next!=null) {
            temp = temp.next;
        }
        System.out.println(temp.key);
    }

    public static void main(String[] args) {
        LinkedList ll = new LinkedList(5);
        ll = new LinkedList(4);
        ll = new LinkedList(3);
        ll = new LinkedList(2);
        ll = new LinkedList(1);

        ll = new LinkedList(new LNode(10));
        ll = new LinkedList(new LNode(9));
        ll = new LinkedList(new LNode(8));
        ll = new LinkedList(new LNode(7));
        ll = new LinkedList(new LNode(6));

        ll.display();
        ll.sort();
        ll.display();
        ll.find();

    }
}