"""Practical 2: Array queue for a ticket booking counter."""


class TicketQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.tickets = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, customer):
        if self.size == self.capacity:
            print("Queue Overflow: the counter queue is full.")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.tickets[self.rear] = customer
        self.size += 1
        print(f"Added customer: {customer}")

    def dequeue(self):
        if self.size == 0:
            print("Queue Underflow: no customer is waiting.")
            return None
        customer = self.tickets[self.front]
        self.tickets[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Booked ticket for: {customer}")
        return customer

    def display(self):
        if self.size == 0:
            print("The queue is empty.")
            return
        print("Customers waiting:")
        for offset in range(self.size):
            index = (self.front + offset) % self.capacity
            print(f"- {self.tickets[index]}")


def main():
    queue = TicketQueue()
    while True:
        print("\n1. Enqueue  2. Dequeue  3. Display  4. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            queue.enqueue(input("Enter customer name: ").strip())
        elif choice == "2":
            queue.dequeue()
        elif choice == "3":
            queue.display()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
