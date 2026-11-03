"""Practical 4B: Recursive traversals of a university library catalog tree."""

from practical_4a_recursive_binary_tree import (
    create_tree,
    inorder,
    postorder,
    preorder,
)


def main():
    print("Enter catalog categories. Use a blank value for an empty child.")
    root = create_tree()
    for label, traversal in (
        ("Catalog order (inorder)", inorder),
        ("Catalog structure (preorder)", preorder),
        ("Removal order (postorder)", postorder),
    ):
        result = []
        traversal(root, result)
        print(f"{label}: {' | '.join(result)}")


if __name__ == "__main__":
    main()
