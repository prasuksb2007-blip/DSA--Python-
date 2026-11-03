"""Practical 8A: BFS using an adjacency list."""

from collections import deque


def bfs(graph, start):
    visited = {start}
    result = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return result


def main():
    vertex_count = int(input("Number of vertices: "))
    edge_count = int(input("Number of edges: "))
    graph = {vertex: [] for vertex in range(vertex_count)}
    for _ in range(edge_count):
        first, second = map(int, input("Enter an edge (u v): ").split())
        graph[first].append(second)
        graph[second].append(first)
    start = int(input("Starting vertex: "))
    print("BFS:", " ".join(map(str, bfs(graph, start))))


if __name__ == "__main__":
    main()
