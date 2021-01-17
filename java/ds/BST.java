import java.util.*;

class BST {

	private class Node {
		Node left;
		Node right;
		int val;

		Node(int val) {
			this.val = val;
			this.left = null;
			this.right = null;
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
		List<Integer> lst = new ArrayList<Integer>(Arrays.asList(8, 3, 1, 4, 6, 2, 19, 16, 5));
		for (int val : lst) {
			bst.addNode(val);
		}
		bst.levelorder();
		System.out.println(bst.getAncestor(16, 19).val);
	}

	public void addNode(int val) {
		this.root = addNodeHelper(this.root, val, 0);
	}

	public BST.Node addNodeHelper(Node root, int val, int height) {
		if (root == null) {
			if (height > this.height) {
				this.height = height;
			}
			return new BST.Node(val);
		} else if (val <= root.val) {
			root.left = addNodeHelper(root.left, val, height + 1);
		} else {
			root.right = addNodeHelper(root.right, val, height + 1);
		}
		return root;
	}

	public int removeNode(int val) {
		this.root = removeNodeHelper(this.root, val);
		return val;
	}

	public BST.Node removeNodeHelper(Node root, int val) {
		if (val < root.val) {
			root.left = removeNodeHelper(root.left, val);
		} else if (val > root.val) {
			root.right = removeNodeHelper(root.right, val);
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
			root.val = temp.val;
			tempPrev.right = removeNodeHelper(temp, temp.val);
		}
		return root;
	}

	public void inorder() {
		inorderHelper(this.root);
		System.out.println();
	}

	public void inorderHelper(Node node) {
		if (node != null) {
			inorderHelper(node.left);
			System.out.print(node.val + " ");
			inorderHelper(node.right);
		}
	}

	public void levelorder() {
		if (this.root == null)
			return;
		Deque<BST.Node> q = new ArrayDeque<BST.Node>();
		q.addLast(this.root);
		q.addLast(new BST.Node(Integer.MIN_VALUE));
		while (q.size() > 1) {
			Node n = q.pollFirst();
			if (n.val == Integer.MIN_VALUE) {
				System.out.println();
				q.addLast(new BST.Node(Integer.MIN_VALUE));
			} else {
				System.out.print(n.val + " ");
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
		Map<Integer, int[]> lookup = new HashMap<Integer, int[]>();
		printLeftViewHelper(this.root, 0, 0, lookup);

		for (int y = 0; y <= this.height; y++) {
			System.out.println("Height " + y + ": " + lookup.get(y)[1]);
		}
		System.out.println();
	}

	public void printLeftViewHelper(Node node, int x, int y, Map<Integer, int[]> lookup) {
		if (node == null) {
			return;
		} else if (!lookup.containsKey(y) || x < lookup.get(y)[0]) {
			lookup.put(y, new int[] { x, node.val });
		}
		printLeftViewHelper(node.left, x - 1, y + 1, lookup);
		printLeftViewHelper(node.right, x + 1, y + 1, lookup);
	}

	public void printVertical() {
		Map<Integer, ArrayList<ArrayList<Integer>>> lookup = new HashMap<Integer, ArrayList<ArrayList<Integer>>>();
		int[] minWidth = new int[] { 0 }, maxWidth = new int[] { 0 };
		this.printVerticalHelper(this.root, 0, 0, lookup, minWidth, maxWidth);
		for (int x = minWidth[0]; x <= maxWidth[0]; x++) {
			Collections.sort(lookup.get(x), new VerticalNodesComparator());
			for (ArrayList<Integer> n : lookup.get(x)) {
				System.out.print(n.get(1) + " ");
			}
			System.out.println();
		}
	}

	public void printVerticalHelper(Node node, int x, int y, Map<Integer, ArrayList<ArrayList<Integer>>> lookup,
			int[] minWidth, int[] maxWidth) {
		if (node == null)
			return;
		if (!lookup.containsKey(x)) {
			ArrayList<ArrayList<Integer>> ar = new ArrayList<ArrayList<Integer>>();
			ar.add(new ArrayList<Integer>(Arrays.asList(y, node.val)));
			lookup.put(x, ar);
		} else {
			lookup.get(x).add(new ArrayList<Integer>(Arrays.asList(y, node.val)));
		}
		minWidth[0] = (x < minWidth[0]) ? x : minWidth[0];
		maxWidth[0] = (x > maxWidth[0]) ? x : maxWidth[0];
		printVerticalHelper(node.left, x - 1, y + 1, lookup, minWidth, maxWidth);
		printVerticalHelper(node.right, x + 1, y + 1, lookup, minWidth, maxWidth);
	}

	public Node getAncestor(int val1, int val2) {
		return getAncestorHelper(this.root, val1, val2);
	}

	private Node getAncestorHelper(Node node, int val1, int val2) {
		if (node == null) {
			return null;
		} else if ((val1 < node.val && val2 > node.val) || val1 == node.val || val2 == node.val) {
			return node;
		}
		return (val1 < node.val) ? getAncestorHelper(node.left, val1, val2) : getAncestorHelper(node.right, val1, val2);
	}
}

class VerticalNodesComparator implements Comparator<ArrayList<Integer>> {

	@Override
	public int compare(ArrayList<Integer> o1, ArrayList<Integer> o2) {
		return o1.get(0).compareTo(o2.get(0));
	}
}
