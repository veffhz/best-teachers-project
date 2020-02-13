from werkzeug import exceptions
from flask import render_template, request

from application import app
from application.models import db
from application.models import Teacher, Booking, Request
from application.forms import BookingForm, RequestForm
from application.data_helper import goals, days_of_week
from application.data_helper import grouped_by_hours


@app.route('/')
def main():
    teachers = Teacher.query.limit(6).all()
    return render_template('index.html', teachers=teachers,
                           goals=goals)


@app.route('/all/')
def get_all_teachers():
    teachers = Teacher.query.all()
    return render_template('index.html', teachers=teachers,
                           goals=goals)


@app.route('/goals/<goal_code>/')
def get_goal(goal_code):
    goal = goals[goal_code]
    teachers = Teacher.query.filter(Teacher._goals.contains(goal_code)).order_by(Teacher.rating.desc())
    return render_template('goal.html', goal=goal, teachers=teachers)


@app.route('/profiles/<int:teacher_id>/')
def get_profile(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    grouped_days = grouped_by_hours(teacher.free)
    goals_by_codes = [goal['desc'] for code, goal in goals.items()
                      if code in teacher.goals]
    profile = {
        'teacher': teacher,
        'goals': goals_by_codes,
        'hours': grouped_days
    }
    return render_template('profile.html', profile=profile,
                           days_of_week=days_of_week)


@app.route('/request/')
def get_request():
    form = RequestForm()
    return render_template('request.html', goals=goals, form=form)


@app.route('/request_done/', methods=['POST'])
def send_request():
    new_request = Request()
    form = RequestForm(obj=new_request)
    form.populate_obj(new_request)
    db.session.add(new_request)
    db.session.commit()
    new_request.goal = goals[new_request.goal]['desc']
    return render_template('request_done.html', request_data=new_request)


@app.route('/booking/<int:teacher_id>/')
def get_booking(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    booking_day = days_of_week[request.args.get('day')]
    booking_hour = request.args.get('hour')
    booking_data = {
        'teacher': teacher,
        'day': booking_day['full_ver'],
        'hour': booking_hour
    }
    form = BookingForm()
    return render_template('booking.html', booking_data=booking_data, form=form)


@app.route('/booking_done/', methods=['POST'])
def send_booking():
    new_booking = Booking()
    form = BookingForm(obj=new_booking)
    form.populate_obj(new_booking)
    db.session.add(new_booking)
    db.session.commit()
    return render_template('booking_done.html', booking_data=new_booking)


@app.errorhandler(exceptions.NotFound)
def not_found(e):
    return render_template("404.html"), e.code


@app.errorhandler(exceptions.InternalServerError)
def server_error(e):
    return render_template("500.html"), e.code
