"""
Title:
Implementation of Binary Tree and  Non Recursive Tree Traversals (In-order, Preorder, and Post-order)

Problem Statement:
Create a Binary Tree and implement the following  Non recursive traversal techniques:
 Print the Node
 Push it into Stack
 move toward its left
while stack is not empty Pop node and move towards its right repeat step 1, 2, 3
Display the nodes of the binary tree using each traversal method.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Stack:
    def __init__(self, capacity=100):
        self.top = -1
        self.capacity = capacity
        self.st = [None] * capacity

    def push(self, x):
        if self.top == self.capacity - 1:
            print("Stack Overflow !!")
            return
        self.top += 1
        self.st[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack Underflow !! Nothing to pop.")
            return None
        x = self.st[self.top]
        self.top -= 1
        return x

    def is_empty(self):
        return self.top == -1


def create():
    val = input("Enter value for node (press Enter for None): ")
    if val == "":
        return None
    
    root = Node(val)
    print(f"Enter left child of {val}:")
    root.left = create()
    print(f"Enter right child of {val}:")
    root.right = create()
    
    return root


def iterative_preorder(root):
    if root is None:
        return
    
    s = Stack()
    s.push(root)
    
    while not s.is_empty():
        node = s.pop()
        print(node.data, end=" ")
        
        if node.right is not None:
            s.push(node.right)
        if node.left is not None:
            s.push(node.left)
    print()


def iterative_inorder(root):
    s = Stack()
    curr = root
    
    while curr is not None or not s.is_empty():
        while curr is not None:
            s.push(curr)
            curr = curr.left
            
        curr = s.pop()
        print(curr.data, end=" ")
        curr = curr.right
    print()


def iterative_postorder(root):
    if root is None:
        return
    
    s1 = Stack()
    s2 = Stack()
    s1.push(root)
    
    while not s1.is_empty():
        node = s1.pop()
        s2.push(node)
        
        if node.left is not None:
            s1.push(node.left)
        if node.right is not None:
            s1.push(node.right)
            
    while not s2.is_empty():
        node = s2.pop()
        print(node.data, end=" ")
    print()


# Driver Code
if __name__ == "__main__":
    print("=== Create Binary Tree ===")
    root = create()

    print("\nNon-Recursive Preorder Traversal:")
    iterative_preorder(root)

    print("Non-Recursive Inorder Traversal:")
    iterative_inorder(root)

    print("Non-Recursive Postorder Traversal:")
    iterative_postorder(root)