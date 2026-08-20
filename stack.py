class Stack:
    def __init__(self):
        # -1 means the stack is completely empty
        self.top = -1
        # Fixed-size list representing our stack memory
        self.st = [0] * 5
    
    def push(self, x):
        # Check if the stack has reached its maximum index (4)
        if self.top == 4:
            print("Stack Overflow !!")
            return
        
        self.top = self.top + 1
        self.st[self.top] = x
        print(f"Pushed: {x}")
    
    def pop(self):
        if self.top == -1:
            print("Stack Underflow !! Nothing to pop.")
            return None

        x = self.st[self.top]
        print(f"Popped item: {x}")
        self.top = self.top - 1
        return x
    
    def peek(self):
        if self.top == -1:
            return None
        return self.st[self.top]
    
    def display(self):
        if self.top == -1:
            print("Stack is empty !!")
            return

        print("Stack elements (Top to Bottom):")
        # Loop backwards from the top element down to index 0
        for i in range(self.top, -1, -1):
            print(f"| {self.st[i]} |")
        print("-----")


# --- Execution Menu ---
s = Stack()

while True:
    try:
        ch = int(input("\n1 for push\n2 for pop\n3 for display\n4 for peek\n5 for exit\nYour choice: "))
        
        if ch == 1:
            data = int(input("Enter a number to push: "))
            s.push(data)
        elif ch == 2:
            s.pop()
        elif ch == 3:
            s.display()
        elif ch == 4:
            val = s.peek()
            if val is None:
                print("Stack is empty !!")
            else:
                print("Top value is:", val)
        elif ch == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid option! Please pick 1-5.")
    except ValueError:
        print("Please enter a valid choice.")

