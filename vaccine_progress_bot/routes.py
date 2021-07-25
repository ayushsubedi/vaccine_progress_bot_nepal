from vaccine_progress_bot import application
from vaccine_progress_bot import basic_auth
from flask import render_template

@application.route('/')
def hello():
    return ('vaccine_progress_bot_working')


@application.route('/tweet')
@basic_auth.required
def tweet():
    # TODO tweet
    return 'basic auth working'