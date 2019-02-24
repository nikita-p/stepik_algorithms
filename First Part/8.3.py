import random
import sys

def ed_dis(s1, s2):
    m,n = len(s1), len(s2)
    d = [ [0]*(n+1) for _ in range(m+1) ]
    for i in range(m+1):
        d[i][0] = i
    for j in range(n+1):
        d[0][j] = j
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            d[i][j] = min( d[i][j-1] + 1, d[i-1][j] + 1, d[i-1][j-1] + (s1[i-1] != s2[j-1]) )
        
    return d[m][n]
    
def test(n_iter=100):
    for i in range(n_iter):
        length = random.randint(0, 128)
        s = "".join( random.choice("01") for _ in range(length))
        print(s)
        assert ed_dis(s, "") == ed_dis("", s) == len(s)
        assert ed_dis(s, s) == 0

    assert ed_dis("ab", "ab") == 0
    assert ed_dis("short", "ports") == 3

def st():
    s1 = input()
    s2 = input()
    
    print(ed_dis(s1, s2))
    
if __name__=="__main__":
    test()
