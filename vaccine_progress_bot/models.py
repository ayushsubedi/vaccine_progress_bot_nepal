import tweepy
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