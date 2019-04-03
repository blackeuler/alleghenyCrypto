from numberTheory import modExp

def fermats(number):
    """ Returns true if number is prime """
    return modExp(2,number-1,number)%number == 1
        