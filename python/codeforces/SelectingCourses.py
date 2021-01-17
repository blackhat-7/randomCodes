def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a


n, x = map(int, input().split())
classroom = list(map(int, input().split()))

# formatted = []
d = 0
for num in classroom:
    if num >= x:
        d = gcd(d, num-x)

    if num < x:
        d = gcd(d, x - num)

print(d)
