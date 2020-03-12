import json

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    about = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float)
    picture = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    _goals = db.Column(db.String, nullable=False)
    _free = db.Column(db.Text, nullable=False)
    bookings = db.relationship("Booking", back_populates="teacher")

    @property
    def goals(self):
        return self._goals.split(';')

    @goals.setter
    def goals(self, goals):
        self._goals = ';'.join(goals)

    @property
    def free(self):
        return json.loads(self._free)

    @free.setter
    def free(self, free):
        self._free = json.dumps(free)


class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    day = db.Column(db.String(15), nullable=False)
    hour = db.Column(db.String(15), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    teacher = db.relationship("Teacher", back_populates="bookings")


class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    goal = db.Column(db.String(15), nullable=False)
    time = db.Column(db.String(15), nullable=False)
