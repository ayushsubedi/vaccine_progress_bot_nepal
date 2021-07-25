from flask import Flask
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname
from flask_basicauth import BasicAuth

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://54c455ebfc144a4d99d175b11505ae0e@o717172.ingest.sentry.io/5878697",
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

application = Flask(__name__)
basic_auth = BasicAuth(application)

# Secret key for form
application.config['SECRET_KEY'] = environ.get('SECRET_KEY')

# Basic auth
application.config['BASIC_AUTH_USERNAME'] = environ.get('BASIC_AUTH_USERNAME')
application.config['BASIC_AUTH_PASSWORD'] = environ.get('BASIC_AUTH_PASSWORD')

#Tweet
application.config['API_KEY'] = environ.get('API_KEY')
application.config['API_SECRET_KEY'] = environ.get('API_SECRET_KEY')
application.config['ACCESS_TOKEN'] = environ.get('ACCESS_TOKEN')
application.config['ACCESS_TOKEN_SECRET'] = environ.get('ACCESS_TOKEN_SECRET')

from vaccine_progress_bot import routes