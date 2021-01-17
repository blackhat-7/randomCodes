public class MyLinkedList {
    private class Node {
        private Node next;
        private Node prev;
        private int data;

        public Node getNext() {
            return next;
        }

        public void setNext(Node next) {
            this.next = next;
        }

        public Node getPrev() {
            return prev;
        }

        public void setPrev(Node prev) {
            this.prev = prev;
        }

        public int getData() {
            return data;
        }

        public void setData(int data) {
            this.data = data;
        }

        public Node(int data) {
            this.data = data;
        }
    }

    private Node head;

    public MyLinkedList(Node head) {
        this.head = head;
    }

    public static void main(String[] args) {

    }

    public void addNode(int data) {
        if (this.head == null)
            this.head = new Node(data);
        Node p = this.head;
        while (p.next != null) {
            p = p.next;
        }
        p.next = new Node(data);
    }

    public void removeNode(int data) {
        if (this.head == null)
            return;
        Node p = this.head;
        while (p.next != null || p.next.data != data) {
            p = p.next;
        }
        if (p.next != null) {
            p.next = p.next.next;
        }
    }
}
