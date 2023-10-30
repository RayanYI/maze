class Graph :   

    def __init__(self):
        self.adj = {} #Dictionnaire dont les clés sont les noeuds du graphe. Pour chaque clé on a une liste de voisins associée
        self.weight = {} #Dictionnaire dont les clés sont des tuples de noeuds et les valeurs associés sont le poids de l'arête formée

    def is_in_graph(self, sommet : str or int) -> bool :
        """Méthode qui vérifie si un sommet est dans le graphe"""
        return sommet in self.adj.keys()  #Retourne un booléen
    
    def get_adj(self) -> dict:
        """Méthode qui renvoie le dictionnaire d'ajacence du graphe"""
        return self.adj
    
    def add_sommet(self, sommet : str or int):
        """Méthode qui ajoute un sommet dans le graphe"""
        if not self.is_in_graph(sommet):
            self.adj[sommet]=[]

    def arc_in_graph(self,u :str or int, v : str or int) -> bool:
        """Méthode qui donne la présence de l'arc (u,v)"""
        return (u,v) in self.poids.keys()   

    def presence_arete(self,u : str or int, v: str or int) -> bool:
        """Méthode qui donne la présence de l'arc (u,v) dans le graphe"""
        return (u,v) in self.weight.keys() and (v,u) in self.weight.keys()       


    def add_arc(self, arc : tuple, p : int):
        """Méthode qui ajoute un arc de sommets dans les dictionnaires du graphes avec un poids donné"""
        u = arc[0]  #initialisation de variables représentant les sommets de l'arc
        v = arc[1]
        if (self.is_in_graph(u)) and (self.is_in_graph(v)) and (arc not in self.weight.keys()):    #on vérifie si les deux sommets sont dans le graphe et si l'arc n'existe pas déjà
            self.adj[u].append(v) #modification des listes d'adjacences respectives
            self.weight[arc] = p #ajout d'un arc pondéré

    def add_arete(self, sommets : tuple, p : int):
        """Méthode qui ajoute une arête connectant les sommets indiqués avec un poids donné"""
        u = sommets[0]
        v = sommets[1]
        self.add_arc((u,v),p)
        self.add_arc((v,u),p)    #Une arete est en fait 2 arcs qui vont dans les 2 sens
    
    def copy_liste_sommet(self) -> list:
        """Méthode qui renvoie une copie de la liste des sommets"""
        return list(self.adjacence.keys)
    
    def child(self, sommet : int or str) -> list:
        return self.adj[sommet]
    
    def set_weight_arc(self, arc : tuple, new_p : int):
        """Méthode qui modifie le poids d'un arc"""
        self.weight[arc] = new_p

    def set_weight_arete(self, sommets : tuple, new_p : int):
        """Méthode qui modifie le poids d'une arête, donc de deux arcs"""
        u = sommets[0]
        v = sommets[1]
        self.set_weight_arc((u,v), new_p)
        self.set_weight_arc((v,u), new_p)
        
    def get_weight_arc(self, arc : tuple) -> int:
        """Méthode qui donne le poids d'un arc indiqué"""
        return self.weight[arc]
    
    def set_arete(self, sommets : tuple, p : int):
        """Méthode qui crée une arête connectant les sommets indiqués et ayant un poids donné au préalable"""
        self.add_arete(sommets, p)
        self.set_weight_arete(sommets, p)