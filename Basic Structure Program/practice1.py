class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert a key into the BST
    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key < current.val:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    # Iterative / Non-Recursive Preorder Traversal (Root -> Left -> Right)
    def preorder_traversal(self):
        if self.root is None:
            return []
        
        result = []
        stack = [self.root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Right child is pushed first so Left child is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result

    # Iterative / Non-Recursive Inorder Traversal (Left -> Root -> Right)
    def inorder_traversal(self):
        result = []
        stack = []
        current = self.root
        
        while stack or current:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            
            # Current must be NULL at this point
            current = stack.pop()
            result.append(current.val)
            
            # We have visited the node and its left subtree. Now, it's right subtree's turn
            current = current.right
            
        return result

# --- Execution Example ---
if __name__ == "__main__":
    bst = BST()
    # Constructing a sample tree
    nums = [50, 30, 20, 40, 70, 60, 80]
    for num in nums:
        bst.insert(num)
        
    print("5 A: Generic BST Traversals")
    print(f"Non-Recursive Preorder: {bst.preorder_traversal()}")
    print(f"Non-Recursive Inorder : {bst.inorder_traversal()}")
