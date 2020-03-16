import math


def prime_factors(n):
    d = set()
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            d.add(i)
    if n > 1:
        d.add(n)
    return list(d)


t = int(input())

for i in range(t):
    guess = False

    print(1, 10**5)
    a = int(input())
    pf1 = prime_factors(10**10-a)
    q2 = min(pf1)
    for j in range(q2, 10**9):
        lst = []
        for k in pf1:
            lst.append(j**2%k)

        if len(set(lst)) == len(lst):
            q2 = j
            break

    print(1, q2)
    b = int(input())

    prime = pf1[0]
    for j in range(len(pf1)):
        if (q2**2)%pf1[j]==b:
            prime = pf1[j]
    print(2, prime)

    ans = input()
    if ans=="No":
        exit()