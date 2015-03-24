import json
import namedtuple

tweets_data_path = 'tweet.log'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print len(tweets_data)
class Counter(dict):
    def __missing__(self,key):
        return 0
country = Counter()

for tweet in tweets_data:
    if tweet['country_code'] != None:
        country[tweet['country_code']]+=1

#tweets['country'] = map(lambda tweet: tweet['country_code'] if tweet['country_code'] != None else None, tweets_data)
#tweets_by_country = tweets['country'].value_counts()