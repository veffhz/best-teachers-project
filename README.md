Best teachers project with Flask
==================
[![Heroku](https://heroku-badge.herokuapp.com/?app=best-teachers-project&style=flat)](https://best-teachers-project.herokuapp.com)

##### features:
 - index page for show random 6 teachers
 - profile page for show teacher detail
 - booking page for send lesson order
 - send request for selection teacher
 
##### requirements:
 - Python 3.5+
 - Flask 1.1.1
 - Gunicorn 20.0.4

##### install requirements:
`pip3 install -r requirements.txt`

##### create and fill db 
`flask db upgrade`

`python migrate_to_db.py`

##### run app:
 - run `gunicorn 'wsgi:app'`
 - open default page http://127.0.0.1:8000
