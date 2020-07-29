#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        wordList.append(beginWord)
        n = len(wordList)
        if n == 1:
            return []
            
        m = len(wordList[0])
        for i in range(n-1):
            for j in range(i+1, n):
                if all(wordList[i][k] == wordList[j][k] for k in range(m)):
                    graph[i].add(j)
                    graph[j].add(i)
            
        # BFS for all shortest paths
        def bfs(src):
            q = collections.deque()
            dist = [float('inf')] * n
            parent = [set() for i in range(n)]
            q.append(src)
            dist[src] = 0
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v] > dist[u] + 1:
                        dist[v] = dist[u] + 1
                        parent[v] = set([u])
                        q.push(v)
                    elif dist[v] == dist[u] + 1:
                        parent[v].add(u)
            print(dist, parent)

        bfs(n-1)
        return []
        
# @lc code=end

