from numberTheory import mInverse, extendedEuclidean,modExp, binaryModExp,erato
import pytest

@pytest.mark.parametrize("a,n,aInverse",
[
    (1, 5, 1),
    (2, 5, 3),
    (3, 5, 2),
    (4, 5, 4),
    (2, 5, 3),

]
)
def test_mInverse(a,n,aInverse):
    assert mInverse(a,n) == aInverse

@pytest.mark.parametrize("a,b,x,y",
[
    (1914, 899, 8,-17),
    (1398, 324, -19,82),

    

]
)
def test_extendedEucledean(a,b,x,y):
    xr ,yr = extendedEuclidean(a,b) 
    assert xr == x
    assert yr == y

@pytest.mark.parametrize("y,x,n, b",
[
    (7, 256, 13,9),
    (2, 1234, 789,481),
    (113535859035722866,116402471153538991,211463707796206571,30120)
   

]
)
def test_modExp(y,x,n,b):
    assert modExp(y,x,n) == b

@pytest.mark.parametrize("y,x,n, b",
[
    (7, 256, 13,9),
    (2, 1234, 789,481),
    (113535859035722866,116402471153538991,211463707796206571,30120)
   

]
)
def test_binaryModExp(y,x,n,b):
    assert binaryModExp(y,x,n) == b
@pytest.mark.parametrize("limit,listPrimes",
[
    (3,[2]),
    (30,[2,3,5,7,11,13,17,19,23,29]),
    (100,[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])
]
)
def test_erato(limit,listPrimes):
    assert erato(limit) == listPrimes