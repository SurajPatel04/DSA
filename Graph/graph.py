class Graph:
    def __init__(self):
        self.adj_list = {}
        
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    
    def print_grapgh(self):
        for vertex in self.adj_list:
            print(vertex, ': ', self.adj_list[vertex])

    def add_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            
            # Loop in the D: [A,B, C]
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
            
graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edges("A","B")
graph.add_edges("A","C")
graph.add_edges("A","D")
graph.add_edges("B","D")
graph.add_edges("C","D")

print("Before Remove\n")
graph.print_grapgh()

print("\nAfter reomve\n")
graph.remove_vertex("D")
graph.print_grapgh()