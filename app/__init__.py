# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:51:09 2019

@author: KaranKapoor
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes