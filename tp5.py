import heapq
import numpy as np

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']
vertex_count = len(vertices)
vertex_to_idx = {vertex: i for i, vertex in enumerate(vertices)}

graph_matrix = np.full((vertex_count, vertex_count), float('inf'))

connections = [
    ('A', 'C', 1), ('A', 'B', 4),
    ('B', 'F', 3),
    ('C', 'D', 8), ('C', 'F', 7),
    ('D', 'H', 5),
    ('F', 'H', 1), ('F', 'E', 1),
    ('E', 'H', 2),
    ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
    ('G', 'M', 4),
    ('M', 'L', 1),
    ('L', 'G', 4), ('L', 'E', 2)
]

for src, dst, cost in connections:
    src_idx = vertex_to_idx[src]
    dst_idx = vertex_to_idx[dst]
    graph_matrix[src_idx][dst_idx] = cost
    graph_matrix[dst_idx][src_idx] = cost

print("Undirected Weighted Graph Matrix:")
for line in graph_matrix:
    formatted_row = [" inf" if x == float('inf') else f"{int(x):4d}" for x in line]
    print(" ".join(formatted_row))

idx_to_vertex = {i: v for v, i in vertex_to_idx.items()}

def find_shortest_path(matrix, source, target):
    src_idx = vertex_to_idx[source]
    tgt_idx = vertex_to_idx[target]

    shortest_distances = [float('inf')] * vertex_count
    shortest_distances[src_idx] = 0
    predecessors = [None] * vertex_count
    queue = [(0, src_idx)]

    while queue:
        dist, current = heapq.heappop(queue)
        if dist > shortest_distances[current]:
            continue

        for next_idx in range(vertex_count):
            edge_weight = matrix[current][next_idx]
            if edge_weight != float('inf'):
                new_dist = dist + edge_weight
                if new_dist < shortest_distances[next_idx]:
                    shortest_distances[next_idx] = new_dist
                    predecessors[next_idx] = current
                    heapq.heappush(queue, (new_dist, next_idx))

    route = []
    current_idx = tgt_idx
    while current_idx is not None:
        route.append(idx_to_vertex[current_idx])
        current_idx = predecessors[current_idx]
    route = route[::-1]  # Reverse the path

    return route, shortest_distances[tgt_idx]

source_vertex = input("Input source vertex (A-M): ").upper().strip()
target_vertex = input("Input target vertex (A-M): ").upper().strip()

if source_vertex in vertex_to_idx and target_vertex in vertex_to_idx:
    shortest_route, total_cost = find_shortest_path(graph_matrix, source_vertex, target_vertex)
    print(f"Shortest route from {source_vertex} to {target_vertex}: {' -> '.join(shortest_route)}")
    print(f"Total cost of path: {total_cost}")
else:
    print("Error: Please enter valid vertex labels (A-M).")