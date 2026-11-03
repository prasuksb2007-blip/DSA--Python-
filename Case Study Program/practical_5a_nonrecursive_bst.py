"""Practical 5A: Non-recursive inorder and preorder BST traversals."""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    current = root
    while True:
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
                break
            current = current.left
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
                break
            current = current.right
        else:
            break
    return root


def inorder(root):
    result, stack, current = [], [], root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(str(current.data))
        current = current.right
    return result


def preorder(root):
    if root is None:
        return []
    result, stack = [], [root]
    while stack:
        current = stack.pop()
        result.append(str(current.data))
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return result


def main():
    values = map(int, input("Enter BST values separated by spaces: ").split())
    root = None
    for value in values:
        root = insert(root, value)
    print("Inorder:", " ".join(inorder(root)))
    print("Preorder:", " ".join(preorder(root)))


if __name__ == "__main__":
    main()
