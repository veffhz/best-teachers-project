from flask_wtf import FlaskForm
from wtforms import StringField


class MyForm(FlaskForm):
    name = StringField('name')
