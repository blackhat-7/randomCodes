#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = collections.defaultdict(set)
        self.posts = collections.defaultdict(collections.deque)
        self.time = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if len(self.posts[userId]) == 10:
            self.posts[userId].popleft()
        self.posts[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """

        heap = []
        for post in self.posts[userId]:
            heapq.heappush(heap, post)

        for following in self.users[userId]:
            if following != userId:
                for post in self.posts[following]:
                    heapq.heappush(heap, post)
        res = heapq.nlargest(10, heap)
        return [post[1] for post in res]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.users[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

