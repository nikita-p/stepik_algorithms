#Максимум в скользящем окне через два стека

class Node():
    def __init__(self, val=-1, prev=None):
        self.val = val
        self.prev = prev
        self.max = max(val, self.prev.max) if not(prev==None) else val

class Stack():
    def __init__(self):
        self.node = Node()
        self.size = 0
        
    def push(self, val):
        self.node = Node(val, self.node)
        self.size += 1
    
    def pop(self):
        if(self.size==0):
            return 0
        nd, self.node = self.node, self.node.prev
        self.size -= 1
        return (nd.val, nd.max)

class Queue():
    def __init__(self, n, arr):
        self.stack1 = Stack()
        self.stack2 = Stack()
        for i in range(n):
            self.stack1.push(arr[i])
        
    def push(self, a):
        self.stack1.push(a)
        #print(self.stack1.node.max)

    def pop(self):
        if self.stack2.size==0:
            while not(self.stack1.size==0):
                val = self.stack1.pop()
                self.stack2.push(val[0])
        nd = self.stack2.pop()
        return max(self.stack1.node.max, nd[1])

def window(n, lst):
    q = Queue(n, lst)
    a = []
    for i in lst[n:]:
        a.append(q.pop())
        q.push(i)
    a.append(q.pop())
    return a

def test():
    print(window(1, [2, 1, 5]))
    print(window(4, [2, 7, 3, 1, 5, 2, 6, 2]))
    assert window(1, [2, 1, 5]) == [2, 1, 5]
    assert window(4, [2, 7, 3, 1, 5, 2, 6, 2]) == [7, 7, 5, 6, 6]

def m():
    m = int(input())
    lst = list(map(int, input().split(' ')))
    n = int(input())
    a = window(n, lst)
    for i in a:
        print(i, end=' ')
    print()

if __name__=="__main__":
    m()
    #test()
