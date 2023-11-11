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
        flag = {(0,0):0}
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        while(len(q) > 0 and founded == False):
            n = len(q)
            count += 1
            while n > 0 and founded ==False:
                curr = q.pop(0)
                for move in moves:
                    x = curr[0]+move[0]
                    y = curr[1]+move[1]
                    if x >=0 and x<self.x and y>=0 and y <self.y and (x,y) not in flag:
                        q.append((x,y))
                        flag[(x,y)] = count
                        if (x,y) == (self.x-1,self.y-1):
                            founded =True
                            break
                n-=1

        if not founded:
            return False

        curr = (self.x-1,self.y-1)
        while curr != (0,0):
            mini = 10e9
            next = None
            flag[curr] = -1
            for neighboor in self.graph.get_adj()[curr]:
                if neighboor in flag and flag[neighboor] != -1 and flag[neighboor] < mini:
                    mini = flag[neighboor]
                    next = neighboor
            self.render.add_segment(point1=curr, point2=next, color='g')#tracer segment de curr a neighboor
            curr = next

        print(count)# distance la plus courte jusqu'a la sortie

        return True