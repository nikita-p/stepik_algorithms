# В первой строке даны целое число 1≤n≤105 и массив A[1…n] из n различных натуральных чисел, не превышающих 109, в порядке возрастания, 
#   во второй — целое число 1≤k≤105 и k натуральных чисел b1,…,bk, не превышающих 109. 
# Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi, или −1, если такого j нет.

def out():
    arr = list(map(int, input().split(' ')))
    l = arr.pop(0)
    b = list(map(int, input().split(' ')))
    
    for k in b[1:]:
        
        start, end = 0, l
        while(True):
            point = (start + end)//2
            #print(start, end)
                        
            if(k==arr[point]):
                print(point+1, end=' ')
                break
            if(start==end-1):
                print(-1, end= ' ')
                break
            if(k>arr[point]):
                start, end = point, end
            else:
                start, end = start, point
        #print("NEXT")
    print()


if __name__=="__main__":
    out()
