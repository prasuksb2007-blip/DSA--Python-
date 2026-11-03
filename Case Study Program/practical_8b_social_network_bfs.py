"""Practical 8B: Level-by-level BFS in a friendship network."""

from collections import deque


def bfs_levels(graph, start):
    levels = {start: 0}
    queue = deque([start])
    while queue:
        person = queue.popleft()
        for friend in graph[person]:
            if friend not in levels:
                levels[friend] = levels[person] + 1
                queue.append(friend)
    return levels


def main():
    people = [person.strip() for person in input("Enter user names separated by commas: ").split(",")]
    graph = {person: [] for person in people}
    friendship_count = int(input("Number of friendships: "))
    for _ in range(friendship_count):
        first, second = input("Enter friendship (user1,user2): ").split(",")
        first, second = first.strip(), second.strip()
        if first not in graph or second not in graph:
            raise ValueError("Both users must be in the user list.")
        graph[first].append(second)
        graph[second].append(first)
    start = input("Starting user: ").strip()
    if start not in graph:
        raise ValueError("Starting user is not in the user list.")
    levels = bfs_levels(graph, start)
    for level in sorted(set(levels.values())):
        users = [user for user, distance in levels.items() if distance == level]
        print(f"Level {level}: {', '.join(users)}")


if __name__ == "__main__":
    main()
