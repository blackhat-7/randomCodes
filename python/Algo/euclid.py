def euclid(a, b):
    if b == 0:
        return a
    return euclid(b, a % b)


def euclidIterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a


gcd = euclidIterative(34, 153)
print(gcd)

'''
15 = 10*1 + 5
10 = 5*2 + 0


'''
