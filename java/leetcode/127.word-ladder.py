#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        tree, wordSet, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordSet:
            return 0
        
        bq, eq, nq, found, dist = {beginWord}, {endWord}, set(), False, 1

        while bq and not found:
            dist += 1
            wordSet -= bq
            for x in bq:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in wordSet:
                        if y in eq:
                            found = True
                            break
                        else:
                            nq.add(y)
            bq, nq = nq, set()
            if bq > eq:
                bq, eq = eq, bq
        return dist if found else 0
# @lc code=end

