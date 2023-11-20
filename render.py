import matplotlib.pyplot as plot
from graphe import Graph
plot.gca().get_xaxis()
plot.gca().get_yaxis()
axes = plot.gca()
#axes = plot.gca()


class Render:

    def set_axes(self, x, y):
        """Méthode qui permet de définir la borne supérieure des axes"""
        axes.set_xlim(0,x)
        axes.set_ylim(0, y)
        
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

        for i in range(x+1):
            for j in range(y+1):
                if (i,j) not in dict_adj or (i,j+1) not in dict_adj[(i,j)]:
                    self.add_segment(point1=(i-0.5,(2*j+1)/2), point2 = (i+0.5,(2*j+1)/2),color='r')

                if (i,j) not in dict_adj or (i+1,j) not in dict_adj[(i,j)]:
                    self.add_segment(point1=((2*i+1)/2,j-0.5), point2 = ((2*i+1)/2,j+0.5),color='b')

        #self.display()


if __name__ == "__main__":
    render = Render()
    
    # Ajout de quelques segments de test
    render.add_segment((1, 1), (2, 2), color='r')
    render.add_segment((2, 2), (3, 1), color='g')
    
    # Affichage de la figure
    render.display()

