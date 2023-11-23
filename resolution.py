from graphe import Graph
from render import Render
class Resolution:

    def __init__(self,PrimTree:Graph,x:int,y:int,render:Render):
        self.graph = PrimTree
        self.x = x
        self.y = y
        self.render = render

    def shortestPathSolving(self)->bool:

        adj = self.graph.get_adj()

        if (self.x,self.y) not in adj or (0,0) not in adj:
            return False

        founded = False
        q = [(0,0)]
        flag = {(0,0):(0)}

        while(len(q)>0 and founded == False):
            curr = q.pop(0)

            for neighboor in adj[curr]:
                if neighboor in flag:
                    continue
                flag[neighboor] = curr

                if neighboor == (self.x,self.y):
                    founded = True
                    break
                q.append(neighboor)

        if not founded:
            return False

        curr = (self.x,self.y)
        while curr != (0,0):
            next = flag[curr]
            self.render.add_segment(curr,next,color='r')
            curr = next

        return True
