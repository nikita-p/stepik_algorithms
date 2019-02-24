l, r = [], []

def cutter(start, end):
    m = start + (end - start)//2
    #print(start, end, "FF", m)
    return m

def dichotomyStart(p, start, end):
    m = cutter(start, end)    
    if( (end-start)==1 ):
        if( l[start]<=p and l[end]>p ):
            return end
        if( l[end]<=p ):
            return len(l)
        if( l[start]>p ):
            return start 
    if( m<1 ):
        return 0 if l[0]>p else len(l)
    
    if( l[m]>p and l[m-1]<=p ):
        return m
    if( l[m]>p and l[m-1]>p ):
        return dichotomyStart(p, start, m)
    if( l[m]<=p and l[m-1]<=p ):
        return dichotomyStart(p, m, end)
    return -1

def dichotomyEnd(p, start, end):
    m = cutter(start, end)    
    if( (end-start)==1 ):
        if( r[start]<p and r[end]>=p ):
            return end
        if( r[end]<p ):
            return len(l)
        if( r[start]>=p ):
            return start     
    if( m<1 ):
        return 0 if r[0]>=p else len(l)
    
    if( r[m]>=p and r[m-1]<p ):
        return m
    if( r[m]>=p and r[m-1]>=p ):
        return dichotomyEnd(p, start, m)
    if( r[m]<p and r[m-1]<p ):
        return dichotomyEnd(p, m, end)
    return -1
    
def num(p):
    s = dichotomyStart(p, 0, len(l)-1)
    e = dichotomyEnd(p, 0, len(r)-1)
    return ( s - e )

if __name__=="__main__":
    n1, n2 = map(int, input().split(' '))
    for i in range(n1):
        a, b = map(int, input().split(' '))
        l.append(a)
        r.append(b)
    points = list(map(int, input().split(' ')))
    l.sort()
    r.sort()
    #print(l, r)
    for p in points:
        print(num(p), end=" ")
    print()
