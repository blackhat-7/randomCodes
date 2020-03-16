package JRM;
import java.util.*;


class LinkedList {
    LNode head;
    LinkedList(int m) {
        head = null;
    }

    class LNode {
        int key;
        LNode next;
        LNode(int k) {
            key = k;
            next = null;
        }
    }
    
    void add(int v) {
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
    
    void delete(int x) {
        int c = 1;
        LNode temp = head;
        if (x==1) {
            head = head.next;
        }
        else {
            while(temp!=null && c!=x-1) {
                temp = temp.next;
                c++;
            }
            if (temp.next!=null) {
                temp.next = temp.next.next;
            }
            else {
                temp.next = null;
            }
        }
        if(temp.next==null) {
            System.out.println(head.key);
        }
        else {
            System.out.println(temp.next.key);
        }
    }

    void print() {
        LNode temp = head;
        while(temp != null) {
            System.out.print(temp.key + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        for(int i=0; i<t; i++) {
            int n = sc.nextInt();
            LinkedList l = new LinkedList(n);
            for(int j=0; j<n; j++) {
                l.add(sc.nextInt());
            }
            int x = sc.nextInt();
            if (x>n) {
                System.out.println("Invalid Input!");
            }
            else if (x==0) {
                System.out.println("False");
                System.out.println(0);
                l.print();
            }
            else {
                System.out.println("True");
                l.delete(x);
                l.print();
            }
        }
        sc.close();
    }
}