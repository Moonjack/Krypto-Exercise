import random, sys, transposition2

def main():
    random.seed(42)
    #for i in range(20):
    message = 'ABCDEFGHIJKLMNOPQRSTUWXYZ' * random.randint(4, 40)
    message = list(message)
    random.shuffle(message)
    message = ''.join(message)
    i = 0
    key = 15
    print('plaintext: ' +  message)
       # for key in range(1, int(len(message)/2)):
    transposition2.encryptMessage(key,message)
    encrypted = transposition2.parseCiphertext(len(message))
    decrypted = transposition2.decryptMessage(len(encrypted),key)
    print('ENRYPTED:' + encrypted)
    print('DECRYPTED: ' + decrypted)
    if message != decrypted:
        print("MISMATCH")
    else:
        print("MATCH")
        print("----")
        transposition2.debugDecryptMessage(len(message),key)

if __name__ == '__main__':
    main()
