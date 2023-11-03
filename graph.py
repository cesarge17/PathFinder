class graph:
    def __init__(self):
        self.graph_dict = {}
    def add_nodo(self, nodo):
        self.graph_dict[nodo] = []
    def add_arista(self, arista):
        n1 = arista.get_n1()
        n2 = arista.get_n2()
        self.graph_dict[n1].append(n2)
        self.graph_dict[n2].append(n1)
    def get_aristas(self):
        return self.graph_dict


class nodo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __str__(self):
        return f"({self.x},{self.y})"
    
class arista:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def get_n1(self):
        return self.n1
    def get_n2(self):
        return self.n2
    def __str__(self):
        return f"({self.n1.__str__()}, {self.n2.__str__()})"