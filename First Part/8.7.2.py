

def calc(n):
    r = [0]*(n+1)
    for i in range(2, n+1):
        r[i] = min( r[i-1], r[i//2] if i%2==0 else float("inf"), r[i//3] if i%3==0 else float("inf") ) + 1
    #print(r)
    
    lst = [n]
    i = n
    while not(i==1):
        i = i//3 if (i%3==0) and (r[i//3]<r[i]) else i//2 if (i%2==0) and (r[i//2]<r[i]) else i-1
        lst.append(i)

    #print( (r[n], sorted(lst)) )
    return (r[n], sorted(lst))

    
def test():
    assert calc(1) == (0, [1])
    assert calc(5) == (3, [1, 2, 4, 5])
    assert calc(96234) == (14, [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234])

def m():
    n = int(input())
    return calc(n)

if __name__=="__main__":
    s = m()
    print( s[0] )
    [print(k, end=' ') for k in s[1]]
    print()
    #test()
