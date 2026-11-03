class StudentRecord:
    def __init__(self, admission_id, name, course):
        self.admission_id = admission_id
        self.name = name
        self.course = course

    def __repr__(self):
        return f"[ID: {self.admission_id} | {self.name} | {self.course}]"


class StudentNode:
    def __init__(self, record):
        self.record = record
        self.left = None
        self.right = None


class StudentAdmissionBST:
    def __init__(self):
        self.root = None

    # Insert student record based on Admission ID
    def insert_student(self, admission_id, name, course):
        new_record = StudentRecord(admission_id, name, course)
        new_node = StudentNode(new_record)
        
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if admission_id < current.record.admission_id:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    # Non-Recursive Preorder Traversal
    def iterative_preorder(self):
        if self.root is None:
            print("No records found.")
            return

        stack = [self.root]
        print("\n--- Student Records (Preorder Traversal) ---")
        while stack:
            node = stack.pop()
            print(node.record)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # Non-Recursive Inorder Traversal (Yields Sorted Admission IDs)
    def iterative_inorder(self):
        if self.root is None:
            print("No records found.")
            return

        stack = []
        current = self.root
        print("\n--- Student Records Sorted by Admission ID (Inorder Traversal) ---")
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            print(current.record)
            current = current.right


# --- Scenario Execution ---
if __name__ == "__main__":
    admission_system = StudentAdmissionBST()
    
    # Simulating student admissions (Unsorted arrival)
    admission_system.insert_student(105, "Alice Smith", "Computer Science")
    admission_system.insert_student(102, "Bob Jones", "Electrical Engineering")
    admission_system.insert_student(108, "Charlie Brown", "Mechanical Engineering")
    admission_system.insert_student(101, "Diana Prince", "Data Science")
    admission_system.insert_student(104, "Evan Wright", "Computer Science")

    # Display results
    print("5 B: Student Admission System")
    admission_system.iterative_preorder()
    admission_system.iterative_inorder()
