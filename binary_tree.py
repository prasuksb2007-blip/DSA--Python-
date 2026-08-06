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
        new_node=Node(val)
        print(f"Enter left child of {val}:")
        new_node.left=self.create()
        print(f"Enter right child of {val}:")
        new_node.right=self.create()
        return new_node
    