class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)

class BiTree:
    def __init__(self,root):
        self.root = root        
    def n(self,root,data):
        if data<root.data:
            if root.left is None:
                newNode = Node(data)
                self.root.left = newNode
            else:
                self.n(root.left,data)
        else:
            if root.right is None:
                newNode = Node(data)
                self.root.right = newNode
            else:
                self.n(root.right,data)
    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        print(root.data)
        if root.right!=None:
            self.inorder(root.right)

root = Node(4)
a = BiTree(root)
a.n(root,2)
a.n(root,1)
a.n(root,3)
a.n(root,6)
a.n(root,7)
a.n(root,5)
a.inorder(root)
