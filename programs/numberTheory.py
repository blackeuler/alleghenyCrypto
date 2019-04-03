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
        #print(f"{a} = {b} x {quotient} + {remainder}")
        e_y = -quotient*y[1] + y[0]
        e_x = -quotient*x[1] + x[0]
        #print(f"e_x = -{quotient} x {x[1]} + {x[0]}")
        x[0] = x[1]
        x[1] = e_x
        y[0] = y[1]
        y[1] = e_y
        a, b = b, a % b
    return (e_y, e_x)


def mInverse(a, n):
    """
    Finds the inverse of a integer modn
    """
    assert gcd(a,n)==1
    x,y = extendedEuclidean(a,n)
    return x%n


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

def binaryModExp(y,x,n):
    binary = bin(x)
    s = [1,]
    r = [0 for i in range(len(binary[2:]))]
    for index ,i in enumerate(binary[2:]):
        if index == len(binary[2:]):
            break
        if i == '1':
            r[index] = (s[index]*y)%n
        elif i =='0':
            r[index] =  s[index]
        s.append((r[index]**2)%n)
    return r[-1]
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
    for i, m in enumerate(m):
        z = product//m
        print(f"z = {product}/{m} = {z}")
        y = mInverse(z, m)
        print(f"y = {z}^-1modm = {y}")
        x += a[i]*z*y
        print(f"x = {x}")
    return x % product


def toNum(char):
    return ord(char) % 97


def toLetter(num):
    return chr(num + 97)

def randMatrix(dimension):
    import random
    ones = [[1]*dimension for i in range(dimension)]
    for i in range(dimension):
        for j in range(dimension):
            ones[i][j] = random.randint(1,26)
    return ones

def buildMatrix(key,dim):
    assert len(key) % dim ==0
    index = 0
    matrix = randMatrix(dim)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = toNum(key[index]) %26
            index=index +1
    return matrix

def matrixMultiply(A, B):
    bRows,aRows,aCols,bCols = len(B),len(A),len(A[0]),len(B[0])
    if bRows != aCols:
        raise Exception("Num of Col needs to match Num of Rows")
    result = [[0 for i in range(bCols)] for j in range(aRows)]
    for row in range(aRows):
        for col in range(bCols):
            for i in range(aRows):
                try:
                    result[row][col] += A[row][i]*B[i][col]
                except IndexError:
                    print("Threw Exception")
                    print(f"Row{row}  Col {col} i:{i} ")
    return result

def gaussianElim(matrix):
    n = len(matrix)
    for col in range(n):
        print("Column:"+str(col))
        print(matrix)
        for row in range(col,n):
            if(matrix[row][col]):
                if(row != col):
                    print("Swapping")
                    matrix[row],matrix[col] = matrix[col],matrix[row]
                    print(matrix) 
                else:
                    print("Not Swapping")
                break
        for row in range(col+1,n):
            while True:
                delw = matrix[row][col]/matrix[col][col]
                for j in range(col,n):
                    matrix[row][col] = matrix[row][col] - (delw * matrix[col][j])
                if (matrix[row][col]==0):
                    break
                else:
                    print("Swapping")
                    
                    matrix[row],matrix[col] = matrix[col],matrix[row]
                    
                    print(matrix)
    return matrix
    # May the heavens forgive me for going down this rabbit hole

def bareiss(matrix):
        n = len(matrix)
        for i in range(n-1):
            for j in range(i+1,n):
                for k in range(i+1,n):
                    matrix[j][k] = matrix[j][k] *matrix[i][i] - matrix[j][i]*matrix[i][k]
                    if(i):
                        matrix[j][k] /= matrix[i-1][i-1]
        return matrix[n-1][n-1]
test = [[-2,2,-3],[-1,1,3],[2,0,1]]

