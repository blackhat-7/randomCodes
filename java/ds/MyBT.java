import java.util.*;

class MyBT {
    Node root;
    void add(int key) {
        root = addUtil(root, key);
    }
    Node addUtil(Node root, int key) {
        if (root == null) return new Node(key);
        if (key < root.data) {
            root.left = addUtil(root.left, key);
        } else {
            root.right = addUtil(root.right, key);
        }
        return root;
    }
    
    void inorder() {
        System.out.println("Inorder: ");
        inorderRecur(root);
        System.out.println();
        inorderIter();
    }
    void inorderRecur(Node node) {
        if (node != null) {
            inorderRecur(node.left);
            System.out.print(node.data + " ");
            inorderRecur(node.right);
        }
    }
    void inorderIter() {
        Node curr = root;
        while (curr != null) {
            if (curr.left == null) {
                System.out.print(curr.data + " ");
                curr = curr.right;
            }
            else {
                Node pre = curr.left;
                while (pre.right != null && pre.right != curr) {
                    pre = pre.right;
                }
                if (pre.right == null) {
                    pre.right = curr;
                    curr = curr.left;
                } else {
                    pre.right = null;
                    System.out.print(curr.data + " ");
                    curr = curr.right;
                }
            }
        }

        System.out.println();
    }

    void preorder() {
        System.out.println("Preorder: ");
        preorderRecur(root);
        System.out.println();
        preorderIter();
    }
    void preorderRecur(Node root) {
        if (root != null) {
            System.out.print(root.data + " ");
            preorderRecur(root.left);
            preorderRecur(root.right);
        }
    }

    void preorderIter() {
        Node curr = root;
        while (curr != null) {
            if (curr.left == null) {
                System.out.print(curr.data + " ");
                curr = curr.right;
            } else {
                Node pre = curr.left;
                while (pre.right != null && pre.right != curr) {
                    pre = pre.right;
                }
                if (pre.right == null) {
                    System.out.print(curr.data + " ");
                    pre.right = curr;
                    curr = curr.left;
                } else {
                    pre.right = null;
                    curr = curr.right;
                }
            }
        }
        System.out.println();
    }

    void postorder() {
        System.out.println("Postorder: ");
        postorderRecur(root);
        System.out.println();
        postorderIter();
    }
    void postorderRecur(Node root) {
        if (root != null) {
            postorderRecur(root.right);
            System.out.print(root.data + " ");
            postorderRecur(root.left);
        }
    }
    void postorderIter() {
        Node curr = root;
        while (curr != null) {
            if (curr.right == null) {
                System.out.print(curr.data + " ");
                curr = curr.left;
            } else {
                Node pre = curr.right;
                while (pre.left != null && pre.left != curr) {
                    pre = pre.left;
                }
                if (pre.left == null) {
                    pre.left = curr;
                    curr = curr.right;
                } else {
                    pre.left = null;
                    System.out.print(curr.data + " ");
                    curr = curr.left;
                }
            }
        }
        System.out.println();
    }

    void convertToMirror() {
        convertToMirrorUtil(root);
    }
    void convertToMirrorUtil(Node root) {
        if (root == null) return;
        if (root.left != null) convertToMirrorUtil(root.left);
        if (root.right != null) convertToMirrorUtil(root.right);
        Node temp = root.left;
        root.left = root.right;
        root.right = temp;
        return;
    }

    void LCA(int key1, int key2) {
        Node[] lca = new Node[1];
        if (search(root, key1) && search(root, key2))
            lcaUtil(root, lca, key1, key2);
        if (lca[0] != null)
            System.out.println("LCA : " + lca[0].data);
        else
            System.out.println("Not present");
    }
    boolean lcaUtil(Node root, Node[] lca, int key1, int key2) {
        if (root == null) {
            return false;
        } else if (key1 == root.data || key2 == root.data) {
            lca[0] = root;
            return true;
        }
        boolean left = lcaUtil(root.left, lca, key1, key2);
        boolean right = lcaUtil(root.right, lca, key1, key2);
        if (left && right)
            lca[0] = root;
        return left || right;
        
    }
    boolean search(Node root, int key) {
        if (root == null) {
            return false;
        } else if (key == root.data) {
            return true;
        }
        return search(root.left, key) || search(root.right, key);
    }

    void levelorder() {
        Node node = root;
        Queue<Node> q = new LinkedList<>();
        q.add(node);
        q.add(null);
        while (q.size()!=1) {
            node = q.poll();
            if (node == null) {
                System.out.println();
                q.add(null);
                continue;
            }
            System.out.print(node.data + " ");
            if (node.left != null) {
                q.add(node.left);
            }
            if (node.right != null) {
                q.add(node.right);
            }
        }
        System.out.println();
    }

    void spiralOrder() {
        Node node = root;
        Stack<Node> s1 = new Stack<>();
        Stack<Node> s2 = new Stack<>();
        s1.push(node);
        while (!s1.isEmpty() || !s2.isEmpty()) {
            while(!s1.isEmpty()){
                Node n = s1.pop();
                System.out.print(n.data+" ");
                if(n.right!=null){
                    s2.push(n.right);
                }
                if(n.left!=null){
                    s2.push(n.left);
                }
            }
            System.out.println();
            while(!s2.isEmpty()){
                Node n = s2.pop();
                System.out.print(n.data+" ");
                if(n.left!=null){
                    s1.push(n.left);
                }
                if(n.right!=null){
                    s1.push(n.right);
                }
            }
            System.out.println();
        }
    }

