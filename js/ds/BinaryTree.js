class Node {
    constructor(data) {
        this.data = data;
        this.left = null
        this.right = null;
    }
}
class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    add(data) {
        this.root = this.addUtil(data, this.root);
    }
    addUtil(data, node) {
        if (node === null) {
            return new Node(data);  
        } else if (data < node.data) {
            node.left = this.addUtil(data, node.left);
        } else {
            node.right = this.addUtil(data, node.right);
        }
        return node;
    }

    remove(data) {
        this.root = this.removeUtil(data, this.root);
    }
    removeUtil(data, node) {
        if (node === null) {
            return null;
        }
        if (data == node.data) {
            if (node.left != null && node.right != null) {
                let min = node.right;
                let minParent = node;
                while (min.left != null) {
                    minParent = min;
                    min = min.left;
                }
                node.data = min.data;
                minParent = this.removeUtil(min.data, minParent);
            } else if (node.left == null) {
                node = node.right
            } else if (node.right == null) {
                node = node.left;
            }
        }
        else if (data < node.data) {
            node.left = this.removeUtil(data, node.left);
        } else {
            node.right = this.removeUtil(data, node.right);
        }
        return node;
    }

    inorder(root=this.root) {
        if (root != null) {
            this.inorder(root.left);
            process.stdout.write(root.data + " ");
            this.inorder(root.right);
        }
    }
}

tree = new BinarySearchTree();
tree.add(5);
tree.add(2);
tree.add(8);
tree.add(6);
tree.add(7);
tree.add(3);
tree.inorder();
console.log();
tree.remove(7);
tree.inorder();
