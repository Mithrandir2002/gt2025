def build_adjacency_matrix(connections, total_nodes):
    matrix = [[0] * total_nodes for _ in range(total_nodes)]
    for src, dst in connections:
        matrix[src - 1][dst - 1] = 1
    return matrix

def traverse_inorder(structure, start):
    if start not in structure or not structure[start]:
        return [start]
    result = []
    if structure[start]:  # Check if there’s a left child
        result.extend(traverse_inorder(structure, structure[start][0]))
    result.append(start)
    if len(structure[start]) > 1:  # Check if there’s a right child
        result.extend(traverse_inorder(structure, structure[start][1]))
    return result

graph_edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
total_nodes = 8

graph_matrix = build_adjacency_matrix(graph_edges, total_nodes)
print("Adjacency Matrix of Graph G:")
for line in graph_matrix:
    print(line)

tree_structure = {
    1: [3, 2],
    2: [6, 5],
    3: [4],
    4: [8],
    5: [7],
    6: [],
    7: [],
    8: []
}

start_node = int(input("\nEnter starting node for inorder traversal: "))
traversal_result = traverse_inorder(tree_structure, start_node)
print(f"Inorder traversal from node {start_node}: {traversal_result}")