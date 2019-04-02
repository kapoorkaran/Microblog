# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:39:55 2019

@author: KaranKapoor
"""
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'karan'}
    post = [{'author':{'username':'utkarsh'},
             'body':'qwertyuio'
            },
            {'author':{'username':'sashi'},
             'body':'zxcvbnm'
            }
        ]
    return render_template('index.html', user=user, title='Home', post=post)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user{}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)