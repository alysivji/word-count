from collections import Counter
import logging
import os
import string

from flask import flash, render_template, request
from nltk.corpus import stopwords
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

VOWELS = ['a', 'e', 'i', 'o', 'u']
STOPWORDS = stopwords.words('english')


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


def _process_word(word: str):
    """
    Get word stem and lower case word
    """
    word = word.lower()

    # words that aren't plural but end in s
    if word.endswith('is'):
        pass

    # plural nouns
    elif (word.endswith('ches') or word.endswith('xes') or
          word.endswith('ses') or word.endswith('shes') or
          word.endswith('zes')):
        word = word[:-2]
    elif word.endswith('oes'):
        word = word[:-2]
    elif word.endswith('ves'):
        word = word[:-3] + 'f'
    elif word.endswith('ies'):
        if word[-4] not in VOWELS:
            word = word[:-3] + 'y'
    # when in doubt, remove the s to make singular
    elif word.endswith('s') and not word.endswith('ss'):
        word = word[:-1]

    # conjugated verbs
    elif word.endswith('ing'):
        word = word[:-3]
    elif word.endswith('ed'):
        word = word[:-2]

    return word


#############
# Controllers
#############

@app.route('/', methods=['GET', 'POST'])
def index():
    form = WordCountForm()

    if form.validate_on_submit():
        exclude_stopwords = form.exclude_stopwords.data

        # user uploads file
        if 'text_file' in request.files:
            file = request.files['text_file']

            if file and _allowed_file(file.filename):
                filename = secure_filename(file.filename)
                full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(full_path)
                lines = _extract_lines_from_file(full_path)
                return word_count(lines=lines,
                                  exclude_stopwords=exclude_stopwords)
            else:
                flash('File requires txt extensions')

        # user enters text
        if form.entered_text.data is not '':
            lines = []
            for line in form.entered_text.data.splitlines():
                lines.append(line.strip().translate(table))
            return word_count(lines=lines,
                              exclude_stopwords=exclude_stopwords)

    return render_template('index.html', form=form)


def word_count(lines, exclude_stopwords):
    """
    Loop thru lines, count words, and output table
    """

    # import pdb; pdb.set_trace()

    word_counter = Counter()
    for line in lines:
        for word in line.split():
            if exclude_stopwords:
                words = [_process_word(word)
                         for word in line.split()
                         if word not in STOPWORDS]
            else:
                words = [_process_word(word)
                         for word in line.split()]
            word_counter += Counter(words)

    return render_template(
        'top_words.html',
        top_words=word_counter.most_common(25),
    )
