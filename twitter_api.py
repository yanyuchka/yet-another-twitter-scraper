#!/usr/bin/python 

## this script does basic twitter streaming listening
## use appropriate function to write the stream to stdout or a text file 

import tweepy as tw
import sys

## user credentials to access Twitter API should be passed to the script 
## simple length check on the credentials
if len(sys.argv) > 4:
  consumer_key =  sys.argv[1]
  consumer_secret = sys.argv[2]
  access_token = sys.argv[3]
  access_token_secret = sys.argv[4]
else:
  print 'Please, enter your Consumer Key, Consumer Secret Key, Access Token, Access Token Key all at once'


## basic class to print tweets to stdout
class stdOutListener(tw.streaming.StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

## basic class to print tweets to a file
class toFileListener(tw.streaming.StreamListener):

    def on_data(self, data):
        with open('tweets.txt','a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print status
    

if __name__ == '__main__':
  
  ## handle Twitter authetification and the connection to Twitter Streaming API
  l = toFileListener() ## use stdOutListener() to write to stdout
  auth = tw.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  stream = tw.Stream(auth, l)

  ## filter Twitter Streams to filter data by keywords
  stream.filter(track=['s'])

