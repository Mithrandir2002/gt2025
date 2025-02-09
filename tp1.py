def create_graph():
    return {
        1: [2, 3],
        2: [1, 4],
        3: [1, 5],
        4: [2, 6],
        5: [3, 6],
        6: [4, 5]
    }


def find_path(graph, current, target, path=None):
    if path is None:
        path = []

    path = path + [current]

    if current == target:
        return path

    for adjacent in graph.get(current, []):
        if adjacent not in path:
            new_path = find_path(graph, adjacent, target, path)
            if new_path:
                return new_path

    return None


def main():
    network = create_graph()

    try:
        start = int(input("Enter start node (1-6): "))
        end = int(input("Enter end node (1-6): "))

        if start not in network or end not in network:
            print("Invalid node! Node doesn't exist in the graph")
            return

        path = find_path(network, start, end)

        if path:
            print("True")
        else:
            print("False")

    except ValueError:
        print("Please enter valid numbers")


if __name__ == "__main__":
    main()