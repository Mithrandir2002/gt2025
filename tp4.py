import heapq

def generate_weighted_graph():
    graph_size = 9
    graph = [[0 for _ in range(graph_size)] for _ in range(graph_size)]
    connections = [
        (1, 2, 4), (1, 5, 1), (1, 7, 2),
        (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8),
        (4, 6, 6), (4, 7, 4), (4, 8, 3),
        (5, 6, 9), (5, 7, 10),
        (6, 9, 2),
        (7, 9, 8),
        (8, 9, 1),
        (9, 8, 7)
    ]
    for src, dst, cost in connections:
        graph[src - 1][dst - 1] = cost
        graph[dst - 1][src - 1] = cost
    return graph

def display_graph_matrix(matrix):
    print("Weighted Graph Matrix:")
    for line in matrix:
        print(" ".join(f"{x:2d}" for x in line))

def run_prim_algorithm(graph, source):
    size = len(graph)
    explored = [False] * size
    priority_queue = [(0, source, source)]
    spanning_tree, total_cost = [], 0

    while priority_queue:
        cost, from_node, to_node = heapq.heappop(priority_queue)
        if explored[to_node]:
            continue
        explored[to_node] = True
        if from_node != to_node:
            spanning_tree.append((from_node + 1, to_node + 1, cost))
            total_cost += cost
        for next_node in range(size):
            if graph[to_node][next_node] > 0 and not explored[next_node]:
                heapq.heappush(priority_queue, (graph[to_node][next_node], to_node, next_node))
    return spanning_tree, total_cost

def run_kruskal_algorithm(graph):
    size = len(graph)
    edge_list = [(graph[x][y], x, y) for x in range(size) for y in range(x + 1, size) if graph[x][y] > 0]
    edge_list.sort()

    roots = list(range(size))
    heights = [0] * size

    def get_root(node):
        if roots[node] != node:
            roots[node] = get_root(roots[node])
        return roots[node]

    def merge_sets(node1, node2):
        root1, root2 = get_root(node1), get_root(node2)
        if root1 != root2:
            if heights[root1] > heights[root2]:
                roots[root2] = root1
            else:
                roots[root1] = root2
                if heights[root1] == heights[root2]:
                    heights[root2] += 1

    spanning_tree, total_cost = [], 0
    for cost, src, dst in edge_list:
        if get_root(src) != get_root(dst):
            merge_sets(src, dst)
            spanning_tree.append((src + 1, dst + 1, cost))
            total_cost += cost

    return spanning_tree, total_cost

if __name__ == "__main__":
    weighted_graph = generate_weighted_graph()
    display_graph_matrix(weighted_graph)

    start_node = int(input("\nInput the starting node for Prim's algorithm (1-9): ")) - 1
    prim_result, prim_cost = run_prim_algorithm(weighted_graph, start_node)
    print("\nPrim's MST Result:")
    for src, dst, cost in prim_result:
        print(f"Connection {src} to {dst} with cost {cost}")
    print(f"Prim's Total Cost: {prim_cost}")

    kruskal_result, kruskal_cost = run_kruskal_algorithm(weighted_graph)
    print("\nKruskal's MST Result:")
    for src, dst, cost in kruskal_result:
        print(f"Connection {src} to {dst} with cost {cost}")
    print(f"Kruskal's Total Cost: {kruskal_cost}")