import java.util.*;

public class BST {

    private static class Node {
        Node left;
        Node right;
        int data;

        Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "data=" + data +
                    '}';
        }
    }

    private Node root;
    private int height;

    BST() {
        this.root = null;
        this.height = 0;
    }

    public static void main(String[] args) {
        BST bst = new BST();
        List<Integer> lst = new ArrayList<>(Arrays.asList(10, 5, 15, 7, 3, 20, 13));
        for (int data : lst) {
            bst.addNode(data);
        }
        int[] preorder = {10, 5, 3, 7, 15, 13, 20};
        int[] inorder = {3, 5, 7, 10, 13,15, 20};
        BST bst2 = new BST();
        bst2.root = bst.preorderInorderBT(preorder, inorder, 0, inorder.length-1);
        System.out.println(areTreesIdentical(bst.root, bst2.root));
    }

    public void addNode(int data) {
        this.root = addNodeHelper(this.root, data, 0);
    }

    private BST.Node addNodeHelper(Node root, int data, int height) {
        if (root == null) {
            if (height > this.height) {
                this.height = height;
            }
            return new BST.Node(data);
        } else if (data <= root.data) {
            root.left = addNodeHelper(root.left, data, height + 1);
        } else {
            root.right = addNodeHelper(root.right, data, height + 1);
        }
        return root;
    }

    public int removeNode(int data) {
        this.root = removeNodeHelper(this.root, data);
        return data;
    }

    private BST.Node removeNodeHelper(Node root, int data) {
        if (data < root.data) {
            root.left = removeNodeHelper(root.left, data);
        } else if (data > root.data) {
            root.right = removeNodeHelper(root.right, data);
        } else if (root.left == null && root.right == null) {
            return null;
        } else if (root.left == null) {
            return root.right;
        } else if (root.right == null) {
            return root.left;
        } else {
            Node temp = root.left;
            Node tempPrev = root;
            while (temp.right != null) {
                tempPrev = temp;
                temp = temp.right;
            }
            root.data = temp.data;
            tempPrev.right = removeNodeHelper(temp, temp.data);
        }
        return root;
    }

    public void inorder() {
        inorderHelper(this.root);
        System.out.println();
    }

    private void inorderHelper(Node node) {
        if (node != null) {
            inorderHelper(node.left);
            System.out.print(node.data + " ");
            inorderHelper(node.right);
        }
    }

    public void preorder() {
        preorderHelper(this.root);
        System.out.println();
    }

    private void preorderHelper(Node node) {
        if (node != null) {
            System.out.print(node.data + " ");
            preorderHelper(node.left);
            preorderHelper(node.right);
        }
    }

    public void levelorder() {
        if (this.root == null)
            return;
        Deque<BST.Node> q = new ArrayDeque<>();
        q.addLast(this.root);
        q.addLast(new BST.Node(Integer.MIN_VALUE));
        while (q.size() > 1) {
            Node n = q.pollFirst();
            if (n.data == Integer.MIN_VALUE) {
                System.out.println();
                q.addLast(new BST.Node(Integer.MIN_VALUE));
            } else {
                System.out.print(n.data + " ");
                if (n.left != null) {
                    q.addLast(n.left);
                }
                if (n.right != null) {
                    q.addLast(n.right);
                }
            }
        }
        System.out.println();
    }

    public int getHeight() {
        return height;
    }

    public void printLeftView() {
        Map<Integer, int[]> lookup = new HashMap<>();
        printLeftViewHelper(this.root, 0, 0, lookup);

        for (int y = 0; y <= this.height; y++) {
            System.out.println("Height " + y + ": " + lookup.get(y)[1]);
        }
        System.out.println();
    }

    private void printLeftViewHelper(Node node, int x, int y, Map<Integer, int[]> lookup) {
        if (node == null) {
            return;
        } else if (!lookup.containsKey(y) || x < lookup.get(y)[0]) {
            lookup.put(y, new int[] { x, node.data });
        }
        printLeftViewHelper(node.left, x - 1, y + 1, lookup);
        printLeftViewHelper(node.right, x + 1, y + 1, lookup);
    }

    public void printVertical() {
        Map<Integer, ArrayList<ArrayList<Integer>>> lookup = new HashMap<>();
        int[] minWidth = new int[] { 0 }, maxWidth = new int[] { 0 };
        this.printVerticalHelper(this.root, 0, 0, lookup, minWidth, maxWidth);
        for (int x = minWidth[0]; x <= maxWidth[0]; x++) {
            lookup.get(x).sort(Comparator.comparing(o -> o.get(0)));
            for (ArrayList<Integer> n : lookup.get(x)) {
                System.out.print(n.get(1) + " ");
            }
            System.out.println();
        }
    }

    private void printVerticalHelper(Node node, int x, int y, Map<Integer, ArrayList<ArrayList<Integer>>> lookup,
                                    int[] minWidth, int[] maxWidth) {
        if (node == null)
            return;
        if (!lookup.containsKey(x)) {
            ArrayList<ArrayList<Integer>> ar = new ArrayList<>();
            ar.add(new ArrayList<>(Arrays.asList(y, node.data)));
            lookup.put(x, ar);
        } else {
            lookup.get(x).add(new ArrayList<>(Arrays.asList(y, node.data)));
        }
        minWidth[0] = Math.min(x, minWidth[0]);
        maxWidth[0] = Math.max(x, maxWidth[0]);
        printVerticalHelper(node.left, x - 1, y + 1, lookup, minWidth, maxWidth);
        printVerticalHelper(node.right, x + 1, y + 1, lookup, minWidth, maxWidth);
    }

    public Node getAncestor(int data1, int data2) {
        return getAncestorHelper(this.root, data1, data2);
    }

    private Node getAncestorHelper(Node node, int data1, int data2) {
        if (node == null) {
            return null;
        } else if ((data1 < node.data && data2 > node.data) || data1 == node.data || data2 == node.data) {
            return node;
        }
        return (data1 < node.data) ? getAncestorHelper(node.left, data1, data2) : getAncestorHelper(node.right, data1, data2);
    }

    public Node getNextNodeOnSameLevel(int data) {
        return this.getNextNodeOnSameLevelHelper(this.root, data, 0, new int[] {0});
    }

    public Node getAncestorBT(int data1, int data2) {
        return this.getAncestorBTHelper(this.root, data1, data2);
    }

    private Node getAncestorBTHelper(Node node, int data1, int data2) {
        if (node == null)
            return null;
        if (node.data == data1 || node.data == data2)
            return node;
        Node left = getAncestorBTHelper(node.left, data1, data2);
        Node right = getAncestorBTHelper(node.right, data1, data2);
        if (left == null)
            return right;
        if (right == null)
            return left;
        return node;
    }

    private boolean searchNodeBT(Node node, int data) {
        if (node == null)
            return false;
        return this.searchNodeBT(node.left, data) || this.searchNodeBT(node.right, data);
    }

    private Node getNextNodeOnSameLevelHelper(Node node, int data, int currentLevel, int[] nodeLevel) {
        Node n = null;
        if (node != null) {
            if (currentLevel == nodeLevel[0]) {
                return node;
            }
            if (node.data == data)
                nodeLevel[0] = currentLevel;
            n = getNextNodeOnSameLevelHelper(node.left, data, currentLevel, nodeLevel);
            if (n == null)
                n = getNextNodeOnSameLevelHelper(node.right, data, currentLevel, nodeLevel);
        }
        return n;
    }

    public LinkedList<Node> getAncestorsBT(int data) {
        return this.getAncestorsBTHelper(this.root, data, new LinkedList<>());
    }

    private LinkedList<Node> getAncestorsBTHelper(Node node, int data, LinkedList<Node> ancestors) {
        if (node == null)
            return null;
        ancestors.addLast(node);
        if (node.data == data)
            return new LinkedList<>(ancestors);
        LinkedList<Node> path = getAncestorsBTHelper(node.left, data, ancestors);
        if (path == null)
            path = getAncestorsBTHelper(node.right, data, ancestors);
        ancestors.removeLast();
        return path;
    }

    public static boolean areTreesIdentical(Node root1, Node root2) {
        if (root1 == null && root2 == null)
            return true;
        if (root1.data == root2.data) {
            return areTreesIdentical(root1.left, root2.left) && areTreesIdentical(root1.right, root2.right);
        }
        return false;
    }

    public boolean isCompleteBT() {
        Queue<Node> q = new LinkedList<>(Arrays.asList(root, null));
        while (q.size() > 1) {
            Node n = q.poll();
            if (n == null)
                q.add(null);
            else {
                if (n.data == Integer.MIN_VALUE) {
                    if (q.peek() != null && q.peek().data != Integer.MIN_VALUE)
                        return false;
                    continue;
                }
                q.add(n.left == null ? new Node(Integer.MIN_VALUE) : n.left);
                q.add(n.right == null ? new Node(Integer.MIN_VALUE) : n.right);
            }
        }
        return true;
    }

    public Node convertToMirrorBT(Node node) {
        if (node == null)
            return null;
        Node curr = new Node(node.data);
        curr.left = convertToMirrorBT(node.right);
        curr.right = convertToMirrorBT(node.left);
        return curr;
    }

    public Node preorderInorderBT(int[] preorder, int[] inorder, int low, int high) {
        if (low > high)
            return null;
        Node node = new Node(0);
        int mid = 0;
        HashSet<Integer> in = new HashSet<>();
        for (int i=low; i<=high; i++) {
            in.add(inorder[i]);
        }
        for (int i=0; i<preorder.length; i++) {
            if (in.contains(preorder[i])) {
                node.data = preorder[i];
                mid = Arrays.binarySearch(inorder, preorder[i]);
                break;
            }
        }
        node.left = preorderInorderBT(preorder, inorder, low, mid-1);
        node.right = preorderInorderBT(preorder, inorder, mid+1, high);
        return node;
    }
}
