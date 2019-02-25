#Скобки в коде
#Проверить, правильно ли расставлены скобки в данном коде

class Node():
    def __init__(self, value=None, next=None, index=None):
        self.value = value
        self.next = next
        self.index = index

class Stack():
    
    def __init__(self):
        self.first = Node()
        self.size = 0
       
    def annihilate(self):
        f, s = self.first.value, self.first.next.value
        c1 = (f==")") and (s=="(")
        c2 = (f=="]") and (s=="[")
        c3 = (f=="}") and (s=="{")
        if c1 or c2 or c3:
            self.pop()
            self.pop()
            return 1
        return -1

    def push(self, a, ind):
        f = self.first
        
        if ( a in "([{}])" ):
            self.first = Node(a, f, ind)
            self.size += 1
        else:
            return 0
        
        s = self.annihilate()
        if ( a in "}])") and (s==-1):
            return -1
        
        return 0

    def pop(self):
        f = self.first
        self.first = self.first.next
        self.size -= 1
        return f.index

def bra(n):
    s = Stack()
    for i in range(len(n)):
        r = s.push(n[i], i+1)
        if (r==-1):
            break
        
    if s.size>0:
        return s.pop()
     
    return "Success"

def m():
    n = input()
    return bra(n)
    
def test():
    assert bra("([](){([])})") == "Success"
    assert bra("()[]}") == 5
    assert bra("{{[()]]") == 7
    print(bra("foo(bar[i);"))
    assert bra("foo(bar[i);") == 10
    assert bra("foo(bar);") == "Success"
    assert bra("{[}") == 3
    assert bra("{") == 1
    assert bra("([](){([])})") == "Success"
    assert bra("()[]}") == 5
    assert bra("{{[()]]") == 7
    print(bra("{{{[][][]"))
    assert bra("{{{[][][]") == 3
    assert bra("{*{{}") == 3
    assert bra("[[*") == 2
    assert bra("{*}") == "Success"
    assert bra("{{") == 2
    assert bra("{}") == "Success"
    assert bra("") == "Success"
    assert bra("}") == 1
    assert bra("*{}") == "Success"
    assert bra("{{{**[][][]") == 3
    assert bra("()({}") == 3
    print(bra("]]]"))
    assert bra("]]]") == 1 


if __name__=="__main__":
    print( m() )
    #test()
