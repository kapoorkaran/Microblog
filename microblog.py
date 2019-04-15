# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:49:20 2019

@author: KaranKapoor
"""

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
