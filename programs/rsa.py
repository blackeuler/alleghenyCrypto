from random import randint
from primality import fermats
from numberTheory import mInverse,binaryModExp
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



    def generatePrimes(self):
        #generate 2 random number
        p,q = randint(200,500),randint(200,500)
        #test for primality
        while not fermats(p) and fermats(q):
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
        #return message ** e mod n
        #
        pass

    def decrypt(self,cipher):
         return binaryModExp(cipher,self._RSA__secret_key[2],self.public_key[0])%self.public_key[0] 
        
        