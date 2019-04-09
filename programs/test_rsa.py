import pytest
from rsa import RSA,attack
from primality import fermats
def test_generateExp():
    rsa = RSA()
    assert rsa.generateDecExp(885320963,238855417,9007) == 116402471153538991

@pytest.mark.parametrize("p,q,e,cipher,decrypted",
[
    (885320963,238855417,9007,113535859035722866,30120),
    (61,53,17,855,123),

]
)
def test_decrypt(p,q,e,cipher,decrypted):
    rsa = RSA(p,q,e)
    assert rsa.decrypt(cipher) == decrypted

def test_toNum():
    rsa = RSA()
    assert rsa.toNum("cat") == 121029 

def test_attack():
    rsa = RSA()
    assert rsa._RSA__secret_key[0] == attack(rsa.public_key[0])

def test_generatePrimes():
    rsa = RSA()
    p,q = rsa.generatePrimes()
    assert fermats(p) == True
    assert fermats(q) == True