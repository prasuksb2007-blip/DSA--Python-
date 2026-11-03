"""Practical 4A: Recursive traversals of a binary tree."""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree():
    value = input("Enter node value (blank for no node): ").strip()
    if not value:
        return None
    node = Node(value)
    print(f"Left child of {value}:")
    node.left = create_tree()
    print(f"Right child of {value}:")
    node.right = create_tree()
    return node


def inorder(root, result):
    if root is not None:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)


def preorder(root, result):
    if root is not None:
        result.append(root.data)
        preorder(root.left, result)
        preorder(root.right, result)


def postorder(root, result):
    if root is not None:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.data)


def main():
    root = create_tree()
    for name, traversal in (
        ("Inorder", inorder),
        ("Preorder", preorder),
        ("Postorder", postorder),
    ):
        result = []
        traversal(root, result)
        print(f"{name}: {' '.join(result)}")


if __name__ == "__main__":
    main()
