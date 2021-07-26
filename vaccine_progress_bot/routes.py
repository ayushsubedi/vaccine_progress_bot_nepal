from vaccine_progress_bot import application
from vaccine_progress_bot import basic_auth
from vaccine_progress_bot.models import TwitterClient
from vaccine_progress_bot.helpers import progress_bar
from flask import render_template
import pandas as pd

SOURCE = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Nepal.csv'

# https://www.macrotrends.net/countries/NPL/nepal/population-growth-rate
POPULATION = 29674920.0


@application.route('/')
def hello():
    return ('future home of vaccine bot nepal')


@application.route('/get_data')
@basic_auth.required
def get_data():
    data = pd.read_csv(SOURCE).iloc[-1].to_dict()
    percentage_fully_vaccinated = round(100*data.get('people_fully_vaccinated')/POPULATION, 3)
    percentage_partially_vaccinated = round(100*data.get('people_vaccinated')/POPULATION, 3)
    final = "Fully Vaccinated\n" +\
    progress_bar.get(int(percentage_fully_vaccinated)) +" "+str(percentage_fully_vaccinated) +"%"+\
    "\n\n" +\
    "Partially Vaccinated\n" +\
    progress_bar.get(int(percentage_partially_vaccinated)) +" "+str(percentage_partially_vaccinated) +"%"+\
    "\n" +\
    ' Latest Data ---> ' + data.get('date')
    return final, str(data.get('date'))
    

@application.route('/post_tweet')
@basic_auth.required
def post_tweet():
    twitter_client = TwitterClient()
    tweet_text, date_new = get_data()
    date_old = twitter_client.get_last_tweet_date()
    if (date_new == date_old):
        return 'duplicate'
    twitter_client.post_tweet(tweet_text)
    return 'done'


@application.route('/get_last_tweet_date')
@basic_auth.required
def get_last_tweet_date():
    twitter_client = TwitterClient()
    return twitter_client.get_last_tweet_date()
