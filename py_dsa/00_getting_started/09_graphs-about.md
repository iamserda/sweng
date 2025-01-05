# 9. Graphs

## README for Graphs

Graphs are a powerful and versatile data structure that represents a set of nodes (also called vertices) and the connections (edges) between them. They are used to model real-world problems involving pairwise relationships among objects. Graphs can be directed (where edges have direction) or undirected (where edges do not have direction) and can include cycles or be acyclic. Edges can also have weights, making these structures incredibly useful for representing networks like roads, telecommunications, and social networks.

### Key Concepts
- **Vertex**: A node in the graph.
- **Edge**: A connection between two vertices in the graph.
- **Path**: A sequence of vertices where each adjacent pair is connected by an edge.
- **Cycle**: A path that starts and ends at the same vertex.
- **Weighted Graphs**: Graphs where edges have weights or costs associated with them.
- **Directed Graphs (Digraphs)**: Graphs where edges have directions.
- **Undirected Graphs**: Graphs where edges do not have directions.

### Key Operations
- **Add Vertex**: Add a new vertex to the graph.
- **Add Edge**: Add a new edge to the graph connecting two vertices.
- **Find Path**: Determine a path from one vertex to another.
- **Search**: Perform a search (e.g., breadth-first search or depth-first search) across the graph.

### Use Cases
- Modeling networks (social networks, computer networks, etc.).
- Pathfinding algorithms (e.g., GPS navigation).
- Flow networks (e.g., determining the maximum flow in a network).

### Python Implementation
A simple way to represent a graph in Python is using a dictionary for an adjacency list, where keys are vertices and values are lists of neighbors.

```python
class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, src, dest):
        if src not in self.graph:
            self.add_vertex(src)
        if dest not in self.graph:
            self.add_vertex(dest)
        self.graph[src].append(dest)
        if not self.directed:
            self.graph[dest].append(src)

    def find_path(self, start_vertex, end_vertex, path=None):
        if path is None:
            path = []
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in self.graph:
            return None
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                extended_path = self.find_path(neighbor, end_vertex, path)
                if extended_path: 
                    return extended_path
        return None

# Example usage
graph = Graph(directed=True)
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_edge("A", "B")
print(graph.find_path("A", "B"))  # Output: ['A', 'B']
```

## Further Steps
- Explore different graph representations (e.g., adjacency matrices, edge lists) and their use cases.
- Implement graph algorithms like Dijkstra's algorithm for shortest path, breadth-first search (BFS), and depth-first search (DFS).

Graphs are a fundamental data structure in computer science, useful for solving a wide variety of problems where relationships between pairs of objects need to be represented and analyzed. Tries are next!