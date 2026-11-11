# 1348. Tweet Counts Per Frequency
# Problem: https://leetcode.com/problems/tweet-counts-per-frequency/
# Submitted: 2026-11-11 17:25 EST
# Intuition: A tweet's offset from the query start determines its bucket.
# Approach: Store timestamps by tweet name. For each query, scan that tweet's timestamps and count those in the inclusive range by dividing their offsets by the bucket duration.
# Complexity: O(1) amortized time per record and O(t + b) time per query for t timestamps under the queried name and b buckets. Space is O(n) for n recorded tweets and O(b) for the result.

class TweetCounts:

    def __init__(self):
        self.tweets = {} # dict to store tweets and time posted at

    def recordTweet(self, tweetName: str, time: int) -> None:

        # add time for tweetName to the dict
        if tweetName not in self.tweets:
            self.tweets[tweetName] = []
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list[int]:

        intervals = {
            'minute': 60,
            'hour': 3600,
            'day': 86400
        }

        interval = intervals[freq]

        # calc num windows needed
        n = (endTime - startTime) // interval + 1
        result = [0] * n

        # increment count at each window
        for time in self.tweets.get(tweetName, []):
            if startTime <= time <= endTime:
                i = (time - startTime) // interval
                result[i] += 1

        return result

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
