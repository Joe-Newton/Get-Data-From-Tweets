# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '912340095189045248-oYFQwAK84frF7qSHqoOlrez8sePAi3n'
ACCESS_SECRET = 'ocnB6cAXOidsrPv2PNEVxbqgXrWoLyjr227UFv4LfMlXs'
CONSUMER_KEY = 'JZlWREnSH1yKihk75X8c0AZfu'
CONSUMER_SECRET = 'FI0ASBbXf389e0YU3mzUMA2O77a2H8eYWmXy2vDjDzqftZ7nlQ'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# sets parameters of what tweets to extract data about
iterator = twitter_stream.statuses.filter(track = "#savememountainrescue", language = "en")

# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet, indent = 4)  
    
    
       
    if tweet_count <= 0:
        break 
