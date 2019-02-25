#Высота дерева
#Вычислить высоту данного дерева.

import sys

class Graph():
    def __init__(self, v):
        self.nodes = v
        self.parents = [-1]*(len(v))

    def Parents(self, ind):
        if self.nodes[ind] == -1:
            return 1
        #print(self.parents)
        if self.parents[ind]>=0:
            return self.parents[ind]
        self.parents[ind] = self.Parents(self.nodes[ind]) + 1
        return self.parents[ind]

def height(v):
    mc = 0
    for i in v:
        j, count = i, 1
        while not(j==-1):
            #print(j)
            count += 1
            j = v[j]
        mc = max( count, mc )
    return mc
    
def height2(v):
    g = Graph(v)
    #print()
    return max( [g.Parents(i) for i in range(len(v))] )

def test():
    assert height2([4, -1, 4, 1, 1]) == 3
    assert height2([-1, 0, 4, 0, 3]) == 4

def m():
    n = int(input())
    v = list(map(int, input().split(' ')))
    return height2(v)


if __name__=="__main__":
    sys.setrecursionlimit(20000)
    print( m() )
    #test()
