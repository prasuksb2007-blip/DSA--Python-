"""Practical 7B: DFS exploration of a city road network."""

from practical_7a_matrix_dfs import dfs


def main():
    locations = input("Enter location names separated by commas: ").split(",")
    locations = [location.strip() for location in locations]
    index = {name: number for number, name in enumerate(locations)}
    matrix = [[0] * len(locations) for _ in locations]
    road_count = int(input("Number of roads: "))
    for _ in range(road_count):
        first, second = input("Enter road (location1,location2): ").split(",")
        first, second = first.strip(), second.strip()
        if first not in index or second not in index:
            raise ValueError("Both locations must be in the location list.")
        matrix[index[first]][index[second]] = 1
        matrix[index[second]][index[first]] = 1
    start = input("Starting location: ").strip()
    if start not in index:
        raise ValueError("Starting location is not in the location list.")
    order = dfs(matrix, index[start])
    print("DFS exploration:", " -> ".join(locations[number] for number in order))


if __name__ == "__main__":
    main()
