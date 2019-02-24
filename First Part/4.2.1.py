import re

class Tree(object):

    def __init__(self):
        self.queue = []
        self.codes = {}
    
    def create(self, syms, freq):
        syms_freq = list(zip(syms, freq))
        self.queue = sorted(syms_freq, key=lambda x: x[1], reverse=True)
        syms = [ q[0] for q in self.queue]
        self.codes = dict( zip(syms, [ '' for i in self.queue ]) )
        
    def extract(self):
        queue = self.queue
        codes = self.codes
        
        if(len(queue)==1):
            z = {queue[0][0]: '0'}
            return z
        
        for i in range(len(queue)-1):
            lefts = queue.pop()
            rights = queue.pop()
            #print(lefts, rights)
            for r in rights[0]:
                codes[r] = '0' + codes[r]
            for l in lefts[0]:
                codes[l] = '1' + codes[l]
            queue.append( (lefts[0]+rights[0], lefts[1]+rights[1]) )
            queue.sort(key = lambda x: x[1], reverse=True)
        return codes
        
    

def code():
    s = input()
    syms = list(set(s))
    freq = [len(re.findall(sym, s)) for sym in syms]
    t = Tree()
    t.create(syms, freq)
    codes = t.extract()
    s1 = ''
    for sym in s:
        s1 += str(codes[sym])
    
    print( len(set(s)), len(s1) )
    for key in codes:
        print(key + ": " + str(codes[key]))
    print(s1)


if __name__=="__main__":
    code()
