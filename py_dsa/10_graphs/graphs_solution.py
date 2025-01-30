class Graph:
    def __init__(self):
        self.adjancy_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjancy_list.keys():
            self.adjancy_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex_one, vertex_two):
        if vertex_one and vertex_two in self.adjancy_list:
            adj_set1 = set(self.adjancy_list[vertex_one])
            adj_set2 = set(self.adjancy_list[vertex_two])
            if vertex_two not in adj_set1:
                self.adjancy_list[vertex_one].append(vertex_two)
                if vertex_one not in adj_set2:
                    self.adjancy_list[vertex_two].append(vertex_one)
                    return True
        return False

    def print_adjency_list(self):
        for vertex, adj_list in self.adjancy_list.items():
            print(f"{vertex}: {adj_list}")

# Testing Arenas
my_graph = Graph()
assert my_graph.add_vertex("MJ23") is True
assert my_graph.add_vertex("LJ23") is True
my_graph.print_adjency_list()

assert my_graph.add_edge("LJ23", "MJ23") is True
my_graph.print_adjency_list()
