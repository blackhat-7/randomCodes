x = [-2,-5,6,-2,-3,1,5,-6]

maxSum = 0
currentSum = 0

for i in x:
	currentSum += i
	if currentSum<0 :
		currentSum = 0
	if maxSum<currentSum :
		maxSum = currentSum

print(maxSum)