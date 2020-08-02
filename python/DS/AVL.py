class AVL:
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
            self.height = 1
    
    def __init__(self):
        self.root = None
    
    def get_height(self, root): return root.height if root else 0

    def left_rotate(self, root):
        x, y, T2 = root, root.right, root.right.left
        y.left, x.right = x, T2
        y.height, x.height = 1 + max(self.get_height(y.left), self.get_height(y.right)), 1 + max(self.get_height(x.left), self.get_height(x.right))
        return y

    def right_rotate(self, root):
        x, y, T2 = root, root.left, root.left.right
        y.right, x.left = x, T2
        y.height, x.height = 1 + max(self.get_height(y.left), self.get_height(y.right)), 1 + max(self.get_height(x.left), self.get_height(x.right))
        return y

    def add(self, key):
        def add_util(root):
            if not root:
                return AVL.Node(key)
            elif key < root.data:
                root.left = add_util(root.left)
            else:
                root.right = add_util(root.right)
            
            root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
            balance = self.get_height(root.left) - self.get_height(root.right)

            if balance > 1 and key < root.left.data:
                return self.right_rotate(root)

            elif balance > 1 and key > root.left.data:
                root.left = self.left_rotate(root.left)
                print(root.right)
                return self.right_rotate(root)

            elif balance < -1 and key > root.right.data:
                return self.left_rotate(root)

            elif balance < -1 and key < root.right.data:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

            return root
        self.root = add_util(self.root)

    def preorder(self):
        def preorder_util(root):
            if root:
                print(root.data, end=" ")
                preorder_util(root.left)
                preorder_util(root.right)
        preorder_util(self.root)
        print()




my_avl = AVL()
my_avl.add(10)
my_avl.add(20)
my_avl.add(30)
my_avl.add(40)
my_avl.add(50)
my_avl.add(25)
my_avl.preorder()