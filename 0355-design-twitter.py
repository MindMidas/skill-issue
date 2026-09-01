# 355. Design Twitter
# Problem: https://leetcode.com/problems/design-twitter/
# Submitted: 2026-09-01 15:36 EDT
# Intuition: Only each followed user's latest ten tweets can enter the latest-ten feed.
# Approach: Store timestamped tweets and follow sets, then heap-merge recent candidates.
# Complexity: Average O(1) post/follow/unfollow, O(f + log(f+1)) feed; O(T + F) stored space.

import heapq

class Twitter:

    def __init__(self):
        self.tweets_by_user = {}
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_by_user:
            self.tweets_by_user[userId] = []
        self.tweets_by_user[userId].append((-self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        heap = []
        
        # get users own tweets
        if userId in self.tweets_by_user:
            for tweet in self.tweets_by_user[userId][-10:]:
                heap.append(tweet)
        
        if userId in self.following:
            for followingId in self.following[userId]:
                if followingId in self.tweets_by_user:
                    for tweet in self.tweets_by_user[followingId][-10:]:
                        heap.append(tweet)
        
        heapq.heapify(heap)

        news_feed = []
        while heap and len(news_feed) < 10:
            news_feed.append(heapq.heappop(heap)[1])

        return news_feed
                        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            return
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)