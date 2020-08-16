class MyBT {
    static class Node  {
        Node left = null, right = null;
        int val, countRight = 0;
        Node(int val) {
            this.val = val;
        }
    }

    Node root;
    MyBT() {
        root = null;
    }

    Node insert(Node root, int key, int[] count) {
        if (root == null) return new Node(key);
        else if (key < root.val) {
            root.left = insert(root.left, key, count);
            count[0] += root.countRight + 1;
        } else {
            root.right = insert(root.right, key, count);
            root.countRight++;
        }
        return root;
    }
}
public class countInversionBT {

    public static void main(String[] args) {
        int[] arr = {8, 5, 2, 1};
        int[] count = {0};
        MyBT bt = new MyBT();
        for (int i : arr) {
            bt.root = bt.insert(bt.root, i, count);
        }
        System.out.println(count[0]);
        
    }
}
