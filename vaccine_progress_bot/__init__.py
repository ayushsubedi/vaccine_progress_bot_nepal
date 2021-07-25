from flask import Flask
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname
from flask_basicauth import BasicAuth


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

# html to img
application.config['HCTI_API_USER_ID'] = environ.get('HCTI_API_USER_ID')
application.config['HCTI_API_KEY'] = environ.get('HCTI_API_KEY')

from vaccine_progress_bot import routes