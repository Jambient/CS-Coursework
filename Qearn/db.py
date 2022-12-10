from flaskext.mysql import MySQL
from flask import Flask, current_app, g
from pymysql import cursors

app = Flask(__name__)
mysql = MySQL(autocommit=True, cursorClass=cursors.DictCursor)
mysql.init_app(app)

def get_db():
    if 'db' not in g:
        g.db = mysql.connect().cursor()

    return g.db

def get_sql():
    return MySQL(app)

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()