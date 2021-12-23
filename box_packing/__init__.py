from flask import Flask, url_for
from box_packing.box_manager import BoxManager
import sqlite3


connection = sqlite3.connect('moving.db', check_same_thread=False)
connection.row_factory = sqlite3.Row

db = BoxManager(connection)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1A37BbcCJh67'

    with app.app_context():
        from box_packing import routes

        with open(url_for('static', filename='sql/create_db.sql'), 'r') as f:
            db.run_sql_script(f)

    return app
