# booky/__init__.py

import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap

from flask_login import LoginManager

from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.login_view = 'authenticaton.do_the_login'
login_manager.session_protection = 'strong'

bcrypt = Bcrypt()

def create_app(ctype):

    app = Flask(__name__)

    a = os.path.join(os.getcwd(), 'config')
    b = ctype + '.py'
    c = os.path.join(a, b)
    print (c)
    configuration = c

    app.config.from_pyfile(configuration)

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from booky.catalog import main
    app.register_blueprint(main)

    from booky.auth import authentication
    app.register_blueprint(authentication)

    return app

