from heapq import heapify, heappop, heappush

n, k = map(int, input().split())

a = list(map(int, input().split()))

m = []
for i in range(n):
	m.append([a[i], i])

heapify(m)

while(k):
	minV = m[0][0]
	x = heappop(m)
	heappush(m, [minV+1,x[1]])
	a[x[1]] = a[x[1]]+1
	k-=1


for i in a:
	print(i, end=" ")
