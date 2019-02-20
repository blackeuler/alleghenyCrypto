from numberTheory import mInverse,toLetter,toNum

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