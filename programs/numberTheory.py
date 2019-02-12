def gcd(a, b):
    """
    Returns the greatest common denominator of a and b

    Parameters:
    a (int):Positive Integer
    b (int):Positive Integer
    """
    while(a % b != 0):
        a, b = b, a % b
    return b


def extendedEuclidean(a, b):
    """
    Returns the two integer solutions to the equation
    ax+by = 1
    Parameters:
    a (int):Positive Integer
    b (int):Positive Integer
    Returns:
    e_x = x
    e_y = y
    """
    x = [0, 1]
    y = [1, 0]
    e_x = None
    e_y = None
    while(a % b != 0):
        quotient, remainder = a//b, a % b
        print(f"{a} = {b} x {quotient} + {remainder}")
        e_y = -quotient*y[1] + y[0]
        e_x = -quotient*x[1] + x[0]
        print(f"e_x = -{quotient} x {x[1]} + {x[0]}")
        x[0] = x[1]
        x[1] = e_x
        y[0] = y[1]
        y[1] = e_y
        a, b = b, a % b
    return e_x, e_y


def mInverse(a, n):
    """
    Finds the inverse of a integer modn
    """

    for i in range(0, n):
        if (a*i) % n == 1:
            return i
    return -1


def modEquation(a, b, n):
    """
    Solves for the equation ax =b modn
    Returns -1 if no solution
    """
    d = gcd(a, n)
    if d == 1:
        return (b*mInverse(a, n)) % n
    else:
        if b % d == 0:
            return modEquation(a//d, b//d, n//d)
        else:
            return -1


def modExp(y, x, n):
    """
    Returns the y^x modn
    """
    a, b, c = x, 1, y
    while(a != 0):
        if a % 2 == 0:
            a, b, c = a/2, b, c**2 % n
        elif a % 2 != 0:
            a, b, c = a-1, (b*c) % n, c
    return b


def CRT(a, m):
    """
    Returns the integer solution to the system a congruences
    Parameters:
    a (list):List of remainders amodn
    n (list):List of modulos    amodn
    Returns:
    x the solution to the system of congruences
    """
    from functools import reduce
    x = 0
    product = reduce(lambda a, b: a*b, m)
    for i,m in enumerate(m):
        z = product//m
        print(f"z = {product}/{m} = {z}")
        y = mInverse(z,m)
        print(f"y = {z}^-1modm = {y}")
        x += a[i]*z*y
        print(f"x = {x}")
    return x % product