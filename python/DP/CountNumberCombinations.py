def countCombinations(matrix, n, lookup, row=0, col=0, number=''):
    if row < 0 or col < 0 or row > 3 or col > 2 or matrix[row][col] == '*' or matrix[row][col] == '#':
        return 0
    if n == 1:
        return 1
    
    key = (number, row, col)
    if key not in lookup:
        curr = countCombinations(matrix, n - 1, lookup, row, col, number + matrix[row][col])
        left  = countCombinations(matrix, n - 1, lookup, row, col - 1, number + matrix[row][col]) 
        right = countCombinations(matrix, n - 1, lookup, row, col + 1, number + matrix[row][col])
        up    = countCombinations(matrix, n - 1, lookup, row - 1, col, number + matrix[row][col])
        down  = countCombinations(matrix, n - 1, lookup, row + 1, col, number + matrix[row][col])
        lookup[key] = curr + left + right + up + down
    
    return lookup[key]









# Maximum N-digit number allowed
N = 8

# mobile keypad
matrix = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

n = 8
lookup = dict()
count = 0
for row in range(4):
    for col in range(3):
        if ('', row, col) not in lookup and matrix[row][col].isdigit():
            count += countCombinations(matrix, n, lookup, row, col)

print(count)