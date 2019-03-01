#Стек с поддержкой максимума

class Node():
    def __init__(self, val=-1, prev=None):
        #self.val = val
        self.prev = prev
        self.max = max(val, prev.max if not(prev==None) else -1 )

class Stack():
    def __init__(self):
        self.node = Node()
        
    def push(self, a):
        self.node = Node(a, self.node)
        #print("M"+self.node.max)

    def pop(self):
        self.node = self.node.prev

    def max(self):
        return self.node.max
        
    def Enter(self, command):
        if command[0]=="push":
            self.push(int(command[1]))
        if command[0]=="pop":
            self.pop()
        if command[0]=="max":
            print(self.max())
        return

def m():
    n = int(input())
    s = Stack()
    command = [0]*n
    for i in range(n):
        command[i] =  input() 
    for com in command:
        s.Enter(com.split(' '))
    

if __name__=="__main__":
    m()
    #test()
