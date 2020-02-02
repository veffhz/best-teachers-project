import json
import random
import pathlib
from collections import defaultdict, OrderedDict

from flask import current_app as app

days_of_week = OrderedDict({
    "mon": {"short_ver": "Пн",
            "full_ver": "Понедельник"},
    "tue": {"short_ver": "Вт",
            "full_ver": "Вторник"},
    "wed": {"short_ver": "Ср",
            "full_ver": "Среда"},
    "thu": {"short_ver": "Чт",
            "full_ver": "Четверг"},
    "fri": {"short_ver": "Пт",
            "full_ver": "Пятница"},
    "sat": {"short_ver": "Сб",
            "full_ver": "Суббота"},
    "sun": {"short_ver": "Вс",
            "full_ver": "Воскресенье"}
})


def random_limit(dictionary, quantity):
    if len(dictionary) < quantity:
        return random.sample(dictionary.items(), len(dictionary))
    return random.sample(dictionary.items(), quantity)


def grouped_by_hours(days):
    by_hours = defaultdict(dict)
    for day_of_week in days_of_week.keys():
        for hour, is_accessible in days[day_of_week].items():
            by_hours[hour].update({day_of_week: is_accessible})
    return by_hours


def save_data(file, data):
    old_data = read_json_data(file)
    if old_data and isinstance(old_data, list):
        old_data.append(data)
        write_json_data(file, old_data)
    else:
        write_json_data(file, [data])


def write_json_data(json_file, data):
    path = pathlib.Path(__file__).parent / json_file
    booking_data_json = json.dumps(data, ensure_ascii=False)
    path.write_text(booking_data_json)


def read_json_data(json_file):
    path = pathlib.Path(__file__).parent / json_file
    if path.exists():
        return json.loads(path.read_text())


def read_to_dict_json_data(json_file, key):
    items = read_json_data(json_file)
    if items:
        return {item[key]: item for item in items}


teachers = read_to_dict_json_data(app.config.get('TEACHERS_FILE'), 'id') or {}
goals = read_json_data(app.config.get('GOALS_FILE')) or {}
