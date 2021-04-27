def count_pal(n):
    total = 6**n
    if n % 2 == 0:
        return 6**(n//2)
    else:
        return 6**(n//2+1)


for i in range(1, 6):
    print(count_pal(i))
