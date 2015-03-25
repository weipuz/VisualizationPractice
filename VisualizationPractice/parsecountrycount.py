import json,csv
from collections import defaultdict
    
    
tweets_data_path = 'tweet_vote5sos.log'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print len(tweets_data)

with open('CountryCodes.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = dict((rows[1],rows[2]) for rows in reader)


country = defaultdict(int)
for tweet in tweets_data:
    if 'place' in tweet and tweet['place'] != None:
        place = tweet['place']
        if 'country_code' in place and place['country_code'] != None:
            key = mydict[place['country_code']]
            country[key] += 1
print country
#with open('country_result.json','w') as out:
#    json.dump(country,out)
with open('country_result.csv','w') as outfile:
    out = csv.writer(outfile)
    out.writerow(('name','count'))
    out.writerows(country.items())

