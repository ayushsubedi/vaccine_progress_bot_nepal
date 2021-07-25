from vaccine_progress_bot import application
from flask import render_template

@application.route('/')
def hello():
    return ('vaccine_progress_bot_working')


@application.route('/tweet')
def tweet():
    // TODO tweet
    return 'basic auth working'