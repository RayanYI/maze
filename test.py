from generation_grille import Generation
from render import Render



#Il faut mettre en commentaire le test non choisi sinon pb d'échelle des axes

test1= Generation()
aff = Render()
aff.set_axes(4, 6)
test1.dico_grid_not_weighted(4, 6)
aff.display_graph(test1.graph)

test2 = Generation()
aff2 = Render()
aff2.set_axes(8, 4)
test2.dico_grid_weighted(8, 4)
aff2.display_graph(test2.graph)