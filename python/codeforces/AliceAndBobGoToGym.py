import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
    
a, b, x, y = map(int, input().split())

l = lcm(a, b)

d = math.ceil(x/l)
e = math.floor(y/l)
print(d, e)
if d == x//l or e == y//l:
    print(e-d+1)
else:
    print(e-d)