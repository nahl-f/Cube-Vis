from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
#setting up the database
db = SQLAlchemy()
DB_NAME = 'users.db'

def create_app():
    app = Flask(__name__)
    #encrypts cookies and session data related to the website
    app.config['SECRET_KEY'] = 'randomkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #sets up the page directories for the website
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Time
    create_database(app)

    login_manager = LoginManager()
    #if the user isn't logged in, redirect them to login page
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    #telling flask how to load the user
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    #only creates database if it already doesn't exist in order to prevent overwriting existing data
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')

