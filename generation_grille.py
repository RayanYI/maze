from graphe import Graph
from random import Random


class Generation : 
    def __init__(self):
        self.graph = Graph()
    
    def dico_grid_not_weighted(self, width : int, height : int) -> tuple :
        """Méthode qui renvoie les dictionnaires de poids et d'ajdacence du graphe non pondéré d'une grille de largeur et de hauteur spécifiées"""
        p = 1   #Non pondéré donc on met le poids à 1 pour toutes les arêtes car on doit malgré tout utiliser un poids
        for i in range(height+1):
            for j in range(width+1):  #Doubles boucles qui parcourent les cases de la grille
                x = j
                y = i
                case_courante= (x, y)
                self.graph.add_sommet(case_courante)   #Ajout d'une case
                self.graph.add_arete((case_courante, (x+1, y)), p)   #On essaie d'ajouter une arête à chaque case adjacente du graphe
                self.graph.add_arete((case_courante, (x-1, y)), p)
                self.graph.add_arete((case_courante, (x, y+1)), p )
                self.graph.add_arete((case_courante, (x, y-1)) , p)
        return self.graph.get_adj(), self.graph.weight
    
    def dico_grid_weighted(self, width : int, height : int) -> tuple :
        """Méthode qui renvoie les dictionnaires de poids et d'ajdacence du graphe pondéré aléatoirement d'une grille de largeur et de hauteur spécifiées"""  
        for i in range(height+1):
            for j in range(width+1):
                random= Random()
                p = random.uniform(0,1) 
                x = j
                y = i
                case_courante= (x, y)
                self.graph.add_sommet(case_courante)   
                self.graph.add_arete((case_courante, (x+1, y)), p)  
                self.graph.add_arete((case_courante, (x-1, y)), p)
                self.graph.add_arete((case_courante, (x, y+1)), p )
                self.graph.add_arete((case_courante, (x, y-1)) , p)
        return self.graph.get_adj(), self.graph.weight


        