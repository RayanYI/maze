from graphe import Graph
from math import inf
from generation_grille import Generation
from render import Render 

class Algo :


    def __init__(self, graph : Graph ):
        self.graph = graph
        self.adj = self.graph.get_adj()
        self.cost= {}
        self.parent = {}

    def minimal(self, liste : list) -> int :
        """'Méthode qui retourne l'indice de l'élément minimal d'une liste """
        if liste != []:
            mini = liste[0]
            index = 0
            for i in range(1, len(liste)):
                if liste[i]< mini:
                    mini = liste[i]
                    index = i
            return index
        
    def prim(self)-> Graph: 
        """Méthode qui exécute l'algorithme de Prim sur le graphe associé à Algo"""
        for sommet in self.graph.copy_liste_sommet():   #On initialise les coûts et parents de noeuds
            self.cost[sommet]=inf
            self.parent[sommet]=None
        queue = self.graph.copy_liste_sommet()  #On initialise la file
        while queue != []:
            queue_costs = []    #On a besoin d'une liste qui contient les coûts des sommets de la file dans le même ordre, donc on a la réinitialise à chaque coût
            for sommet in queue:    
                queue_costs.append(self.cost[sommet])   
            index_mini = self.minimal(queue_costs)  #On récupère l'indice du plus petit sommet avec la méthode minimal
            sommet_mini=queue[index_mini]   #On peut le trouver car les indices des éléments de queue_costs correspondent aux éléments de queue
            childs = self.adj[sommet_mini]
            for child in childs :
                if (child in queue) and (self.graph.get_weight_arc((sommet_mini, child))< self.cost[child]):
                    self.cost[child] = self.graph.get_weight_arc((sommet_mini, child))  #On définit le poids et le parent unique en fonction pour chaque enfant si on trouve un arc assez court dans notre graphe initial
                    self.parent[child] = sommet_mini
            queue.pop(index_mini)   #On supprime le sommet minimal et pas avant car sinon on a une disjonction entre queue_costs et queue
        return self.parent  #Renvoi a priori inutile mais demandé... 

    def generate_tree(self, graph : Graph, weight  : dict) -> Graph:
        """Méthode qui renvoie le graphe associé à l'arbre dont on a défini les arêtes et les poids avec la méthode prim"""
        dict_tree = self.prim()
        tree = Graph()  #Un arbre est un graphe vérifiant certaines propriétés
        for child in dict_tree.keys():
            tree.add_sommet(child)
        for child in dict_tree.keys():
            tree.add_arete((dict_tree[child], child), self.cost[child])

            
        return tree
    



