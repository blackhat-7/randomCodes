from collections import deque


def lee(mat, sx, sy, dx, dy, visited):
    def is_valid(x, y):
        if x < 0 or y < 0 or x >= len(mat) or y >= len(mat[0]) or (x, y) in visited:
            return False
        return True

    q = deque()
    q.append((sx, sy, 0))
    visited = set()
    visited.add((sx, sy))
    min_d = float('inf')
    while q:
        x, y, d = q.popleft()
        if x == dx and y == dy:
            min_d = d
            break
        if is_valid(x+1, y):
            q.append((x+1, y, d+1))
        if is_valid(x-1, y):
            q.append((x-1, y, d+1))
        if is_valid(x, y+1):
            q.append((x, y+1, d+1))
        if is_valid(x, y-1):
            q.append((x, y-1, d+1))
    return min_d


mat = [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
       [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
       [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
       [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
       [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
       [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
       [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
       [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
       ]

path_length = lee(mat, 0, 0, 7, 5, set())
print(path_length)
