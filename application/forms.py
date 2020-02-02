from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, RadioField, HiddenField, SubmitField

from application.data_helper import goals


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
    goal = RadioField(choices=[(goal_code, goal['desc'].capitalize()
                                ) for goal_code, goal in goals.items()], default='travel')

    time = RadioField(choices=[('1-2', '1-2 часа в неделю'),
                               ('3-5', '3-5 часов в неделю'),
                               ('5-7', '5-7 часов в неделю'),
                               ('7-10', '7-10 часов в неделю')], default='5-7')
    submit = SubmitField('request_submit')
