from flask import Flask
from box_packing.box_manager import BoxManager
import sqlite3

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:8000'
app.config['SECRET_KEY'] = '1A37BbcCJh67'

connection = sqlite3.connect('moving.db', check_same_thread=False)
connection.row_factory = sqlite3.Row

db = BoxManager(connection)

with app.app_context():
    db.create_db()


from box_packing import routes

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)