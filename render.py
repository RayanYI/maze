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
    def set_hexagonal_axes(self,x,y):
        axes.set_xlim(-3/2, x + 3/2)
        axes.set_ylim(-3/2, y + 3/2)
        
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
        def pointy_hex_corner(center, size, i):
            angle_deg = 60 * i - 30
            angle_rad = np.pi / 180 * angle_deg
            return (center[0] + size * np.cos(angle_rad), center[1] + size * np.sin(angle_rad))

        def getCenter(i,j):
            x, y = i * np.sqrt(3), j * (6 / 4)
            if j % 2 != 0:
                x += np.sqrt(3) / 2
            return (x,y)

        dict_adj = PrimTree.get_adj()
        #print(dict_adj)
        x, y = int(axes.get_xlim()[1])-1, int(axes.get_ylim()[1])-1
        #print(x,y)
        moveOdd = [(1,1),(0,1),(-1,0),(0,-1),(1,-1),(1,0)]
        moveEven = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,0)]

        """
        top right (1,2)
        top left(2,3)
        left(3,4)
        bottomLeft(4,5)
        bottomRight(5,6)
        right(6,7)
        """

        i=0
        while getCenter(i,0)[0]<=x:
            j=0
            while getCenter(0,j)[1]<=y:
                center = getCenter(i, j)
                #print(getCenter(0,j),y)
                if j % 2 != 0:
                    # print("odd")
                    for k in range(len(moveOdd)):
                        next = getCenter(i + moveOdd[k][0], j + moveOdd[k][1])
                        if next[0]<=x+3 and next[1]<=y+3 and (center not in dict_adj or next not in dict_adj[center]):
                            self.add_segment(pointy_hex_corner(center, 1, k + 1), pointy_hex_corner(center, 1, k + 2),color='b')
                            #print(f"odd{center, i, j, getCenter(i + moveOdd[k][0], j + moveOdd[k][1])}")
                else:
                    for k in range(len(moveEven)):
                        # print("even")
                        next = getCenter(i + moveEven[k][0], j + moveEven[k][1])
                        if next[0]<=x+3 and next[1]<=y+3 and (center not in dict_adj or next not in dict_adj[center]):
                            self.add_segment(pointy_hex_corner(center, 1, k + 1), pointy_hex_corner(center, 1, k + 2),color='b')
                            #print(f"even {center, getCenter(i + moveEven[k][0], j + moveEven[k][1])}")
                j+=1
            i+=1

if __name__ == "__main__":
    render = Render()
    
    # Ajout de quelques segments de test
    render.add_segment((1, 1), (2, 2), color='r')
    render.add_segment((2, 2), (3, 1), color='g')
    
    # Affichage de la figure
    render.display()

