from flask import request, render_template, make_response
from flask import current_app as app
from box_packing.models import db, User
from box_packing.form import CheckForm


@app.route('/', methods=['GET', 'POST'])
def check_form():
    """Check form for submitting daily habits"""
    form = CheckForm()
    if form.validate_on_submit():
        return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=)