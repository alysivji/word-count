from collections import Counter
import logging
import os
import string

from flask import flash, render_template, request
from werkzeug.utils import secure_filename

from app import app
from app.forms import WordCountForm

###############
# Configuration
###############

logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = set(['txt'])

# map punctuation to None
table = str.maketrans({key: None for key in string.punctuation})


##################
# Helper Functions
##################

def _allowed_file(filename):
    return ('.' in filename and
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)


def _extract_lines_from_file(file):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            lines.append(line.strip().translate(table))
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
                lines = _extract_lines_from_file(full_path)
                return word_count(lines=lines)
            else:
                flash('Error with file. Requires extension txt')

        # user enters text
        if form.entered_text.data is not '':
            lines = []
            for line in form.entered_text.data.splitlines():
                lines.append(line.strip().translate(table))
            return word_count(lines=lines)

    return render_template('index.html', form=form)


def word_count(lines):
    """
    Loop thru lines and count words
    """
    # import pdb; pdb.set_trace()
    word_counter = Counter()
    for line in lines:
        words = [word.lower() for word in line.split()]
        word_counter += Counter(words)

    from flask import jsonify
    return jsonify(word_counter)
