#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    height = -1
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightmost = defaultdict(lambda: (float('-inf'), 0))
        def traverse(root, y=0):
            if not root:
                return None
            self.height = max(self.height, y)
            rightmost[y] = root.val
            traverse(root.left, y+1)
            traverse(root.right, y+1)
        
        traverse(root)
        return [rightmost[y] for y in range(self.height+1)]
            
        
# @lc code=end

'''

'''