import pytest
from rsa import RSA

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