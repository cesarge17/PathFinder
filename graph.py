class graph:
    def __init__(self):
        self.graph_dict = {}
    def add_node(self, node):
        self.graph_dict[node] = []
    def add_edge(self, edge):
        n1 = edge.get_n1()
        n2 = edge.get_n2()
        self.graph_dict[n1].append(n2)
        self.graph_dict[n2].append(n1)
    def get_edges(self):
        return self.graph_dict


class node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __str__(self):
        return f"({self.x},{self.y})"
    
class edge:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def get_n1(self):
        return self.n1
    def get_n2(self):
        return self.n2
    def __str__(self):
        return f"({self.n1.__str__()}, {self.n2.__str__()})"
    

""""
graph = graph()


node1 = node(1,2)
node2 = node(3,4)


graph.add_node(node1)
graph.add_node(node2)

graph.add_edge(edge(node1, node2))

for node in graph.get_edges().values():
    for value in node:
        print(value) 
"""