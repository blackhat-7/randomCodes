def count_down_from(x=10):
    for i in range(x, -1, -1):
        yield i**2


for c in count_down_from():
    print(c)
