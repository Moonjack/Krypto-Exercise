
initAlphaLow='abcdefghijklmnopqrstuvwxyz'
initAlphaUpp='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dicEncodeAlphaLow={}
dicEncodeAlphaUpp={}
dicDecodeNum={}
encodeList=[]
def main():
    
    initEncode()
    initDecode()
    #testEncoder()
    message='vigenerechiffre'
  #-------Encode--->-ENCRYPTION---->Decode-----------#
  ####################################################
    encodedlist=list(encode(message))                #
    print(encodedlist)                               #
    key = [17,14,19]                                 #
    encryptedlist=list(encrypt(encodedlist,key))     #
    print(encryptedlist)                             #
    print(decode(encryptedlist))                     #
  ####################################################                                                   

   #-----DECRYPTION-------------->Decode-------------#
    decryptedlist =list(decrypt(encryptedlist,key))  #
    print(decode(decryptedlist))                     #
   ###################################################                                                  

def initEncode():
    for s in range(0,26):
        dicEncodeAlphaLow[initAlphaLow[s]] = s
        dicEncodeAlphaUpp[initAlphaUpp[s]] = s
def initDecode():
    i=0
    for s in initAlphaLow:
        dicDecodeNum[i]=s
        i+=1
    dicDecodeNum[-1]='#'

def testEncoder():
    for s in initAlphaLow:
        print(dicEncodeAlphaLow[s], end =' ')
    print('\n')
    for s in initAlphaUpp:
        print(dicEncodeAlphaUpp[s], end = ' ')


def encode(message):
    g = []
    for s in message:
        if s.isupper():
            g.append(dicEncodeAlphaUpp[s])
        elif s.islower():
            g.append(dicEncodeAlphaLow[s])
        else:
            g.append(-1)


    return g
def decode(listnum):
    char=[''] * len(listnum)
    for s in listnum:
        char += dicDecodeNum[s]

    return ''.join(char)


def encrypt(message,key):
    for s in range(0,len(message)):
        if message[s] == -1:
            continue
        message[s] = (message[s] + key[s % len(key)]) % 26

    return message




def decrypt(message,key):
    for s in range(0,len(message)):
        message[s] = (message[s] - key[s % len(key)]) % 26
        if message[s] >= 0:
            message[s] = message[s] % 26
        else:
            message[s] = 26 + message[s]

    return message






if __name__=='__main__':
    main()
