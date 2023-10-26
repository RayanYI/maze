class Graph :   

    def __init__(self):
        self.adj = {} #Dictionnaire dont les clés sont les noeuds du graphe. Pour chaque clé on a une liste de voisins associée
        self.weight = {} #Dictionnaire dont les clés sont des tuples de noeuds et les valeurs associés sont le poids de l'arête formée

    def is_in_graph(self, sommet):
        """Méthode qui vérifie si un sommet est dans le graphe"""
        return sommet in self.adj.keys()  #Retourne un booléen
    
    def get_adj(self):
        return self.adj
    
    def add_sommet(self, sommet):
        if not self.is_in_graph(sommet):
            self.adj[sommet]=[]

    def arc_in_graph(self,u, v):
        """Méthode qui donne la présence de l'arc (u,v)"""
        return (u,v) in self.poids.keys()   

    def presence_arete(self,u, v):
        """Méthode qui donne la présence de l'arc (u,v) dans le graphe"""
        return (u,v) in self.weight.keys() and (v,u) in self.weight.keys()       


    def add_arc(self, arc, p):
        u = arc[0]  #initialisation de variables représentant les sommets de l'arc
        v = arc[1]
        if (self.is_in_graph(u)) and (self.est_dans_graphe(v)) and (arc not in self.poids.keys()):    #on vérifie si les deux sommets sont dans le graphe et si l'arc n'existe pas déjà
            self.adj[u].append(v) #modification des listes d'adjacences respectives
            self.weight[arc] = p #ajout d'un arc pondéré

    def add_arete(self, sommets, p):
        u = sommets[0]
        v = sommets[1]
        self.add_arc((u,v),p)
        self.add_arc((v,u),p)    #Une arete est en fait 2 arcs qui vont dans les 2 sens
    
    def copy_liste_sommet(self):
        return list(self.adjacence.keys)
    
    def child(self, sommet):
        return self.adj[sommet]
    
    def set_weight_arc(self, arc, new_p):
        self.weight[arc] = new_p

    def set_weight_arete(self, sommets, new_p):
        u = sommets[0]
        v = sommets[1]
        self.set_weight_arc((u,v), new_p)
        self.set_weight_arc((v,u), new_p)
        
    def get_weight_arc(self, arc):
        return self.weight[arc]
    
    def set_arete(self, sommets, p):
        self.add_arete(sommets, p)
        self.set_weight_arete(sommets, p)