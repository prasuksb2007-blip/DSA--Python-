"""Practical 3: Singly linked list for a dynamic library catalog."""


class Node:
    def __init__(self, title):
        self.title = title
        self.next = None


class LibraryCatalog:
    def __init__(self):
        self.head = None

    def insert_beginning(self, title):
        node = Node(title)
        node.next = self.head
        self.head = node

    def insert_end(self, title):
        node = Node(title)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def delete_beginning(self):
        if self.head is None:
            print("The catalog is empty.")
            return None
        title = self.head.title
        self.head = self.head.next
        print(f"Removed book: {title}")
        return title

    def display(self):
        if self.head is None:
            print("The catalog is empty.")
            return
        current = self.head
        while current is not None:
            print(current.title, end=" -> ")
            current = current.next
        print("None")


def main():
    catalog = LibraryCatalog()
    while True:
        print("\n1. Insert beginning  2. Insert end  3. Delete beginning")
        print("4. Display  5. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            catalog.insert_beginning(input("Enter book title: ").strip())
        elif choice == "2":
            catalog.insert_end(input("Enter book title: ").strip())
        elif choice == "3":
            catalog.delete_beginning()
        elif choice == "4":
            catalog.display()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
