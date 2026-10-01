from typing import List
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId, userId, len(self.tweets[userId])))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        candidates = []
        for user in users:
            if len(self.tweets[user]) > 0:
                candidates.append(self.tweets[user][-1])
        heapq.heapify(candidates)
        
        feed = []
        while candidates and len(feed) < 10:
            tweet = heapq.heappop(candidates)
            feed.append(tweet[1])
            idx = tweet[3] - 1
            if idx >= 0:
                heapq.heappush(candidates, self.tweets[tweet[2]][idx])
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
