class Node:
    key = None
    left = None
    right = None
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

class BST:
    root = None

    def add(self, val):
        def addUtil(root, val):
            if root==None:
                root = Node(val)

            else:
                if val > root.key:
                    root.right =  addUtil(root.right, val)
                else:
                    root.left = addUtil(root.left, val)

            return root

        self.root = addUtil(self.root, val)
        return self.root


    def k_dist_nodes(self, key: int, k: int) -> None:
        def util(node: Node, key: int, k: int, path: list):
            if node is None:
                return None
            if node.key == key:
                return 

def main():
    bst = BST()
    bst.add(3)
    bst.add(4)
    bst.add(2)
    bst.add(1)

    print(bst.root.left.left.key)


if __name__ == "__main__":
    main()
