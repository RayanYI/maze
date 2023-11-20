from generation_grille import *
from render import *
from algo_Prim import *

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