#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        def deepCopy(node, visited):
            if not node:
                return None
            new_node = Node(node.val)
            visited[node] = new_node
            for neigh in node.neighbors:
                if neigh not in visited:
                    deepCopy(neigh, visited)
                new_node.neighbors.append(visited[neigh])
            return new_node

        return deepCopy(node, {})
        
# @lc code=end

