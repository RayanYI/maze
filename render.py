import matplotlib.pyplot as plot
from graphe import Graph
plot.gca().get_xaxis()
plot.gca().get_yaxis()
axes = plot.gca()
axes = plot.gca()


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
        
        
if __name__ == "__main__":
    render = Render()
    
    # Ajout de quelques segments de test
    render.add_segment((1, 1), (2, 2), color='r')
    render.add_segment((2, 2), (3, 1), color='g')
    
    # Affichage de la figure
    render.display()

