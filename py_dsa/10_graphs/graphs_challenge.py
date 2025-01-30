class Graph:
    def __init__(self):
        self.adjency_list_dictio = {}
    
    def add_new_vertex(self, vertex):
        if vertex not in self.adjency_list_dictio.keys():
            self.adjency_list_dictio[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex_key, adj_list in self.adjency_list_dictio.items():
            print(f"{vertex_key}: {adj_list}")
            
    

my_graph = Graph()

assert my_graph.add_new_vertex("MJ23") == True
assert my_graph.add_new_vertex("LJ23") == True
my_graph.adjency_list_dictio.get("KB24")
my_graph.print_graph()
