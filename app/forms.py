from flask_wtf import FlaskForm
from wtforms import FileField, TextAreaField, SubmitField


class WordCountForm(FlaskForm):
    entered_text = TextAreaField('Paste Text')
    text_file = FileField('Text File')
    submit = SubmitField('Count Words')
