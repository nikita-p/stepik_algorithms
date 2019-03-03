#Обработка сетевых пакетов

class Node():
    def __init__(self, time0=0, dur=0, prev=None):
        self.time0 = max( time0, -1 if prev==None else (prev.time0 + prev.dur) )
        self.dur = dur
        self.prev = prev
        self.next = None

class Queue():
    def __init__(self, size):
        self.max_size = size
        self.cur_size = 0
        self.first = None
        self.last = self.first
        
    def push(self, time0, dur):
        if (self.cur_size==0):
            self.cur_size += 1
            self.first = Node(time0, dur)
            self.last = self.first
            return self.first.time0
        
        dur0 = self.last.dur
        time = self.last.time0
        #print("q", self.cur_size)
        #print("tt",time0, time, dur0)
        cur_s = self.cur_size
        max_s = self.max_size
        
        if (cur_s==max_s) and (time0<time+dur0):
            return -1
        
        if (cur_s<max_s):
            self.first.next = Node(time0, dur, self.first)
            self.first = self.first.next
            self.cur_size += 1
            return self.first.time0
            
        self.pop()
        return self.push(time0, dur)
        
    def pop(self):
        if(self.cur_size<=0):
            return -10
        self.last = self.last.next
        self.cur_size -= 1
        return 1


def handler(size, pockets):
    q = Queue(size)
    for p in pockets:
        print( q.push(p[0], p[1]) )

def m():
    size, n = map(int, input().split(' '))
    pockets = [0]*(n)
    for i in range(n):
        pockets[i] = list(map(int, input().split(' ')))
    handler( size, pockets )
    



if __name__=="__main__":
    m()
