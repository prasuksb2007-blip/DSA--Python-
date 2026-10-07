class Graph:
    def __init__(self):
        self.v = 0 
        self.e = 0
        self.g = [[0 for i in range (7)] for j in range(7)]

    def create(self):
        self.v = int(input("Enter no. of vertices: "))
        self.e = int(input("Enter no. of edges: "))

        for i in range(self.e):
            print(f"\nEnter edge {i+1} with its weight ")
            u = int(input("Starting of the vertex: "))
            v = int(input("Ending of the vertex: "))
            w = int(input("Weight of the vertex: "))
            self.g[u][v] = self.g[v][u] = w # due to undirected graph
            # self.g[u][v] = w due to directed graph

    def display(self):
        for i in range(self.v):
            for j in range(self.v):
                print(self.g[i][j], end= " ")
            print()

def main():
    g = Graph()
    g.create()
    g.display()

if __name__ == "__main__":
    main()