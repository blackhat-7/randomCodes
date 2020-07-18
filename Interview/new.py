'''
        
1 2 3 4 5 6 7 8 9
        |       |


tortoise = x

haire = 2x

l + nx + f 
l + ny + f

l + nx + f = 2 * (l + ny + f)
nx = l + 2ny + f
nx - 2ny - f = l


n(x - 2y) - f = l

array
partitions

3 1 1 7

3117

3
11
7

311
7

31
17

3
117

10^6


def divide(array, i, j, lookup):
    if i == j:
        return prime[i]
    
    key = (i, j)
    if key not in lookup:
        ans = False
        for k in range(j-i):
            ans = divide(array, i, k, lookup) and divide(array, k+1, j)






primes = [1] * n

for i in range(sqrt(n)):
    if primes[i] == 0:
        for j in range(sqrt(n)):
            primes[i*j] = 0


13

2
2*1 2*3 2*3 2*4



for i in range(n):
    if primes[i]:
        flag = 0
        for j in range(n):
            if i % j == 0:
                primes[i] = 0
                flag = 1
                break






array in AP

a b c d e f g

b-a = e-d f-e...
c-b d-c

d-b = 2(b-a)



b-a c-b d-c e-d 


d = arr[i] - arr[i-1]

6
4


7 - 1 = 6
11 - 7 = 4

1 3 7 9 11

2 4 8 10

arr[mid - 1] - arr[low]
arr[high] - arr[mid + 1]


2 4 6 10

4 - 2 = 2
10 - 6 = 4

6 10




low = 1 high = 7
mid = 3

3 - 1 = 2 
7 - 3 = 4




x%4 = 1
y = x / 4
(x/4)%5 = 4

x = 1 mod4
x/4 = 4 mod5

x = 16 mod5 = 1 mod5

x = 1 mod4 x/5 = 1/5 mod 5 

x = 1 mod 4
x = 1 mod 5
x = 1 mod 20



'''