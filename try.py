class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def add_vertes(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def printGraph(self):
        if self.adj_list is not None:
            for v in self.adj_list:
                print(v, ": ", self.adj_list[v])
                
    def add_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def  remove_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v1].remove(v2)

graph = Graph()
graph.add_vertes("A")
graph.add_vertes("B")
graph.add_vertes("C")
graph.add_vertes("D")
graph.add_vertes("E")

graph.add_edges("A","B")
graph.add_edges("A","E")
graph.add_edges("B","C")
graph.add_edges("D","C")
graph.add_edges("D","E")

graph.printGraph()