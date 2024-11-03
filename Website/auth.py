from flask import Blueprint, render_template, request, flash, redirect, url_for, Flask
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import re


auth = Blueprint('auth', __name__)
#all of the decorators allow different paths within the website tabs.
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #retrieving the username and password that was passed in the form
        username = request.form.get('username')
        password = request.form.get('password')
        #returns user with the entered username
        user = User.query.filter_by(username=username).first()
        #ensures user actually exists and has an account
        if user:
            #checks is password entered matches database password registered
            if check_password_hash(user.password, password):
                flash('Logged in sucessfully!', category = 'success')
                login_user(user, remember = True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category = 'error')
        else:
            flash('User does not exist.', category = 'error')
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        passwordconf = request.form.get('passwordconf')
        user = User.query.filter_by(username=username).first()
        #checks to ensure the username isn't already in use
        if user:
            flash("Username already exists", category = 'error')
        #check to ensure username has an appropriate length
        elif len(username) < 4:
            flash('Your username must be greater than 3 characters', category='error')
        elif len(username) > 20:
            flash('Your username cannot be greater than 20 characters', category = 'error')
        #ensuring password is secure
        elif len(password) < 8:
            flash('Your password must have at least 7 characters.', category='error')
        elif not re.search("[a-z]", password):
            flash('Password must contain at least 1 lowercase character.', category = 'error')
        elif not re.search("[A-Z]", password):
            flash('Password must contain at least 1 uppercase character.', category = 'error')
        elif not re.search("[0-9]", password):
            flash('Password must contain at least 1 numeric character.', category='error')
        elif not re.search("[$#@*!]", password):
            flash('Password must contain at least 1 special character ($#@*!) .', category='error')
        elif password != passwordconf:
            flash("Passwords don't match.", category = 'error')
        else:
            #password is put through a built in hash function for encryption
            new_user = User(username = username, password = generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()

            #testing code, allows me to see database
            tables = User.metadata.tables.values()

            for table in tables:
                # Get all rows from the table
                query = db.session.query(table)
                results = query.all()
                for row in results:
                    print(row)
                print('Table', table.name)
                
            flash('Account created!', category = 'success')
            return redirect(url_for('auth.login'))
    return render_template('signup.html', user = current_user)

