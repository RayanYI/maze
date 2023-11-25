from generation_grille import Generation
from graphe import Graph
from render import Render
from math import inf
from algo_Prim import Algo
from resolution import Resolution


#Test de graphe
graphe1=Graph()
graphe1.add_sommet("A")
graphe1.add_sommet("B")
graphe1.add_sommet("C")
graphe1.add_sommet("D")
graphe1.add_arete(("A","B"), 2)
graphe1.add_arete(("A","D"), 1)
graphe1.add_arete(("D","B"), 2)
graphe1.add_arete(("C","D"), 2)
print(graphe1.get_adj(), graphe1.weight)



#Il faut mettre en commentaire le test non choisi sinon pb d'échelle des axes

"""test1= Generation()
aff = Render()
aff.set_axes(4, 6)
test1.dico_grid_not_weighted(4, 6)
aff.display_graph(test1.graph)
"""

test2 = Generation()
aff2 = Render()
aff2.set_axes(10, 10)
test2.dico_grid_weighted(10,10)
"""#aff2.display_graph(test2.graph)"""

test = Generation()
test.dico_grid_weighted(2, 2)


test= Graph()
algo=Algo(test2.graph)
print(algo.prim())
tree=algo.generate_tree(test2.graph, test2.graph.weight)
print(tree.adj)
print(algo.parent)
aff2.display_PrimTree(tree)
res=Resolution(tree, 10, 10, aff2)
res.shortestPathSolving()
aff2.display()

