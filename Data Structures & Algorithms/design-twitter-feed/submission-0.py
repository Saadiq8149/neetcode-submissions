class Twitter:

    def __init__(self):
        self.timestamp = 1

        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)

        heap = []
        for followee in self.followMap[userId]:
            tweets = self.tweetMap[followee]

            if tweets:
                idx = len(tweets) - 1
                timestamp, tweetId = tweets[idx]

                heapq.heappush(
                    heap,
                    (-timestamp, tweetId, followee, idx)
                )

        res = []

        while heap and len(res) < 10:
            _, tweetId, followee, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx > 0:
                timestamp, prevTweetId = self.tweetMap[followee][idx - 1]

                heapq.heappush(
                    heap,
                    (-timestamp, prevTweetId, followee, idx - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].discard(followeeId)