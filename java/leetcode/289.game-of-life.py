#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get(i, j):
            if i < 0 or j < 0:
                return 0
            try:
                return board[i][j]
            except:
                return 0

        m = len(board)
        if m == 0:
            return []
        n = len(board[0])
        dup = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                count = get(i,j-1) + get(i-1,j-1) + get(i-1,j) + get(i-1,j+1) + get(i,j+1) + get(i+1,j+1) + get(i+1,j) + get(i+1,j-1)
                if board[i][j]:
                    dup[i][j] = 1 if count == 2 or count == 3 else 0
                elif count == 3:
                    dup[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = dup[i][j]
        
# @lc code=end

