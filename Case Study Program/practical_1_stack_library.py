"""Practical 1: Stack-based library book return management."""


class BookStack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.books = []

    def push(self, book):
        if len(self.books) == self.capacity:
            print("Stack Overflow: the return stack is full.")
            return
        self.books.append(book)
        print(f"Returned book: {book}")

    def pop(self):
        if not self.books:
            print("Stack Underflow: no books to arrange.")
            return None
        book = self.books.pop()
        print(f"Arranged book: {book}")
        return book

    def peek(self):
        if not self.books:
            print("The stack is empty.")
            return None
        return self.books[-1]

    def display(self):
        if not self.books:
            print("The stack is empty.")
            return
        print("Books from top to bottom:")
        for book in reversed(self.books):
            print(f"- {book}")


def main():
    stack = BookStack()
    while True:
        print("\n1. Return book  2. Arrange book  3. Top book  4. Display  5. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            stack.push(input("Enter book title: ").strip())
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            top = stack.peek()
            if top is not None:
                print("Top book:", top)
        elif choice == "4":
            stack.display()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
