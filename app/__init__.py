# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:51:09 2019

@author: KaranKapoor
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#Flask-Login keeps track of the logged in user by storing its unique identifier in Flask's user session, 
#a storage space assigned to each user who connects to the application. 
#Each time the logged-in user navigates to a new page, Flask-Login retrieves the ID of the user from the session, 
#and then loads that user into memory.
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login= LoginManager(app)
login.login_view = 'login'
#The 'login'is the the name you would use in a url_for() call to get the URL.

from app import routes, models