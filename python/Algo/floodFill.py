from collections import deque


def floodFillBfs(M, x, y, replacement):
    target = M[x][y]
    q = deque()
    visited = set()
    q.append((x, y))
    visited.add((x, y))

    def isValid(x, y):
        if x < 0 or y < 0 or x >= len(M) or y >= len(M[0]) or M[x][y] != target:
            return False
        return True
    while q:
        x, y = q.popleft()
        M[x][y] = replacement
        if isValid(x-1, y):
            q.append((x-1, y))
            visited.add((x-1, y))
        if isValid(x+1, y):
            q.append((x+1, y))
            visited.add((x+1, y))
        if isValid(x, y-1):
            q.append((x, y-1))
            visited.add((x, y-1))
        if isValid(x, y+1):
            q.append((x, y+1))
            visited.add((x, y+1))


M = [
    ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
    ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
    ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
    ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
    ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
    ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
    ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
    ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
    ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

# start node
x = 3
y = 9

# target color = "X"
# replacement color
replacement = 'C'

# replace target color with replacement color
floodFillBfs(M, x, y, replacement)

# print the colors after replacement
for r in M:
    print(r)
