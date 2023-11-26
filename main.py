from render import *
from algo_Prim import *
from resolution import Resolution

grille = Generation()
hexa = input("Souhaitez-vous générer un labyrinthe Hexagonale (Oui : O)")
height = int(input("Quelle est la hauteur du labyrinthe souhaitée ?"))
width = int(input("Quelle est la largeur du labyrinthe souhaitée ?"))
biasis = None
if hexa !='O':
    biasis= input("Souhaitez-vous induire un biais (Si oui indiquer : O)")

if biasis == "O":
    horizontal_biasis = float(input("Indiquez les valeurs du biais horizontal"))
    vertical_biasis = float(input("Indiquer les valeurs du biais vertical"))
    grille.dico_grid_weighted_biaise(width, height,vertical_biasis, horizontal_biasis)
elif hexa!='O':
    grille.dico_grid_weighted(width, height)
else:
    grille.dico_hexagonal_grid_weighted(width, height)

prim = Algo(grille.graph)
laby=prim.generate_tree(grille.graph, grille.graph.weight)
aff = Render()
res = Resolution(laby,aff)

if hexa == 'O':
    aff.set_hexagonal_axes(width, height)
    aff.draw_hexagonal_Maze(laby)
    target = (width - (width % np.sqrt(3)), height - (height % 1.5))  # coordonnées du centre de la sortie
    if (((height - (height % 1.5)) / 1.5)) % 2 != 0:  # si le nombre de ligne est impair
        target = (width - (width % np.sqrt(3)) + np.sqrt(3) / 2, height - (height % 1.5))
    res.shortestPathSolving(target=target)

else:
    aff.set_axes(width, height)
    aff.display_PrimTree(laby)
    res.shortestPathSolving(target=(width, height))

aff.display()