class Graph :   
    def __init__(self):
        self.adjacence = {} #Dictionnaire dont les clés sont les noeuds du graphe. Pour chaque clé on a une liste de voisins associée
        self.poids = {} #Dictionnaire dont les clés sont des tuples de noeuds et les valeurs associés sont le poids de l'arête formée

    def est_dans_graphe(self, sommet):
        """Méthode qui vérifie si un sommet est dans le graphe"""
        return sommet in self.adjacence.keys()  #Retourne un booléen
    
    def get_adjacence(self):
        return self.adjacence
    
    def ajoute_sommet(self, sommet):
        if not self.est_dans_graphe(sommet):
            self.adjacacence[sommet]=[]

    def ajoute_arc(self, arc, p):
        u = arc[0]  #initialisation de variables représentant les sommets de l'arc
        v = arc[1]
        if (self.est_dans_graphe(u)) and (self.est_dans_graphe(v)) and (arc not in self.poids.keys()):    #on vérifie si les deux sommets sont dans le graphe et si l'arc n'existe pas déjà
            self.adjacence[u].append(v) #modification des listes d'adjacences respectives
            self.poids[arc] = p #ajout d'un arc pondéré

    def ajoute_arete(self, sommets):
        self.ajoute_ar
        
