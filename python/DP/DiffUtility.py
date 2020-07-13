
def diff(string1, string2, i, j, lookup):
    if i > 0 and j > 0 and string1[i-1] == string2[j-1]:
        diff(string1, string2, i-1, j-1, lookup)
        print(string1[i-1], end = ' ')
    
    elif i > 0 and (j == 0 or lookup[i-1][j] < lookup[i][j-1]):
            diff(string1, string2, i, j-1, lookup)
            print('+ ' + string2[j-1], end = ' ')

    elif i > 0 and (j == 0 or lookup[i-1][j] >= lookup[i][j-1]):
        diff(string1, string2, i-1, j, lookup)
        print('- ' + string1[i-1], end = ' ')


string1 = input()
string2 = input()

len1 = len(string1) + 1
len2 = len(string2) + 1

lookup = [[0]*len2 for i in range(len1)]

for i in range(len1):
    for j in range(len2):
        if i == 0 or j == 0:
            lookup[i][j] = 0
        else:
            if string1[i-1] == string2[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
            else:
                lookup[i][j] = max(lookup[i-1][j], lookup[i][j-1])

# Diff

diff(string1, string2, len1-1, len2-1, lookup)


'''
  0 a b d
0 0 0 0 0
a 0 1 0 0
c 0 1 1 1
d 0 1 1 2

'''