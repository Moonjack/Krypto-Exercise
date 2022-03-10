from array import *
import pyperclip
import math
matrix=[]

myMessage = 'Common sense is not so common.'
charmx=[]
def main():
    #myMessage = 'Common sense is not so common.'
    myKey = 8
    encryptMessage(myKey, myMessage)
    ciphertext = parseCiphertext(len(myMessage))
    print(ciphertext)
    decrypttext = decryptMessage(len(ciphertext),myKey)
    print(decrypttext)
    debugDecryptMessage(len(ciphertext),myKey)

def parseCiphertext(l):
    ciphertext=['']*l
    k = 0
    for s in range(0,len(charmx)):
        for i in range(0,len(charmx[s])):
            ciphertext[k]+=charmx[s][i]
            k+=1
    return ''.join(ciphertext)
def encryptMessage(key, message):
    ciphertext =[''] * len(message)

    for s in range(0,key):
        charmx.append([])
    for column in range(len(message)):
        currentIndex = column % key
        charmx[currentIndex].append(message[column])
def decryptMessage(l,key):
    message =['']*l
    space = int(math.ceil(len(message) / float(key)))
    for i in range(0,space):
        for s in range(0,len(charmx)):
            if i < len(charmx[s]):
                message[i]+=charmx[s][i]        
    return ''.join(message)

def debugDecryptMessage(l,key):
    message =['']*l
    space = int(math.ceil(len(message) / float(key)))
    print('<---DEBUG MESSAGE--->',end='')
    for i in range(0,space): 
        print("\n")
        for s in range(0,len(charmx)):
            if i < len(charmx[s]):
                print(charmx[s][i],end='|') 
if __name__ == '__main__':
    main()
