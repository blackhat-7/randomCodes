from random import randint as randi

def gcdRecursive(a, b):
    if b == 0:
        return a
    return gcdRecursive(b, a%b)

def gcdIterative(a, b):
    while b:
        a, b = b, a%b
    return a

def gcdExtended(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, g = gcdExtended(b, a%b)
    x, y = y1, x1 - y1*int(a/b)
    return x, y, g

def gcdExtendedIterative(a, b):
    while b:
        a, b = b, a%b
    


if __name__ == '__main__':
    # for i in range(10):
    #     a, b = randi(0, 1000000), randi(0, 1000000)
    #     if (gcdRecursive(a, b) != gcdIterative(a,b)):
    #         print(False)
    print(gcdExtended(1914, 899))