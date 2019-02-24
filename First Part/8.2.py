#Последовательнократная подпоследовательность

def finder(arr):
    indexes = [ -1 for i in range(len(arr)) ]
    for i1 in range(len(arr)):
        for i2 in range(i1+1, len(arr)):
            if ( arr[i2]%arr[i1]==0 and indexes[i2]<indexes[i1]+1 ):
                indexes[i2] = indexes[i1]+1

    #print(indexes)
    #print(arr)
    print( max(indexes)+2 )

if __name__=="__main__":
    n = input()
    arr = list( map( int, input().split(' ') ) )
    finder(arr)
