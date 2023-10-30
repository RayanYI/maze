import matplotlib.pyplot as plot
from graphe import Graph

class render:
    
    def __init__(self):
        # Crée une nouvelle figure pour le rendu
        self.fig, self.ax = plot.subplots()
        self.ax.axis('scaled')  # Permet d'obtenir un cadrage correct
        
    def add_segment(self, point1 : tuple, point2 : tuple, color : str):
        """Méthode qui permet d'ajouter un segment"""
        x1, y1 = point1
        x2, y2 = point2
        plot.gca().add_line(plot.Line2D((x1, x2), (y1, y2), color=color))
        
    def display(self):
        plot.show() # Affiche la figure
    
    def display_graph(self, graph : Graph):
        """Méthode qui affiche un graphe en ajoutant des segments pour chaque arête"""
        for node, edges in graph.items():
            for neighbor, weight in edges.items():
                self.add_segment(node, neighbor, color='b')  # Par exemple, affiche les arêtes en bleu
        self.display()
        
        
if __name__ == "__main__":
    render = render()
    
    # Ajout de quelques segments de test
    render.add_segment((1, 1), (2, 2), color='r')
    render.add_segment((2, 2), (3, 1), color='g')
    
    # Affichage de la figure
    render.display()

