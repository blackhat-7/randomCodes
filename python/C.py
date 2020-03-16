import math

t = int(input())

while(t):
	primes = set()

	x = int(input())
	if x%2==0:
		primes.add(2)
	while x%2 == 0: 
		x = x//2

	for i in range(3,int(math.sqrt(x))+1,2): 
		while x%i == 0: 
			primes.add(i)
			x = x//i

	if x > 2: 
		primes.add(x)
	if len(primes)!=2:
		print(-1)
	else:
		primes = list(primes)
		primes = sorted(primes)
		print(primes[0], primes[1])

	t-=1