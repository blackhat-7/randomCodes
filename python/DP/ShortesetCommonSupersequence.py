string1 = input()
string2 = input()

length1 = len(string1) + 1
length2 = len(string2) + 1

lookup = [[0]*length2 for i in range(length1)]

for i in range(length1):
    for j in range(length2):
        if i == 0:
            lookup[i][j] = j
        elif j == 0:
            lookup[i][j] = i
        else:
            if string1[i-1] == string2[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
            else:
                lookup[i][j] = min(lookup[i-1][j] + 1, lookup[i][j-1] + 1)

print(lookup[length1-1][length2-1])

superSequence = ""

row = length1 -1
col = length2 - 1

while row >= 0 and col >= 0:
    if string1[row-1] == string2[col-1]:
        superSequence = string1[row-1] + superSequence
        row -= 1; col -= 1;
    elif col > 0 and lookup[row][col-1]+1 == lookup[row][col]:
        superSequence = string2[col-1] + superSequence
        col -= 1
    elif row > 0 and lookup[row-1][col]+1 == lookup[row][col]:
        superSequence = string1[row-1] + superSequence
        row -= 1

print(superSequence)