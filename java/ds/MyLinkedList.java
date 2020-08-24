public class MyLinkedList {
    
    private Node head;

    public void add(int val) {
        if (head == null) {
            head = new Node(val, null);
        }
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = new Node(val, null);
    }

    public boolean removeByVal(int val) {
        if (head != null) {
            if (head.val == val ) {
                head = head.next;
                return true;
            }
            Node temp = head;
            while(temp.next != null && temp.next.val != val) {
                temp = temp.next;
            }
            if (temp.next != null) {
                temp.next = temp.next.next;
                return true;
            }
        }
        return false;
    }

    public boolean removeByIndex(int index) {
        if (head != null) {
            if (index == 0) {
                head = head.next;
                return true;
            }
            Node temp = head;
            while (temp.next != null && index != 1) {
                temp = temp.next;
                --index;
            }
            if (temp.next != null) {
                temp.next = temp.next.next;
                return true;
            }
        }
        return false;
    }

    public void print() {
        Node temp = head;
        while(temp != null) {
            System.out.print(temp.val + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        MyLinkedList ll = new MyLinkedList();
        ll.add(1);
        ll.add(5);
        ll.add(2);
        ll.add(3);
        ll.add(6);
        ll.print();
        ll.removeByVal(3);
        ll.print();
        ll.removeByIndex(2);
        ll.print();
    }

    class Node {
        protected int val;
        protected Node next;
        public Node(int val, Node next) {
            this.val = val;
            this.next = next;
        }
    }    
}