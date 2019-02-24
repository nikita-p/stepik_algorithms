

def summator(stairs):
    n = len(stairs)
    sums = [0]*(n+1)
    
    sums[1] = stairs[0]
    for i in range(2, n+1):
        sums[i] = max(sums[i-1], sums[i-2]) + stairs[i-1]

    return sums[n]    
    
def test():
    assert summator([1,2]) == 3
    assert summator([2,-1]) == 1
    assert summator([-1,2,1]) == 3

def m():
    n = int(input())
    stairs = list(map(int, input().split(' ')))
    return summator(stairs)


if __name__=="__main__":
    print( m() )
    #test()
