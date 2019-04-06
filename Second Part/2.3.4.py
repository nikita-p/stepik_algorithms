


class IndSet:
    
    def __init__(self, x):
        self.x = x
        self.next = None
        
    def Find(self):
        p = self
        while( not( p.next == None ) ):
            p = p.next
        return p.x

    def Union(self, y):
        y.next = self
        return



def handler(eq, neq, n):
    g = []
    for i in range(1,n+1):
        z = IndSet(i)
        g.append( z )
    
    for e in eq:
        #print(e)
        g[e[0]-1].Union(g[e[1]-1])

    for n in neq:
        #print(n, g[n[0]-1].Find(), g[n[1]-1].Find())
        if ( g[n[0]-1].Find() == g[n[1]-1].Find() ):
            return 0
    
    return 1
    


def inp():    
    n, e, d = map( int, input().split(' ') )
    eq = [list( map( int, input().split(' ') ) ) for _ in range(e)]
    neq = [list( map( int, input().split(' ') ) ) for _ in range(d)]
    return handler(eq, neq, n)


if __name__=="__main__":
    print( inp() )
    #print( handler([[1,2], [1,3]], [[2,4]], 4) )
