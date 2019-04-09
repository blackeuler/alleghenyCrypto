from random import randint
from primality import fermats
from numberTheory import mInverse,binaryModExp,erato
class RSA():
    __secret_key = ()
    public_key = ()

    def __init__(self,p=None,q=None,e=65537):
        print(p)
        self.setKeys(p,q,e)

    
    def setKeys(self,p=None,q=None,e=65537):
        print("Setting Keys......")
        if p is None or q is None:
            print("Generating Random Primes....")
            p,q = self.generatePrimes()
        N = p*q
        print("Calculating Decryption Exponent......")
        d = self.generateDecExp(p,q,e)
        self._RSA__secret_key = (p,q,d)
        print(f"Secret Primes:{p},{q} Decryption Exponent:{d}")
        self.public_key = (N,e)
        print(f"Public Key:{N} and {e}")


    def generatePrimes(self):
        #generate 2 random number
        p,q = randint(200,500),randint(200,500)
        #test for primality
        while not fermats(p) or not fermats(q):
            if not fermats(p):
                p = randint(200,500)
            if not fermats(q):
                q = randint(200,500)
        return p,q
    def generateDecExp(self,p,q,e):
        #Calculate (p-1)*(q-1)
        phiN = (p-1)*(q-1)
        #Choose large random number d for decryption
        #Calculate modInverse of d mod (p-1)(q-1)
        d = mInverse(e,phiN)
        #return tuple of e and p*q
        return d
    def encrypt(plaintext, sender_public_key):
        # plaintext to number
        message = self.toNum(plaintext)
        e = sender_public_key[1]
        n = sender_public_key[0]
        return binaryModExp(message,e,n)
        

    def decrypt(self,cipher):
         return binaryModExp(cipher,self._RSA__secret_key[2],self.public_key[0])%self.public_key[0] 
        
    def toNum(self,plaintext):
        s=''
        for i in plaintext:
           s += str(ord(i)%96+9)
        return int(s)

    def toLetters(self, numbers):
        letters = ''
        numbers = str(numbers)
        for i,k in zip(numbers[0::2], numbers[1::2]):
            letters += chr(int(str(i+k))-9+96)
        return letters

def attack(n):
    primes = erato(n)
    for prime in primes:
        if n%prime ==0:
            return prime

def attack2(m):
    from math import sqrt
    lim = int(sqrt(m))+1
    for i in range(3,lim,2):
        if m%i ==0:
            return i