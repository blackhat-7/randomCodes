#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree, wordSet, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList:
            return []
        found, beginLayer, endLayer, newLayer, rev = False, {beginWord}, {endWord}, set(), False

        while beginLayer and not found: 
            wordSet -= beginLayer
            for x in beginLayer:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in wordSet:
                        if y in endLayer:
                            found = True
                        else:
                            newLayer.add(y)
                        tree[x].add(y) if not rev else tree[y].add(x)
            beginLayer, newLayer = newLayer, set()
            if beginLayer > endLayer:
                beginlayer, endLayer, rev = endLayer, beginLayer, not rev
        
        def findPath(x):
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in findPath(y)]

        return findPath(beginWord)
            
            
        
# @lc code=end

