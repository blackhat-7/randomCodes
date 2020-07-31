#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.deque()
        self.indices = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.indices:
            return False
        self.indices[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.indices:
            return False
        self.data[self.indices[val]] = self.data[-1]
        self.indices[self.data[-1]] = self.indices[val]
        self.data.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

