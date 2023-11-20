from graphe import Graph
from random import Random


class Generation : 
    def __init__(self):
        self.graph = Graph()
        self.width = 0
        self.height = 0
    
    def dico_grid_not_weighted(self, width : int, height : int) -> tuple :
        """Méthode qui renvoie les dictionnaires de poids et d'ajdacence du graphe non pondéré d'une grille de largeur et de hauteur spécifiées"""
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        self.width = width
        self.height = height
        p = 1   #Non pondéré donc on met le poids à 1 pour toutes les arêtes car on doit malgré tout utiliser un poids
        for i in range(height+1):   #Doubles boucles qui parcourent les cases de la grille
            for j in range(width+1):  # +1 car on a besoin du nombre de cases +1 pour tout connecter et former une grille d'effectivement largeur sur hauteur
                x = j
                y = i
                case_courante= (x, y)
                self.graph.add_sommet(case_courante)   #Ajout d'une case
                for move in moves:
                    self.graph.add_arete((case_courante, (x+move[0], y+move[1])), p)

        return self.graph.get_adj(), self.graph.weight
    
    def dico_grid_weighted(self, width : int, height : int) -> tuple :
        """Méthode qui renvoie les dictionnaires de poids et d'ajdacence du graphe pondéré aléatoirement d'une grille de largeur et de hauteur spécifiées"""
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        self.width = width
        self.height = height
        for i in range(height+1):
            for j in range(width+1):
                random= Random()
                p = random.uniform(0,1) 
                x = j
                y = i
                case_courante= (x, y)
                self.graph.add_sommet(case_courante)
                for move in moves:
                    self.graph.add_arete((case_courante, (x+move[0], y+move[1])), p)
        return self.graph.get_adj(), self.graph.weight


    def dico_grid_weighted_biaise(self, width : int, height : int, biaise_x:int = 0, biaise_y:int = 0) -> tuple :
        """Méthode qui renvoie les dictionnaires de poids biaisé et
         d'ajdacence du graphe pondéré aléatoirement
         d'une grille  de largeur et de hauteur spécifiées """
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.width = width
        self.height = height
        for i in range(height + 1):
            for j in range(width + 1):
                random = Random()
                p = random.uniform(0, 1)
                x = j
                y = i
                case_courante = (x, y)
                self.graph.add_sommet(case_courante)
                for move in moves:
                    # si on se deplace horizontalement on ajoute biaise_x a p sinon biaise_y
                    self.graph.add_arete((case_courante, (x + move[0], y + move[1])), p+abs(move[0])*biaise_x+abs(move[1])*biaise_y)

        return self.graph.get_adj(), self.graph.weight

    def dico_hexagonal_grid_weighted(self, width: int, height: int) -> tuple:
        """Méthode qui renvoie les dictionnaires de poids et d'ajdacence du graphe pondéré aléatoirement d'une grille de largeur et de hauteur spécifiées"""
        moves = [(1, 0), (-1, 0), (1, 1), (-1, 1),(-1,-1),(1,-1)]
        self.width = width
        self.height = height
        for i in range(height + 1):
            for j in range(width + 1):
                random = Random()
                p = random.uniform(0, 1)
                x = j
                y = i
                case_courante = (x, y)
                self.graph.add_sommet(case_courante)
                for move in moves:
                    if x+move[0] >= 0 and x+move[0] <=width and y+move[1] >=0 and y+move[1] <=height:
                        self.graph.add_arete((case_courante, (x + move[0], y + move[1])), p)

        return self.graph.get_adj(), self.graph.weight