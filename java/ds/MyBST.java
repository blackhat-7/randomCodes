import java.util.*;

public class MyBST<T extends Comparable <? super T>> {
    static class Node <T> {
        T data;
        Node<T> left;
        Node<T> right;
        public Node(T data) {
            this.data = data;
        }
    }

    Node<T> root;

    public MyBST() {
        this.root = null;
    }

    public void add(T data) {
        if (root == null) {
            root = new Node<T>(data);
            return;
        }
        addUtil(root, data);
    }

    public Node<T> addUtil(Node<T> root, T data) {
        if (root == null) {
            return new Node<T>(data);
        } else if (data.compareTo(root.data) <= 0) {
            root.left = addUtil(root.left, data);
        } else {
            root.right = addUtil(root.right, data);
        }
        return root;
    }

    public boolean remove(T data) {
        return removeUtil(root, data);
    }

    public boolean removeUtil(Node<T> root, T data) {
        if (root == null) {
            return false;
        } else if (data.compareTo(root.data) == 0) {
            return true;
        } else if (data.compareTo(root.data) < 0) {
            removeUtil(root.left, data);
        } else {
            removeUtil(root.right, data);
        }
        return false;
    }

    public void inOrder() {
        inOrderUtil(root);
        System.out.println();
    }
    public void inOrderUtil(Node<T> root) {
        if (root != null) {
            inOrderUtil(root.left);
            System.out.print(root.data + " ");
            inOrderUtil(root.right);
        }
    }

    public ArrayList<LinkedList<T>> getAllArrayLists() {
        return getAllArrayListsUtil(root);
    }

    public ArrayList<LinkedList<T>> getAllArrayListsUtil(Node<T> root) {
        ArrayList<LinkedList<T>> res = new ArrayList<>();
        if (root == null) {
            res.add(new LinkedList<>());
            return res;
        }

        ArrayList<LinkedList<T>> leftSeq = getAllArrayListsUtil(root.left);
        ArrayList<LinkedList<T>> rightSeq = getAllArrayListsUtil(root.right);
        
        LinkedList<T> prefix = new LinkedList<>();
        prefix.add(root.data);

        for (LinkedList<T> left : leftSeq) {
            for (LinkedList<T> right : rightSeq) {
                ArrayList<LinkedList<T>> temp = new ArrayList<>();
                weave(left, right, prefix, temp);
                res.addAll(temp);
            }
        }

        return res;
    }

    public void weave(LinkedList<T> left, LinkedList<T> right, LinkedList<T> prefix, ArrayList<LinkedList<T>> res) {
        
        if (left.size() == 0 || right.size() == 0) {
            LinkedList<T> temp = (LinkedList<T>) prefix.clone();
            temp.addAll(left);
            temp.addAll(right);
            res.add(temp);
            return;
        }

        T leftData = left.removeFirst();
        prefix.addLast(leftData);
        weave(left, right, prefix, res);
        prefix.removeLast();
        left.addFirst(leftData);

        T rightData = right.removeFirst();
        prefix.addLast(rightData);
        weave(left, right, prefix, res);
        prefix.removeLast();
        right.addFirst(rightData);
    }

    public void morrisInorderTraversal() {
        Node<T> current = root;
        while (current != null) {
            if (current.left == null) {
                System.out.print(current.data + " ");
                current = current.right;
            } else {
                Node<T> predecessor = current.left;
                while (predecessor.right != current && predecessor.right != null) {
                    predecessor = predecessor.right;
                }

                if (predecessor.right == null) {
                    predecessor.right = current;
                    current = current.left;
                } else {
                    predecessor.right = null;
                    System.out.print(current.data + " ");
                    current = current.right;
                }
            }
        }
    }

    public static void main(String[] args) {
        MyBST<Integer> bst = new MyBST<>();        
        bst.add(20);
        bst.add(50);
        bst.add(10);
        bst.add(25);
        bst.add(5);
        bst.add(15);
        bst.add(60);
        bst.add(70);
        bst.add(65);
        bst.add(80);
        bst.inOrder();
        bst.morrisInorderTraversal();
        // ArrayList<LinkedList<Integer>> ans = bst.getAllArrayLists();

        // for (LinkedList<Integer> temp : ans) {
        //     System.out.println(temp.toString());
        // }
    }
}