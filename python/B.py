n, m = map(int, input().split())
teamSolved = dict()
teamTime = dict()
bhayanakCount = 0
bhayanakTime = 0

while(m):

	x, y = input().split()
	
	if x in teamSolved:
		teamSolved[x] += 1
		teamTime[x] += int(y)
	else :
		teamSolved[x] = 1
		teamTime[x] = int(y)
	
	if x=='BhayanakMaut':
		bhayanakCount += 1
		bhayanakTime += int(y)

	m-=1


rank = 1

for i in teamSolved:
	if teamSolved[i] > bhayanakCount:
		rank+=1
	if teamSolved[i] == bhayanakCount and teamTime[i]<bhayanakTime:
		rank+=1

print(rank)


