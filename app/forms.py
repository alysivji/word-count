from flask_wtf import FlaskForm
from wtforms import BooleanField, FileField, TextAreaField, SubmitField


class WordCountForm(FlaskForm):
    entered_text = TextAreaField('Paste Text')
    text_file = FileField('Text File')
    exclude_stopwords = BooleanField('Exclude Stopwords?', default=False)
    submit = SubmitField('Count Words')
