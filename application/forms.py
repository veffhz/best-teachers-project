from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, RadioField, HiddenField, SubmitField


class BookingForm(FlaskForm):
    name = StringField(validators=[InputRequired()])
    phone = StringField(validators=[InputRequired()])
    day = HiddenField('day')
    hour = HiddenField('hour')
    teacher_id = HiddenField('teacher_id')
    submit = SubmitField('booking_submit')


class RequestForm(FlaskForm):
    name = StringField(validators=[InputRequired()])
    phone = StringField(validators=[InputRequired()])
    goal = RadioField()
    time = RadioField()
    submit = SubmitField('request_submit')
