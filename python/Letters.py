n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

lst = [1,a[0]]
for i in range(1,n):
	lst.append([b[i-1][1], b[i-1]+a[i]])

for i in b:

	c = 0
	d = len(lst)
	j = (c+d)//2
	
	while(True):
		if i>lst[j][0] and i<=lst[j][1]:
			print(j, i-lst[j][0])
			break
		else:
			if i>lst[j][0]:
				j = j+(len(lst)-j)//2
			else:
				j = j//2