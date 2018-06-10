# booky/catalog/__init.py

from flask import Blueprint
main = Blueprint('main', __name__, template_folder='templates')


from booky.catalog import routes
