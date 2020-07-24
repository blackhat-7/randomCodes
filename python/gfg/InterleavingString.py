a, b = input().split()
c = ''
i = 0; j = 0
parity = 0
while i < len(a) and j < len(b):
    if parity == 0:
        c += a[i]
        i += 1
    else:
        c += b[j]
        j += 1
    parity = 1 - parity
while i < len(a):
    c += a[i]
    i += 1
while j < len(b):
    c += b[j]
    j += 1
print(c)
