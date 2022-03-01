import json
from tweepy import Stream
from datetime import datetime
from api_keys import access_token,access_token_secret,consumer_key,consumer_secret




# define an file to store collected tweets

out = open(f"stored_tweets_{datetime.now()}.txt","w")

# Implements a class to connect with Twitter

class TwitterListener(Stream):

    def on_data(self,data):
        data = json.dumps(data.decode("utf-8"))
        out.write(data)
        return True
    
    def on_error(self, status):
        print(status)


# implementing main function 
if __name__ == "__main__":
    twitter_listener = TwitterListener(consumer_key, consumer_secret, access_token, access_token_secret)
    twitter_listener.filter(track=['#russia'])

