
class Number:
    def __init__(self, num, name):
        self.number = num
        self.name = name

class PhoneBook:
    def __init__(self):
        n = 10000000
        self.table = [None]*n 
        
    def Find(self, phone):
        b = self.table[phone]
        if not(b==None):
            print(b)
            return
        print("not found")
        return
    
    def Add(self, phone, name):
        self.table[phone] = name
        return

    def Del(self, phone):
        self.table[phone] = None
        return

def handler():
    n = int(input())
    pb = PhoneBook()
    for _ in range(n):
        act = input().split(' ')
        if act[0]=="add":
            pb.Add(int(act[1]), act[2])
        if act[0]=="find":
            pb.Find(int(act[1]))
        if act[0]=="del":
            pb.Del(int(act[1]))
    

if __name__=="__main__":
    handler()
