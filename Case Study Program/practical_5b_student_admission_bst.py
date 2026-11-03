"""Practical 5B: Student admission records in a BST."""


class Student:
    def __init__(self, admission_id, name):
        self.admission_id = admission_id
        self.name = name
        self.left = None
        self.right = None


def insert(root, admission_id, name):
    if root is None:
        return Student(admission_id, name)
    if admission_id < root.admission_id:
        root.left = insert(root.left, admission_id, name)
    elif admission_id > root.admission_id:
        root.right = insert(root.right, admission_id, name)
    return root


def inorder(root):
    result, stack, current = [], [], root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(f"{current.admission_id}:{current.name}")
        current = current.right
    return result


def preorder(root):
    if root is None:
        return []
    result, stack = [], [root]
    while stack:
        current = stack.pop()
        result.append(f"{current.admission_id}:{current.name}")
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return result


def main():
    root = None
    count = int(input("Enter number of students: "))
    for _ in range(count):
        admission_id = int(input("Admission ID: "))
        name = input("Student name: ").strip()
        root = insert(root, admission_id, name)
    print("Inorder:", " | ".join(inorder(root)))
    print("Preorder:", " | ".join(preorder(root)))


if __name__ == "__main__":
    main()
