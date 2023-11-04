from graph import *
import random

class maze:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.maze_graph = graph()

    def get_maze_graph(self):
        return self.maze_graph

    def create_maze(self):
        
        visited = [[False] * self.width for _ in range(self.height)]
        stack = []
        
        
        current_node = node(0, 0)
        stack.append(current_node)
        self.maze_graph.add_node(current_node) 
        visited[current_node.get_x()][current_node.get_y()] = True      
        
        while True:
            next_node = self.select_neighbour(current_node.get_x(), current_node.get_y(), visited)
            
           

            if next_node!=None:
                stack.append(next_node)
                self.maze_graph.add_node(next_node)
                self.maze_graph.add_edge(edge(current_node, next_node))
                current_node = next_node
                visited[current_node.get_x()][current_node.get_y()] = True      

            else:
                stack.pop()
                if stack:
                    current_node = stack[-1]

            for edges, manuel in self.maze_graph.get_edges():
                print(edges.__str__())
                
                

            user_input = input()

            if not stack:
                break

        
        



    def select_neighbour(self, current_x, current_y, visited):
        directions  = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        if current_x<=0:
            directions.remove((-1,0))
        if current_y<=0:
            directions.remove((0,-1))
        if current_x>=self.height-1 :
            directions.remove((1,0))
        if current_y>=self.width-1 :
            directions.remove((0,1))

        for choices in directions.copy():
            if(visited[current_x + choices[0]][current_y + choices[1]]==True):
                directions.remove(choices)
        
        
        if(not directions):
            return None
        
        else:
            direction = random.choice(directions)
            return node(current_x + direction[0], current_y + direction[1])
        
mari = maze(5, 5)


mari.create_maze()