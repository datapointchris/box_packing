from box_packing.box_manager import BoxManager
from flask import request, render_template, make_response
import sqlite3

from flask import Flask

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')

connection = sqlite3.connect('moving.db')

db = BoxManager(connection)


@app.route('/', methods=['GET', 'POST'])
def index():
    boxes = db.get_all_boxes()
    single_box = db.get_box(request.form.get('single_box_id'))
    print(single_box)
    return render_template('index.html', boxes=boxes, single_box=single_box)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=4500)
