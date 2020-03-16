n, k = map(int, input().split())

a = list(map(int, input().split()))

lst1 = []
for i in range(len(a)):
	lst1.append([a[i],i])

lst1 = sorted(lst1,key=lambda lst1:lst1[0])
print(lst1)

while(k!=0) :
	if (lst1[0][0] != lst1[1][0]) :
		while(k!=0 and lst1[0][0]<lst1[1][0]):
			lst1[0][0] += 1
			k-=1
	else :
		lst1[0][0]+=1
		k-=1
	
	i=1
	while(lst1[i][1>]lst1[i-1][1]):
		x = lst[i][1]
		lst1[i][1] = lst1[i-1][1]
		lst1[i-1][1] = x
		i+=1
	print(k)



print(sorted(lst1,key=lambda lst1:lst1[1]))