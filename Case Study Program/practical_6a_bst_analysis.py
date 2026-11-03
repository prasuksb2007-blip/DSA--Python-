"""Practical 6A: Level order, height, and leaf analysis of a BST."""

from collections import deque

from practical_5a_nonrecursive_bst import Node, insert


def level_order(root):
    if root is None:
        return []
    levels, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(str(node.data))
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        levels.append(level)
    return levels


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def leaves(root, result):
    if root is None:
        return
    if root.left is None and root.right is None:
        result.append(str(root.data))
        return
    leaves(root.left, result)
    leaves(root.right, result)


def print_levels(label, root):
    print(label)
    for number, level in enumerate(level_order(root), start=1):
        print(f"Level {number}: {' '.join(level)}")


def main():
    values = map(int, input("Enter original BST values: ").split())
    original = None
    for value in values:
        original = insert(original, value)
    print_levels("Original tree:", original)
    new_value = int(input("Enter a value for the new tree: "))
    updated = insert(original, new_value)
    print_levels("New tree:", updated)
    leaf_nodes = []
    leaves(updated, leaf_nodes)
    print("Height:", height(updated))
    print("Leaf nodes:", " ".join(leaf_nodes))


if __name__ == "__main__":
    main()
