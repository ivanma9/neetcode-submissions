class Twitter:

    def __init__(self):
        # followee: follower 
        # 1: 1, 2
        # 2: 2
        self.followers = defaultdict(set)
            # userId: [(tweet_#, tweet_ids] 
        self.tweets = collections.defaultdict(list)
        self.tweet_count = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweet_count, tweetId))
        self.tweet_count +=1
        self.followers[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
      
        # show top 10 most recent tweets from all follower of userId
        # use maxHeap
        maxHeap = []
        for follower in self.followers[userId]:
            # greater time is more recent
            for time, tweet in self.tweets[follower]:
                print(time, tweet)
                heapq.heappush(maxHeap, (-time, tweet))
        # return heapq.nsmallest(10, maxHeap)
        top_10_tweets = []
        i = 0
        n = min(len(maxHeap), 10)
        while (i < n):
            time, tweet = heapq.heappop(maxHeap)
            top_10_tweets.append(tweet)
            i+=1
        return top_10_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
            

