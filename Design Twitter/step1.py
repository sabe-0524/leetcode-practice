from typing import List
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweet_by_user = {}
        self.following = defaultdict(set)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet_by_user:
            self.tweet_by_user[userId] = [(self.counter, tweetId, userId)]
        else:
            heapq.heappush(self.tweet_by_user[userId], (self.counter, tweetId, userId))
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        show_num = 10
        feed = []
        candidates = []
        folowees = self.following[userId]
        for folowee in folowees | {userId}:
            if not self.tweet_by_user or folowee not in self.tweet_by_user:
                continue
            heapq.heappush(candidates, heapq.heappop(self.tweet_by_user[folowee]))
        
        for _ in range(show_num):
            if not candidates:
                break
            showed = heapq.heappop(candidates)
            feed.append(showed)
            if self.tweet_by_user[showed[2]]:
                heapq.heappush(candidates, heapq.heappop(self.tweet_by_user[showed[2]]))
        
        for tweet in feed:
            heapq.heappush(self.tweet_by_user[tweet[2]], tweet)
        
        for candidate in candidates:
            heapq.heappush(self.tweet_by_user[candidate[2]], candidate)
        
        return [tweet for _, tweet, _ in feed]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
