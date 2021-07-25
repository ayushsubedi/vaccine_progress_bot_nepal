from vaccine_progress_bot import application
from vaccine_progress_bot import basic_auth
from vaccine_progress_bot.models import TwitterClient
from flask import render_template
import pandas as pd

SOURCE = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Nepal.csv'

@application.route('/')
def hello():
    return ('vaccine_progress_bot_working')


@application.route('/get_data')
@basic_auth.required
def get_data():
    data = pd.read_csv(SOURCE).iloc[-1].to_dict()
    return data

@application.route('/post_tweet')
@basic_auth.required
def post_tweet():
    twitter_client = TwitterClient()
    tweet_text = 'testing'
    twitter_client.post_tweet(tweet_text)
    return 'done'