from flask import Blueprint, render_template, request, url_for, g, flash, jsonify
import flask_excel as excel
import pandas as pd

from pybo.forms import FileForm
from pybo.views.auth_views import login_required

bp = Blueprint('file', __name__, url_prefix='/file')


@bp.route('/upload/', methods=('GET', 'POST'))
@login_required
def upload():
    form = FileForm()
    if request.method == 'POST' and form.validate_on_submit():
        upload_files = request.files.getlist('file')
        f = upload_files[0]
        # f = request.files['file']
        data_xls = pd.read_excel(f)
        return data_xls.to_html()

    return render_template('file/file_form.html', form=form)
