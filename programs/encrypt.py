from numberTheory import gcd, toLetter, toNum, buildMatrix, matrixMultiply


def shift(plaintext="test", key=3):
    plaintext = plaintext.lower()
    cipher = ""
    for char in plaintext:
        d = toNum(char)
        cipher += toLetter((d+key) % 26)
    return cipher


def affine(plaintext="affine", alpha=9, beta=2):
    if gcd(alpha, 26) != 1:
        raise Exception 
    plaintext = plaintext.lower()
    cipher = ""
    for char in plaintext:
        d = toNum(char)
        cipher += toLetter((alpha*d + beta) % 26)
    return cipher


def vigenere(plaintext="hereishowitworks", key="vector"):
    plaintext.lower()
    cipher = ""
    for i, char in enumerate(plaintext):
        shift = toNum(key[i % len(key)])
        d = toNum(char)
        cipher += toLetter((d+shift) % 26)
    return cipher

def hill(plaintext="CAT",key="GYBNQKURP", block_size=3):
    if len(key)%block_size !=0:
        raise Exception("Matrix Size error")
    plaintext = plaintext.lower()
    key = key.lower()
    keyMatrix = buildMatrix(key,block_size)
    
    numbers=[]
    for letter in plaintext:
        numbers.append(toNum(letter))
    numbers = [numbers[i:i+block_size] for i in range(0, len(numbers),block_size)]
    for plain_block in range(len(numbers)):
        vTranspose = [[item] for item in numbers[plain_block]]
        numbers[plain_block] = matrixMultiply(keyMatrix,vTranspose)
    cipher = [toLetter(num%26) for sublist in numbers for liste in sublist for num in liste]
    return "".join(cipher)


 