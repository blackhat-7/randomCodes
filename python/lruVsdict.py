import time
from functools import lru_cache
from random import randint as randi

class Solution:
    m = None
    n = None
    def longestIncreasingPath(self, matrix):
        if len(matrix) == 0: return 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        
        @lru_cache(None)
        def dfs(i, j, prev=None):
            if i < 0 or j < 0 or i == self.m or j == self.n or (prev is not None and prev >= matrix[i][j]):
                return 0
            n = dfs(i-1, j, matrix[i][j])
            s = dfs(i+1, j, matrix[i][j])
            e = dfs(i, j+1, matrix[i][j])
            w = dfs(i, j-1, matrix[i][j])
            return max(n, s, e, w) + 1
        
        length = 0
        
        for i in range(self.m):
            for j in range(self.n):
                length = max(length, dfs(i, j))
        return length
    
    def longestIncreasingPath2(self, matrix):
        if len(matrix) == 0: return 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        
        def dfs(i, j, lookup, prev=None):
            if i < 0 or j < 0 or i == self.m or j == self.n or (prev is not None and prev >= matrix[i][j]):
                return 0
            key = (i, j, prev)
            if key not in lookup:
                n = dfs(i-1, j, lookup, matrix[i][j])
                s = dfs(i+1, j, lookup, matrix[i][j])
                e = dfs(i, j+1, lookup, matrix[i][j])
                w = dfs(i, j-1, lookup, matrix[i][j])
                lookup[key] = max(n, s, e, w) + 1
            return lookup[key]
        
        length = 0
        lookup = {}

        for i in range(self.m):
            for j in range(self.n):
                length = max(length, dfs(i, j, lookup))
        return length

lru_max, lru_min, lru_avg = 0, float('inf'), 0
dic_max, dic_min, dic_avg = 0, float('inf'), 0

for i in range(1, 6):
    matrix = [[randi(0, 1000)]*1000 for _ in range(1000)]

    sol = Solution()
    start = time.time()
    ans = sol.longestIncreasingPath(matrix)
    lru = time.time()-start
    start = time.time()
    ans2 = sol.longestIncreasingPath2(matrix)
    dic = time.time()-start
    
    lru_max = max(lru_max, lru)
    lru_min = min(lru_min, lru)
    lru_avg = (lru_avg * (i-1) + lru) / i

    dic_max = max(dic_max, dic)
    dic_min = min(dic_min, dic)
    dic_avg = (dic_avg * (i-1) + dic) / i
    
    print(ans == ans2)

print("LRU:")
print("MAX : ", str(lru_max), "MIN : ", str(lru_min), "AVG : ", str(lru_avg))
print("DIC")
print("MAX : ", str(dic_max), "MIN : ", str(dic_min), "AVG : ", str(dic_avg))