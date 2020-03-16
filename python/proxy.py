import math

t = int(input())

for i in range(t):
	d = int(input())
	s = input()

	numP = s.count("P")
	m = math.ceil(d*0.75)
	x = m-numP
	proxy = 0

	if (d<=4):
		if numP>=m:
			print(0)
		else:
			print(-1)
	else:
		if numP>=m:
			print(0)
		else:
			arr = []
			for j in range(d-4):
				if (s[j+2]=="A"):
					if ((s[j]=="P" or s[j+1]=="P") and (s[j+3]=="P" or s[j+4]=="P")):
						proxy+=1
				if (proxy==x):
					break
			
			if proxy==x:
				print(proxy)
			else:
				print(-1)