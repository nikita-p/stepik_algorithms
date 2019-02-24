#Сортировка подсчётом (линейная по времени)

def sortP(q):
    M = [0 for i in range(10)]
    for i in q:
        M[i-1] += 1
    for k in range(10):
        for i in range(M[k]):
            print(k+1, end=' ')
    print() 
    

if __name__=="__main__":
    n = input()
    q = list(map(int, input().split(' ')))
    sortP(q)
