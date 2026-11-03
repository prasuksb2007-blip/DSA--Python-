"""Practical 6B: Employee ID BST analysis."""

from practical_6a_bst_analysis import height, leaves, print_levels
from practical_5a_nonrecursive_bst import insert


def main():
    values = map(int, input("Enter employee IDs: ").split())
    root = None
    for employee_id in values:
        root = insert(root, employee_id)
    print_levels("Employee tree:", root)
    leaf_nodes = []
    leaves(root, leaf_nodes)
    print("Tree height:", height(root))
    print("Leaf employee IDs:", " ".join(leaf_nodes))


if __name__ == "__main__":
    main()
