import tweepy
import json
from tweepy import OAuthHandler
from vaccine_progress_bot import application

class TwitterClient(object):
    '''
    Twitter Client
    '''

    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # read keys from the secret credentials file
        api_key = application.config['API_KEY']
        api_secret = application.config['API_SECRET_KEY']
        access_token = application.config['ACCESS_TOKEN']
        access_token_secret = application.config['ACCESS_TOKEN_SECRET']

        try:
            self.auth = OAuthHandler(api_key, api_secret)
            self.auth.set_access_token(access_token,
                                       access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print('Error: Authentication error')
    
    def post_tweet(self, text):
        self.api.update_status(text)

    def get_last_tweet_date(self):
        tweet = self.api.user_timeline(count=1)[0]
        json_data = json.loads(json.dumps(tweet._json))
        return json_data.get('text')[-10:]