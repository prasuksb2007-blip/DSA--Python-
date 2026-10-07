#create binary tree and perform inorder, preorder and postorder traversals.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def create(self):
        val=input("Enter the value for node:")
        if val=="":
            return None
        root=Node(val)
        print(f"Enter left child of {val}:")
        root.left=self.create()
        print(f"Enter right child of {val}:")
        root.right=self.create()
        return root
    def preorder(self,root):
        if root is not None:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
class BinaryTree:
    def __init__(self):
        self.root=None
    def create(self):
        self.root=Node(None)
        return self.root.create()
    def preorder(self,root):
        Node.preorder(self.root,root)
    def inorder(self,root):
        Node.inorder(self.root,root)
    def postorder(self,root):
        Node.postorder(self.root,root)
def main():
    bt=BinaryTree()
    print("Create Binary Tree:")
    root=bt.create()
    print("\nInorder Traversal:")
    bt.inorder(root)
    print("\nPreorder Traversal:")
    bt.preorder(root)
    print("\nPostorder Traversal:")
    bt.postorder(root)
if __name__=="__main__":
    main()
