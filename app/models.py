# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:35:10 2019

@author: KaranKapoor
"""

from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login



class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64),index=True, unique=True)
    email=db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    post = db.relationship('Post', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username) 
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
#Because Flask-Login knows nothing about databases, it needs the application's help in loading a user. 
#For that reason, the extension expects that the application will configure a user loader function, 
#that can be called to load a user given the ID. 
@login.user_loader
def load_user(id):
    #databases that use numeric IDs need to convert the string to integer as you see above.
    return User.query.get(int(id))