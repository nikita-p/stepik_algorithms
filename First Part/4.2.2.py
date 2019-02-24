
def decoder():
    k, l = map(int, input().split(' '))
    dic = dict()
    for i in range(k):
        sym, code = map(str, input().split(': '))
        dic[code] = sym
    
    codeword = input()
    
    srch = ''
    decode_word = ''
    for i in codeword:
        srch += i
        if srch in dic:
            decode_word += dic[srch]
            srch = ''
    print(decode_word)


if __name__=="__main__":
    decoder()
