fv = 0

for i in range(45):
	fv += 1095
	fv += 0.12*fv

print(fv)