    void reverseLevelOrderTraversal() {
        Node node = root;
        List<Integer> levels = new ArrayList<>();
        Queue<Node> q = new LinkedList<>();
        q.add(node);
        levels.add(node.data);
        while(!q.isEmpty()){
            Node n = q.poll();
            if(n.right!=null){
                q.add(n.right);
                levels.add(n.right.data);
            }
            if(n.left!=null){
                q.add(n.left);
                levels.add(n.left.data);
            }
        }
        for (int i=levels.size()-1;i>=0;i--){
             System.out.print(levels.get(i)+" ");
        }
        System.out.println();
    }

    void isBTcomplete() {
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        boolean nullNode = false;
        while (!q.isEmpty()) {
            Node n = q.poll();
            if (n.left != null) {
                if (nullNode) {
                    System.out.println(false);
                    return;
                }
                q.add(n.left);
            } else {
                nullNode = true;
            }
            if (n.right != null) {
                if (nullNode) {
                    System.out.println(false);
                    return;
                }
                q.add(n.right);
            } else {
                nullNode = true;
            }
        }
        System.out.println(true);
    }

    void bottomView() {
        int minX[] = new int[] {Integer.MAX_VALUE}, maxX[] = new int[] {Integer.MIN_VALUE};
        Map<Integer,int[]> map = new HashMap<>();
        map.put(0, new int[] {0, root.data});
        bottomViewUtil(root, 0, 0, minX, maxX, map);
        for (int i=minX[0]; i<=maxX[0]; i++) {
            System.out.print(map.get(i)[1] + " ");
        }
        System.out.println();
    }
    void bottomViewUtil(Node node, int x, int y, int minX[], int maxX[], Map<Integer,int[]> map) {
        if (node == null) {
            return;
        }
        if (x < minX[0]) {
            minX[0] = x;
            map.put(x, new int[] {y, node.data});
        }
        else if (x > maxX[0]) {
            maxX[0] = x;
            map.put(x, new int[] {y, node.data});
        } else {
            if (map.get(x)[0] < y) {
                map.put(x, new int[] {y, node.data});
            }
        }
        bottomViewUtil(node.left, x-1, y+1, minX, maxX, map);
        bottomViewUtil(node.right, x+1, y+1, minX, maxX, map);
    }

    void areTheyCousins(int x, int y) {
        Tuple infoX = new Tuple(null, 0, x);
        Tuple infoY = new Tuple(null, 0, y);
        areTheyCousinsUtil(root, infoX, infoY, null, 0);
        if (infoX.parent != infoY.parent && infoX.level == infoY.level) {
            System.out.println("Cousins");
            return;
        }
        System.out.println("Not cousins");
    }
    void areTheyCousinsUtil(Node node, Tuple x, Tuple y, Node parent, int level) {
        if (node == null)
            return;
        if (node.data == x.data) {
            x.parent = parent;
            x.level = level;
        }
        if (node.data == y.data) {
            y.parent = parent;
            y.level = level;
        }
        areTheyCousinsUtil(node.left, x, y, node, level+1);
        areTheyCousinsUtil(node.right, x, y, node, level+1);

    }

    void printCousin(int x) {
        Tuple infoX = new Tuple(null, -1, x);
        Node cousin = printCousinUtil(root, infoX, null, 0);
        if (cousin != null) {
            System.out.println(cousin.data);
        } else {
            System.out.println("No cousin exists");
        }
    }
    Node printCousinUtil(Node node, Tuple x, Node parent, int level) {
        if (node == null) {
            return null;
        }
        if (node.data == x.data) {
            x.parent = parent;
            x.level = level;
        } else if (x.level == level && x.parent != parent) {
            return node;
        }
        Node left = printCousinUtil(node.left, x, node, level+1);
        if (left != null) return left;
        return printCousinUtil(node.right, x, node, level+1);
    }

    void checkSumTree() {
        if (root == null) {
            System.out.println(true);
            return;
        }
        System.out.println((checkSumTreeUtil(root) >= 0 ? true : false));
    }
    int checkSumTreeUtil(Node node) {
        int left = 0, right = 0;
        boolean isLeaf = true;
        if (node.left != null) {
            left = checkSumTreeUtil(node.left);
            isLeaf = false;
        }
        if (node.right != null) {
            right = checkSumTreeUtil(node.right);
            isLeaf = false;
        }
        if (left < 0 || right < 0 || !isLeaf && left + right != node.data)
            return Integer.MIN_VALUE;
        return node.data + left + right;

    }

    void diameter() {
        long diameter[] = new long[] {0};
        diameterUtil(root, diameter);
        System.out.println(diameter[0]);
    }
    long diameterUtil(Node node, long diameter[]) {
        if (node == null)
            return 0;
        long left = diameterUtil(node.left, diameter);
        long right = diameterUtil(node.right, diameter);
        diameter[0] = Math.max(diameter[0], left+right+1);
        return Math.max(left, right) + 1;
    }

    public static void main(String[] args) {
        MyBT bt = new MyBT();
        bt.root = new Node(1);
        bt.root.left = new Node(9);
        bt.root.right = new Node(13);
        bt.root.left.left = new Node(4);
        bt.root.left.right = new Node(5);
        bt.root.right.left = new Node(6);
        bt.root.right.right = new Node(7);
        bt.levelorder();
        bt.diameter();
    }

    static class Node {
        int data;
        Node left, right;
        
        Node(int data) {
            this.data = data;
        }
    }

    static class Tuple {
        Node parent;
        int level, data;
        Tuple(Node parent, int level, int data) { 
            this.parent = parent;
            this.level = level;
            this.data = data;
        }
    }
}

