# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:39:55 2019

@author: KaranKapoor
"""
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required 
def index():
#    user = {'username': 'karan'}
#   posts = [{'author':{'username':'utkarsh'},
#             'body':'qwertyuio'
#            },
#            {'author':{'username':'sashi'},
#             'body':'zxcvbnm'
#            }
#        ]
    return render_template("index.html", title='Home Page')
@app.route('/login', methods=['GET', 'POST'])
def login():
#if user already logged in redirect to index    
#the current_user variable comes from flask login can be used at any time during the handling to obtain 
#the user object that represents the client of the request.
    if current_user.is_authenticated:  #is_authenticated, which comes in handy to check if the user is logged in or not.
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() 
#first(), which will return the user object if it exists, or None if it does not.
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page=url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))