"""Practical 7A: DFS using an adjacency matrix."""


def dfs(matrix, start):
    visited = [False] * len(matrix)
    result = []

    def visit(vertex):
        visited[vertex] = True
        result.append(vertex)
        for neighbour, connected in enumerate(matrix[vertex]):
            if connected and not visited[neighbour]:
                visit(neighbour)

    visit(start)
    return result


def main():
    vertex_count = int(input("Number of vertices: "))
    edge_count = int(input("Number of edges: "))
    matrix = [[0] * vertex_count for _ in range(vertex_count)]
    for _ in range(edge_count):
        first, second = map(int, input("Enter an edge (u v): ").split())
        matrix[first][second] = matrix[second][first] = 1
    print("Adjacency matrix:")
    for row in matrix:
        print(*row)
    start = int(input("Starting vertex: "))
    print("DFS:", " ".join(map(str, dfs(matrix, start))))


if __name__ == "__main__":
    main()
