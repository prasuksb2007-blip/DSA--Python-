"""
Title:
Implementation of Binary Tree and Recursive Tree Traversals (In-order, Preorder, and Post-order)

Problem Statement:
Create a Binary Tree and implement the following recursive traversal techniques:
 Inorder Traversal
 Preorder Traversal
 Postorder Traversal
Display the nodes of the binary tree using each traversal method.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# --- Binary Tree Creation ---
def create_tree():
    value = input("Enter node value (or 'NULL' / '-1' for no node): ").strip()
    if value == "-1" or value.upper() == "NULL":
        return None

    new_node = Node(value)

    print(f"Enter left child of {value}:")
    new_node.left = create_tree()

    print(f"Enter right child of {value}:")
    new_node.right = create_tree()

    return new_node


# --- Recursive Traversals ---
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


# --- Main Driver Function ---
def main():
    print("=== Create Library Catalog Binary Tree ===")
    root = create_tree()

    print("\n--- Book Categories (Inorder Traversal) ---")
    inorder(root)

    print("\n\n--- Catalog Structure (Preorder Traversal) ---")
    preorder(root)

    print("\n\n--- Archive/Delete Order (Postorder Traversal) ---")
    postorder(root)
    print()


if __name__ == "__main__":
    main()