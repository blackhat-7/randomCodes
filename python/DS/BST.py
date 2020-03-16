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
        self.root = self.addUtil(self.root, val)
        return self.root

    def addUtil(self, root, val):
        if root==None:
            root = Node(val)

        else:
            if val > root.key:
               root.right =  self.addUtil(root.right, val)
            else:
                root.left = self.addUtil(root.left, val)

        return root
    



def main():
    bst = BST()
    bst.add(3)
    bst.add(4)
    bst.add(2)
    bst.add(1)

    print(bst.root.left.left.key)


if __name__ == "__main__":
    main()