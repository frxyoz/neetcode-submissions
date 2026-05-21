from collections import defaultdict
from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        followees = self.follows[userId] | {userId}

        for user in followees:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index - 1)
                )

        while heap and len(res) < 10:
            negTime, tweetId, user, nextIndex = heapq.heappop(heap)

            res.append(tweetId)

            # push older tweet from same user
            if nextIndex >= 0:
                time, tweetId = self.tweets[user][nextIndex]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, nextIndex - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)