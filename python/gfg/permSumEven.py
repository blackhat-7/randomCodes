from functools import lru_cache

@lru_cache(None)
def permSumEven(low, high, k, sm=0):
    if k == 0:
        return [[]] if sm & 1 == 0 else []
    res = []
    for i in range(low, high+1):
        x = permSumEven(low, high, k-1, sm+i)
        for y in x:
            res.append([i] + y)
    return res

def permlen(low, high, k):
    even = sum(1 for x in range(low,high+1) if x&1 == 0)
    odd = sum(1 for x in range(low,high+1) if x&1 != 0)

    even_total = odd_total = 0
    even_prev = 1
    odd_prev = 0
    for _ in range(k):
        even_total = even*even_prev + odd*odd_prev
        odd_total = odd*even_prev + even*odd_prev
        odd_prev = odd_total
        even_prev = even_total
    return even_total

        

low = 1
high = 10
k = 2

res = permSumEven(low, high, k)
resLen = permlen(low, high, k)
print(res, len(res))
print(resLen)

'''
4 5 3
even: 1
odd: 1

even: 2 
odd: 2

even: 4
odd: 4


'''





