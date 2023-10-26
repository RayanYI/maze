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

    def presence_arc(self,u, v):
        """Méthode qui donne la présence de l'arc (u,v)"""
        return (u,v) in self.poids.keys()   

    def presence_arete(self,u, v):
        """Méthode qui donne la présence de l'arc (u,v) dans le graphe"""
        return (u,v) in self.poids.keys() and (v,u) in self.poids.keys()       


    def ajoute_arc(self, arc, p):
        u = arc[0]  #initialisation de variables représentant les sommets de l'arc
        v = arc[1]
        if (self.est_dans_graphe(u)) and (self.est_dans_graphe(v)) and (arc not in self.poids.keys()):    #on vérifie si les deux sommets sont dans le graphe et si l'arc n'existe pas déjà
            self.adjacence[u].append(v) #modification des listes d'adjacences respectives
            self.poids[arc] = p #ajout d'un arc pondéré

    def ajoute_arete(self, sommets, p):
        u = sommets[0]
        v = sommets[1]
        self.ajoute_arc((u,v),p)
        self.ajoute_arc((v,u),p)    #Une arete est en fait 2 arcs qui vont dans les 2 sens
    
    def copie_liste_sommet(self):
        return list(self.adjacence.keys)
    
    def sucesseurs(self, sommet):
        return self.adjacence[sommet]
    
    def set_poids_arc(self, arc, nouveau_p):
        self.poids[arc] = nouveau_p

    def set_poids_arete(self, sommets, nouveau_p):
        u = sommets[0]
        v = sommets[1]
        self.set_poids_arc((u,v), nouveau_p)
        self.set_poids_arc((v,u), nouveau_p)
        
    def get_poids_arc(self, arc):
        return self.poids[arc]
    
    def set_arete(self, sommets, p):
        self.ajoute_arete(sommets, p)
        self. set_poids_arete(sommets, p)
