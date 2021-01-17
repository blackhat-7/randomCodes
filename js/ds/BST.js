class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  addNode(val) {
    this.root = this.addNodeHelper(this.root, val);
  }
  addNodeHelper(root, val) {
    if (root == null) {
      return new Node(val);
    } else if (val <= root.val) {
      root.left = this.addNodeHelper(root.left, val);
    } else {
      root.right = this.addNodeHelper(root.right, val);
    }
    return root;
  }

  removeNode(val) {
    this.root = this.removeNodeHelper(this.root, val);
  }
  removeNodeHelper(root, val) {
    if (root.left == null && root.right == null) {
      return null;
    }
    if (val < root.val) {
      root.left = this.removeNodeHelper(root.left, val);
    } else if (val > root.val) {
      root.right = this.removeNodeHelper(root.right, val);
    } else if (root.left != null && root.right != null) {
      let temp = root.left;
      let tempPrev = root;
      while (temp.right != null) {
        tempPrev = temp;
        temp = temp.right;
      }
      tempPrev.right = this.removeNodeHelper(temp, temp.val);
      root.val = temp.val;
    } else {
      return root.left == null ? root.right : root.left;
    }
    return root;
  }

  preorder() {
    this.preorderHelper(this.root);
    console.log();
  }
  preorderHelper(root) {
    if (root != null) {
      process.stdout.write(`${root.val} `);
      this.preorderHelper(root.left);
      this.preorderHelper(root.right);
    }
  }

  inorder() {
    this.inorderHelper(this.root);
    console.log();
  }
  inorderHelper(root) {
    if (root != null) {
      this.inorderHelper(root.left);
      process.stdout.write(`${root.val} `);
      this.inorderHelper(root.right);
    }
  }

  postorder() {
    this.postorderHelper(this.root);
    console.log();
  }
  postorderHelper(root) {
    if (root != null) {
      this.postorderHelper(root.left);
      this.postorderHelper(root.right);
      process.stdout.write(`${root.val} `);
    }
  }

  levelOrder() {
    const q = [this.root, null];
    while (q.length > 1) {
      const u = q.shift();
      if (u == null) {
        console.log();
        q.push(null);
      } else {
        process.stdout.write(`${u.val} `);
        if (u.left != null) {
          q.push(u.left);
        }
        if (u.right != null) {
          q.push(u.right);
        }
      }
    }
    console.log();
  }
}

bst = new BST();

nodeVals = [15, 10, 20, 8, 12, 16];
for (val of nodeVals) {
  bst.addNode(val);
}
bst.inorder();
bst.removeNode(16);
bst.inorder();
