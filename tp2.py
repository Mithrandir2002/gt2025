class GraphAnalyzer:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self._edges = {}
        for i in range(1, vertex_count + 1):
            self._edges[i] = []
        self._adj_matrix = None

    def add_edge(self, origin, destination):
        self._edges[origin].append(destination)
        self._adj_matrix = None

    def get_adjacency_matrix(self):
        if self._adj_matrix is not None:
            return self._adj_matrix

        self._adj_matrix = [[0] * self.vertex_count for _ in range(self.vertex_count)]
        for src, targets in self._edges.items():
            for dst in targets:
                self._adj_matrix[src - 1][dst - 1] = 1
        return self._adj_matrix

    def _build_undirected_graph(self):
        undirected_graph = {}
        for i in range(1, self.vertex_count + 1):
            undirected_graph[i] = set()

        for src, targets in self._edges.items():
            for dst in targets:
                undirected_graph[src].add(dst)
                undirected_graph[dst].add(src)
        return undirected_graph

    def _bfs(self, start, graph, visited):
        queue = [start]
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def count_weak_components(self):
        visited = set()
        component_count = 0
        undirected_graph = self._build_undirected_graph()

        for vertex in range(1, self.vertex_count + 1):
            if vertex not in visited:
                component_count += 1
                visited.add(vertex)
                self._bfs(vertex, undirected_graph, visited)

        return component_count

    def _dfs(self, node, graph, visited, finish_stack=None):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self._dfs(neighbor, graph, visited, finish_stack)
        if finish_stack is not None:
            finish_stack.append(node)

    def _transpose_graph(self):
        transposed = {}
        for i in range(1, self.vertex_count + 1):
            transposed[i] = []

        for src, targets in self._edges.items():
            for dst in targets:
                transposed[dst].append(src)
        return transposed

    def count_strong_components(self):
        visited = set()
        finish_stack = []

        for vertex in range(1, self.vertex_count + 1):
            if vertex not in visited:
                self._dfs(vertex, self._edges, visited, finish_stack)

        transposed_graph = self._transpose_graph()

        visited.clear()
        component_count = 0

        while finish_stack:
            node = finish_stack.pop()
            if node not in visited:
                component_count += 1
                self._dfs(node, transposed_graph, visited)

        return component_count


def main():
    num_vertices = 9
    edges = [
        (1, 2), (1, 4), (2, 3), (2, 6),
        (3, 7), (3, 8), (4, 5), (5, 5),
        (5, 9), (6, 5), (6, 7), (7, 5),
        (7, 8), (8, 9),
    ]

    analyzer = GraphAnalyzer(num_vertices)
    for src, dest in edges:
        analyzer.add_edge(src, dest)

    print("Adjacency Matrix:")
    matrix = analyzer.get_adjacency_matrix()
    for row in matrix:
        print(row)

    weak_components = analyzer.count_weak_components()
    strong_components = analyzer.count_strong_components()

    print("\nNumber of Weakly Connected Components:", weak_components)
    print("Number of Strongly Connected Components:", strong_components)


if __name__ == "__main__":
    main()