# booky/auth/__init.py

from flask import Blueprint
authentication = Blueprint('authentication', __name__, template_folder='templates')

from booky.auth import routes