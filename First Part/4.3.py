
class Queue:
    
    def __init__(self):
        self.queue = []

    def insert(self, n):
        self.queue.append(n)
        self.upper()
        #print(self.queue)
        
    def extract(self):
        m = self.queue[0]
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        self.getLast()
        self.downer()
        #print(self.queue)
        return m
        
    def get_childrens(self, i):
        queue = self.queue
        kids = []
        if( 2*i+1 < len(queue) ):
            kids.append( (2*i+1, queue[2*i+1]) )
        if( 2*i+2 < len(queue) ):
            kids.append( (2*i+2, queue[2*i+2]) )
        return kids
        
    def get_parent(self, i):
        queue = self.queue
        if( (i-1)//2 < 0 ):
            return (-1, queue[0])
        return ((i-1)//2, queue[ (i-1)//2 ])

    def upper(self):
        q = self.queue
        k = len(q)-1
        
        for ii in range(len(q)):
            p = self.get_parent(k)
            if (p[0] < 0) or (p[1] >= q[k]):
                break
            if (p[1] < q[k]):
                q[p[0]], q[k] = q[k], q[p[0]]
                k = p[0]
        
        return        
    
    def downer(self):
        q = self.queue
        k = 0
        
        for ii in range(len(q)):
            c = self.get_childrens(k)
            if( len(c) == 0 ):
                break
            #print(c)
            ind, min_val = max(c, key=lambda x: x[1])
            if( q[k] < min_val ):
                q[k], q[ind] = q[ind], q[k]
                k = ind
            else:
                break
        return    

    def getLast(self):
        return self.queue.pop()

if __name__=="__main__":
    t = Queue()
    n = int(input())
    for i in range(n):
        command = input().split(' ')
        if(command[0] == "Insert"):
            t.insert(int(command[1]))
        if(command[0] == "ExtractMax"):
            m = t.extract()
            print(m)
