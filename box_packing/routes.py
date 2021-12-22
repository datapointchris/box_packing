from flask import request, render_template, redirect, url_for

from box_packing import app, db


def convert_box_id_to_name(results, mapping):
    for result in results:
        id = result.get('box_id')
        box = mapping.get(id)
        result['box'] = box
        del result['box_id']
    return results


@app.route('/', methods=['GET', 'POST'])
def index():
    last_box_id = request.args.get('last_box_id')
    box_sort_1 = request.form.get('box_sort_1')
    box_sort_2 = request.form.get('box_sort_2')
    box_id = last_box_id or request.form.get('selected_box_id', 1)
    boxes = db.get_all_boxes(box_sort_1, box_sort_2)
    selected_box = db.get_box(box_id)
    selected_box_items = db.get_box_items(box_id)
    return render_template(
        'index.html',
        boxes=boxes,
        selected_box=selected_box,
        selected_box_items=selected_box_items,
    )


@app.route('/search/', methods=['GET', 'POST'])
def search():
    search_text = request.form.get('search_text')
    search_results = db.text_search(search_text)
    box_mapping = db.get_box_id_mappings()
    results = convert_box_id_to_name(search_results, box_mapping)
    return render_template(
        'search.html',
        results=results,
    )


@app.route('/add_box/', methods=['POST'])
def add_box():
    name = request.form.get('name')
    size = request.form.get('size')
    liquid = request.form.get('liquid', 0)
    warm = request.form.get('warm', 0)
    essential = request.form.get('essential', 0)
    box = {
        'name': name,
        'size': size,
        'liquid': liquid,
        'warm': warm,
        'essential': essential,
    }
    db.add_box(box)
    return redirect(url_for('index'))


@app.route('/add_item/', methods=['POST'])
def add_item():
    box_id = request.form.get('box_id')
    name = request.form.get('name')
    essential = request.form.get('essential', 0)
    warm = request.form.get('warm', 0)
    liquid = request.form.get('liquid', 0)
    item = {
        'box_id': box_id,
        'name': name,
        'essential': essential,
        'warm': warm,
        'liquid': liquid,
    }
    db.add_box_item(item)
    return redirect(url_for('index', last_box_id=box_id))


@app.route('/delete_item/', methods=['POST'])
def delete_item():
    box_id = request.form.get('box_id')
    item_id = request.form.get('item_id')
    db.delete_item(box_id, item_id)
    return redirect(url_for('index', last_box_id=box_id))


@app.route('/delete_box/', methods=['POST'])
def delete_box():
    box_id = request.form.get('box_id')
    db.delete_box(box_id)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
