def gcd(a, b):
    while(a%b != 0):
        a, b = b, a%b
    return b

def eE(a,b):
    #x_0 = 0 x_1=1 x_j = -q_j-1*x_j-1+x_j-2
    #recursion possibly
    # as + nt = 1, need quotients
    x = [0,1]
    y=[1,0]
    e_x = None
    e_y = None
    while(a%b != 0):
        quotient,remainder = a//b, a%b
        print(f"{a} = {b} x {quotient} + {remainder}")
        e_y = -quotient*y[1] + y[0]
        e_x = -quotient*x[1] + x[0]
        print(f"e_x = -{quotient} x {x[1]} + {x[0]}")
        x[0] = x[1]
        x[1] = e_x
        y[0] = y[1]
        y[1] = e_y
        a, b = b, a%b
    return e_x,e_y

def mInverse(a,n):
    
    for i in range(0,n):
        if (a*i)% n ==1:
            return i
    return -1
def modEquation(a,b,n):
    d = gcd(a,n)
    if d == 1:
        return (b*mInverse(a,n))%n
    else:
        if b%d ==0:
            return modEquation(a//d,b//d,n//d)
        else:
            return -1

def modExp(y,x,n):
    a,b,c = x, 1, y
    while(a!=0):
        if a%2 ==0:
            a,b,c = a/2,b,c**2%n
        elif a%2 != 0:
            a,b,c = a-1,(b*c)%n,c
    return b

