#Рюкзак
import random

def number(W, w):
    if  (len(w)==0):
        return 0
    return max( ( number(W-w[-1], w[:-1]) + w[-1] ) if (W-w[-1])>=0 else 0, number(W, w[:-1]) )


def number2(W, w):
    n = len(w)
    d = [ [0]*(W+1) for _ in range(n+1) ]
    
    for i in range(1, W+1):
        for j in range(1, n+1):
            d[j][i] = d[j-1][i]
            if (i - w[j-1] >= 0):
                d[j][i] = max( d[j][i], d[j-1][i-w[j-1]] + w[j-1] )
    
    for row in d:
        print(row)
    print()
    return d[n][W]

def m():
    W, n = map(int, input().split(' '))
    w = list(map(int, input().split(' ')))
    return number2(W, w) 


def test():
    assert number2(10, [1, 4, 8]) == 9
    n  = random.randint(1,12)
    sp = [random.randint(1,4) for _ in range(random.randint(5,8))]
    assert number2(n, sp) == number(n, sp)

if __name__=="__main__":
    print( m() )
    #test()
