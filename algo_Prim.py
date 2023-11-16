from graphe import Graph
from math import inf

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
        
    def prim(self):
        for sommet in self.graph.copy_liste_sommet():
            self.cost[sommet]=inf
            self.parent[sommet]=None
        queue = self.graph.copy_liste_sommet()
        while queue != []:
            queue_costs = []
            for sommet in queue:
                queue_costs.append(self.cost[sommet])
            index_mini = self.minimal(queue_costs)
            sommet_mini=queue[index_mini]

            childs = self.adj[sommet_mini]
            for child in childs :
                if (child in queue) and (self.graph.get_weight_arc((sommet_mini, child))< self.cost[child]):
                    self.cost[child] = self.graph.get_weight_arc((sommet_mini, child))
                    self.parent[child] = sommet_mini
            queue.pop(index_mini)
        return self.parent

    def generate_tree(self, graph : Graph, weight  : dict) -> Graph:
        dict_tree = self.prim()
        tree = Graph()
        for child in dict_tree.keys():
            parent = dict_tree[child]
            tree.add_sommet(child)
            if parent != None : 
                tree.add_arete((child, parent), weight[(child, parent)])
        return tree


    
    


