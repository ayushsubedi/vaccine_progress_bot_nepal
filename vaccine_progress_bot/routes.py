from vaccine_progress_bot import application
from vaccine_progress_bot import basic_auth
from vaccine_progress_bot.models import TwitterClient
from flask import render_template

@application.route('/')
def hello():
    return ('vaccine_progress_bot_working')


@application.route('/post_tweet')
@basic_auth.required
def post_tweet():
    twitter_client = TwitterClient()
    tweet_text = 'testing'
    twitter_client.post_tweet(tweet_text)
    return 'done'