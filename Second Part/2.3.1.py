#Переставить элементы заданного массива чисел так, чтобы он удовлетворял свойству мин-кучи.

class Bunch():
    def __init__(self, size, arr):
        self.size = size
        self.changes = []
        self.arr = arr
        
    def SiftDown(self, i):
        a = self.arr
        if (2*i+1 >= self.size ):
            return
        
        ind = ( 2*i + 1 if a[2*i+1]<a[2*i+2] else 2*i+2 ) if (2*i+2 < self.size) else ( 2*i + 1 )
        if( a[ind] < a[i] ):
            a[i], a[ind] = a[ind], a[i]
            self.changes.append( (i, ind) )
            self.SiftDown(ind)
        return
        
    def seed(self):
        p = self.size - 1
        for i in range( (p-1)//2, -1, -1 ):
            self.SiftDown(i)

    def print(self):
        ch = self.changes
        print(len(ch))
        for i in ch:
            print(i[0], i[1])
        return

def m():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    q = Bunch(n, arr)
    q.seed()
    q.print()



if __name__=="__main__":
    m()
