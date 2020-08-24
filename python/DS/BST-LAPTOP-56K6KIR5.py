import collections

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
    
    def preOrderTraversal(self):
        if self.root == None:
            return
        stack = collections.deque()
        stack.append(self.root)
        while(stack):
            curr = stack.pop()
            if curr.left != None:
                stack.append(curr.left)
            if curr.right != None:
                stack.append(curr.right)
            print(curr.key)

    def inOrderTraversal(self):
        if self.root == None:
            return
        stack = collections.deque()
        curr = self.root
        while(curr != None or stack):
            while(curr != None):
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            print(curr.key, end = " ")
            curr = curr.right
        print()


    def levelOrderTraversal(self):
        if self.root == None:
            return
        q = collections.deque()
        q.append(self.root)
        q.append(None)

        while(q):
            curr = q.popleft()
            if curr == None:
                if q:
                    q.append(None)
                    print()
            else:
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
                print(curr.key, end = " ")
        print()



def main():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.add(1)
    bst.add(2)
    bst.add(4)
    bst.add(6)
    bst.add(9)

    bst.inOrderTraversal()
    bst.levelOrderTraversal()

if __name__ == "__main__":
    main()