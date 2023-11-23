import matplotlib.pyplot as plot
import numpy as np
from graphe import Graph
plot.gca().get_xaxis()
plot.gca().get_yaxis()
axes = plot.gca()



class Render:

    def set_axes(self, x, y):
        """Méthode qui permet de définir la borne supérieure des axes"""
        axes.set_xlim(-1,x+1)
        axes.set_ylim(-1, y+1)
        
    def add_segment(self, point1 : tuple, point2 : tuple, color : str):
        """Méthode qui permet d'ajouter un segment"""
        x1, y1 = point1
        x2, y2 = point2
        plot.gca().add_line(plot.Line2D((x1, x2), (y1, y2), color=color))

    def display(self):
        plot.show() # Affiche la figure
    
    def display_graph(self, graph : Graph):
        """Méthode qui affiche un graphe en ajoutant des segments pour chaque arête. 
        Attention afin de bien l'utiliser contrôler l'échelle des axes avant son appel"""
        dict_adj = graph.get_adj()
        for node in dict_adj.keys():
            print(node)
            for neighboor in dict_adj[node]:
                self.add_segment(node, neighboor, color='b')  # Par exemple, affiche les arêtes en bleu
        self.display()

    def display_PrimTree(self,graph:Graph):
        dict_adj = graph.get_adj()
        x,y = int(axes.get_xlim()[1]),int(axes.get_ylim()[1])

        for i in range(x):
            self.add_segment(point1=(i -0.5, -0.5), point2=(i + 0.5, -0.5), color='b')

        for j in range(y):
            self.add_segment(point1=(-0.5, j-0.5), point2=(-0.5, j+0.5), color='b')

        for i in range(x):
            for j in range(y):
                if (i,j) not in dict_adj or (i,j+1) not in dict_adj[(i,j)]:
                    self.add_segment(point1=(i-0.5,(2*j+1)/2), point2 = (i+0.5,(2*j+1)/2),color='b')

                if (i,j) not in dict_adj or (i+1,j) not in dict_adj[(i,j)]:
                    self.add_segment(point1=((2*i+1)/2,j-0.5), point2 = ((2*i+1)/2,j+0.5),color='b')

        #self.display()

    def draw_hexagonal_Maze(self,PrimTree:Graph):
        m = 0.5
        def drawTopRight(center: tuple):
            a = (center[0] + m*np.sin(0), center[1] + m*np.cos(0))
            b = (center[0] + m*np.sin(1.04719755), center[1] + m*np.cos(1.04719755))
            self.add_segment(a, b, color='b')

        def drawRight(center: tuple):
            a = (center[0] + m*np.sin(1.04719755), center[1] + m*np.cos(1.04719755))
            b = (center[0] + m*np.sin(2.0943951), center[1] + m*np.cos(2.0943951))
            self.add_segment(a, b, color='b')

        def drawBottomRight(center: tuple):
            a = (center[0] + m*np.sin(2.0943951), center[1] + m*np.cos(2.0943951))
            b = (center[0] + m*np.sin(3.14159265), center[1] + m*np.cos(3.14159265))
            self.add_segment(a, b, color='b')

        def drawBottomLeft(center: tuple):
            a = (center[0] + m*np.sin(3.14159265), center[1] + m*np.cos(3.14159265))
            b = (center[0] + m*np.sin(4.1887902), center[1] + m*np.cos(4.1887902))
            self.add_segment(a, b, color='b')

        def drawLeft(center: tuple):
            a = (center[0] + m*np.sin(4.1887902), center[1] + m*np.cos(4.1887902))
            b = (center[0] + m*np.sin(5.23598776),center[1] + m*np.cos(5.23598776))
            self.add_segment(a, b, color='b')

        def drawTopLeft(center: tuple):
            a = (center[0] + m*np.sin(5.23598776), center[1] + m*np.cos(5.23598776))
            b = (center[0] + m*np.sin(6.28318531), center[1] + m*np.cos(6.28318531))
            self.add_segment(a, b, color='b')

        dict_adj = PrimTree.get_adj()
        x, y = int(axes.get_xlim()[1]), int(axes.get_ylim()[1])

        for i in range(x+1):
            for j in range(y+1):

                if (i,j) not in dict_adj or (i+1,j) not in dict_adj[(i,j)]:
                    drawRight((i,j))
                if (i,j) not in dict_adj or (i-1,j) not in dict_adj[(i,j)]:
                    drawLeft((i,j))
                if (i,j) not in dict_adj or (i+1,j+1) not in dict_adj[(i,j)]:
                    drawTopRight((i,j))
                if (i,j) not in dict_adj or (i-1,j+1) not in dict_adj[(i,j)]:
                    drawTopLeft((i,j))
                if (i, j) not in dict_adj or (i-1, j-1) not in dict_adj[(i, j)]:
                    drawBottomLeft((i,j))
                if (i,j) not in dict_adj or (i+1,j-1) not in dict_adj[(i,j)]:
                    drawBottomRight((i,j))

if __name__ == "__main__":
    render = Render()
    
    # Ajout de quelques segments de test
    render.add_segment((1, 1), (2, 2), color='r')
    render.add_segment((2, 2), (3, 1), color='g')
    
    # Affichage de la figure
    render.display()

