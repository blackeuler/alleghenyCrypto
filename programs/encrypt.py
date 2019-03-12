from numberTheory import gcd, toLetter, toNum, randMatrix


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

def hill(plaintext="howareyou",key=3):
    plaintext.lower()
    numbers=[]
    for letter in plaintext:
        numbers.append(toNum(letter))
    numbersArray = [numbers[i:i+key] for i in range(0, len(numbers),key)]
    print(numbers)
    print(numbersArray)
    keyM = randMatrix(key)
    
    cipher = ""