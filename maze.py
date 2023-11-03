import graph

class maze:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
        fila = [True] *width
        self.visitados = [[fila]*height]
    def get_visitados(self):
        return self.visitados


maze = maze(5,130)
print( maze.get_visitados())