from generation_grille import Generation
from graphe import Graph
from render import Render
from math import inf
from algo_Prim import Algo



#Il faut mettre en commentaire le test non choisi sinon pb d'échelle des axes

"""test1= Generation()
aff = Render()
aff.set_axes(4, 6)
test1.dico_grid_not_weighted(4, 6)
aff.display_graph(test1.graph)
ex1 = Algo(test1.graph)

print(ex1.prim())"""

test2 = Generation()
aff2 = Render()
aff2.set_axes(14, 15)
test2.dico_grid_weighted(14,15)
"""#aff2.display_graph(test2.graph)"""

test = Generation()
test.dico_grid_weighted(2, 2)

###Test de Prim##
test= Graph()
algo=Algo(test2.graph)
print(algo.prim())
tree=algo.generate_tree(test2.graph, test2.graph.weight)
print(tree.adj)
aff2.display_PrimTree(tree)
