# Importing necessary Libraries

import tweepy

# My API key

with open ("Twitter API.txt", "r") as myfile:
    twitterapi = myfile.read().splitlines()

# Setting up my API with Tweepy

auth = tweepy.OAuthHandler(twitterapi[0],twitterapi[1])
auth.set_access_token(twitterapi[2],twitterapi[3])
api = tweepy.API(auth)

# India's Where on earth ID

india_woeid = 23424848

# Getting trending data from twitter

trending = api.get_place_trends(india_woeid)

trendingdict = {'Trending topic':[],'No. of tweets':[]}
for trend in trending[0]['trends'][:10]:
    trendingdict['Trending topic'].append(trend['name'])
    trendingdict['No. of tweets'].append(trend['tweet_volume'])

# Visual Part

import pandas as pd

Trending_Topics = pd.DataFrame(trendingdict)
Trending_Topics = Trending_Topics.fillna('-')
Trending_Topics.index = Trending_Topics.index + 1

# Top 10 Trending Topics in India

print(Trending_Topics)

