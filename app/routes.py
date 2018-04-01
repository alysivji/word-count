import logging
import os

from flask import flash, render_template, url_for, redirect, request
from werkzeug.utils import secure_filename

from app import app
from app.forms import WordCountForm

logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = set(['txt'])


##################
# Helper Functinos
##################

def _allowed_file(filename):
    return ('.' in filename and
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)


def extract_lines_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines


#############
# Controllers
#############

@app.route('/', methods=['GET', 'POST'])
def index():
    form = WordCountForm()

    if form.validate_on_submit():
        # user uploads file
        if 'text_file' in request.files:
            file = request.files['text_file']

            if file and _allowed_file(file.filename):
                filename = secure_filename(file.filename)
                full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(full_path)
                lines = extract_lines_from_file(full_path)
                return url_for('word_count', lines=lines)
            else:
                flash('Error with file. Requires extension txt')

        # user enters text
        if form.entered_text.data is not '':
            lines = []
            for line in form.entered_text.data.split():
                lines.append(line.strip())
            return url_for('word_count', lines=lines)

    return render_template('index.html', form=form)


@app.route('/wc')
def word_count(lines):
    """
    Loop thru lines and count words
    """
    from flask import jsonify  # noqa
    return jsonify(lines)
