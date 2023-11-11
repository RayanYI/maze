from graphe import Graph
from render import Render
class Resolution:

    def __init__(self,PrimTree:Graph,x:int,y:int,render:Render):
        self.graph = PrimTree
        self.x = x
        self.y = y
        self.render = render

    def shortestPathSolving(self)->bool:
        if (self.x-1,self.y-1) not in self.graph.get_adj() or (0,0) not in self.graph.get_adj():
            return False
        founded = False
        q = [(0,0)]
        flag = {(0,0):True}
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while(len(q) > 0 and founded == False):
            curr = q.pop(0)
            for move in moves:
                x = curr[0]+move[0]
                y = curr[1]+move[1]
                if x >=0 and x<self.x and y>=0 and y <self.y and (x,y) not in flag:
                    q.append((x,y))
                    flag[(x,y)] = True
                    if (x,y) == (self.x-1,self.y-1):
                        founded =True
                        break

        if not founded:
            return False

        curr = (self.x-1,self.y-1)
        while curr != (0,0):
            for neighboor in self.graph.get_adj()[curr]:
                if neighboor in flag and flag[neighboor] == True:
                    self.render.add_segment(point1=curr, point2=neighboor, color='g')#tracer segment de curr a neighboor
                    flag[curr]=False
                    curr = neighboor
                    break
        return True