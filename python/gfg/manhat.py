import math

def bruteForce(numPeople, x, y):
    m = max(x)
    n = max(y)
    matrix =[[0]*n for i in range(m)]
    cood = [0,0]

    for i in range(len(numPeople)):
        xi = x[i]-1
        yi = y[i]-1
        zi = numPeople[i]
        for j in range(m):
            for k in range(n):
                matrix[j][k] += zi*(abs(xi-j)+abs(yi-k))

    # print(matrix)
    minv = float('inf')
    for i in range(m):
        for j in range(n):
            minv = min(matrix[i][j], minv)
            cood = [i+1,j+1]
    print(cood)
    return minv
        

def optimal(numPeople, x, y):
    xans = min(x)
    yans = min(y)
    res = 0
    print(xans, yans)
    for i in range(len(numPeople)):
        zi = numPeople[i]
        res += zi*(abs(xans-x[i]-1) + abs(yans-y[i]-1))
    return res


'''
1 1      3 1
         3 1

2

11 33
  22
1+1+1+1
2+2+2+2
3

'''


if __name__ == '__main__':
    numPeople = [100,1]
    x = [1, 2]
    y = [1, 2]
    print(bruteForce(numPeople, x, y))
    print(optimal(numPeople, x, y))

