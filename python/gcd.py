def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def gcdIterative(a,b):
    while b:
        a, b = b, a%b
    return a


print(gcdIterative(1072, 42))
    









'''
a0 = b0*q0 + r0
b0 = r0*q1 + r1
r0 = r1*q2 + r2
....
rn = r(n-1)*qn + 0

r(n-1) is the answer

'''