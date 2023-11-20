from generation_grille import *
from render import *
from algo_Prim import *
from resolution import Resolution
from graphe import Graph

#Labyrinthe Normal
""""
grille = Generation()
height = int(input("Quelle est la hauteur du labyrinthe souhaitée ?"))
width = int(input("Quelle est la largeur du labyrinthe souhaitée ?"))
biasis = input("Souhaitez-vous induire un biais (Si oui indiquer : O)")
if biasis == "O":
    horizontal_biasis = int(input("Indiquez les valeurs du biais horizontal"))
    vertical_biasis = int(input("Indiquer les valeurs du biais vertical"))
    grille.dico_grid_weighted_biaise(width, height,horizontal_biasis, vertical_biasis)
else:
    grille.dico_grid_weighted(width, height)

prim = Algo(grille.graph)
laby=prim.generate_tree(grille.graph, grille.graph.weight)
aff = Render()
aff.set_axes(width, height)
aff.display_PrimTree(laby)
res = Resolution(laby,width,height,aff)
res.shortestPathSolving()
aff.display()"""

#Labyrinthe Hexagonale

grille = Generation()
grille.dico_hexagonal_grid_weighted(20,20)
prim = Algo(grille.graph)
laby=prim.generate_tree(grille.graph, grille.graph.weight)
aff = Render()
aff.set_axes(20, 20)
g = Graph()
aff.draw_hexagonal_Maze(laby)
res = Resolution(laby,20,20,aff)
res.shortestPathSolving()
aff.display()