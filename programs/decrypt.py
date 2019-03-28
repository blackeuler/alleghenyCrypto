from numberTheory import mInverse,toLetter,toNum, buildMatrix,matrixMultiply
import numpy as np

def shift(cipher="whvw", key=3):
    plaintext = ""
    for char in cipher:
        d = toNum(char)
        plaintext+= toLetter((d-key)%26)
    return plaintext

def affine(cipher="cvvwpm", alpha=9, beta=2):
    inverse = mInverse(alpha,26)
    plaintext = ""
    for char in cipher:
        d = toNum(char)
        plaintext += toLetter((inverse*d - inverse*beta)%26)
    return plaintext

def vigenere(cipher="citxwjcsybhnjvml", key="vector"):
    plaintext = ""
    for i, char in enumerate(cipher):
        shift = toNum(key[i % len(key)])
        d = toNum(char)
        plaintext += toLetter((d-shift) % 26)
    return plaintext

def hill(cipher="poh", key="GYBNQKURP", block_size = 3):
    cipher = cipher.lower()
    key = key.lower()
    keyMatrix = buildMatrix(key,block_size)
    from numpy.linalg import inv
    keyMatrix = inv(keyMatrix).tolist()
    numbers=[]
    for letter in cipher:
        numbers.append(toNum(letter))
    numbers = [numbers[i:i+block_size] for i in range(0, len(numbers),block_size)]
    for plain_block in range(len(numbers)):
        vTranspose = [[item] for item in numbers[plain_block]]
        numbers[plain_block] = matrixMultiply(keyMatrix,vTranspose)
    cipher = [num for sublist in numbers for liste in sublist for num in liste]
    return cipher