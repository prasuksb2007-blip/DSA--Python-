
class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.g = []

    def create(self):
        self.v = int(input("Enter no. of vertices: "))
        self.e = int(input("Enter no. of edges: "))
        self.g = [[0 for _ in range(self.v)] for _ in range(self.v)]

        for i in range(self.e):
            print(f"\nEnter edge {i+1} with its weight ")
            u = int(input("Starting of the vertex: "))
            v = int(input("Ending of the vertex: "))
            w = int(input("Weight of the vertex: "))
            if 0 <= u < self.v and 0 <= v < self.v:
                self.g[u][v] = self.g[v][u] = w  # undirected graph
            else:
                print(f"Invalid edge: vertices must be between 0 and {self.v - 1}.")

    def dfs(self, start):
        """Return the DFS traversal beginning at start."""
        if not 0 <= start < self.v:
            raise ValueError(f"Start vertex must be between 0 and {self.v - 1}.")

        visited = [False] * self.v
        traversal = []

        def visit(vertex):
            visited[vertex] = True
            traversal.append(vertex)
            for neighbour in range(self.v):
                if self.g[vertex][neighbour] != 0 and not visited[neighbour]:
                    visit(neighbour)

        visit(start)
        return traversal

    def display(self):
        for i in range(self.v):
            for j in range(self.v):
                print(self.g[i][j], end= " ")
            print()

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

def main():
    g = Graph()
    g.create()
    print("\nAdjacency matrix:")
    g.display()
    if g.v > 0:
        start = int(input("\nEnter starting vertex for DFS: "))
        try:
            result = g.dfs(start)
            print("DFS traversal:", " ".join(map(str, result)))
        except ValueError as error:
            print(error)

if __name__ == "__main__":
    main()